#!/usr/bin/python3
''' Module documentation'''
import csv
import requests
from sys import argv
BASE_URL = 'https://jsonplaceholder.typicode.com'


def export_tasks_to_csv(employee_id):
    try:
        response = requests.get(f'{BASE_URL}/users/{employee_id}')
        response.raise_for_status()
        user_data = response.json()
        employee_name = user_data.get('name')

        response = requests.get(f'{BASE_URL}/todos', params={'userId': employee_id})
        response.raise_for_status()
        todos = response.json()

        csv_file_name = f"{employee_id}.csv"
        with open(csv_file_name, "w", newline='') as csv_file:
            fieldnames = [
                "USER_ID",
                "USERNAME",
                "EMPLOYEE_NAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"
            ]
            writer = csv.DictWriter(
                csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            
            writer.writeheader()

            for task in todos:
                writer.writerow({
                    "USER_ID": employee_id,
                    "USERNAME": user_data.get('username'),
                    "EMPLOYEE_NAME": employee_name,
                    "TASK_COMPLETED_STATUS": task['completed'],
                    "TASK_TITLE": task['title']
                })

        print(f"Tasks for employee {employee_name} have been exported to {csv_file_name}.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)

    employee_id = int(argv[1])
    export_tasks_to_csv(employee_id)
