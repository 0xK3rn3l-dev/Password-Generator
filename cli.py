from utils import generate_multiple_passwords
import time
import os
from utils import clear_screen

# FOR LINUX
#from tqdm import tqdm 
# Also platform.system() to check
# also need to add mac realisation
#need to add list passwords for gui
# test mb unitest or pytest? 

from alive_progress import alive_bar

def save_passwords_to_file(passwords, filename=None):
    if filename is None:
        filename = input("Enter filename to save passwords (default passwords.txt): ") or "passwords.txt"

    if not filename.endswith('.txt'):
        filename += '.txt'
    
    save_dir = "passwords"
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as file:
        for pwd in passwords:
            file.write(pwd + '\n')
    print(f"Passwords saved to:\n")
    print(f"  - filename: {filepath}\n")


def get_yes_no_input(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print("[ERROR] Invalid input! Please enter 'y' or 'n'.\n")

def add_description(pwd, description):
    return f"{pwd} | {description}"


def CLI_mode():
    cli_welcome =  ("\n\t\t\t\t==============================\n")
    cli_welcome += ("\t\t\t\t    Password Generator CLI    \n")
    cli_welcome += ("\t\t\t\t==============================\n")
    print(cli_welcome)

    while True:
        try:
            length = int(input("Password length (default 12): ") or "12")
            use_upper = input("Use uppercase? (y/n, default y): ").lower() != 'n'
            use_lower = input("Use lowercase? (y/n, default y): ").lower() != 'n'
            use_digits = input("Use digits? (y/n, default y): ").lower() != 'n'
            use_special = input("Use special chars? (y/n, default y): ").lower() != 'n'
            count = int(input("How many passwords? (default 1): ") or "1")

            print("Generating passwords...")
            passwords = []

            with alive_bar(count, title="Progress", bar="smooth", spinner="dots_waves") as bar:
                for _ in range(count):
                    pwd = generate_multiple_passwords(1, length=length, 
                                                    use_uppercase=use_upper, 
                                                    use_lowercase=use_lower, 
                                                    use_digits=use_digits, 
                                                    use_special=use_special)[0]
                    passwords.append(pwd)
                    bar()
                    time.sleep(0.01)

            print("Generation complete!\n")
            
            print("Generated passwords:")
            print("-" * 30)
            for i, pwd in enumerate(passwords, 1):
                print(f"{i}. {pwd}")
            print("-" * 30 + "\n")
            

            add_desc_choice = get_yes_no_input("Add description to passwords? (y/n): ")
            passwords_with_desc = passwords.copy()
            
            if add_desc_choice == 'y':
                while True:
                    print("\nCurrent passwords:")
                    for i, pwd in enumerate(passwords_with_desc, 1):
                        print(f"{i}. {pwd}")
                    
                    choice = input("\nEnter password number(s) to add/change description (e.g., '1,3,5' or 'all'), or 'done' to finish: ").strip().lower()

                    if choice == 'done':
                        break
                    elif choice == 'all':
                        for i in range(len(passwords_with_desc)):
                            desc = input(f"Description for password {i+1}: ").strip()
                            if desc:
                                passwords_with_desc[i] = add_description(passwords[i], desc)
                        print("\n[OK] Descriptions added to all passwords.")
                    else:
                        try:
                            numbers = [int(x.strip()) for x in choice.split(',')]
                            valid_numbers = [n for n in numbers if 1 <= n <= len(passwords_with_desc)]
                            
                            if not valid_numbers:
                                print("[ERROR] No valid numbers entered.")
                                continue
                            
                            for num in valid_numbers:
                                desc = input(f"Description for password {num}: ").strip()
                                if desc:
                                    passwords_with_desc[num-1] = add_description(passwords[num-1], desc)
                            
                            print(f"[OK] Descriptions added to passwords: {', '.join(map(str, valid_numbers))}")
                        except ValueError:
                            print("[ERROR] Invalid input. Please enter numbers separated by commas.")
                

                print("\nFinal passwords with descriptions:")
                print("-" * 40)
                for i, pwd in enumerate(passwords_with_desc, 1):
                    print(f"{i}. {pwd}")
                print("-" * 40 + "\n")
            else:
                print("\nFinal passwords:")
                print("-" * 30)
                for i, pwd in enumerate(passwords, 1):
                    print(f"{i}. {pwd}")
                print("-" * 30 + "\n")


            save_choice = get_yes_no_input("Save passwords to file? (y/n): ")
            if save_choice == 'y':
                    if add_desc_choice == 'y':
                        filename = input("Enter base filename (default: passwords): ") or "passwords"
                        print()
                        save_passwords_to_file(passwords_with_desc, filename + ".txt")
                    else:
                        save_passwords_to_file(passwords)
            else:
                print("Passwords not saved.\n")


            continue_choice = get_yes_no_input("Generate more passwords? (y/n): ")
            if continue_choice == 'n':
                print("\nGoodbye!")
                break
            else:
                clear_screen()
                print("\n\t\t\t\t" + "="*50)
                print("\t\t\t\t\t    Generating new passwords...")
                print("\t\t\t\t" + "="*50 + "\n")
                continue
                

        except ValueError:
            print("[ERROR] Invalid input! Please enter a valid number.\n")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}\n")