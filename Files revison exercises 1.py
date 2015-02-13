#Callum

with open ("files1.txt",mode="w",encoding="utf-8") as new_file:
    for files in range(5):
        files = input("Please enter your line of text: ")
        new_file.write(files)
        new_file.write("\n")



with open ("files1.txt",mode="r",encoding="utf-8") as new_file:
    for line in new_file:
        print(line,end="")
