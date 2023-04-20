import csv
import os
from task_manager import add_task, display_tasks

def main():
    while True:
        print("\nTo-do List Manager")
        print("-------------------")
        display_tasks()
        new_task = input("Enter a new task or type 'q' to quit: ").strip()
        
        if new_task.lower() == 'q':
            break
        else:
            add_task(new_task)

if __name__ == "__main__":
    main()
