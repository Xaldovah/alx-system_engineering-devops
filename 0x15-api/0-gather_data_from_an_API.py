#!/usr/bin/python3
"""This is the get_employee_todo_progress module
"""
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

    user_res = requests.get(user_url).json()
    name = user_res.get('name')
    user_res = requests.get(todo_url).json()
    total = len(user_res)
    incomplete = sum([elem['completed'] is False for elem in user_res])
    completed = total - incomplete

    str = "Employee {emp_name} is done with tasks({completed}/{total}):"
    print(str.format(
        emp_name=name, completed=completed, total=total))

    for elem in user_res:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))
