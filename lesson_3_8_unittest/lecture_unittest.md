# Лекція. Unit Testing у Python

## 1. Що таке Unit Testing

**Unit Testing** — це тестування окремих, найменших логічно завершених частин програми.

Такими частинами можуть бути:

* функція;
* метод класу;
* окремий компонент;
* невеликий фрагмент бізнес-логіки.

Наприклад, маємо функцію:

```python
def sum_two_values(a, b):
    return a + b
```

Її можна перевірити незалежно від усього іншого застосунку:

```python
result = sum_two_values(10, 20)

assert result == 30
```

Ми перевіряємо конкретну одиницю поведінки:

> якщо передати `10` і `20`, функція повинна повернути `30`.

Саме тому тест називається **unit test** — ми тестуємо одну одиницю функціональності.

# 2. Навіщо потрібні Unit Tests

Уявімо, що наш проєкт складається з 100 функцій.

Ми змінили одну:

```python
def sum_two_values(a, b):
    return a - b
```

На перший погляд, програма може продовжувати запускатися.

Але тест:

```python
def test_sum_two_values():
    result = sum_two_values(10, 20)
    assert result == 30
```

одразу покаже проблему.

Отримаємо:

```text
AssertionError
```

Тобто тестування дозволяє:

1. знаходити помилки;
2. перевіряти, що нові зміни не зламали стару функціональність;
3. автоматично перевіряти код після кожної зміни;
4. документувати очікувану поведінку програми.

# 3. Найпростіший тест — `assert`

У Python є вбудована конструкція:

```python
assert condition
```

Якщо умова `True` — тест проходить.

```python
assert 2 + 2 == 4
```

Якщо `False` — виникає:

```text
AssertionError
```

Наприклад:

```python
assert 2 + 2 == 5
```

дасть:

```text
AssertionError
```

У файлі `test_2_adv.py` є саме такий підхід:

```python
expected = True
actual = 1 == 1

assert expected == actual, f"Get {actual}, but {expected}"
```

Тут другим аргументом можна передати повідомлення про помилку. 

# 4. `assert` у реальному Unit Test

Розглянемо функцію:

```python
def test_function(value):
    return value * 20
```

Ми можемо написати:

```python
def test_function():
    value = 100
    expected = 2000

    actual = test_function(value)

    assert actual == expected
```

Тут дуже важлива структура тесту.

## Arrange → Act → Assert

### Arrange

Підготовка даних:

```python
value = 100
expected = 2000
```

### Act

Виконання функції:

```python
actual = test_function(value)
```

### Assert

Перевірка результату:

```python
assert actual == expected
```

Цей підхід часто скорочено називають:

> **AAA — Arrange, Act, Assert**

У тесті множення з `test_1_basic.py` ця структура фактично використовується явно через коментарі `A`, `Action`, `assert`. 

# 5. Що саме ми повинні тестувати

Для функції:

```python
def sum_two_values(a, b):
    return a + b
```

недостатньо перевірити тільки:

```python
sum_two_values(10, 20)
```

Потрібно подумати про різні сценарії.

### Позитивний сценарій

```python
10 + 20 = 30
```

### Нуль

```python
0 + 10 = 10
```

### Від'ємні числа

```python
-10 + 5 = -5
```

### Однакові числа

```python
10 + 10 = 20
```

Тобто Unit Test — це не просто:

> «запустити функцію».

Ми повинні перевірити **очікувану поведінку**.

# 6. `unittest`

Python має стандартний фреймворк для тестування — `unittest`.

Підключення:

```python
import unittest
```

Тестовий клас успадковується від:

```python
unittest.TestCase
```

Наприклад:

```python
class UserTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(2 + 2, 4)
```

Цей підхід використаний у `test_1_basic.py`. 

# 7. Правила написання тестів `unittest`

Метод тесту повинен починатися з:

```text
test_
```

Наприклад:

```python
def test_sum(self):
    ...
```

А ось такий метод:

```python
def check_sum(self):
    ...
```

`unittest` автоматично тестом не сприйме.

Тому:

```python
class UserTestCase(unittest.TestCase):

    def test_sum(self):
        ...

    def test_multiply(self):
        ...

    def test_power(self):
        ...
```

# 8. `assertEqual`

