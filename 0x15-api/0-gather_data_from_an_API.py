#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    """ Return employees and task
    """
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]

    employee = requests.get(url + 'users/' + user_id)
    employee = employee.json()

    task = requests.get(url + "todos?userId=" + user_id)
    task = task.json()

    list_task_done = []

    for counter in task:
        if counter.get("completed") is True:
            list_task_done.append(counter)

    task_done = len(list_task_done)
    task_total = len(task)

    print("Employee {} is done with task({}/{}):".format(
        employee.get('name'), task_done, task_total))

    for count in list_task_done:
        print('\t {}'.format(count.get('title')))
