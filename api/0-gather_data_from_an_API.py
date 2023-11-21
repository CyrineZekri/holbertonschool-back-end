#!/usr/bin/python3
import requests
import sys

def fetch_todo_list_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user = user_response.json()
        todos = todos_response.json()

        completed_tasks = [task for task in todos if task['completed']]
        total_tasks = len(todos)

        print(f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")
    else:
        print("Failed to fetch data. Please check the employee ID and your internet connection.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_todo_list_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