Найчастіше використовується:

```python
self.assertEqual(actual, expected)
```

Наприклад:

```python
def test_sum_two_values(self):
    value1 = 10
    value2 = 20

    result = sum_two_values(value1, value2)

    self.assertEqual(result, value1 + value2)
```

Це означає:

> фактичний результат повинен бути рівний очікуваному.

У файлі `test_1_basic.py` ця конструкція використовується для перевірки суми, степеня, конкатенації та ділення. 

# 9. `assertTrue`

Інший варіант:

```python
self.assertTrue(condition)
```

Наприклад:

```python
self.assertTrue(8 == 8)
```

У файлі:

```python
multiply_result = multiply_a * multiply_b

self.assertTrue(
    multiply_result == expected_result,
    f"We multiply {multiply_a} * {multiply_b} and get {multiply_result}, "
    f"but expected is {expected_result}"
)
```



Але якщо ми порівнюємо два значення, краще використовувати:

```python
self.assertEqual(actual, expected)
```

замість:

```python
self.assertTrue(actual == expected)
```

Тобто:

```python
self.assertEqual(result, 8)
```

краще описує намір тесту.

# 10. Порівняння різних типів даних

`unittest` має спеціалізовані assertion methods.

Наприклад:

```python
self.assertEqual(1, 1)
self.assertEqual("test", "test")
self.assertEqual(True, True)
```

Для списків:

```python
self.assertListEqual(
    [1, 2, 3],
    [1, 2, 3]
)
```

Для перевірки типу:

```python
self.assertIsInstance("test", str)
```

Для перевірки ідентичності об'єктів:

```python
self.assertIs(value1, value2)
```

У `test_2_adv.py` показано цілий набір таких перевірок. 

# 11. Основні Assertions

Корисно запам'ятати:

| Assertion                  | Що перевіряє           |
| -------------------------- | ---------------------- |
| `assertEqual(a, b)`        | `a == b`               |
| `assertNotEqual(a, b)`     | `a != b`               |
| `assertTrue(x)`            | `x` істинне            |
| `assertFalse(x)`           | `x` хибне              |
| `assertIs(a, b)`           | це той самий об'єкт    |
| `assertIsNone(x)`          | `x is None`            |
| `assertIsNotNone(x)`       | `x is not None`        |
| `assertIsInstance(x, T)`   | `x` має тип `T`        |
| `assertGreater(a, b)`      | `a > b`                |
| `assertGreaterEqual(a, b)` | `a >= b`               |
| `assertLess(a, b)`         | `a < b`                |
| `assertLessEqual(a, b)`    | `a <= b`               |
| `assertRegex(text, regex)` | текст відповідає regex |

Наприклад, у файлі:

```python
self.assertGreater(20, 10)
self.assertGreaterEqual(20, 20)
self.assertLess(10, 20)
self.assertLessEqual(10, 10)
self.assertRegex('test text', r'^test')
```



# 12. Тестування винятків

Тестувати потрібно не тільки правильний результат.

Іноді правильна поведінка функції — **викинути exception**.

Наприклад:

```python
def desc(x, y):
    if y == 0:
        raise ValueError('should not be equal 0')

    return x / y
```

Для нормального випадку:

```python
result = desc(20, 10)

self.assertEqual(result, 2.0)
```

Але що робити з:

```python
desc(20, 0)
```

Ми очікуємо `ValueError`.

# 13. `assertRaises`

У `unittest` для цього використовується:

```python
with self.assertRaises(ValueError):
    desc(20, 0)
```

Тест пройде, якщо `ValueError` дійсно виникне.

Якщо exception не виникне — тест провалиться.

У `test_1_basic.py` саме так перевіряється заборона ділення на нуль для функції `desc`. 

# 14. Перевірка конкретного exception

Можна зберегти exception:

```python
with self.assertRaises(ValueError) as error:
    desc(20, 0)
```

Тепер змінна `error` містить інформацію про exception.

Це корисно, якщо потрібно перевірити не тільки тип помилки, але й повідомлення.

Наприклад:

```python
with self.assertRaises(ValueError) as error:
    desc(20, 0)

self.assertEqual(
    str(error.exception),
    "should not be equal 0"
)
```

