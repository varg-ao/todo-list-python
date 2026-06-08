tarefas = []

while True:
    print("\n=== MENU ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        print("\nLista de tarefas:")

        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa para remover!")
            continue

        print("\nLista de tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

        try:
            indice = int(input("Digite o número da tarefa a ser removida: "))
            if 1 <= indice <= len(tarefas):
                tarefa_removida = tarefas.pop(indice - 1)
                print(f"Tarefa '{tarefa_removida}' removida!")
            else:
                print("Número inválido, escolha um item da lista!")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            print("\nLista atualizada:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")
    elif opcao == "4":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")