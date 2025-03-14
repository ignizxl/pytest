import pytest
from prova3 import calc_pontos

def test_pontos_lojaX_cartaoX():
    assert calc_pontos(100, True, True) == 300

def test_pontos_lojaX_sem_cartaoX():
    assert calc_pontos(100, True, False) == 150

def test_pontos_fora_lojaX_com_cartaoX():
    assert calc_pontos(100, False, True) == 100

def test_pontos_fora_lojaX_sem_cartaoX():
    assert calc_pontos(100, False, False) == 0

def test_descarta_centavos():
    assert calc_pontos(99.99, True, True) == 297  # 99 * 3

def test_valor_invalido():
    with pytest.raises(ValueError, match="O valor da compra deve ser um número."):
        calc_pontos("cem reais", True, True)

def test_valor_negativo():
    with pytest.raises(ValueError, match="O valor da compra não pode ser negativo."):
        calc_pontos(-50, True, True)
