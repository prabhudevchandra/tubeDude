#Task 1: Create a Dictionary of Student Marks

std_data = {'chandu':426,'malli':576,'bharati':543,'kallesh':376}
userAsk = input("Enter the Student's name: ").lower()
if userAsk in std_data:
    marks = std_data[userAsk]
    print(f'{userAsk} marks is {marks}')
else:
    print("Student not found")


# Task 2: Demonstrate List Slicing
l = []
for i in range(1,11):
    l.append(i)
print(f'Original list: {l}')
e = l[:5]
print(f'Extracted first five elements: {e}')
r = e[::-1]
print(f'Reversed extracted elements: {r}')

