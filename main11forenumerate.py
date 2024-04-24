fruit = ["яблоко","банан","груша","апельсин"]

for i,value in enumerate(fruit,1):
    if i == 2:
        continue
    print(str(i) + " - " + value)