У `test_4_unit.py` використовується конструкція `as zde` / `as ve` саме для отримання об'єкта винятку, хоча в поточному коді його додатково не перевіряють. 

# 15. Unit Test для функції з різними сценаріями

Уявімо функцію:

```python
def sum_list_last_first(values):
    ...
```

Тести з `test_4_unit.py` перевіряють різні ситуації.

### Три елементи

```python
my_list = [1, 2, 3]

actual = sum_list_last_first(my_list)
expected = 1.5

assert actual == expected
```

### Два елементи

```python
my_list = [1, 2]

actual = sum_list_last_first(my_list)
expected = 1.0

assert actual == expected
```

### Один елемент

```python
my_list = [1]

actual = sum_list_last_first(my_list)

assert actual is None
```

Тобто тестуємо не тільки happy path, але й граничні випадки. 

# 16. Boundary Values

Окрема важлива концепція — **boundary values**, або граничні значення.

Якщо функція працює зі списком, потрібно подумати:

```text
[]
[1]
[1, 2]
[1, 2, 3]
```

Якщо функція приймає число:

```text
-1
0
1
```

Якщо приймає рядок:

```text
""
"a"
"long string"
```

Помилки дуже часто знаходяться саме на межах допустимих значень.

# 17. Тестування помилок

У `test_4_unit.py` є тест:

```python
my_list = [3, 5, -3]

with self.assertRaises(ZeroDivisionError):
    sum_list_last_first(my_list)
```

Тут тест перевіряє, що для конкретних даних функція повинна завершитися `ZeroDivisionError`. 

Також перевіряється неправильний тип аргументу:

```python
my_list = {3, 5, -3}

with self.assertRaises(ValueError):
    sum_list_last_first(my_list)
```

Це приклад **negative testing** — ми перевіряємо неправильні вхідні дані. Коли користувач надсилає не list або dict - програма піднімає виключення.

# 18. Позитивні та негативні тести

Умовно тести можна розділити на:

### Positive testing

Перевіряємо правильні вхідні дані:

```python
sum_two_values(10, 20) == 30
```

### Negative testing

Перевіряємо неправильні дані:

```python
desc(20, 0)
```

і очікуємо:

```python
ValueError
```

Хороший набір Unit Tests повинен містити обидва типи сценаріїв.

# 19. Запуск `unittest`

У наших файлах використовується:

```python
unittest.main(verbosity=2)
```

`verbosity=2` означає більш детальний вивід результатів тестування.

Запустити файл можна:

```bash
python test_1_basic.py
```

Або безпосередньо через IDE.

При успішному виконанні отримаємо щось на кшталт:

```text
test_01_sum ... ok
test_02_multiply ... ok
test_03_function ... ok
...
----------------------------------------------------------------------
Ran 8 tests

OK
```

# 20. Skip — коли тест потрібно пропустити

Іноді тест існує, але зараз його запускати не потрібно.

Наприклад, функціональність ще не реалізована.

`unittest` має декоратор:

```python
@unittest.skip("reason")
```

Наприклад:

```python
@unittest.skip("Feature is not ready")
def test_new_feature(self):
    ...
```

Тест буде пропущено.

У `test_2_adv.py` наведені чотири механізми:

```python
@unittest.skip(reason)
@unittest.skipIf(condition, reason)
@unittest.skipUnless(condition, reason)
@unittest.expectedFailure
```



# 21. `skipIf` та `skipUnless`

### `skipIf`

Пропустити тест, якщо умова `True`:

```python
@unittest.skipIf(condition, "Not supported")
def test_feature(self):
    ...
```

Наприклад:

```python
@unittest.skipIf(True, "Temporary disabled")
def test_something(self):
    ...
```

### `skipUnless`

Запустити тест тільки якщо умова `True`:

```python
@unittest.skipUnless(condition, "Required environment")
def test_feature(self):
    ...
```

Це корисно для тестів, які залежать від:

* операційної системи;
* версії Python;
* наявності зовнішнього сервісу;
* спеціальної конфігурації.

# 22. `expectedFailure`

Іноді ми знаємо, що тест зараз падає.

Наприклад, функціональність ще не виправлена.

Можна написати:

```python
@unittest.expectedFailure
def test_known_bug(self):
    ...
```

Тоді падіння такого тесту не буде сприйматися як звичайний failed test.

