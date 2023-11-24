#!/usr/bin/python3
''' Module documentation '''
import csv
import requests
import sys


def export_tasks_to_csv(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user data
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    todos_response = requests.get(
        f'{base_url}/todos',
        params={
            'userId': employee_id})

    # Check if both requests were successful
    if user_response.status_code == 200 and todos_response.status_code == 200:
        user = user_response.json()
        todos = todos_response.json()

        # Prepare data for CSV
        tasks_data = [
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        ]
        for task in todos:
            tasks_data.append([
                employee_id,
                user['username'],
                task['completed'],
                task['title']
            ])

        # Write data to CSV
        csv_file_name = f"{employee_id}.csv"
        with open(csv_file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            writer.writerows(tasks_data)

        print(
            f"Tasks for employee {user['name']} have been exported to {csv_file_name}.")
    else:
        print("Failed to fetch data")


# Command line argument check and script execution
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Please enter a user ID.")
        sys.exit(1)
    else:
        user_id = sys.argv[1]
        export_tasks_to_csv(user_id)
