# ROADMAP Project 3: Service Management System

## Що має виходити після кожного модуля

**Домен на вибір:**

* Auto Service & Parts Store
* Beauty Clinic / Aesthetic Medicine

Архітектура та логіка однакові, змінюється лише предметна область.

# Module 1. Python Basics + Git

**Теми:** синтаксис, змінні, умови, цикли, функції, Git basics

## Що зробити

Створити просту CLI-систему для записів клієнтів і замовлень.

## Мінімальний функціонал

Користувач може:

* додати клієнта;
* створити запис/замовлення;
* переглянути список записів;
* видалити запис.

## Приклад CLI

```bash 
python main.py
```

Меню:

```text 
1. Add client
2. Create appointment/order
3. Show appointments/orders
4. Delete
5. Exit
```

## Структура запису

### Auto Service

```python 
order = {
    "client": "John",
    "vehicle": "Toyota Camry",
    "status": "Created"
}
```

### Beauty Clinic

```python 
appointment = {
    "client": "Anna",
    "procedure": "Facial Cleaning",
    "status": "Scheduled"
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

Repository:

```bash 
git init
git add .
git commit -m "lesson 1-7 service management"
```

## Результат модуля

CLI застосунок без збереження.

# Module 2. Python Core / OOP

**Теми:** classes, inheritance, exceptions, modules

## Що зробити

Переписати застосунок на класи.

## Створити класи

```python 
Client
Service
Order
ServiceManager
```

## Domain models

### Auto Service

* Customer
* Vehicle
* RepairOrder
* Part

### Beauty Clinic

* Client
* PatientProfile
* Appointment
* Product

## Order/Appointment model

```python 
client
service
status
date
total_price
```

## Додати методи

* create_order()
* update_status()
* delete_order()
* list_orders()

## Exceptions

Обробляти:

```python 
Client not found
Invalid price
Invalid menu choice
```

## Результат модуля

ООП service management system.

# Module 3. Files + Advanced Python

**Теми:** JSON, CSV, decorators, typing, virtualenv, pip

## Що зробити

Додати збереження даних.

## Storage

Файли:

```text 
clients.json
orders.json
```

## Поведінка програми

* load data from JSON
* save data to JSON

## CSV export

```python 
export_orders_to_csv()
```

## Typing

```python 
def create_order(client_name: str, service_name: str) -> None:
```

## Decorators

```python 
@log_action
```

## Результат

Дані зберігаються між запусками.

# Module 4. Testing + HTTP

**Теми:** pytest, requests, mocking

## Що зробити

Покрити бізнес-логіку тестами.

## Тести

* create_order
* delete_order
* update_status
* calculate_total_price

## HTTP integration

### Auto Service

API для автоданих:

* brands/models lookup

### Beauty Clinic

API для повідомлень або mock notifications.

## Приклад

```python 
send_notification()
```

## Результат

Unit tests + API integration.

# Module 5. Databases

**Теми:** SQLite, SQL, PostgreSQL

## Що зробити

Перенести з JSON у базу даних.

## Таблиці

### clients

* id
* name
* phone
* email

### services

* id
* name
* price
* duration

### orders/appointments

* id
* client_id
* service_id
* status
* total_price
* created_at

### inventory

* id
* name
* quantity
* price

## SQL operations

* INSERT
* UPDATE
* DELETE
* SELECT
* JOIN

## Нові можливості

* inventory tracking
* service history

## Результат

DB-backed application.

# Module 6. Django Basics

**Теми:** Django models/views/templates/forms/admin

## Що зробити

Перетворити CLI на web app.

## Pages

### Authentication

* login
* register
* logout

### Clients

* client list
* create/edit/delete client

### Orders/Appointments

* list
* detail
* create
* edit
* change status

### Inventory

* products/parts list
* quantity management

## Django Admin

Керування:

* clients
* services
* orders
* inventory

## Результат

Web CRM/ERP система.

# Module 7. Django REST Framework

**Теми:** serializers, viewsets, routers, permissions

## Що зробити

Створити API.

## Endpoints

```text 
/api/clients/
/api/orders/
/api/services/
/api/inventory/
```

## CRUD

* GET
* POST
* PUT
* DELETE

## Authentication

* token auth

## Результат

REST API для service management system.

# Module 8. Final Improvements / Deploy Prep

**Теми:** refactoring, documentation, deployment prep

## Що зробити

Refactor:

* clean architecture
* split modules

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

* calendar scheduling
* notifications
* low stock alerts
* analytics dashboard
* PDF invoices/reports

## Final project structure

```text 
service_manager/
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

# Візуальний прогрес

### Після module 1

консольний менеджер клієнтів і записів

### Після module 3

service manager із файлами

### Після module 5

DB-backed CRM system

### Після module 7

mini CRM/ERP web app
