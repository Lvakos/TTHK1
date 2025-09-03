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

#kirjuta programm mis küsib kasutajalt järgmised andmed
# nimi
# vanus
 #elukoht(linn)
 #lemmikfilm
 #lemmikmuusik
# kolm lemmiktoitu
 
#1. salvesta iga sastus eraldi muutujasse
#2. väljesta tervitustekst, kus kasutakse nimi ja vanus
#3. väljesta lause elukoha kohta
#4. väljesta lause lemmikfilmi kohta ja muusika kohta
#5. väljesta kõik toidud ühes lauses. (Minu lemmiktoidud on ?,? ja ?)
print("=================================================================================")

nimi = input("What is your name?: ")
vanus = input("How old are you?: ")
elukoht = input("Where do you live? (City): ")
lemmikfilm = input("What your favourite movie?: ")
lemmikmuusik = input("What yours favourite song? ")
lemmiktoitu = input("What's your three favourite food?(Name only food, (burger, hotdog and pizza): ")

print("=================================================================================")
print("Welcome ", nimi)
print("You're ", vanus + " years old")
print("You're living in ", elukoht)
print("Your favourite movie is: ", lemmikfilm)
print("Your favourite song is: ", lemmikmuusik)
print("And your three favourite food are: ", lemmiktoitu)
print("Done!")