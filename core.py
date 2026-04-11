import sys
from gui import GUI_mode
from cli import CLI_mode

def Print_welcome_text():
    logo = r"""
 ____                                     _ 
|  _ \ __ _ ___ _____      _____  _ __ __| |
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
    """
    print(logo)
    Welcome_text = "\nThis tool for generating a random passwords.\n"
    Welcome_text += "You can choose the length and the type your password.\n"
    Welcome_text += "So, what mode you choose: GUI OR CLI? (GUI / CLI): \n"
    print(Welcome_text)

def get_mode_input():
    if len(sys.argv) > 1:
        mode = sys.argv[1].upper()
        if mode in ["GUI", "CLI"]:
            return mode
        else:
            print(f"[ERROR] Invalid mode '{sys.argv[1]}' provided as argument. Please choose GUI or CLI\n")
            sys.argv.pop(1)
            Print_welcome_text()
            return input('> ').strip().upper()
    else:
        Print_welcome_text()
        return input('> ').strip().upper()

def choose_mode():
    mode = get_mode_input()
    modes = {
        "GUI": GUI_mode,
        "CLI": CLI_mode
    }

    if mode in modes:
        return modes[mode]()
    else:
        print(f"[ERROR]Invalid mode {mode}. Please choose GUI or CLI.\n")
        return choose_mode()