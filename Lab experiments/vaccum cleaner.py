location = "A"
A = "Dirty"
B = "Dirty"

while A == "Dirty" or B == "Dirty":

    if location == "A":
        if A == "Dirty":
            print("Suck dirt from A")
            A = "Clean"
        else:
            print("Move Right")
            location = "B"

    elif location == "B":
        if B == "Dirty":
            print("Suck dirt from B")
            B = "Clean"
        else:
            print("Move Left")
            location = "A"

print("Both locations are clean!")
