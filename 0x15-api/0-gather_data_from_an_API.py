#!/usr/bin/python3
"""a Python script that use REST API"""
import requests
from sys import argv


def get_from_api():
        """a function for a given employee ID,
        returns information about his/her TODO list progress."""
        usr_url = "https://jsonplaceholder.typicode.com/users"
        emp_id = argv[1]
        full_url = "{}/{}".format(usr_url, emp_id)

        response = requests.get(full_url)
        emp_name = response.json().get("name")

        todo_url = "{}/todos".format(full_url)
        response = requests.get(todo_url)

        all_tasks = response.json()
        done_tasks = []
        for task in all_tasks:
                if task.get("completed"):
                        done_tasks.append(task)

        # EMPLOYEE_NAME  NUMBER_OF_DONE_TASKS  TOTAL_NUMBER_OF_TASKS
        print("Employee {} is done with tasks({}/{})"
                     .format(emp_name, len(done_tasks), len(all_tasks)))

        for task in done_tasks:
                print("\t {}".format(task.get('title')))

if __name__ == '__main__':
        get_from_api()