# task_manager.py

import csv
import os
from datetime import datetime

def add_task(task_description):
    if task_description.strip():
        while True:
            due_date = input("Enter the due date (YYYY-MM-DD): ").strip()
            try:
                due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
                if due_date_obj >= datetime.now().date():
                    break
                else:
                    print("Please enter today's date or a future date.")
            except ValueError:
                print("Invalid date format. Please use 'YYYY-MM-DD'.")

        while True:
            priority = input("Enter the priority (0, 1, 2, 3): ").strip()
            if priority in ('0', '1', '2', '3'):
                break
            else:
                print("Invalid priority. Please enter 0, 1, 2, or 3.")

        with open("tasks.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([task_description, due_date, f"P{priority}"])
    else:
        print("Task description cannot be an empty string.")

def display_tasks():
    if os.path.exists("tasks.csv"):
        with open("tasks.csv", "r") as file:
            tasks = list(csv.reader(file))
            print("\nTo-do List:")
            print("No. | Description            | Due Date  | Priority")
            print("----+------------------------+-----------+----------")
            for index, task in enumerate(tasks, start=1):
                print(f"{index: <4}| {task[0]: <22}| {task[1]: <10}| {task[2]}")
    else:
        print("\nNo tasks yet. Start adding tasks!")

def remove_task(task_number=None):
    if task_number is None:
        try:
            task_number = int(input("Enter the task number to remove: "))
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
            return

    with open("tasks.csv", "r") as file:
        tasks = list(csv.reader(file))

    if 0 < task_number <= len(tasks):
        del tasks[task_number - 1]

        with open("tasks.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
    else:
        print("Invalid task number. Please try again.")