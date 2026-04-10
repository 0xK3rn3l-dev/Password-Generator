from utils import generate_multiple_passwords, score_password

def save_passwords_to_file(passwords):
    filename = input("Enter filename to save passwords (default passwords.txt): ") or "passwords.txt"
    with open(filename, 'w') as file:
        for pwd in passwords:
            file.write(pwd + '\n')
    print(f"Passwords saved to {filename}\n")


def get_yes_no_input(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print("[ERROR] Invalid input! Please enter 'y' or 'n'.\n")


def CLI_mode():
    print("=== Password Generator CLI ===\n")

    while True:
        try:
            length = int(input("Password length (default 12): ") or "12")
            use_upper = input("Use uppercase? (y/n, default y): ").lower() != 'n'
            use_lower = input("Use lowercase? (y/n, default y): ").lower() != 'n'
            use_digits = input("Use digits? (y/n, default y): ").lower() != 'n'
            use_special = input("Use special chars? (y/n, default y): ").lower() != 'n'
            count = int(input("How many passwords? (default 1): ") or "1")

            passwords = generate_multiple_passwords(count, length=length, 
                                                    use_uppercase=use_upper, use_lowercase=use_lower, 
                                                    use_digits=use_digits, use_special=use_special)
            
            for i, pwd in enumerate(passwords, 1):
                score_info = score_password(pwd)
                print(f"{i}. {pwd}")
                print(f"   └─ Score: {score_info['score']}, Level: {score_info['level']}, Color: {score_info['color']}, {score_info['text']}\n")

            save_choice = get_yes_no_input("Save passwords to file? (y/n): ")
            if save_choice == 'y':
                save_passwords_to_file(passwords)
            else:
                print("Passwords not saved.\n")


            continue_choice = get_yes_no_input("Generate more passwords? (y/n): ")
            if continue_choice == 'n':
                print("\nGoodbye!")
                break
            else:
                print("\n" + "="*50)
                print("Generating new passwords...")
                print("="*50 + "\n")
                continue
                

        except ValueError:
            print("[ERROR] Invalid input! Please enter a valid number.\n")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}\n")



