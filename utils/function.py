import json
from datetime import datetime


def load_operations(filename):
    """загрузка данных из json"""
    with open(filename, "r", encoding="utf-8") as f:
        json_operations = json.load(f)
        return json_operations


def get_executed_operations(dict_list):
    """фильтрации данных по ключу """
    operations_list = []

    for file in dict_list:
        if file.get("state") == "EXECUTED":
            operations_list.append(file)
    return operations_list


def sorted_by_date(my_list):
    """функция сортировки
    5 последних операций по дате"""
    sorted_operations = sorted(my_list, key=lambda x: x["date"], reverse=True)
    return sorted_operations[:5]


def get_info_by_date(date):
    """функция переводит дату в заданный формат,
    принимает словарь, возвращает отформатированую дату """
    date_operation = datetime.fromisoformat(date)
    new_date = date_operation.strftime('%d.%m.%Y')
    return new_date


def get_purpose_of_payment(descriptions):
    """функция выводит назначение платежа"""
    info_description = descriptions.get("description")
    return info_description


def print_masked_cards(number):
    """выводит информацию на соответствие
    номера карты или счета, в зависимости от кол-ва символов
    вазвращает соответстуюший формат"""
    for card in number:
        if len(number) == 16:
            return f"{number[:4]} {number[4:6]} ** **** {number[12:]}"
        return f"**{number[-4:]}"


def conversion_transaction(operations):
    """получает строку с наименованием счета/карты
    возвращает строку в формате для вывода на печать
    использует функцию print_masked_cards
    если данные отсутствуют - выводит "нет данных" """
    if operations:
        operation_list = operations.split(" ")
        besides_the_last = " ".join(operation_list[:-1])
        number = operation_list[-1]
        masked = print_masked_cards(number)
        return f"{besides_the_last} {masked}"
    else:
        return "Нет данных"


def get_output_data(operation):
    """получает словарь, возвращает 3 строки в нужном формате,
    использует функции get_info_by_date, conversion_transaction"""
    operation_date = get_info_by_date(operation["date"])
    operation_description = operation["description"]
    conversion_from = conversion_transaction(operation.get("from"))
    conversion_to = conversion_transaction(operation.get("to"))
    operation_amount = float(operation["operationAmount"]["amount"])
    currency = operation["operationAmount"]["currency"]["name"]

    return (f'{operation_date} {operation_description}\n'
            f'{conversion_from} -> {conversion_to}\n'
            f'{operation_amount} {currency}\n')