Це корисний механізм під час розробки, але ним не варто маскувати реальні проблеми.

# 23. Проблема зовнішніх залежностей

Тепер переходимо до найцікавішої частини — **Mocking**.

У нас є клас:

```python
class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_post(self):
        url = f"{self.base_url}/posts"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return response.text
```



Метод `get_post()` використовує зовнішній API через:

```python
requests.get(url)
```

# 24. Чому не варто робити реальний HTTP-запит у Unit Test

Можна було б написати:

```python
def test_get_post():
    client = APIClient(
        "https://jsonplaceholder.typicode.com"
    )

    result = client.get_post()

    assert result
```

Але це вже не дуже хороший Unit Test.

Чому?

Тест залежить від:

* Internet;
* доступності API;
* DNS;
* сервера;
* response time;
* актуального стану API;
* rate limits.

Якщо API лежить, наш Unit Test впаде.

Але проблема може бути **не в нашому коді**.

# 25. Що таке Mock

**Mock** — це об'єкт-замінник, який використовується замість реального об'єкта або зовнішньої залежності.

Замість:

```python
requests.get(...)
```

ми можемо сказати:

> «У цьому тесті не ходи в Internet. Я сам створю відповідь API».

Це і є **mocking**.

# 26. `Mock`

Імпортуємо:

```python
from unittest.mock import Mock
```

Створюємо:

```python
mock_response = Mock()
```

Тепер можемо задати йому потрібні властивості:

```python
mock_response.status_code = 200
```

І навіть поведінку методів:

```python
mock_response.json.return_value = {
    "data": "example_data"
}
```

Саме така конструкція використана у `test_3_mock.py`. 

# 27. `patch`

Але одного `Mock` недостатньо.

Наш код все одно викликає:

```python
requests.get(url)
```

Тому потрібно замінити `requests.get` на Mock.

Для цього використовується:

```python
patch
```

```python
from unittest.mock import patch
```

У тесті:

```python
@patch('requests.get')
def test_get_post_success(self, mock_get):
    ...
```

Тепер усередині цього тесту `requests.get` замінений mock-об'єктом. 

# 28. Як працює Mock + patch

Маємо:

```python
@patch('requests.get')
def test_get_post_success(self, mock_get):
```

`mock_get` — це заміна:

```python
requests.get
```

Тому можемо сказати:

```python
mock_get.return_value = mock_response
```

Тобто:

```python
requests.get(...)
```

фактично поверне:

```python
mock_response
```

# 29. Повний Unit Test API Client

Логіка тесту:

```python
@patch('requests.get')
def test_get_post_success(self, mock_get):

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'data': 'example_data'
    }

    mock_get.return_value = mock_response

    api_client = APIClient(
        base_url='https://api.example.com'
    )

    result = api_client.get_post()

    self.assertEqual(
        result,
        {'data': 'example_data'}
    )
```

Зверніть увагу:

**реального HTTP-запиту немає.**

# 30. Mock дозволяє перевірити не тільки результат

Це одна з головних переваг Mock.

Ми можемо перевірити:

> чи був викликаний `requests.get()`?

У нашому коді:

```python
mock_get.assert_called_once_with(
    'https://api.example.com/posts'
)
```

Тобто тест перевіряє:

1. метод викликав `requests.get`;
2. викликав його рівно один раз;
3. передав правильний URL.

У `test_3_mock.py` ця перевірка присутня в обох тестах. 

# 31. Два рівні перевірки Mock

Можна перевірити результат:

```python
self.assertEqual(
    result,
    {'data': 'example_data'}
)
```

І взаємодію:

```python
mock_get.assert_called_once_with(
    'https://api.example.com/posts'
)
```

Це два різні питання:

### State / Result

> Що повернула наша функція?

### Interaction

> Як наша функція взаємодіяла із залежністю?

Обидва типи перевірок можуть бути важливими.

# 32. Тестування помилки API

У другому тесті ми створюємо:

```python
mock_response.status_code = 404
```

і:

```python
mock_response.text = "{'data': 'example_data'}"
```

Тоді:

```python
result = api_client.get_post()
```

повинен повернути:

```python
response.text
```

а не:

```python
response.json()
```

Тест перевіряє:

