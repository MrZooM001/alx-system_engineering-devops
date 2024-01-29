#!/usr/bin/python3
"""a Python script that exports to JSON"""
import requests
from sys import argv
import json


if __name__ == '__main__':
            """a function that exports data in the JSON format"""

            url = "https://jsonplaceholder.typicode.com/users"
            emp_id = argv[1]
            full_url =  "{}/{}".format(url, emp_id)

            response = requests.get(full_url)
            username = response.json().get('username')

            todo_url = full_url + "/todos"
            response = requests.get(todo_url)
            tasks = response.json()

            dictionary = {emp_id: []}

            for task in tasks:
                        dictionary[emp_id].append({
                                    "task": task.get('title'),
                                    "completed": task.get('completed'),
                                    "username": username
                        })
            with open('{}.json'.format(emp_id), 'w') as filename:
                        json.dump(dictionary, filename)
