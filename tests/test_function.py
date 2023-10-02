from utils.function import get_info_by_date, print_masked_cards, get_executed_operations, sorted_by_date, \
    load_operations, conversion_transaction
import os
def test_get_info_by_date():
    assert get_info_by_date('2022-01-01') == '01.01.2022'
    assert get_info_by_date('2022-02-15') == '15.02.2022'
    assert get_info_by_date('2022-12-31') == '31.12.2022'
    assert get_info_by_date('2023-02-15') == '15.02.2023'
    assert get_info_by_date('2023-12-31') == '31.12.2023'
    assert get_info_by_date('2021-03-17') == '17.03.2021'
    assert get_info_by_date('2021-03-01') == '01.03.2021'


def test_print_masked_cards():
    assert print_masked_cards("1234567890123456") == "1234 56 ** **** 3456"
    assert print_masked_cards("1234567890") == "**7890"
    assert print_masked_cards("1111") == "**1111"


def test_get_executed_operations():
    input_data = [
        {"id": 1, "state": "PENDING"},
        {"id": 2, "state": "EXECUTED"},
        {"id": 3, "state": "FAILED"},
        {"id": 4, "state": "EXECUTED"},
        {"id": 5, "state": "PENDING"},
    ]
    result = get_executed_operations(input_data)
    expected = [
        {"id": 2, "state": "EXECUTED"},
        {"id": 4, "state": "EXECUTED"},
    ]
    assert result == expected


def test_sorted_by_date():
    test_data = [
        {"date": "2023-09-22", "operation": "Buy"},
        {"date": "2023-09-20", "operation": "Sell"},
        {"date": "2023-09-21", "operation": "Buy"},
        {"date": "2023-09-19", "operation": "Sell"},
        {"date": "2023-09-18", "operation": "Buy"},
    ]
    result = sorted_by_date(test_data)
    assert len(result) == 5
    assert result == [
        {"date": "2023-09-22", "operation": "Buy"},
        {"date": "2023-09-21", "operation": "Buy"},
        {"date": "2023-09-20", "operation": "Sell"},
        {"date": "2023-09-19", "operation": "Sell"},
        {"date": "2023-09-18", "operation": "Buy"},
    ]


def test_load_operations():
    path = os.path.join('tests', 'test_operations.json')
    assert len(load_operations(path)) == 1


def test_not_conversion_transaction():
    assert conversion_transaction(None) == "Нет данных"







