#2
#input = int(input("Sisesta number: "))
#while input >= 1:
   # print("Print", input, "korda.")
    #input = input - 1
    
#3
input2 = int(input("sisesta number"))
i = 1
multiplier = 0
while input2 >= i:
    print("Number: ", i)
    multiplier = multiplier + 1
    i = i + multiplier
#4
input3 = int(input("Sisesta number"))
ii = 0
even = 0
odd = 0
while ii < input3:
    ii = ii + 1
    if ii % 2:
        print("Number: ", ii, "Odd")
        odd = odd + 1
    else:
        print("Number: ", ii, "Even")
        even = even + 1
print("Amount of even numbers: ", even)
print("Amount of odd numbers: ", odd)
#5

input4 = int(input("#4/ Sisesta number: "))
iii = 0
while iii <= input4:
    if "3" in str(iii):
        iii = iii + 1
        continue
    print(iii)
    iii = iii + 1

#6
numberr = 0
count = 3
while count != 0:
    ask = int(input("Sisesta number(1-30)"))
    if ask == 12:
        print("Угадал")
        break
    elif ask < 10:
        print("Слишком мало")
        count = count - 1
        continue
    elif ask >= 10 or ask <= 15:
        print("Близко")
        count = count - 1
        continue
    elif ask > 15:
        print("Слишком много")
        count = count - 1
        continue
    
#or
#and
    
#1) kasutaja peab oma paroli sisestama
#2) on võimalus vaadata jääk, välja võtta raha, sisse maksta

parool = "123parol"
jääk = 324
count = 3
insystem = 0

while count > 0:
    kusiparool = input("Sisesta parool")
    if kusiparool == parool:
        insystem = 1
        break
    elif kusiparool != parool:
        print("Wrong password")
        count = count - 1
        continue
    elif count == 0:
        print("Teie kaart blokeeritud")
        break
    
while insystem == 1:
    print("1. välja võtta raha")
    print("2. vaadata jääk")
    print("3. sisse maksta")
    print("4. Logi välja")
    kusi = int(input("Mida sa tahad teha?"))
    if kusi == 1:
        rahavotta = int(input("Kui palju raha sa tahad võtta?: "))
        jääk = jääk - rahavotta
        print("Sa võtad", rahavotta, "eurot. Teie jääk praegu on:", jääk)
        continue
    elif kusi == 2:
        print("Teie jääk praegu on:", jääk)
        continue
    elif kusi == 3:
        sisse = int(input("Kui palju raha sa tahad sisse?"))
        jääk = jääk + sisse
        print("Oled oma kontot", sisse, "euroga täiendanud. Teie jääk praegu on:", jääk)
        continue
    elif kusi == 4:
        break
    elif kusi > 4 or kusi <1:
        print("Wrong choice")

    