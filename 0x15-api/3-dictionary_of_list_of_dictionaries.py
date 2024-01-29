#!/usr/bin/python3
"""a Python script that exports to JSON"""
import requests
import json


if __name__ == '__main__':
            """a function that exports JSON dictionary of list of dictionaries"""
            url = "https://jsonplaceholder.typicode.com/users"
            users = requests.get(url).json()
            with open('todo_all_employees.json', mode="w", newline="") as file:
                        dictionary = {}
                        for user in users:
                                    user_id = user.get('id')
                                    username = user.get('username')
                                    tasks = requests.get('{}{}/todos'.format(url, user_id)).json()
                                    dict_list = []
                                    for dic in tasks:
                                                tmp_dict = {}
                                                tmp_dict["task"] = dic.get('title')
                                                tmp_dict['completed'] = dic.get('completed')
                                                tmp_dict['username'] = username
                                                dict_list.append(tmp_dict)
                                    dictionary[user_id] = dict_list
                        json.dump(dictionary, file)
