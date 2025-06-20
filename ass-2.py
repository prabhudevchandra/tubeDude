#Task 1: Check if a Number is Even or Odd

userInput = int(input("Enter a number: "))

if userInput %2 ==0:
    print(f"{userInput} is an even number.")
else:
    print(f"{userInput} is an odd number.")


#Task 2: Sum of Integers from 1 to 50 Using aLoop
sum = 0

for i in range(1,51):
    sum += i
print(f"The sum of numbers from 1 to 50 is : {sum}")

