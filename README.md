# Cálculo de Pontos do Programa de Fidelidade

Este repositório implementa uma função para calcular pontos de um programa de fidelidade baseado no valor da compra, na forma de pagamento e no local da compra.

> ⚠️ AVISO: Todos os comandos utilizados e testes feitos neste repositório foram realizados em uma distribuição Linux Ubuntu.

## 1. Código Fornecido
O código fornecido apresentava alguns problemas, como:
- Uso incorreto do nome da variável `valor` (deveria ser `valor_compra`).
- Falta de tratamento para valores negativos.
- Consideração de centavos na pontuação.

![cod-fornecido](assets/cod-fornecido.png)

## 2. Código Corrigido
O código foi ajustado para garantir a validação das entradas e para descartar os centavos do valor da compra.

![cod-corrigido](assets/cod-corrigido.png)

## 3. Testes com Pytest
Para garantir a funcionalidade correta da função, foram implementados testes utilizando o `pytest`.

![py-test](assets/py-test.png)

## 4. Como Executar os Testes
Para rodar os testes, basta instalar o `pytest` e executar o seguinte comando:

```bash
pip install pytest
pytest -v
```

depois de executar os comandos acima você deverá obter um resultado como esse:

![py-test-results](assets/py-test-results.png)


## Aproveite este repositório!

Criado por **João Igor dos Santos Barbosa**.

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ignizxl)