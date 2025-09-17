#näide 1
question = int(input("Sisesta sinu vanus"))
if question >= 18:
    text = "sa oled täiskasvane"
else:
    text = "sa oled liiga noor"
    
print(text)

#näide 2
ask = int(input("Sisesta number"))

if ask % 2:
    print("odd")
else:
    print("even")
#näide 3
ask1 = int(input("Sisesta esimene arv"))
ask2 = int(input("Sisesta teine arv"))
ask3 = int(input("Sisesta kolmas arv"))

if ask1 > ask2 and ask1 > ask3:
    print(ask1, "is higher than other numbers")
elif ask2 > ask1 and ask2 > ask3:
    print(ask2, "is higher than other numbers")
elif ask3 > ask2 and ask > ask1:
    print(ask3, "is higher than other numbers")
    
#hinde määramine punktide põhjal
hind = int(input("Sisesta punktid (1-100): "))
if hind <60:
    print("Sinu hind on D")
elif hind >= 60 and hind <= 74:
    print("Sinu hind on C")
elif hind >=75 and hind <= 89:
    print("Sinu hind on B")
elif hind >=90 and hind <=100:
    print("Sinu hind on A")
else:
    print("Incorrect points")