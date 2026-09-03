# ROADMAP Project 1: Task & Bug Manager

## Що має виходити після кожного модуля

# Module 1. Python Basics + Git

**Теми:** синтаксис, змінні, умови, цикли, функції, Git basics

## Що зробити

Створити найпростішу CLI-програму.

## Мінімальний функціонал

Користувач може:

* створити задачу;
* переглянути список задач;
* видалити задачу.

## Приклад CLI

```bash
python main.py
```

Меню:

```text
1. Add task
2. Show tasks
3. Delete task
4. Exit
```

## Структура задачі

Поки що достатньо словника:

```python
task = {
    "title": "Fix login bug",
    "type": "Bug",
    "status": "Open"
}
```

## Що практикуємо

* input()
* print()
* if/elif
* while
* functions
* lists/dicts

## Git

Repository має містити:

```bash
git init
git add .
git commit -m "lesson 1-7 task manager"
```

## Результат модуля

Працюючий консольний task manager без збереження.

# Module 2. Python Core / OOP

**Теми:** classes, inheritance, exceptions, modules

## Що зробити

Переписати проєкт на класи.

## Створити класи

```python
User
Issue
TaskManager
```

## Issue model

```python
title
description
issue_type
priority
status
deadline
```

## Додати методи

* create_issue()
* update_issue()
* delete_issue()
* list_issues()
* change_status()

## Додати типи issue

* Task
* Bug
* Test Case

Можна через:

* inheritance

або

* enum/field

## Exceptions

Обробляти:

```python
Invalid menu choice
Task not found
```

## Результат модуля

ООП консольний застосунок.

# Module 3. Files + Advanced Python

**Теми:** JSON, CSV, decorators, typing, virtualenv, pip

## Що зробити

Додати persistence.

## Збереження задач

Файл:

```text
issues.json
```

## При запуску

* load from JSON

При виході

* save to JSON

## Export

CSV export:

```text
issues.csv
```

## Додати typing

```python
def create_issue(title: str, issue_type: str) -> None:
```

## Logging decorator

Наприклад:

```python
@log_action
def create_issue():
```

## Result

Проєкт уже зберігає дані між запусками.

# Module 4. Testing + HTTP

**Теми:** pytest, requests, mocking

## Що зробити

Покрити бізнес-логіку тестами.

## Написати тести

Для:

* create_issue
* delete_issue
* change_status

## Приклад

```python
def test_create_issue():
```

## HTTP integration

Додати fake API sync.

Наприклад:

```python
https://jsonplaceholder.typicode.com/todos
```

або власний mock API.

## Можливості

* import tasks from API
* export tasks to API

## Result

Проєкт має unit tests + API integration.

# Module 5. Databases

**Теми:** SQLite, SQL, PostgreSQL

## Що зробити

Перенести storage з JSON у DB.

## Таблиці

### users

* id
* username
* email

### issues

* id
* title
* description
* type
* priority
* status
* deadline
* user_id

### comments

* id
* text
* author_id
* issue_id

## SQL operations

* INSERT
* UPDATE
* DELETE
* SELECT
* JOIN

## Додати comments

Issue може мати коментарі.

## Result

Повноцінна БД.

# Module 6. Django Basics

**Теми:** Django models/views/templates/forms/admin

## Що зробити

Перетворити CLI на web app.

## Pages

### Authentication

* login
* register
* logout

### Issues

* issue list
* issue detail
* create issue
* edit issue
* delete issue

## Filters

* by status
* by type
* by priority

## Django Admin

Керування:

* users
* issues
* comments

## Result

Перший web app.

# Module 7. Django REST Framework

**Теми:** serializers, viewsets, routers, permissions

## Що зробити

Створити API.

## Endpoints

```text
/api/issues/
/api/comments/
/api/users/
```

## CRUD

* GET
* POST
* PUT
* DELETE

## Authentication

* token auth

## Result

REST API для фронта або mobile app.

# Module 8. Final Improvements / Deploy Prep

**Теми:** deployment prep, refactoring, best practices

## Що зробити

Refactor:

* split files
* clean architecture

## README

Описати:

* install
* run
* tests

## requirements.txt

```bash
pip freeze > requirements.txt
```

## Optional features

Обрати 2-3:

* kanban board
* attachments
* notifications
* issue history
* dashboard analytics

## Final project structure

```text
task_manager/
    src/
    tests/
    templates/
    static/
    requirements.txt
    README.md
```

# Що студент має в кінці

До завершення курсу студент отримує:

✅ Python CLI application
✅ OOP architecture
✅ JSON/CSV support
✅ pytest tests
✅ SQLite/PostgreSQL
✅ Django web app
✅ REST API
✅ GitHub portfolio project

# Візуально прогрес такий

### Після module 1

маленька консолька

### Після module 3

справжній mini-app із файлами

### Після module 5

DB-backed application

### Після module 7

майже mini-Jira
