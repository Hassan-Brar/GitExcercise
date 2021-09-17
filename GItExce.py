num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
print(num1)
print(num2)

equals=int(num1)+int(num2)

print("Your numbers added together equal to", equals)


if(int(num1) % 2 == 0):                        #Checking if numbers are even or odd
    print(num1 + 'your first number is an even number!')
else:
    print(num1 + 'your first number is an odd number!')

if(int(num2) % 2 == 0):                        
    print(num2 + 'your second number is an even number!')
else:
    print(num2 + 'your second number is an odd number!')