# function declaration
def file_operation():
    file_input = input("Enter the file to be read :")
    try:
        with open(file_input, "r"):
            data = file.read()
        data_modification = data.lower()
        new_data_file = input("Enter the file to write to")
        with open(new_data_file, "w") as output_file:
            output_file.write(data_modification)

        print("The new data is written to {output_file}") 
        exception FileNotFoundError:
            print("the {file_input} was not found")
        exception IOError:
            print("An error occurred when reading '{file_input}' or in writing to '{output_file}'")       

file_operation()