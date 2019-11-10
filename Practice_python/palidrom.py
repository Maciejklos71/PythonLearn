#Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
def palidrom(string):
    string = string.lower().replace(" ","")
    for i in range(0,len(string)):
        if string[i]==string[-i-1]:
            if i == len(string)-1:
                print("This string is palidrom!")
            continue
        if string[i]!=string[-i-1]:
            print("This string isn't palidrom")
            exit()
        print("This string is palidrom!")
palidro = "a tu mam mamuta".lower().replace(" ","")
palidrom(palidro)


