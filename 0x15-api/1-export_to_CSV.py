#!/usr/bin/python3
"""a Python script that export to CSV"""
import requests
from sys import argv


if __name__ == "__main__":
    """a function export data in the CSV format"""

    url = "https://jsonplaceholder.typicode.com/users"
    emp_id = argv[1]
    full_url = url + "/" + emp_id

    response = requests.get(full_url)
    username = response.json().get("username")

    todo_url = full_url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    with open("{}.csv".format(emp_id), "w") as csv:
        for task in tasks:
            csv.write(
                '"{}","{}","{}","{}"\n'.format(
                    emp_id, username, task.get("completed"), task.get("title")
                )
            )
