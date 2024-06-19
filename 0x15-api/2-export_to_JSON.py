#!/usr/bin/python3
'''
    for a given employee ID, returns information about
    his/her TODO list progress and export data in the CSV format.
'''
from sys import argv, exit
import json
import requests


def get_username(user_id):
    '''Gets username of employee with user_id'''
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(user_url)
    if response.status_code == 200:
        data = response.json()
        return data.get('username')


def get_todos(user_id):
    '''Retrieves todos of employee with user_id'''
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(todo_url)
    if response.status_code == 200:
        data = response.json()
        return data


def to_json(username, todos, user_id):
    '''export data in the JSON format.'''
    file_name = f'{user_id}.json'
    result = {}
    tasks = []
    for todo in todos:
        status = todo.get("completed")
        title = todo.get("title")
        data = {"task": title, "completed": status,
                "username": username}
        tasks.append(data)
    result[f"{user_id}"] = tasks
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file)


if __name__ == '__main__':
    if len(argv) < 2:
        exit(-1)

    user_id = argv[1]
    username = get_username(user_id)
    todos = get_todos(user_id)
    to_json(username, todos, user_id)
