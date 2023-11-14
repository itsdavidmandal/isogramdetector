inputfromuser= input("Enter the phrase or word ")
tobeprocessed=inputfromuser.lower()

for x in tobeprocessed:
    if tobeprocessed.count(x)== 1:
        print("true")
        break
    else:
        print("false")
        break
