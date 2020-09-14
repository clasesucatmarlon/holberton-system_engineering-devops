#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    """ Return employees and task
    """
    complete_task = 0
    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]

    value1 = requests.get(url + '/todos')
    value2 = requests.get(url + '/users')

    for todo_dict in value1.json():
        if todo_dict.get('userId') == int(user_id) and \
                todo_dict.get('completed') is True:
            complete_task += 1

    for user_dict in value2.json():
        if user_dict.get('id') == int(user_id):
            user = user_dict.get('name')

    print("Employee {} is done with task({}/20):".format(user, complete_task))

    for todo_dict in value1.json():
        if todo_dict.get('userId') == int(user_id) and \
                todo_dict.get('completed') is True:
            print('\t {}'.format(todo_dict.get('title')))
