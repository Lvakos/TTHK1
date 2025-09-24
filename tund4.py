#Ülesanne 1
hour = int(input("Sisesta tund aeg (1-24): "))

if hour <=6:
    print("Öö")
elif hour <=12:
    print("Hommik")
elif hour <=18:
    print("Päev")
else:
    print("Õhtul")
    
print("===============================================")
#Ülesanne 2
preference = input("Sisesta preference(Kuum või külm): ")

if preference == "kuum":
    typee = input("Sisesta type (tee või kohv): ")
    if typee == "tee":
        print("Valmistame teed")
    elif typee == "kohv":
        print("Valmistame kohvi")
    else:
        print("Incorrect type")
elif preference == "külm":
    print("Väljasta Limonaad")
else:
    print("Incorrect preference")
    exit()
    
print("===============================================")
#Ülesanne 3
color = input("Sisesta värv(Punane, sinine või muu): ")

if color == "punane":
    print("Ere")
elif color == "sinine":
    print("Rahulik")
else:
    print("Tavaline")
    
print("===============================================")
#Ülesanne 4
transport = input("Sisesta transport(Buss või jalgsi): ")
ilm = input("Sisesta ilm(vihm või päike): ")

if transport == "buss":
    if ilm == "vihm":
        print("Sõidame bussiga katuse all")
    else:
        print("Sõidame bussiga mugavalt")
else:
    if ilm == "vihm":
        print("Võtame vihmavarju")
    else:
        print("Läheme jalgsi")

print("===============================================")
#Ülesanne 5
vili = input("Sisesta vili type(Puuvili või köögivili: ")
if vili == "puuvili" or vili == "köögivili":
    print("Nice")
else:
    print("Incorrect type")
    exit()
taste = input("sisesta maitse(Magus, hapu või muu): ")

if vili == "puuvili" and taste == "magus":
    print("Söödav puuvili")
elif vili == "puuvili" and taste == "hapu":
    print("Vitamiinirikas puuvili")
elif vili == "puuvili" and taste == "muu":
    print("Tavaline puuvili")
    exit()
    
if vili == "köögivili" and taste == "magus":
    print("Magus köögivili")
elif vili == "köögivili" and taste == "hapu":
    print("Hapu köögivili")
elif vili == "köögivili" and taste == "muu":
    print("Tavaline köögivili")
exit()