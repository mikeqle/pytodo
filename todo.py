# main.py

import os
from task_manager import add_task, display_tasks, remove_task, mark_task_done, update_task

def clear_screen():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # macOS and Linux
        os.system("clear")

def main():
    last_message = ""

    while True:
        clear_screen()

        print("\nTo-do List Manager")
        print("-------------------")
        
        if last_message:
            print(last_message, "\n")
            last_message = ""
        display_tasks()

        try:
            user_input = input("Enter a new task, 'r' to remove, 'd' to mark done, 'u' to update, or 'q' to quit: \n").strip()

            if user_input.lower() == 'q':
                break
            elif user_input.lower().startswith('r-'):
                try:
                    task_number = int(user_input[2:].strip())
                    remove_task(task_number)
                    last_message = "Task removed successfully."
                except ValueError:
                    last_message = "Invalid input. Please enter 'r-' followed by a valid task number."
            
            elif user_input.lower().startswith('d-'):
                try:
                    task_number = int(user_input[2:].strip())
                    mark_task_done(task_number)
                    last_message = "Task marked as done."
                except ValueError:
                    last_message = "Invalid input. Please enter 'd-' followed by a valid task number."
            
            elif user_input.lower().startswith('u-'):
                try:
                    task_number = int(user_input[2:].strip())
                    update_task(task_number)
                    last_message = "Task updated successfully."
                except ValueError:
                    last_message = "Invalid input. Please enter 'u-' followed by a valid task number."
            else:
                add_task(user_input)
                last_message = "Task added successfully."
        except KeyboardInterrupt:
            last_message = "Interrupt detected. Restarting task input."
            continue

        

if __name__ == "__main__":
    main()