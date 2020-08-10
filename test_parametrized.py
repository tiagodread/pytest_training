import pytest


@pytest.mark.parametrize("valor, resultado", [(1, 2), (2, 3), (5, 6)])
def test_soma(valor, resultado):
    assert 1 + valor == resultado


