import pandas as pd
import numpy as np
import os
import glob
import subprocess
import json
import datetime as dt
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import time
import re
from googletrans import Translator

CSV_DESTINATION_PROD = "bdp131:/var/SP/data/staging/vf_de/bop/"
CSV_DESTINATION_PREPROD = "bdp131:/var/SP/data/staging/vf_de/preprod/bop/"
schema_types = ["people_compensation", "people_hr_ticket" ,"people_organisational" ,"people_recruiting"]
outputpath = os.path.join(os.getcwd(), "output")
schemas = os.path.join(os.getcwd(), "etc", "schema")
log_path = os.path.join(os.getcwd(), "log")
date_for_the_current_run = dt.datetime.now().strftime("%Y%m%d%H%M%S")
current_schema_file_type = ""
current_schema_file_name = ""
sensitive_cols_data_to_remove = {
    "imp_leavers_sf":["Legacy System Employee Number", "Date of Birth", "Phone Number", "Legacy System Payroll ID", "National ID", "Personal Email ID", "Recommended LWD is for reference. It's the leaving date as per notice period, if applicable", "Shortfall in Notice Period"]
}
has_data_issue = False
cols_stats = []

def get_file_name(file_path,schema_type):
    """function to get the file name without it's extention

    Args:
        file_path (str): path of the file

    Returns:
        str: file name
    """
    if (len(file_path) > 0):
        return os.path.split(file_path)[1].split(".")[0].replace(f"datafeed-bop-{schema_type}-", "")
    else:
        return ""

def generate_output_csv_file_format(file_type, filename):
    """ function to generate the output csv file format for sql or bigquery based on file_type

    Args:
        file_type (str): bop_people_compensation|sql_direct_load
        filename (str): name of the schema file

    Returns:
        str: formatted file name
    """
    return os.path.join(outputpath, f"{file_type}_{filename}_{dt.datetime.now().strftime('%Y%m%d%H%M%S')}.csv.gz")

def remove_files_from_dir(dir):
    """removes all the files in a selected directory

    Args:
        dir (str): directory path 
    """
    [f.unlink() for f in Path(dir).glob("*") if f.is_file()]

def run_cmd_based_on_os(cmd):
    """run a given command based on the os

    Args:
        cmd (str): the command to run

    Raises:
        NotImplementedError: if the user is using an unsupported operating system (supported: (*nix | windows))
    """
    if os.name == "nt":
        subprocess.run(["C:\\Program Files\\Git\\bin\\bash.exe", "-c", cmd])
    elif os.name == "posix":
        subprocess.run(["bash", "-c", cmd])
    else:
        raise NotImplementedError("unSupported operating system")

def set_current_schema_file_name(name):
    """ set the private global variable current_schema_file_name

    Args:
        name (str): value to set the current_schema_file_name
    """
    global current_schema_file_name
    current_schema_file_name = name

def get_current_schema_file_name():
    """ get the private global variable current_schema_file_name

    Returns:
        str: current extended schema the user is comparing against
    """
    return current_schema_file_name
#
def set_current_schema_file_type(type):
    """ set the private global variable current_schema_file_type

    Args:
        name (str): value to set the current_schema_file_type
    """
    global current_schema_file_type
    current_schema_file_type = type

def get_current_schema_file_type():
    """ get the private global variable current_schema_file_type

    Returns:
        str: current extended schema the user is comparing against
    """
    return current_schema_file_type

def set_has_data_issue(flag):
    """set if there is an issue while validating the data

    Args:
        flag (boolean): true|false if there is a data issue
    """
    global has_data_issue
    has_data_issue = flag

def get_has_data_issue():
    """ get has_data_issue

    Returns:
        boolean: true|false if there is a data issue
    """
    return has_data_issue

