import math


def formatar_reais(valor):
    """Converte 1234.5 em 'R$ 1.234,50' (formato brasileiro)."""
    sinal = "-" if valor < 0 else ""
    texto = f"{abs(valor):,.2f}"  # ex.: 1,234.50
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{sinal}R$ {texto}"


def ler_texto(mensagem):
    """Pede um texto e repete até o usuário digitar algo não vazio."""
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        print("Erro: este campo não pode ficar vazio.")


def ler_valor(mensagem, permitir_zero=False):
    """Pede um valor em reais e repete até ser válido.

    Por padrão o valor precisa ser maior que zero.
    Com permitir_zero=True, o zero também é aceito.
    """
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
        except ValueError:
            print("Erro: digite apenas números (ex.: 150,50).")
            continue
        if not math.isfinite(valor):
            print("Erro: valor inválido.")
            continue
        if valor < 0 or (valor == 0 and not permitir_zero):
            if permitir_zero:
                print("Erro: o valor não pode ser negativo.")
            else:
                print("Erro: o valor deve ser maior que zero.")
            continue
        return round(valor, 2)


def somar(movimentacoes, tipo):
    """Soma os valores de todas as movimentações de um tipo."""
    total = 0.0
    for m in movimentacoes:
        if m["tipo"] == tipo:
            total += m["valor"]
    return round(total, 2)


def registrar_movimentacao(movimentacoes, tipo):
    """Registra uma 'receita' ou uma 'despesa' na lista."""
    print(f"\n--- Nova {tipo} ---")
    descricao = ler_texto("Descrição: ")
    valor = ler_valor("Valor (R$): ")
    categoria = ler_texto("Categoria: ")

    movimentacoes.append({
        "tipo": tipo,
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
    })
    print(f"{tipo.capitalize()} registrada com sucesso!")


def ver_despesas(movimentacoes):
    """Lista só as despesas, numeradas a partir de 1."""
    print("\n--- Despesas ---")
    numero = 0
    for m in movimentacoes:
        if m["tipo"] == "despesa":
            numero += 1
            print(f"{numero}. {m['descricao']} | {m['categoria']} | "
                  f"{formatar_reais(m['valor'])}")
    if numero == 0:
        print("Nenhuma despesa registrada.")


def ver_total_despesas(movimentacoes):
    print("\n--- Total de despesas ---")
    if somar(movimentacoes, "despesa") == 0:
        print("Nenhuma despesa registrada.")
    else:
        print(f"Total de despesas: "
              f"{formatar_reais(somar(movimentacoes, 'despesa'))}")


def ver_saldo(saldo_inicial, movimentacoes):
    receitas = somar(movimentacoes, "receita")
    despesas = somar(movimentacoes, "despesa")
    saldo_atual = round(saldo_inicial + receitas - despesas, 2)

    print("\n--- Saldo ---")
    print(f"Saldo inicial:     {formatar_reais(saldo_inicial)}")
    print(f"Total de receitas: {formatar_reais(receitas)}")
    print(f"Total de despesas: {formatar_reais(despesas)}")
    print(f"Saldo atual:       {formatar_reais(saldo_atual)}")


def excluir_movimentacao(movimentacoes):
    print("\n--- Excluir movimentação ---")
    if len(movimentacoes) == 0:
        print("Nenhuma movimentação registrada.")
        return

    for i, m in enumerate(movimentacoes, start=1):
        print(f"{i}. [{m['tipo'].capitalize()}] {m['descricao']} | "
              f"{m['categoria']} | {formatar_reais(m['valor'])}")

    entrada = input("Número da movimentação a excluir: ").strip()
    if not entrada.isdecimal() or not 1 <= int(entrada) <= len(movimentacoes):
        print("Número inválido. Nada foi excluído.")
        return

    posicao = int(entrada) - 1
    m = movimentacoes[posicao]
    confirmacao = input(
        f"Excluir '{m['descricao']}' ({formatar_reais(m['valor'])})? (s/n): "
    ).strip().lower()

    if confirmacao == "s":
        movimentacoes.pop(posicao)
        print("Movimentação excluída.")
    else:
        print("Exclusão cancelada. Nada foi excluído.")


def mostrar_menu():
    print("\n===== ORGANIZADOR FINANCEIRO =====")
    print("1 - Registrar despesa")
    print("2 - Ver despesas")
    print("3 - Ver total de despesas")
    print("4 - Ver saldo")
    print("5 - Excluir movimentação")
    print("6 - Registrar receita")
    print("7 - Definir saldo inicial")
    print("8 - Sair")


def main():
    movimentacoes = []

    print("Bem-vindo ao Organizador Financeiro!")
    saldo_inicial = ler_valor(
        "Quanto dinheiro você possui agora? (R$, pode ser 0): ",
        permitir_zero=True,
    )

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            registrar_movimentacao(movimentacoes, "despesa")
        elif opcao == "2":
            ver_despesas(movimentacoes)
        elif opcao == "3":
            ver_total_despesas(movimentacoes)
        elif opcao == "4":
            ver_saldo(saldo_inicial, movimentacoes)
        elif opcao == "5":
            excluir_movimentacao(movimentacoes)
        elif opcao == "6":
            registrar_movimentacao(movimentacoes, "receita")
        elif opcao == "7":
            saldo_inicial = ler_valor(
                "Novo saldo inicial (R$, pode ser 0): ", permitir_zero=True
            )
            print(f"Saldo inicial definido: {formatar_reais(saldo_inicial)}")
        elif opcao == "8":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 8.")


main()