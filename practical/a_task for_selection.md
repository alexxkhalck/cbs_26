# Навчальні проєкти

Для студентів доступні 3 навчальні проєкти, які проходять через усі 50 занять та поступово розвиваються разом із курсом:

**Python Basics → Git → OOP → Files → Databases → HTTP → Testing → Django → REST API → Deployment**

Головна ідея: проєкт має **розвиватися протягом усього навчання**, а не бути одноразовою вправою.

# Доступні проєкти

| Project                   | Domain            | Основний фокус                   |
| ------------------------- | ----------------- | -------------------------------- |
| Task & Bug Manager        | productivity / QA | tasks, bugs, workflows           |
| Expense Tracker           | finance           | calculations, reports, analytics |
| Service Management System | inventory / CRM   | склад, замовлення, клієнти       |

# 1. Task and Bug Manager

## Ідея

Система керування задачами, багами та тест-кейсами.

### Користувач може:

* створювати записи:

  * Task
  * Bug
  * Test Case
* редагувати записи;
* видаляти;
* ставити дедлайни;
* змінювати статус;
* призначати відповідального;
* фільтрувати записи.

## Основні сутності

### User

* username
* email

### Issue

* title
* description
* issue_type
* priority
* status
* deadline

### Comment

* text
* author
* created_at

## Додатково

* history log
* kanban board
* attachments

## Аналог

mini-Jira

# 2. Expense and Budget Tracker

## Ідея

Система керування особистими фінансами.

### Користувач може:

* додавати доходи;
* додавати витрати;
* створювати категорії;
* контролювати бюджет;
* переглядати звіти.

## Основні сутності

### User

* username
* email

### Transaction

* amount
* transaction_type
* category
* date
* description

### Budget

* category
* monthly_limit

## Додатково

* charts
* exchange API
* recurring payments
* export reports

## Аналог

mini-Money Manager

# 3. Service Management System

## Ідея

CRM/ERP система для записів, послуг, складу та замовлень.

Студент може обрати один із доменів:

* **Auto Service & Parts Store**
* **Beauty Clinic / Aesthetic Medicine**

Архітектура, БД та логіка однакові, змінюється лише предметна область.

## Варіант A: Auto Service & Parts Store

### Користувач може:

* додавати клієнтів;
* реєструвати автомобілі;
* створювати замовлення на ремонт;
* додавати послуги;
* керувати складом запчастин;
* відстежувати статус ремонту.

### Основні сутності

* Customer
* Vehicle
* RepairOrder
* Service
* Part

## Варіант B: Beauty Clinic / Aesthetic Medicine

### Користувач може:

* додавати клієнтів;
* створювати картки пацієнтів;
* записувати на процедури;
* керувати каталогом послуг;
* вести облік препаратів та матеріалів;
* відстежувати статус візиту.

### Основні сутності

* Client
* PatientProfile
* Appointment
* Procedure
* Product

## Для обох доменів

### Мінімальний функціонал (MVP)

* CRUD операції
* CLI interface
* JSON storage
* CSV export
* SQLite/PostgreSQL database
* Django web application
* REST API

### Advanced features

* scheduling/calendar
* notifications
* low stock alerts
* analytics dashboard
* PDF reports
* inventory management

## Підсумковий результат

У кінці курсу студент має:

* GitHub repository
* Python application
* tests
* database integration
* Django web app
* REST API
* deploy-ready project