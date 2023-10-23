#!/usr/bin/python3
"""This is the module to export data from API to CSV format
"""
from sys import argv
import csv
import requests


if __name__ == '__main__':
    try:
        employee_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{api}/users/{id}'.format(api=api_url, id=employee_id)
    todo_url = '{user_url}/todos'.format(user_url=user_url)
    fn = '{employee_id}.csv'.format(employee_id=employee_id)

    user_res = requests.get(user_url).json()
    username = user_res.get('username')
    user_res = requests.get(todo_url).json()

    with open(fn, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for element in user_res:
            status = element.get('completed')
            title = element.get('title')
            writer.writerow([employee_id, username, status, title])
