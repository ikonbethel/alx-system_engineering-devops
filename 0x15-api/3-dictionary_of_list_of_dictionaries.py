#!/usr/bin/python3
'''
    for a given employee ID, returns information about
    his/her TODO list progress and export data in the JSON format.
'''
import json
import requests


def get_all_users():
    '''gets all employees'''
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = []
    data = response.json()
    for user in data:
        users.append(user['id'])
    return users


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


def to_json(users):
    '''export data in the JSON format.'''
    file_name = 'todo_all_employees.json'
    result = {}
    for user_id in users:
        username = get_username(user_id)
        todos = get_todos(user_id)
        tasks = []
        for todo in todos:
            status = todo.get('completed')
            title = todo.get('title')
            data = {"username": username, "task": title,
                    "completed": status}
            tasks.append(data)
        result[f"{user_id}"] = tasks
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file)


if __name__ == '__main__':
    users = get_all_users()
    to_json(users)
