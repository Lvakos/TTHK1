arv1 = int(input("Sisesta esimene arv: "))
operaator = input("Sisesta operaator(+, -, *, /): ")
if operaator == "+" or operaator == "-" or operaator == "*" or operaator == "/":
    print("")
else:
    print("incorrect operaator")
    exit()
arv2 = int(input("Sisesta teine arv: "))

if operaator == "/" and arv1 == 0 or arv2 == 0:
    print("Cannot devide using 0")
    exit()
else:
    print("")

if operaator == "+":
    print(arv1 + arv2)
elif operaator == "-":
    print(arv1 - arv2)
elif operaator == "*":
    print(arv1 * arv2)
elif operaator == "/":
    print(arv1 / arv2)
