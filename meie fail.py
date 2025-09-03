print(1+1)
print("1"+"1")
# print("1"+1) # on keelatud!!

# Andme tüübid
# "hello world" - str
# 1 - int
# 1.5 - float

# muutujad
name = "Maksimilian"
perekonnanimi = "Puhtejev"
print(name+" "+perekonnanimi)

# luua muutujad film, aasta, rezisöör, näitleja ja näitleja 2
# tulemus: Film matrix ilmus aastal 1999, rezisöör on wachowski, ning peanäitlejad on Keanu Reeves ja Laurence Fishburne

filminimi = "Skinning"
aasta = "2010"
rezisöör = "Stevan Filipović"
naitleja1 = "Nikola Rakočević"
naitleja2 = "Viktor Savić"
naitleja3 = "Bojana Novakovic"

print("Film "+ filminimi+ " ilmus aastal "+ aasta+ ", rezisöör on " + rezisöör + ", ja peanäitlejad seal on "+ naitleja1+ ", "+ naitleja2+ " ja "+ naitleja3+ ".")

# str() - text -- arv
# int() - arv -- text

lemmikloom = input("Sisesta oma lemmik loom: ")
print("Minu lemmikloom on: " + lemmikloom)

pikkus = int(input("sisesta pikkus: "))
laius = int(input("sisesta laius: "))
umbermot = 2 * (pikkus + laius)
pindala = pikkus * laius
print("ümbermõõt: ", umbermot)
print("laius: ", laius)