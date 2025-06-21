#Task 1
def read_file():
    try:
        with open("sample.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file 'sample.txt' was not found.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))

# Call the function
read_file()


#Task 2 com
def write_and_append_file():
    # Step 1: Write user input to a file
    user_input = input("Enter some text to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(user_input + "\n")

    # Step 2: Append additional input to the same file
    additional_input = input("Enter more text to append to the file: ")
    with open("output.txt", "a") as file:
        file.write(additional_input + "\n")

    # Step 3: Read and display the final content of the file
    print("\nFinal content of output.txt:")
    with open("output.txt", "r") as file:
        for line in file:
            print(line.strip())

# Call the function
write_and_append_file()
