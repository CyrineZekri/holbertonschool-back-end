#!/usr/bin/python3
''' Module documentation '''
import csv
import requests
import sys


def export_tasks_to_csv(employee_id):
    '''Export tasks to a CSV file for the given employee ID.'''
    try:
        base_url = 'https://jsonplaceholder.typicode.com'

        user_response = requests.get(f'{base_url}/users/{employee_id}')
        user_response.raise_for_status()
        user = user_response.json()

        todos_response = requests.get(
            f'{base_url}/todos',
            params={'userId': employee_id})
        todos_response.raise_for_status()
        todos = todos_response.json()

        
        tasks_data = [
            ["USER_ID", "USERNAME", "EMPLOYEE_NAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        ]
        for task in todos:
            tasks_data.append([
                employee_id,
                user['username'],
                user['name'],  
                task['completed'],
                task['title']
            ])

        csv_file_name = f"{employee_id}.csv"
        with open(csv_file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            writer.writerows(tasks_data)

        print(
            f"Tasks for employee {user['name']} have been exported to {csv_file_name}.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Please enter a user ID.")
        sys.exit(1)
    else:
        user_id = sys.argv[1]
        export_tasks_to_csv(user_id)
