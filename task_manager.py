# task_manager.py

import csv
import os

def add_task(task):
    with open("tasks.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([task])

def display_tasks():
    if os.path.exists("tasks.csv"):
        with open("tasks.csv", "r") as file:
            tasks = list(csv.reader(file))
            print("\nTo-do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task[0]}")
    else:
        print("\nNo tasks yet. Start adding tasks!")

def remove_task(task_number):
    with open("tasks.csv", "r") as file:
        tasks = list(csv.reader(file))
        
    if 0 < task_number <= len(tasks):
        del tasks[task_number - 1]

        with open("tasks.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
    else:
        print("Invalid task number. Please try again.")
