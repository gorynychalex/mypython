import os

print(os.getcwd())

with open(os.getcwd()+"\\textfile01.txt","r",encoding="UTF-8") as file1:
    for line in file1:
        print(line.strip())