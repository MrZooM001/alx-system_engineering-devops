#!/usr/bin/python3
"""a Python script that use REST API"""
import requests
from sys import argv


if __name__ == "__main__":
    """a function for a given employee ID,
    returns information about his/her TODO list progress."""
    usr_url = "https://jsonplaceholder.typicode.com/users"
    user_id = int(argv[1])
    full_url = "{}/{}".format(usr_url, user_id)

    response = requests.get(full_url)
    emp_name = response.json().get("name")

    todo_url = "{}/todos".format(full_url)
    response = requests.get(todo_url)

    all_tasks = response.json()
    done_tasks = []
    for task in all_tasks:
        if task.get("completed"):
            done_tasks.append(task)
    print("Employee {} is done with tasks({}/{})".format(
            emp_name, len(done_tasks), len(all_tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
