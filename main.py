tarefas = []

def carregar_tarefas():
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, concluida = linha.strip().split("|")
                tarefas.append({
                    "nome": nome,
                    "concluida": concluida == "True"
                })

    except FileNotFoundError:
        pass
def salvar_tarefas():
    with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa['nome']}|{tarefa['concluida']}\n")
def adicionar_tarefa():
    tarefa = input("Digite a tarefa:")
    tarefas.append({
        "nome": tarefa, 
        "concluida": False
    })
    print("Tarefa adicionada!")
    salvar_tarefas()
def listar_tarefas():
    print("\nLista de tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["concluida"] else "✗"
        print(f"{i}. [{status}] {tarefa['nome']}")
def remover_tarefa():
    if not tarefas:
        print("Nenhuma tarefa para remover!")
        return

    print("\nLista de tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["concluida"] else "✗"
        print(f"{i}. [{status}] {tarefa['nome']}")
    try:
        indice = int(input("Digite o número da tarefa a ser removida: "))
        if 1 <= indice <= len(tarefas):
            tarefa_removida = tarefas.pop(indice - 1)
            salvar_tarefas()    
            print(f"Tarefa '{tarefa_removida['nome']}' removida!")
        else:
            print("Número inválido, escolha um item da lista!")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")
def concluir_tarefa():
    if not tarefas:
        print("Nenhuma tarefa para concluir!")
        return

    print("\nLista de tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["concluida"] else "✗"
        print(f"{i}. [{status}] {tarefa['nome']}")

    try:
        indice = int(input("Digite o número da tarefa a ser concluída: "))
        if 1 <= indice <= len(tarefas):
            tarefas[indice - 1]["concluida"] = True
            salvar_tarefas()    
            print(f"Tarefa '{tarefas[indice - 1]['nome']}' marcada como concluída!")
        else:
            print("Número inválido, escolha um item da lista!")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")  
carregar_tarefas()
while True:
    print("\n=== MENU ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Concluir tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        concluir_tarefa()
    elif opcao == "5":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")