```python
assert result == "{'data': 'example_data'}"
assert isinstance(result, str)
```



# 33. Що саме ми протестували в APIClient

У нас є два сценарії.

### HTTP 200

```text
requests.get()
       ↓
status_code = 200
       ↓
response.json()
       ↓
dict
```

### HTTP 404

```text
requests.get()
       ↓
status_code = 404
       ↓
response.text
       ↓
str
```

Тобто Unit Tests перевіряють **обидві гілки `if`**.

# 34. Code Coverage

Важливо відрізняти:

> «У нас багато тестів»

від:

> «Наш код добре протестований».

Наприклад:

```python
if response.status_code == 200:
    ...
else:
    ...
```

Якщо ми протестували тільки `200`, то друга гілка:

```python
else:
```

залишається неперевіреною.

Тому потрібно тестувати різні шляхи виконання коду.

Це і є одна з причин використання **code coverage**.

# 35. Що потрібно тестувати в першу чергу

Для кожної функції варто поставити собі питання:

### 1. Happy path

Що відбувається при правильних даних?

### 2. Boundary cases

Що відбувається на межах?

### 3. Invalid input

Що буде при неправильних даних?

### 4. Exceptions

Які помилки можуть виникнути?

### 5. Branches

Чи перевірені всі основні гілки `if/else`?

### 6. Dependencies

Чи потрібно ізолювати зовнішні залежності через Mock?

# 36. Хороший Unit Test

Хороший тест повинен бути:

**Independent**

Не залежати від інших тестів.

**Repeatable**

Давати той самий результат при повторному запуску.

**Fast**

Виконуватися швидко.

**Readable**

З назви тесту має бути зрозуміло, що перевіряється.

**Focused**

Перевіряти одну конкретну поведінку.

# 37. Поганий Unit Test

Наприклад:

```python
def test_everything():
    ...
```

У ньому перевіряються:

* база даних;
* API;
* файлові операції;
* логування;
* 10 різних функцій.

Якщо тест впаде, буде складно зрозуміти причину.

Краще:

```python
def test_sum_two_values():
    ...

def test_sum_two_values_with_zero():
    ...

def test_sum_two_values_with_negative():
    ...
```

Кожен тест має зрозумілу відповідальність.

# 38. `assert` vs `unittest`

У наших файлах використовуються обидва підходи:

```python
assert actual == expected
```

і:

```python
self.assertEqual(actual, expected)
```

Обидва можуть перевіряти умови.

Наприклад:

```python
assert result == 30
```

і:

```python
self.assertEqual(result, 30)
```

Але `unittest` надає великий набір спеціалізованих assertion methods:

```python
assertRaises
assertIsInstance
assertRegex
assertGreater
assertLess
assertListEqual
...
```

# 39. А що з `pytest`?

Модуль `pytest` це один із основних інструментів тестування. 

Той самий тест можна написати значно компактніше:

```python
def test_sum_two_values():
    result = sum_two_values(10, 20)

    assert result == 30
```

Для exception:

```python
def test_desc_zero():
    with pytest.raises(ValueError):
        desc(20, 0)
```

Однак атомарні тести коду часто проводять на `unittest`, тому саме його ми розглядаємо як основу цієї лекції.

# 40. Структура тестового файлу

Типова структура:

```text
project/
│
├── src/
│   ├── calculator.py
│   └── api_client.py
│
└── tests/
    ├── test_calculator.py
    └── test_api_client.py
```

У тесті:

```python
from src.calculator import sum_two_values
```

і далі:

```python
class CalculatorTest(unittest.TestCase):

    def test_sum(self):
        ...
```

Тобто production code і test code бажано розділяти.

# 41. Приклад повного тестового класу

```python
import unittest


def sum_two_values(a, b):
    return a + b


class CalculatorTest(unittest.TestCase):

    def test_sum_positive(self):
        actual = sum_two_values(10, 20)

        self.assertEqual(actual, 30)

    def test_sum_zero(self):
        actual = sum_two_values(10, 0)

        self.assertEqual(actual, 10)

    def test_sum_negative(self):
        actual = sum_two_values(-10, 5)

        self.assertEqual(actual, -5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

Це вже повноцінний невеликий набір Unit Tests.

# 42. Типові помилки під час Unit Testing

### Помилка 1 — тестуємо реалізацію замість поведінки

Потрібно перевіряти:

```python
result == expected
```

а не кожен внутрішній рядок функції.

### Помилка 2 — залежність від Internet

Для Unit Test краще використовувати Mock.

### Помилка 3 — один тест перевіряє все

Краще розділяти сценарії.

### Помилка 4 — тестуємо тільки happy path

Потрібні також negative та boundary cases.

### Помилка 5 — тест нічого не перевіряє

Наприклад:

```python
def test_something():
    function()
