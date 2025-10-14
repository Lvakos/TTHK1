sona = "algus"
gues = ["_"] * len(sona)
count = 3

while count > 0:
    print("Current word:", " ".join(gues))  
    userinput = input("Enter a letter: ").lower()  

    if userinput in sona:
        for i in range(len(sona)):
            if sona[i] == userinput:
                gues[i] = userinput  
        print("The letter ", userinput, " is in the word!")
        print("")
    else:
        count -= 1  
        print("Wrong letter! You have ", count, " attempts left.")
        print("")

    if "_" not in gues:
        print("congrats u got it right")
        break

    if count == 0:
        print("no attempts left. the word was:", sona)
