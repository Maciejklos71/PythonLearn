def divisible(number,divider=2):
    if number % 4 is 0 and divider== 2:
        print("number {} is even and divisible by 4".format(number))
    elif number%divider is 0:
      print("number {} is even".format(number))
    else:
        print("number {} is odd".format(number))
print("To leve the program write end")
while True:
    try:
        number = int(input("Give number to check is odd or even"))
        divisible(number)
    except :
        print(" It isn't a number,\n do you want to end ?\n Yes/No")
        answer = input()
        if answer.lower() == "yes":
            exit()
        else:
            continue
#print(divisible(20,5))
#print(divisible(31,6))
#print(divisible(20,4))
