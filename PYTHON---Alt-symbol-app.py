def choose_alt_symbol():
    print("🎉 Welcome to the ALT Symbol Selector! 🎨")
    print("🔤 Use ALT codes to generate special characters (e.g., ALT+65 = 'A').")
    print("✨ Enter a valid ALT code (1-255) to see the corresponding symbol.")
    print("🔍 Type 'exit' to quit the program.\n")

    while True:
        user_input = input("Enter an ALT code or 'exit': ").strip().lower()
        
        if user_input == 'exit':
            print("👋 Goodbye! Have a great day! 🌟")
            break
        
        if user_input.isdigit():
            alt_code = int(user_input)
            if 1 <= alt_code <= 255:
                symbol = chr(alt_code)
                print(f"🌟 ALT+{alt_code} generates the symbol: '{symbol}'")
            else:
                print("⚠ ALT code must be between 1 and 255. Please try again!")
        else:
            print("❌ Invalid input. Please enter a number or 'exit'.")

# Run the function
choose_alt_symbol()
