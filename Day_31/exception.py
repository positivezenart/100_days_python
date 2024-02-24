try:
    file = open("Day_31/data.txt")
    dictionary_val ={"card":"dead"}
    print(dictionary_val["card"])
except FileNotFoundError:
    file=open("Day_31/data.txt","w")
    file.write("do something")
except KeyError as e:
     print(f"{e} key doesnt exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file is closed successfully")

    