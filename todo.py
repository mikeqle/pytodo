# main.py
import os
from task_manager import add_task, display_tasks, remove_task

def main():
    while True:
        os.system("clear")
        print("\nTo-do List Manager")
        print("-------------------")
        display_tasks()
        user_input = input("Enter anew task, 'r' to remove a task, or 'q' to quit: ").strip()

        if user_input.lower() == 'q':
            break
        elif user_input.lower() == 'r':
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        else:
            add_task(user_input)

if __name__ == "__main__":
    main()
