#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f'{url}users/{argv[1]}').json()
    todos = requests.get(f'{url}todos', params={"userId": argv[1]}).json()

    completed = [todo.get("title") for todo in todos if todo.get("completed")]
    print(f'Employee {user.get("name")} '
          f'is done with tasks({len(completed)}/{len(todos)}):')
    for complete in completed:
        print(f'\t {format(complete)}')
