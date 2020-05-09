while True:
    try:
        # Get input with prompt.
        code = input("Enter your code: ")
        # Break if user types q.
        if code == "q":
            break
        # Attempt to parse input.
        value = int(code)
        print("Value:", value)
    except:
        print("Invalid code")

