while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Choose the operation (+, -, *, /): ")
        
        if operator == '+':
            print(f"{num1} + {num2} = {num1+num2}")
        elif operator == '-':
            print(f"{num1} - {num2} = {num1-num2}")
        elif operator == '*':
            print(f"{num1} * {num2} = {num1*num2}")
        elif operator == '/':
            print(f"{num1} / {num2} = {num1/num2}")
        else:
            print("Invalid operation selected. Please try again.")
            continue  # Invalid operation selected, ask the user for input again
        
        is_continue = input("Do you want to perform another calculation? (Y/N): ")
        if is_continue.lower() == 'n':
            break
            
    except ValueError:
        print("Please enter numeric values only.")
