import json

# Open file
f = open('src\datas\datajson1.txt',encoding="UTF-8")

# read content
rawf = f.read()
# cut first wierd symbol
jsonstring=rawf[1:]
data = json.loads(jsonstring)

# Read data
for i in data:
    print()
    for j in i.keys():
        print(j," : ",i[j])

# Save file
with open("src\datas\datajson1.json","w",encoding='UTF-8') as file:
    json.dump(data,file)