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
    borrower = Borrower('Sergio', '254.896.748-56', 5000, 24, 'Comprar uma bike')
    return borrower


@pytest.fixture
def borrower2():
    b2 = Borrower('Fernando', '856.695.874-55', 2000, 12, 'teste')
    return b2


def test_borrower_data(borrower):
    assert 'Sergio' in borrower.name
    assert '254.896.748-56' == borrower.cpf


def test_borrower_request(borrower):
    assert 5000 == borrower.how_much
    assert 24 == borrower.instalments
    assert 'Comprar uma bike' == borrower.reason


def test_borrower_diff(borrower, borrower2):
    assert borrower.name != borrower2.name
    assert borrower.cpf != borrower2.cpf
