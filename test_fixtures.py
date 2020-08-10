import pytest


class Borrower:

    def __init__(self, name, cpf, how_much, instalments, reason):
        self.name = name
        self.cpf = cpf
        self.how_much = how_much
        self.instalments = instalments
        self.reason = reason


@pytest.fixture
def borrower():
    borrower = Borrower('Tiago Góes da Silva', '434.201.478-56', 5000, 24, 'Comprar uma bike')
    return borrower


@pytest.fixture
def borrower2():
    b2 = Borrower('Priscila', '367.222.388-30', 2000, 12, 'Casamento')
    return b2


def test_borrower_data(borrower):
    assert 'Tiago' in borrower.name
    assert '434.201.478-56' == borrower.cpf


def test_borrower_request(borrower):
    assert 5000 == borrower.how_much
    assert 24 == borrower.instalments
    assert 'Comprar uma bike' == borrower.reason


def test_borrower_diff(borrower, borrower2):
    assert borrower.name != borrower2.name
    assert borrower.cpf != borrower2.cpf
