def check_type(input_value):
    # Check if it's an integer
    if input_value.isdigit() or (input_value.startswith('-') and input_value[1:].isdigit()):
        return "Integer"
    
    # Check if it's a float
    if input_value.replace('.', '', 1).isdigit() and input_value.count('.') == 1:
        return "Float"
    
    # If not an int or float, it's a string
    return "String"

# Get user input
user_input = input("Enter a value: ")
result = check_type(user_input)
print(f"The input is of type: {result}")
