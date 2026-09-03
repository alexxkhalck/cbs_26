# import calculator.operation 

# def main():
#     print("Hello from cbs-26!")
#     summa = calculator.operation.add(2, 3)
#     print(summa)
# import calculator.operation as co

# def main():
#     print("Hello from cbs-26!")
#     summa = co.add(2, 3)
#     print(summa)

#from calculator.operation import add #, subtract, multiply, divide
from calculator import add

def main():
    a = """"
    Арифметичний калькулятор — точка входу програми.

    Запуск:
        uv run main.py
        або
        python main.py
    """
    print(a)
    summa = add(2, 3)
    print(summa)


if __name__ == "__main__":
    main()
