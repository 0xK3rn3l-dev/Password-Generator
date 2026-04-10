import sys
from gui import GUI_mode
from cli import CLI_mode

def Print_welcome_text():
    Welcome_text = "This tool for generating a random passwords.\n"
    Welcome_text += "You can choose the length and the type your password.\n"
    Welcome_text += "So, what mode you choose: GUI OR CLI? (GUI / CLI): "
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
            return input().strip().upper()
    else:
        Print_welcome_text()
        return input().strip().upper()

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