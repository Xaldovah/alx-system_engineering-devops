#!/usr/bin/python3
"""This is the get_employee_todo_progress module
"""
import requests
import sys


def get_employee_todo_progress(employee_id: int):
    """
    Retrieve and display an employee's TODO list progress from a REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        """Send a GET request to the user URL to fetch user information"""
        user_res = requests.get(user_url)

        """Send a GET request to the todos URL to
        fetch the employee's TODO list"""
        todos_res = requests.get(todos_url)

        """Parse the JSON data from the responses"""
        user_data = user_res.json()
        todos_data = todos_res.json()

        """Check if the user exists"""
        if user_res.status_code != 200:
            print(f"User with ID {employee_id} not found.")
            return

        """Extract user information"""
        emp_nm = user_data.get("name")

        """Filter completed tasks from the TODO list"""
        fertig = [task for task in todos_data if task["completed"]]
        total = len(todos_data)

        """Print the employee's TODO list progress"""
        print(f"Employee {emp_nm} is done with tasks({len(fertig)}/{total}): ")

        for task in fertig:
            print(f"\t{task['title']}")

    except requests.exceptions.ConnectionError as e:
        print(f"Could not connect to the API: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")


if __name__ == '__main__':
    """This block will only be executed when the script is run directly."""

    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
