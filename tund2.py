# Ülesanne 1
print("Ülesanne 1")
nr1 = int(input("Sisesta esimene täisarv: "))
nr2 = int(input("Sisesta teine täisarv: "))

summa = nr1 + nr2
print("Summa on: ", summa)

vahe = nr1 - nr2
print("Vahe on: ", vahe)

korrutis = nr1 * nr2
print("Korrutis on: ", korrutis)

print("=================================================================================")
# Ülesanne 2
print("Ülesanne 2")

name = input("Sisesta sinu nimi: ")
vanus = int(input("Sisesta sinu vanus: "))
vanuscounted = 2025 - vanus

print("Tere, ", name, "!")
print("Sinu sünniaasta on: ", vanuscounted)
print("=================================================================================")
# Ülesanne 3
print("Ülesanne 3")

seconds = int(input("Sisesta sekundid: "))
if seconds < 1:
    print("incorrect number")
minutescalc = int(seconds / 60) % 60
hourscalc = int(seconds / 3600)
secondscalc = seconds % 60 

if seconds > 0:
    print(f"Tegemist ajaga (HH:MM:SS): {hourscalc:0}:{minutescalc:0}:{secondscalc:0}")
print("=================================================================================")
# Ülesanne 4
print("Ülesanne 4")

arv1 = float(input("Sisesta esimene arv (a): "))
arv2 = float(input("Sisesta teine arv (b): "))

print("Enne vahetamist: a =", arv1, "b =", arv2)
print("Peale vahetamist: a =", arv2, "b =", arv1)

print("=================================================================================")
# Ülesanne 5
print("Ülesanne 5")

lennunumber = int(input("Sisesta lennu number(3 tähe kood): "))
väljumislennujaamakood = input("Sisesta väljumislennujaama kood (3 tähe kood, nt TLL): ")
sihtlennujaamakood = input("Sisesta sihtlennujaama kood (3 tähe kood, nt HEL): ")

väljumiseaeg = input("Sisesta väljumise aeg (TT:MM): ")
hours_str, minutes_str = väljumiseaeg.split(":")
hoursstr = int(hours_str)
minutesstr = int(minutes_str)

addedhours = 2
addedminutes = 30

if minutesstr >= 60:
    hoursstr += minutesstr // 60
    minutesstr = minutesstr % 60
hoursstradded = hoursstr + addedhours
hoursstrs = hoursstradded % 24

minutesstradded = minutesstr + addedminutes
minutesstrs = minutesstradded % 60

print("****************************************")
print("*         AirBaltics Airlines          *")
print("*                                      *")
print("*   Lennu number: XY", lennunumber, "                *")
print("*                                      *")
print("*   ", väljumislennujaamakood,"->", sihtlennujaamakood,"                         *")
print("*                                      *")
print(f"*  Väljumine: {väljumiseaeg} Saabumine: {hoursstrs:02d}:{minutesstrs:02d}  *")
print("*****************************************")

