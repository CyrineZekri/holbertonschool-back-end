#!/usr/bin/python3
''' Module documentation'''
import json
import requests
import sys


def export_tasks_to_json(employee_id):
    '''Export tasks to a JSON file for the given employee ID.'''
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

        json_data = {str(employee_id): []}
        for task in todos:
            json_data[str(employee_id)].append({
                "task": task['title'],
                "completed": task['completed'],
                "username": user['username']
            })

        json_file_name = f"{employee_id}.json"
        with open(json_file_name, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Tasks for employee {user['name']} have been exported to {json_file_name}.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        user_id = sys.argv[1]
        export_tasks_to_json(user_id)
