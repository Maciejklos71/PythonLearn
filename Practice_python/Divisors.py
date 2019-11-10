number = int(input("Give a number to get her divisors"))
divisor_list = [i for i in range(1, number+1) if number % i == 0]
print(divisor_list)
