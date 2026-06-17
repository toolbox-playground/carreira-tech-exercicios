"""
LAB 1 — pytest: Testes Unitários (Aula 2.E)
Estrutura AAA: Arrange → Act → Assert
"""

import pytest
from calculadora import somar, subtrair, dividir, aplicar_desconto, calcular_total


# ── Testes de somar ───────────────────────────────────────────────────────────

def test_somar_dois_positivos():
    assert somar(2, 3) == 5

def test_somar_com_negativo():
    assert somar(-1, 5) == 4

def test_somar_retorna_float_quando_necessario():
    resultado = somar(1.5, 2.5)
    assert isinstance(resultado, float)
    assert resultado == 4.0


# ── Testes de dividir ─────────────────────────────────────────────────────────

def test_dividir_normal():
    assert dividir(10, 2) == 5.0

def test_divisao_por_zero_lanca_erro():
    # Arrange + Act + Assert em uma estrutura só
    with pytest.raises(ValueError) as exc_info:
        dividir(10, 0)
    assert "Divisão por zero" in str(exc_info.value)


# ── Testes de desconto (padrão AAA explícito) ─────────────────────────────────

def test_desconto_aplicado_corretamente():
    # Arrange
    preco = 100.0
    percentual = 20

    # Act
    resultado = aplicar_desconto(preco, percentual)

    # Assert
    assert resultado == 80.0

def test_desconto_zero_retorna_preco_original():
    assert aplicar_desconto(200.0, 0) == 200.0

def test_desconto_invalido_lanca_erro():
    with pytest.raises(ValueError):
        aplicar_desconto(100.0, -5)

def test_desconto_acima_de_100_lanca_erro():
    with pytest.raises(ValueError):
        aplicar_desconto(100.0, 110)


# ── Testes de calcular_total (missão final) ───────────────────────────────────

def test_calcular_total_sem_desconto():
    assert calcular_total(50.0, 3) == 150.0

def test_calcular_total_com_desconto():
    assert calcular_total(100.0, 2, desconto=10) == 180.0

def test_calcular_total_quantidade_zero():
    assert calcular_total(100.0, 0) == 0.0

def test_calcular_total_quantidade_negativa_lanca_erro():
    with pytest.raises(ValueError):
        calcular_total(100.0, -1)
