# Aula 2.E — Testes de Software: Lab Prático

Dois labs cobrindo os conceitos da aula: testes unitários com pytest e testes de API com FastAPI TestClient.

---

## Pré-requisitos

- Python 3.10+

---

## Configurar o ambiente

```bash
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
# venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

---

## Lab 1 — Testes Unitários com pytest

### O que é testado

`calculadora.py` tem 5 funções: `somar`, `subtrair`, `dividir`, `aplicar_desconto` e `calcular_total`.

`test_calculadora.py` cobre:
- Caminhos felizes (resultado correto)
- Erros esperados (`pytest.raises`)
- Casos limite (desconto 0, quantidade 0)

### Rodar os testes

```bash
pytest test_calculadora.py -v
```

Saída esperada:
```
test_calculadora.py::test_somar_dois_positivos              PASSED
test_calculadora.py::test_somar_com_negativo                PASSED
test_calculadora.py::test_dividir_normal                    PASSED
test_calculadora.py::test_divisao_por_zero_lanca_erro       PASSED
...
```

### Ver a cobertura de código

```bash
pytest --cov=calculadora --cov-report=term-missing test_calculadora.py
```

Para relatório HTML (abre no browser):
```bash
pytest --cov=calculadora --cov-report=html test_calculadora.py
open htmlcov/index.html
```

---

## Lab 2 — Testes de API FastAPI com TestClient

### O que é testado

`main.py` é uma API FastAPI com três endpoints: `GET /produtos`, `POST /produtos`, `DELETE /produtos`.

`test_main.py` usa `TestClient` — sem subir servidor, sem banco, testes em milissegundos.

### Rodar os testes da API

```bash
pytest test_main.py -v
```

### Rodar todos os testes com cobertura total

```bash
pytest --cov=. --cov-report=term-missing -v
```

Meta: **70%+ de cobertura** (mesmo critério do CI/CD).

---

## Estrutura dos arquivos

```
aula2e-testes-software/
├── calculadora.py          # funções a testar (Lab 1)
├── test_calculadora.py     # testes unitários (Lab 1)
├── main.py                 # API FastAPI (Lab 2)
├── test_main.py            # testes de API (Lab 2)
├── requirements.txt
├── .gitignore
└── .github/
    └── workflows/
        └── tests.yml       # CI: roda pytest em todo push
```

---

## Padrão AAA — lembrete rápido

Todo teste segue três etapas:

```python
def test_desconto_aplicado_corretamente():
    # Arrange — prepara os dados
    preco, percentual = 100.0, 20

    # Act — executa a função
    resultado = aplicar_desconto(preco, percentual)

    # Assert — verifica o resultado
    assert resultado == 80.0
```

---

## Checklist do lab

- [ ] Todos os testes passam (`pytest -v`)
- [ ] Cobertura acima de 70% (`--cov-fail-under=70`)
- [ ] Você entende cada `assert` — não apenas que passou
- [ ] Tentou quebrar uma função e viu o teste falhar?
