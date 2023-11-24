#!/usr/bin/python3
''' Module documentation'''
import csv
import requests

def export_tasks_to_csv(user_id):
    user_response=requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    if user_response.status_code!=200:
        return f"error fetching user data "
    user_data=user_response.json()
    tasks_response=requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
    if tasks_response.status_code!=200:
        return f"error fetching tasks "
    tasks_data=tasks_response.json()
    csv_data=[["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]]
    for task in tasks_data:
        csv_data.append([user_id], user_data, )