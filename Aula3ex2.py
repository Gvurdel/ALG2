#Um hospital deseja implementar um sistema de gerenciamento de pacientes utilizando listas encadeadas.
#Cada nó da lista deve armazenar informações sobre um paciente, como nome, idade e número do prontuário.
#A lista deve ser ordenada pelo número do prontuário.
#Escreva um programa em Python que permita ao usuário realizar as seguintes operações:
#-Adicionar um novo paciente à lista, informando nome, idade e número do prontuário.
#-Listar todos os pacientes da lista pelo nome.
#-Buscar um paciente pelo número do prontuário.
#O programa deve exibir mensagens de erro caso o número do prontuário já exista na lista ou caso o número informado na busca não seja encontrado.



class Paciente:
    def __init__(self, nome, idade, prontuario):
        # Inicializa um objeto Paciente com nome, idade e número do prontuário
        self.nome = nome
        self.idade = idade
        self.prontuario = prontuario
        self.proximo = None  # O próximo nó na lista encadeada inicialmente é None

class ListaPacientes:
    def __init__(self):
        # Inicializa a lista encadeada de pacientes
        self.cabeca = None  # Inicialmente, a lista está vazia

    def adicionar_paciente(self, nome, idade, prontuario):
        # Adiciona um novo paciente à lista encadeada, mantendo a ordem pelo número do prontuário
        novo_paciente = Paciente(nome, idade, prontuario)  # Cria um novo objeto Paciente
        if self.cabeca is None:
            # Se a lista estiver vazia, o novo paciente se torna a cabeça da lista
            self.cabeca = novo_paciente
        elif self.cabeca.prontuario == prontuario:
            # Se o número do prontuário já existe na lista, exibe uma mensagem de erro
            print("Número de prontuário já existente. Por favor, escolha outro número.")
            return
        elif self.cabeca.prontuario > prontuario:
            # Se o número do prontuário do novo paciente é menor que o da cabeça da lista,
            # o novo paciente se torna a nova cabeça da lista
            novo_paciente.proximo = self.cabeca
            self.cabeca = novo_paciente
        else:
            # Caso contrário, encontra a posição correta para inserir o novo paciente na lista
            anterior = self.cabeca
            atual = self.cabeca.proximo
            while atual is not None and atual.prontuario < prontuario:
                anterior = atual
                atual = atual.proximo
                # Atualiza o valor de "atual" para o próximo nó na lista encadeada
            if atual is not None and atual.prontuario == prontuario:
                # Se o número do prontuário já existe na lista, exibe uma mensagem de erro
                print("Número de prontuário já existente. Por favor, escolha outro número.")
                return
            # Insere o novo paciente na posição correta na lista
            novo_paciente.proximo = atual
            anterior.proximo = novo_paciente

    def listar_pacientes_por_nome(self):
    # Lista todos os pacientes da lista encadeada ordenados pelo nome
        if self.cabeca is None:
        # Se a lista estiver vazia, exibe uma mensagem indicando isso
            print("Lista de pacientes vazia.")
        else:
        # Cria uma lista temporária para armazenar os pacientes
            pacientes_temp = []
            atual = self.cabeca
            while atual is not None:
                pacientes_temp.append(atual)
                atual = atual.proximo
        
        # Bubble Sort para ordenar os pacientes pelo nome
            tamanho = len(pacientes_temp)
            for i in range(tamanho - 1):
                for j in range(0, tamanho - i - 1):
                    if pacientes_temp[j].nome > pacientes_temp[j + 1].nome:
                        pacientes_temp[j], pacientes_temp[j + 1] = pacientes_temp[j + 1], pacientes_temp[j]

        # Exibe as informações dos pacientes ordenados pelo nome
            for paciente in pacientes_temp:
                print("Nome:", paciente.nome, "| Idade:", paciente.idade, "| Prontuário:", paciente.prontuario)

    def buscar_paciente_por_prontuario(self, prontuario):
        # Busca um paciente na lista encadeada pelo número do prontuário
        if self.cabeca is None:
            # Se a lista estiver vazia, exibe uma mensagem indicando isso
            print("Lista de pacientes vazia.")
        else:
            # Percorre a lista encadeada procurando o paciente com o número do prontuário especificado
            encontrado = False
            atual = self.cabeca
            while atual is not None:
                if atual.prontuario == prontuario:
                    # Se o paciente for encontrado, exibe suas informações
                    print("Paciente encontrado - Nome:", atual.nome, "| Idade:", atual.idade, "| Prontuário:", atual.prontuario)
                    encontrado = True
                    break
                atual = atual.proximo
                # Atualiza o valor de "atual" para o próximo nó na lista encadeada
            if not encontrado:
                # Se o paciente não for encontrado, exibe uma mensagem indicando isso
                print("Paciente com prontuário", prontuario, "não encontrado.")


def main():
    lista_pacientes = ListaPacientes()  # Cria uma nova lista de pacientes

    while True:
        # Loop principal do programa, exibindo as opções para o usuário
        print("\nEscolha uma opção:")
        print("1 - Adicionar paciente")
        print("2 - Listar pacientes por nome")
        print("3 - Buscar paciente por prontuário")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            # Se o usuário escolher adicionar paciente, solicita informações e adiciona à lista
            nome = input("Nome do paciente: ")
            idade = int(input("Idade do paciente: "))
            prontuario = int(input("Número do prontuário: "))
            lista_pacientes.adicionar_paciente(nome, idade, prontuario)

        elif opcao == '2':
            # Se o usuário escolher listar pacientes por nome, exibe a lista
            print("\nListagem de pacientes:")
            lista_pacientes.listar_pacientes_por_nome()

        elif opcao == '3':
            # Se o usuário escolher buscar paciente por prontuário, solicita o número do prontuário e busca na lista
            prontuario = int(input("Informe o número do prontuário: "))
            lista_pacientes.buscar_paciente_por_prontuario(prontuario)

        elif opcao == '4':
            # Se o usuário escolher sair, encerra o programa
            print("Encerrando o programa.")
            break

        else:
            # Se o usuário escolher uma opção inválida, exibe uma mensagem de erro
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()  # Chama a função main para iniciar o programa
