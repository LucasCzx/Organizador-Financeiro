<div align="center">

# 💰 Organizador Financeiro

**Controle receitas, despesas e saldo direto do terminal.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Dependências](https://img.shields.io/badge/dependências-nenhuma-success)
![Dados](https://img.shields.io/badge/dados-somente%20em%20memória-orange)

Criado por **Lucas Carlos**

</div>

---

## 📌 Sobre

Programa de terminal em Python para controle financeiro pessoal. Usa apenas Python básico e a biblioteca padrão, sem instalar nada. Todos os dados ficam **somente na memória**: ao fechar o programa, tudo é apagado.

## ✨ Funcionalidades

| Opção | Descrição |
|:---:|---|
| **1** | Registrar despesa (descrição, valor e categoria) |
| **2** | Ver despesas numeradas |
| **3** | Ver total de despesas |
| **4** | Ver saldo atual |
| **5** | Excluir movimentação, com confirmação |
| **6** | Registrar receita (descrição, valor e categoria) |
| **7** | Definir ou corrigir o saldo inicial |
| **8** | Sair |

## 🧮 Cálculo do saldo

```
saldo atual = saldo inicial + receitas − despesas
```

Alterar o saldo inicial recalcula o saldo atual sem mexer nas movimentações.

## 🚀 Como executar

Requisito: **Python 3** instalado.

```bash
python financeiro.py
```

Ao iniciar, o programa pede o saldo inicial (pode ser `0`).

## 🖥️ Exemplo de uso

```
--- Saldo ---
Saldo inicial:     R$ 100,50
Total de receitas: R$ 1.000,00
Total de despesas: R$ 90,00
Saldo atual:       R$ 1.010,50
```

## 🛡️ Validações

- Campos de texto não podem ficar vazios.
- Valores de movimentações devem ser números maiores que zero.
- O saldo inicial aceita zero, mas não valores negativos.
- Aceita vírgula ou ponto decimal (`150,50` ou `150.50`).
- Na exclusão, só é aceito o número de um registro existente. Entrada inválida não exclui nada.
- Valores exibidos no formato brasileiro (`R$ 1.234,50`).

## ⚠️ Limitações

- Os dados **não são salvos**: ao encerrar o programa, tudo é perdido.
- Não utiliza banco de dados, arquivos, APIs ou bibliotecas externas.

## 👤 Autor

**Lucas Carlos**
GitHub: [@LucasCzx](https://github.com/LucasCzx)

## 📄 Direitos autorais

Copyright © 2026 Lucas Carlos. Todos os direitos reservados.
É proibida a cópia, modificação ou distribuição deste projeto sem autorização do autor.