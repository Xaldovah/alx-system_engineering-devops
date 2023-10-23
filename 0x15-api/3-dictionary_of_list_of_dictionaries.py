#!/usr/bin/python3
"""This module exports data to JSON format.
"""
from json import dumps
import requests


def get_tasks_from_employee(response, employee):
    """Get all the tasks of an employee
    """
    emp_tasks = list()

    for task in response:
        if task.get('userId') == employee.get('id'):
            task_data = {
                'username': employee.get('username'),
                'task': task.get('title'),
                'completed': task.get('completed'),
            }

            emp_tasks.append(task_data)

    return emp_tasks


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    users_url = '{api}/users'.format(api=api_url)
    todos_url = '{api}/todos'.format(api=api_url)
    fn = 'todo_all_employees.json'

    user_res = requests.get(users_url).json()
    todo_res = requests.get(todos_url).json()
    users_tasks = dict()

    for user in user_res:
        user_id = user.get('id')

        user_tasks = get_tasks_from_employee(todo_res, {
            'id': user_id,
            'username': user.get('username')
        })
        users_tasks[user_id] = user_tasks

    with open(fn, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps(users_tasks))