```

Такий тест може пройти навіть тоді, коли функція повертає неправильний результат.

# 43. Практична схема написання Unit Test

Коли отримуємо нову функцію:

```python
def some_function(data):
    ...
```

рухаємося за алгоритмом:

```text
1. Зрозуміти контракт функції
          ↓
2. Визначити очікуваний результат
          ↓
3. Визначити позитивні сценарії
          ↓
4. Визначити boundary cases
          ↓
5. Визначити invalid input
          ↓
6. Визначити expected exceptions
          ↓
7. Знайти зовнішні dependencies
          ↓
8. Замокати dependencies
          ↓
9. Написати Arrange → Act → Assert
          ↓
10. Запустити тест
```

# 44. Unit Test як контракт

Цікавий спосіб дивитися на Unit Test:

> **Тест — це executable documentation.**

Наприклад:

```python
def test_desc_with_zero():
    with self.assertRaises(ValueError):
        desc(20, 0)
```

Навіть без перегляду реалізації функції ми бачимо:

> `desc()` не дозволяє передавати `0` другим аргументом.

Тест таким чином документує очікувану поведінку програми.

# 45. Що ми отримуємо від Mock

У прикладі `APIClient` Mock дозволяє нам повністю контролювати зовнішній сервіс.

Ми можемо сказати:

```text
API повернув 200
```

або:

```text
API повернув 404
```

і перевірити поведінку нашого коду.

Тобто ми тестуємо:

> **наш код, а не справжній API.**

Саме це є однією з ключових ідей Unit Testing.

# 46. Unit Test ≠ Integration Test

Це важливе розмежування.

### Unit Test

```text
Function
   ↓
Mock
   ↓
Result
```

Швидкий і ізольований.

### Integration Test

```text
Application
   ↓
Real HTTP API
   ↓
Database
   ↓
Other services
```

Перевіряє взаємодію компонентів.

Наприклад, тест `APIClient` із Mock — це Unit Test.

А тест, який реально відправляє:

```python
requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)
```

і перевіряє відповідь сервера, уже більше схожий на Integration/API test.

# 47. Що потрібно запам'ятати

## Unit Testing

* тестує окрему одиницю коду;
* перевіряє очікувану поведінку;
* повинен бути швидким та ізольованим;
* використовує assertions;
* перевіряє позитивні та негативні сценарії.

## `unittest`

* стандартна бібліотека Python;
* тести наслідують `unittest.TestCase`;
* методи тестів починаються з `test_`;
* використовується `self.assertEqual()`;
* `self.assertRaises()` перевіряє exceptions.

## Mocking

* `Mock` створює тестову залежність;
* `patch` замінює реальний об'єкт Mock-об'єктом;
* `return_value` задає результат виклику;
* `assert_called_once_with()` перевіряє взаємодію із залежністю.

# 48. Фінальна модель у голові

Коли ви бачите функцію:

```python
def function(input):
    ...
```

думайте:

```text
              UNIT TEST
                  │
        ┌─────────┴─────────┐
        │                   │
     INPUT               EXPECTED
        │                 RESULT
        │                   │
        └──────► FUNCTION ◄─┘
                    │
                    ▼
                 ACTUAL
                  RESULT
                    │
                    ▼
                 ASSERT
```

А якщо функція залежить від зовнішнього сервісу:

```text
             UNIT TEST
                 │
          ┌──────┴──────┐
          │             │
       FUNCTION       MOCK
          │             │
          └──────┬──────┘
                 ▼
              RESULT
                 │
                 ▼
              ASSERT
```

**Головна ідея заняття:**

> **Unit Test перевіряє одну конкретну поведінку коду, а Mock дозволяє ізолювати цю поведінку від зовнішніх залежностей.**