number = int(input("Give a number to get her divisors"))
divisor_list =[]
for i in range(1,number+1):
    if number%i == 0:
        divisor_list.append(i)
print(divisor_list)