def validate_feed_data_against_TDS(df, tds_schema_data):
    """validate excell sheet data feed against the extended json schema

    Args:
        df (dataframe): dataframe representation of the selected sheet
        tds_schema_data (json): json representation of the selected schema
    """
    set_has_data_issue(False)
    #pair together the elements of tds_schema_data and df.columns into a tuple of iterators and loop through them
    for index, (schema_col, feed_col) in enumerate(zip(tds_schema_data, df.columns)):
        cols_stats.append({"name":feed_col,"length":len(df[feed_col]),"num_of_issues":0,"tds_name":schema_col["name"],"tds_sequence":schema_col["sequence"]})
        if (schema_col["type"] == "string"):
            # check if anonymized field is of type date
            if (re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$", schema_col["example"])):
                perform_operation_on_fields(
                    df[feed_col], try_cast,schema_col["is-mandatory"], target_type=dt.datetime.strptime, extra_format=["%d.%m.%Y","%Y-%m-%d %H:%M:%S","%m.%d.%Y","%d/%m/%Y","%m/%d/%Y"], col_name=feed_col)
            else:
                perform_operation_on_fields(
                    df[feed_col], is_valid_length, schema_col["is-mandatory"],expected=schema_col["length"], col_name=feed_col)
        elif (schema_col["type"] == "date"):
            cloned_df=df
            extra_format=["%d.%m.%Y","%Y-%m-%d %H:%M:%S","%m.%d.%Y","%d/%m/%Y","%m/%d/%Y","%d-%m-%Y"]
            perform_operation_on_fields(
                cloned_df[feed_col], try_cast, schema_col["is-mandatory"], target_type=dt.datetime.strptime, extra_format=extra_format, col_name=feed_col)
        elif (schema_col["type"] == "datetime"):
            cloned_df=df
            extra_format=["%d.%m.%Y %H:%M:%S","%Y-%m-%d %H:%M:%S","%m.%d.%Y %H:%M:%S","%d/%m/%Y %H:%M:%S","%m/%d/%Y %H:%M:%S","%d/%m/%Y %I:%M:%S %p","%d.%m.%Y %I:%M:%S %p","%d-%m-%Y %I:%M:%S %p","%m/%d/%Y %I:%M:%S %p","%m.%d.%Y %I:%M:%S %p","%m-%d-%Y %I:%M:%S %p"]
            perform_operation_on_fields(
                cloned_df[feed_col], try_cast, schema_col["is-mandatory"], target_type=dt.datetime.strptime, extra_format=extra_format, col_name=feed_col)#

        elif (schema_col["type"] == "double"):
            perform_operation_on_fields(
                df[feed_col], try_cast,schema_col["is-mandatory"], target_type=float, col_name=feed_col)
        elif (schema_col["type"] == "integer"):
            perform_operation_on_fields(
                df[feed_col], try_cast,schema_col["is-mandatory"], target_type=int, col_name=feed_col)
        else:
            print(f"Warning this type {schema_col['type']} is not supported!")

def perform_operation_on_fields(col, operation,is_required, **operationArgs):
    """higher order function that takes an operation and its argument and perform it on a number of elements in a col

    Args:
        col (df[col]): col of the df
        operation (fc): function to be executed
    """
    for index, field in enumerate(col):
        operationArgs["value"] = str(field)
        operationArgs["col_index"] = index
        # skip the null values if not required
        if(not is_required and (pd.isna(field))):
            continue
        operation(**operationArgs)

def try_cast(value, target_type, col_name, col_index, extra_format=None):
    """function to test if the cast is possible

    Args:
        value (any): the value to check against the tds if it matches the right type
        target_type (fc): casting function to the desired type that is in the extended schem 
        col_name (_type_): name of the column in the df
        col_index (int): index pos for the item in the col starting from 0
        extra_format (str, optional): format for date to follow. Defaults to None.

    Returns:
        any: casted value if its possible else False
    """
    try:
        if extra_format !=None:
            for format in extra_format:
                try:
                    return target_type(value, format).date()
                except ValueError:
                    pass
            raise ValueError('no valid date format found')
        elif target_type == int and "." in str(value):
            # cast string into float first to avoid type casting issue from pandas mixed data types
            return target_type(float(value))
        else:
            return target_type(value)
    except (ValueError, TypeError):
        issue_msg = generate_error_log_formatted_msg(issue_type="type_casting", expected=target_type if not extra_format else type(
            dt.datetime.now()), actual=type(value), col_name=col_name, col_index=col_index, value=value)
        log_issue(issue_msg)
        print(issue_msg)
        set_has_data_issue(True)
        increase_num_of_issues_for_col(col_name)
        return False

def is_valid_length(expected, value, col_name, col_index):
    """check the length of the string field

    Args:
        expected (int): expected length
        value (str): 
        col_name (_type_): name of the df col
        col_index (_type_): index of the element in the col_

    Returns:
        boolean: true if its ok else false
    """
    if expected >= len(value):
        return True
    else:
        issue_msg = generate_error_log_formatted_msg(issue_type="field length", expected=expected, actual=len(
            value), col_name=col_name, col_index=col_index, value=value)
        print(issue_msg)
        log_issue(issue_msg)
        set_has_data_issue(True)
        increase_num_of_issues_for_col(col_name)
        return False

def create_dir_if_not_exists(dir_path):
    """creates directory if it doesnt exist

    Args:
        dir_path (str): directory path
    """
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

def log_issue(issue_msg):
    """function to log issues in dir /etc/out

    Args:
        issue_msg (bool): _description_
    """
    create_dir_if_not_exists(log_path)
    error_log_file_path = create_log_file(get_current_schema_file_name())
    with open(error_log_file_path, "+a") as f:
        f.write(issue_msg)

def create_log_file(filename):
    """create formatted file for logging issues

    Args:
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    return os.path.join(log_path, f"validation_errors_log_{filename}_{date_for_the_current_run}.txt")

def generate_error_log_formatted_msg(issue_type, expected, actual, col_name="test_col", col_index=0, value=""):
    """generate error log msg

    Args:
        issue_type (str): type of the issue ex (length|type_casting)
        expected (any): expected in tds
        actual (any): recived from the excell sheet
        col_name (str, optional): col name in df. Defaults to "test_col".
        col_index (int, optional): index of item in the col. Defaults to 0.
        value (str, optional): field value. Defaults to "".

    Returns:
        _type_: formatted string to be added to the log file 
    """
    return f"column {col_name} has an issue {issue_type} expected {expected} but received {actual} at index {col_index+2} for value {value}\n"

def format_df_date_col(data, df):
    """format date cols based on the exporting type bigquery or mysql

    Args:
        data (json): _description_
        df (dataframe): _description_
    Returns:
        df: data frame obj after applying the changes to it
    """
    for schema_col, feed_col in zip(data["schema"], df.columns):
        isDateOfBirth=schema_col["type"] == "string" and re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$", schema_col["example"])
        if (schema_col["type"] == "date" or isDateOfBirth):
            try:
                df[feed_col] = pd.to_datetime(df[feed_col],dayfirst=True)
            except:
                df[feed_col] = pd.to_datetime(df[feed_col],dayfirst=False)
        elif (schema_col["type"] == "datetime"):
            try:
                df[feed_col] = pd.to_datetime(df[feed_col],dayfirst=True)
            except:
                df[feed_col] = pd.to_datetime(df[feed_col],dayfirst=False)
    return df

def increase_num_of_issues_for_col(col_name):
    """increase the number of issues in a givin column 

    Args:
        col_name (str): the name of the column in the df
    """
    for index, col in enumerate(cols_stats):
        if col["name"] == col_name:
            cols_stats[index]["num_of_issues"]=cols_stats[index]["num_of_issues"]+1
            break

def get_formated_cols_stats_msg():
      """write a formatted statistics msg in both the cli and the logging file
      """
      stats_header="\t\t\t\t**********statistics about the run**********"
      global cols_stats
      num_of_cols=len(cols_stats)
      num_of_succesful_cols=num_of_cols-len(list(filter(lambda col:col["num_of_issues"]>0,cols_stats)))
      num_of_failed_cols=num_of_cols-num_of_succesful_cols
      num_of_cols_msg=f"{num_of_cols} columns processed"
      num_of_succesful_cols_msg=f"{num_of_succesful_cols} successfull"
      num_of_failed_cols_msg=f"{num_of_failed_cols} columns with errors\n"
      #cli part
      print(stats_header)
      print(num_of_cols_msg)
      print(num_of_succesful_cols_msg)
      print(num_of_failed_cols_msg)
      print(f"See log for more details")
      #log file part
      log_issue(stats_header+"\n")
      log_issue(num_of_cols_msg+"\n")
      log_issue(num_of_succesful_cols_msg+"\n")
      log_issue(num_of_failed_cols_msg)
      for index, col in enumerate(cols_stats):
        msg=f"column {col['name']} at index {index+1} against {col['tds_name']} at TDS sequence {col['tds_sequence']}  has {col['num_of_issues']} issues out of {col['length']} fields processed\n"
        log_issue(msg)
      cols_stats = []

def send_files_to_system(destination):
    """send files (intended to bigQuery only) with scp to remote system

    Args:
        destination (str): the remote system
    """
    csv_files = glob.glob(os.path.join(outputpath, f"bop_{get_current_schema_file_type()}_*.csv.gz"))
    for file in csv_files:
        # get filename
        linux_file_name = file.replace("\\","/")
        #get from linux_file anmeinterface
        interface_date_name = linux_file_name.split("/")[-1].split(".")[0].replace(f"bop_{get_current_schema_file_type()}_","")
        interface_name = re.sub(r"_\d+","",interface_date_name)
        final_destination = destination + get_current_schema_file_type() + "/" + interface_name
        cmd = f"scp '{linux_file_name}' {final_destination}"
        run_cmd_based_on_os(cmd)
        os.remove(file)
        print(file,"removed and sent to ",final_destination)

# open json-schema file for related csv/dataframe, validate and safe as csv
def generate_csv(df, json_schema, null_surrogate = None):
    """generate csv file from recived dataframe and based on the selected null_surrogate

    Args:
        df (dataframe): _description_
        json_schema (json): json representation of the selected schema 
        null_surrogate (char, none):replacement for empty cells. Defaults to None.
    """
    create_dir_if_not_exists(outputpath)
    with open(json_schema, "r") as f:
        data = json.load(f)

    filename = get_file_name(json_schema,get_current_schema_file_type())
    set_current_schema_file_name(filename)
    #replace all the whitespaces with na
    df = df.replace("^\s+$", pd.NA, regex=True)
    validate_feed_data_against_TDS(df,data["schema"])
    # look if sum of columns are the same in feed and provided schema
    if (len(data["schema"]) == len(df.columns)) and not get_has_data_issue():
        df = format_df_date_col(data,df)
        # validate if requiered fields contain empty values
        for schema_col,feed_col in zip(data["schema"],df.columns):
            if schema_col["is-mandatory"] == True and df[feed_col].isna().any().any() == True:
                return print(f"There are empty values for a required field {feed_col}")
            if null_surrogate is not  None:
                if schema_col["type"] == "datetime":
                    df[feed_col] = df[feed_col].dt.strftime('%Y-%m-%d %H:%M:%S') 
                elif schema_col["type"] == "date":
                    df[feed_col] = df[feed_col].dt.strftime('%Y-%m-%d')
            else:
                if schema_col["type"] == "datetime":
                    df[feed_col] = df[feed_col].dt.strftime('%m/%d/%Y %H:%M:%S') 
                elif schema_col["type"] == "date":
                    df[feed_col] = df[feed_col].dt.strftime('%m/%d/%Y')

        #dataframe to csv if validated
        df.dropna(how="all", inplace=True)
        #replace na with null-surrogate (e.g. \N for mysql)
        if null_surrogate is not None: #triggers when null surrogate is \N
            df.fillna(null_surrogate, inplace=True)
            df.to_csv(generate_output_csv_file_format("sql_direct_load",filename),sep="|",compression="gzip",index=False,encoding="utf-8")
        else:
            df.to_csv(generate_output_csv_file_format(f"bop_{get_current_schema_file_type()}",filename),sep="|",compression="gzip",index=False,encoding="utf-8")
        return print(f"{filename} saved as csv")
    else:
        print("csv columns not machting with BQ-schema! File was not put into Output\n")
        not (len(data["schema"]) ==len(df.columns)) and print(f"number of columns in TDS: {len(data['schema'])}\nnumber of columns in input file: {len(df.columns)}\n")
        return

def ask_null_value():
    """ get the value for the null_surrogate from the user
    """
    print("\n Select null-surrogate:\n")
    print("""
    1) none (recommended for BigQuery)
    2) \\n (only for mysql)
    \n""" )

    user_input = input("Please enter option: ")
    if user_input == "1":
        return None
    elif user_input == "2":
        return r"\N"
    else:
        print("\nWrong Input please try again!")

def select_schema_type_or_default():
    """ get the schema value from the user or return the default schema value
    """
    print("Please Choose the Schema type from the following:")
    for i in range(len(schema_types)):
        print(i," ",schema_types[i])
    schema_type_input=input(f"enter selected schema type default is {schema_types[0]}:")
    if schema_type_input.isdigit() and int(schema_type_input) <= len(schema_types) - 1 and int(schema_type_input) >= 0:
        return schema_types[int(schema_type_input)]
    return schema_types[0]


def remove_senstive_data(sensitive_cols_data_to_remove, get_current_schema_file_name, df):
    """ remove the senstive data files from the input source

    Args:
        get_current_schema_file_name (str): the current selected schema 
        df (dataframe): dataframe
        sensitive_cols_data_to_remove (obj, none): the schemas and the columns to remove from the source input
    """
    if get_current_schema_file_name() in sensitive_cols_data_to_remove:
        for column_name in sensitive_cols_data_to_remove[get_current_schema_file_name()]:
            if column_name in df.columns:
                 df.drop(column_name, axis=1, inplace=True)

def translate_text(text):
    """ translate the greek words only into english

    Args:
        text (str): the current to translate
    """
    greek_alphabet = 'αβΓγΔδεζηΘθικΛλμνΞξοΠπρΣσςτυΦφχΨψΩωΑΒΕΖΗΙΚΛΜΝΟοΡσ/ςΤΥΧ'
    has_greek_letters = False
    
    if text == "nan" or (isinstance(text,str) and len(text) == 0) or not isinstance(text,str):
        return text
    if  isinstance(text,str) and  text[0] in greek_alphabet:
        has_greek_letters= True
    if has_greek_letters:
        translator = Translator()
        translated = translator.translate(text, dest='en')
        return translated.text
    else:
        return text


def remove_bad_characters(df):
    """ remove the bad characters from the input source

    Args:
        df (dataframe): dataframe
    """

    #remove the bad characters from column name
    df.columns = df.columns.str.replace('\r','')
    df.columns = df.columns.str.replace('\n',' ')
    for column_name in df.columns:
        try:
            df[column_name] = df[column_name].apply(translate_text)
            df[column_name] = df[column_name].str.split('\r').str.join('')
            df[column_name] = df[column_name].str.split('\n').str.join(' ')
        except AttributeError:
            pass


if __name__ == "__main__":
    """ the starting point of the tool that asks the user to input in the cli his desired action 

    """
    # Start Dialog in Terminal -> run while 0 is not pressed
    status = ""
    while status != "0":
        # Read and print files in Output folder
        xlsx_files = glob.glob(os.path.join(outputpath, "*.csv.gz"))
        xlsx_filenames = [get_file_name(file,get_current_schema_file_type())  for file in xlsx_files]

        if len(xlsx_files) > 0:
            print(f"\nThere are {len(xlsx_files)} Files in Output-Folder: \n ")
            for file in xlsx_filenames[:10]:
                print(file)
            if len(xlsx_files) > 10:
                print("...")
        else:
            print("\nOutput-folder is empty. Please generate files for transfer.\n")

        # Ask for Action (read Excel, send files , empty folder or stop tool)
        print("\n Please choose one the following options:\n")
        print("""
        1) Generate CSV-files to output-folder
        2) Transfer all files from output-folder
        3) Empty output-folder
        0) Exit Programm
        \n""" )

        status = input("Please enter option: ")

        if status == "1":
            # Choose json schema matching the Excel file.
            schema_type= select_schema_type_or_default()
            set_current_schema_file_type(schema_type)
            print(f"\nCurrent selected schema type: {schema_type}\n")

            schema_files = glob.glob(os.path.join(schemas, f"*{schema_type}*.json"))
            print("\nPlease Choose the right Schema for your Excelfile:")
            for i in range(len(schema_files)):
                print(i," ",get_file_name(schema_files[i],schema_type))

            schema_input = input("Please enter schema: ")
            if not schema_input.isdigit() or int(schema_input) > len(schema_files) - 1 or int(schema_input)<0:
                print("false schema input")
            else:
                # Open Browser to choose excel or csv and load as pandas DF
                root = tk.Tk()
                root.withdraw()
                file = filedialog.askopenfilename(filetypes=[
                            ("Excel or CSV files", ".xlsx .xls .csv")])
                if ".xlsx" in file:
                    # get sheet pos
                    sheet_pos = input("Please enter sheet position (default: First Sheet = 0): ")
                    try:
                        df = pd.read_excel(file,sheet_name=int(sheet_pos))
                    except:
                        df = pd.read_excel(file,sheet_name=0)
                    set_current_schema_file_name(get_file_name(schema_files[int(schema_input)],get_current_schema_file_type()))
                    remove_senstive_data(sensitive_cols_data_to_remove, get_current_schema_file_name, df)
                    remove_bad_characters(df)
                    generate_csv(df,schema_files[int(schema_input)], ask_null_value())
                    xlsx_files = glob.glob(os.path.join(outputpath, "*.xlsx"))

                elif ".csv" in file:
                    df = pd.read_csv(file, sep=None, encoding='utf-8', encoding_errors="ignore", engine="python")
                    set_current_schema_file_name(get_file_name(schema_files[int(schema_input)],get_current_schema_file_type()))
                    remove_senstive_data(sensitive_cols_data_to_remove, get_current_schema_file_name, df)
                    remove_bad_characters(df)
                    generate_csv(df,schema_files[int(schema_input)], ask_null_value())
                    xlsx_files = glob.glob(os.path.join(outputpath, "*.csv"))

                else:
                    print("Wrongfiletype")
            get_formated_cols_stats_msg()     

        elif status == "2":
            schema_type= select_schema_type_or_default()
            set_current_schema_file_type(schema_type)
            output_folder = glob.glob(os.path.join(outputpath, "*.csv.gz"))
            if len(output_folder) > 0:
                # Ask for Action (read Excel, send files , empty folder or stop tool)
                print("\n Please choose transfer destination:\n")
                print(f"""
                1) PROD ({CSV_DESTINATION_PROD})
                2) PREPROD ({CSV_DESTINATION_PREPROD})
                \n""" )
                user_input_destination = input("Please enter option: ")
                if user_input_destination == "1":
                    send_files_to_system(CSV_DESTINATION_PROD)
                elif user_input_destination == "2":
                    send_files_to_system(CSV_DESTINATION_PREPROD)
                else:
                    print("Wrong Input please try again!")
            else:
                print("Output-folder is empty. Please generate files first!")
        elif status == "3":
            remove_files_from_dir(outputpath)
        elif status == "0":
            print("Programm will exit")
        else:
            print("\nWrong Input please try again!")

        input("\npress any key to continue:")
