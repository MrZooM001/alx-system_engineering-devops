#!/usr/bin/python3
"""a Python script that exports to JSON"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """a function that exports data in the JSON format"""

    url = "https://jsonplaceholder.typicode.com/users"
    user_id = argv[1]
    full_url = "{}/{}".format(url, user_id)

    response = requests.get(full_url)
    username = response.json().get("username")

    todo_url = full_url + "/todos"

    response = requests.get(todo_url)
    tasks = response.json()

    dictionary = {user_id: []}

    for task in tasks:
        if task.get("userId" == int(user_id)):
            dictionary[user_id].append(
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username,
                }
            )

    with open("{}.json".format(user_id), "w+") as filename:
        json.dump(dictionary, filename)
