#!/usr/bin/pytho3
"""This module extracts data to json format"""
from json import dumps
from sys import argv
import requests


if __name__ == '__main__':
    try:
        employee_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{api}/users/{id}'.format(api=api_url, id=employee_id)
    todo_url = '{user_url}/todos'.format(user_url=user_url)
    fn = '{employee_id}.json'.format(employee_id=employee_id)

    user_res = requests.get(user_url).json()
    todo_res = requests.get(todo_url).json()
    user_tasks = list()

    for element in todo_res:
        data = {
            'task': element.get('title'),
            'completed': element.get('completed'),
            'username': user_res.get('username')
        }

        user_tasks.append(data)

    with open(fn, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps({employee_id: user_tasks}))
