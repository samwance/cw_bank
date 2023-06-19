import os
from src.utils import get_data, select_data, format_account, sort_data, format_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_select_data(test_data):
    data = select_data(test_data)
    assert len(data) == 5

def test_sort_data(test_data):
    assert sort_data(test_data)[2]['id'] == 142264268


def test_format_data():
    assert format_data([{"id": 214024827, "date": "2018-12-20T16:43:26.929246", "operationAmount": {"amount": "70946.18", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод организации", "from": "Счет 10848359769870775355", "to": "Счет 21969751544412966366"},]) == ['\n20.12.2018 Перевод организации\nСчет **5355 -> Счет **6366\n70946.18 USD\n']
    data = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"}]
    expected_output = ['\n26.08.2019 Перевод организации\nMaestro **** 5199 -> Счет ******9589\n31957.58 руб.\n']
    assert format_data(data) == expected_output

def test_format_account():
    assert format_account(['Maestro', '1596837868705199']) == 'Maestro **** 5199'
    assert format_account(['MasterCard', '7158300734726758']) == 'MasterCard **** **** **** 6758'
    assert format_account(['Счет', '75106830613657916952']) == 'Счет *************6952'


def test_get_data_file_exists():
    assert os.path.exists('operations.json') == True

def test_sort_data_returns_five_transactions(test_data):
    result = sort_data(test_data)
    assert isinstance(result, list)
    assert len(result) == 5

def test_format_data_returns_list(test_data):
    result = format_data(test_data)
    assert isinstance(result, list)
