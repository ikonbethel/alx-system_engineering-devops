#!/usr/bin/python3
'''
    for a given employee ID, returns information about
    his/her TODO list progress and export data in the CSV format.
'''
import csv
from sys import argv, exit
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


def to_csv(username, todos, user_id):
    '''export data in the CSV format.'''
    file_name = f'{user_id}.csv'
    result = []
    for todo in todos:
        data = [f"{str(user_id)}", username]
        status = str(todo.get("completed"))
        title = str(todo.get("title"))
        data.append(status)
        data.append(title)
        result.append(data)
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for row in result:
            writer.writerow(row)


if __name__ == '__main__':
    if len(argv) < 2:
        exit(-1)

    user_id = argv[1]
    username = get_username(user_id)
    todos = get_todos(user_id)
    to_csv(username, todos, user_id)
