#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projeto TaskTracker - Fase 2 (Desafio Etapa Intermediária - Bootcamp II)
Estudante: Bruno Mateus Borges
Curso: Ciência da Computação - CEUB (Campus Asa Norte)
Descrição: Aplicação CLI em Python 3 para gerenciamento de tarefas com validação
estrita de regras de negócio (título obrigatório e prioridades padronizadas).
"""

from typing import List, Dict


def solicitar_titulo() -> str:
    """
    Solicita o título da tarefa garantindo que não seja vazio
    ou composto apenas por espaços em branco.
    """
    while True:
        titulo = input("\nDigite o título da tarefa: ").strip()
        if titulo:
            return titulo
        print("[ERRO] O título da tarefa é obrigatório e não pode ficar em branco. Tente novamente.")


def solicitar_prioridade() -> str:
    """
    Solicita a prioridade da tarefa com validação estrita.
    Aceita exclusivamente: 'Alta', 'Média' (ou 'Media') e 'Baixa'.
    """
    mapa_prioridades = {
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa",
    }

    while True:
        entrada = input("Prioridade da tarefa (Alta, Média ou Baixa): ").strip().lower()
        if entrada in mapa_prioridades:
            return mapa_prioridades[entrada]
        print("[ERRO] Prioridade inválida! Digite exclusivamente 'Alta', 'Média' (ou 'Media') ou 'Baixa'.")


def cadastrar_tarefa(tarefas: List[Dict[str, str]]) -> None:
    """
    Realiza o fluxo completo de cadastro de uma nova tarefa aplicando
    as regras de validação e atribuindo automaticamente o status 'Pendente'.
    """
    print("\n" + "=" * 55)
    print("              CADASTRAR NOVA TAREFA")
    print("=" * 55)

    titulo = solicitar_titulo()

    descricao = input("Descrição da tarefa: ").strip()
    if not descricao:
        descricao = "Sem descrição informada"

    prioridade = solicitar_prioridade()

    data_limite = input("Data limite para conclusão (ex: DD/MM/AAAA): ").strip()
    if not data_limite:
        data_limite = "Não definida"

    nova_tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }

    tarefas.append(nova_tarefa)
    print("\n[SUCESSO] Tarefa cadastrada com sucesso com status 'Pendente'!")


def visualizar_tarefas(tarefas: List[Dict[str, str]]) -> None:
    """
    Exibe todas as tarefas cadastradas de forma legível no terminal
    ou informa claramente caso a lista esteja vazia.
    """
    print("\n" + "=" * 55)
    print("             LISTA DE TAREFAS CADASTRADAS")
    print("=" * 55)

    if not tarefas:
        print("Nenhuma tarefa foi cadastrada no momento.")
        print("Dica: Escolha a opção [1] no menu para registrar sua primeira tarefa.")
        print("=" * 55)
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa #{indice:02d}")
        print(f"  • Título      : {tarefa['titulo']}")
        print(f"  • Descrição   : {tarefa['descricao']}")
        print(f"  • Prioridade  : {tarefa['prioridade']}")
        print(f"  • Data Limite : {tarefa['data_limite']}")
        print(f"  • Status      : {tarefa['status']}")
        print("-" * 55)

    print(f"Total de tarefas registradas: {len(tarefas)}")
    print("=" * 55)


def exibir_menu() -> None:
    """Exibe o menu principal de navegação contínua no terminal."""
    print("\n" + "=" * 55)
    print("         TASKTRACKER CLI - GERENCIADOR DE TAREFAS")
    print("=" * 55)
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("=" * 55)


def main() -> None:
    """Loop principal da aplicação CLI TaskTracker."""
    tarefas: List[Dict[str, str]] = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até logo e bons estudos!\n")
            break
        else:
            print("\n[ERRO] Opção inválida! Por favor, digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()