# task_manager.py
import csv
import os
from datetime import datetime
import textwrap

task_file_path = "/Users/mike/git-projects/2023/to-do-list/tasks.csv"

def get_date_obj(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()

def add_task(task_description):
    if task_description.strip():
        while True:
            due_date = input("Enter the due date (YYYY-MM-DD): ").strip()
            try:
                due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
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
        
        task_number = get_last_task_number()
        with open(task_file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([task_description, due_date, priority, 0, task_number])
    else:
        print("Task description cannot be an empty string.")

def display_tasks():
    if os.path.exists(task_file_path):
        with open(task_file_path, "r") as file:
            tasks = [row for row in csv.reader(file) if row[3] == "0"]
            tasks.sort(key=lambda task: (int(task[2]), get_date_obj(task[1]), int(task[4])))

            if len(tasks) == 0:
                print("No tasks yet. Start adding tasks!")
                return
            
            print("\nTo-do List:")
            print("No. | Description                                          | Due Date  | Priority")
            print("----+------------------------------------------------------+-----------+----------")
            for task in tasks:
                index = int(task[4])
                wrapped_description = textwrap.fill(task[0], width=50)
                wrapped_lines = wrapped_description.splitlines()
                print(f"{index: <4}| {wrapped_lines[0]: <53}| {task[1]: <10}| {task[2]: <9}")
                for line in wrapped_lines[1:]:
                    print(f"    | {line: <53}|           |         ")
            print("----+------------------------------------------------------+-----------+----------")

    else:
        print("\nNo tasks yet. Start adding tasks!")

def remove_task(task_number=None):
    if task_number is None:
        try:
            task_number = int(input("Enter the task number to remove: "))
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
            return

    if os.path.exists(task_file_path):
        with open(task_file_path, "r") as file:
            tasks = list(csv.reader(file))

        found_task = False
        for task in tasks:
            if task[4] == str(task_number):
                tasks.remove(task)
                found_task = True
                break

        if found_task:
            with open(task_file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(tasks)
            print(f"Task {task_number} has been removed.")
        else:
            print(f"No task with task number {task_number} found.")
    else:
        print("No tasks file found.")


def mark_task_done(task_number):
    if os.path.exists(task_file_path):
        with open(task_file_path, "r") as file:
            tasks = list(csv.reader(file))

        found_task = False
        for task in tasks:
            if task[4] == str(task_number):
                task[3] = "1"
                found_task = True
                break

        if found_task:
            with open(task_file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(tasks)
            print(f"Task {task_number} marked as done.")
        else:
            print(f"No task with task number {task_number} found.")
    else:
        print("No tasks file found.")


def get_last_task_number():
    if os.path.exists(task_file_path):
        with open(task_file_path, "r") as file:
            tasks = list(csv.reader(file))
            # return max value of the fifth column (task number)
            return max(int(task[4]) for task in tasks) + 1
    else:
        return 0