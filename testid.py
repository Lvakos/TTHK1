# while menüü ja tekstitöötlus
# A)
text = ""
while True:
    print("1. Sisesta tekst")
    print("2. Kärbi servad (strip)")
    print("3. Eemalda topeltvahed kuni ühekordseks")
    print("4. Näita pikkust ilma tühikuteta")
    print("5. Välju")
    sisesta = int(input("Hello, this is a menu to remove spaces. Choose what you want to do(Kirjuta ainult number): "))
    if sisesta == 1:
        tekst = str(input("Sisesta tekst: "))
        text = tekst
        continue
    elif sisesta == 2:
        if text:
            strip = text.strip()
            text = strip
            print("Done, new text: ", text)
        else:
            print("Esmalt, sisestage tekst")
            continue
    elif sisesta == 3:
        if text:
            while "  " in text:
                text = text.replace("  ", " ")
                print("Sinu text: ", text)
        else:
            print("Esmalt, sisestage tekst")
            continue
    elif sisesta == 4:
        if text:
            print("Sinu text: ", text)
            continue
        else:
            print("Esmalt, sisestage tekst")
            continue
    elif sisesta == 5:
        print("Good bye!")
        break
    else:
        print(" INCORRECT NUMBER ")
        continue
#B)
while True:
    nimi = input("Sisesta nimi: ")
    if len(nimi) > 12:
        print("Too long nimi")
        continue
    elif len(nimi) < 4:
        print("Too small nimi")
        continue
    elif not nimi.isalnum():
        print("There's symbols in nimi")
        continue
    if " " in nimi:
        print("There's spaces in nimi")
    else:
        print("Correct nimi")
        break