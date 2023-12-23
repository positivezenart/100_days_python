with open("Day_24\ew_file.txt", encoding="utf-8", mode ="w") as f:
     f.write(" \n what the fuck?")

with open("Day_24\my_file.txt", encoding="utf-8") as f:
    read_data = f.read()
f.close()

print(read_data)




