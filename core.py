import sys
from gui import GUI_mode
from cli import CLI_mode
from utils import clear_screen


def Print_welcome_text():
    logo = r"""
                                                                    _                        
                                                                   | |                       
                          _ __   __ _ ___ _____      _____  _ __ __| |______ __ _  ___ _ __  
                         | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` |______/ _` |/ _ \ '_ \ 
                         | |_) | (_| \__ \__ \\ V  V / (_) | | | (_| |     | (_| |  __/ | | |
                         | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|      \__, |\___|_| |_|
                         | |                                                 __/ |           
                         |_|                                                |___/           

                                                                        (by 0xK3rn3l)
    """
    Welcome_text = "\n\t\t\t\tThis tool for generating a random passwords.\n"
    Welcome_text += "\t\t\t\tYou can choose the length and the type your password.\n"
    Welcome_text += "\t\t\t\tSo, what mode you choose: GUI OR CLI? (GUI / CLI): \n"
    clear_screen()
    print(logo + Welcome_text)

def get_mode_input():
    if len(sys.argv) > 1:
        mode = sys.argv[1].upper()
        if mode in ["GUI", "CLI"]:
            clear_screen()
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
        clear_screen()
        return modes[mode]()
    else:
        print(f"[ERROR]Invalid mode {mode}. Please choose GUI or CLI.\n")
        return choose_mode()