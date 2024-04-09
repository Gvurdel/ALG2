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
        self.nome = nome
        self.idade = idade
        self.prontuario = prontuario
        self.proximo = None

class ListaPacientes:
    def __init__(self):
        self.cabeca = None

    def adicionar_paciente(self, nome, idade, prontuario):
        novo_paciente = Paciente(nome, idade, prontuario)
        if self.cabeca is None:
            self.cabeca = novo_paciente
        elif self.cabeca.prontuario == prontuario:
            print("Número de prontuário já existente. Por favor, escolha outro número.")
            return
        elif self.cabeca.prontuario > prontuario:
            novo_paciente.proximo = self.cabeca
            self.cabeca = novo_paciente
        else:
            anterior = self.cabeca
            atual = self.cabeca.proximo
            while atual is not None and atual.prontuario < prontuario:
                anterior = atual
                atual = atual.proximo
            if atual is not None and atual.prontuario == prontuario:
                print("Número de prontuário já existente. Por favor, escolha outro número.")
                return
            novo_paciente.proximo = atual
            anterior.proximo = novo_paciente

    def listar_pacientes_por_nome(self):
        if self.cabeca is None:
            print("Lista de pacientes vazia.")
        else:
            atual = self.cabeca
            while atual is not None:
                print("Nome:", atual.nome, "| Idade:", atual.idade, "| Prontuário:", atual.prontuario)
                atual = atual.proximo

    def buscar_paciente_por_prontuario(self, prontuario):
        if self.cabeca is None:
            print("Lista de pacientes vazia.")
        else:
            encontrado = False
            atual = self.cabeca
            while atual is not None:
                if atual.prontuario == prontuario:
                    print("Paciente encontrado - Nome:", atual.nome, "| Idade:", atual.idade, "| Prontuário:", atual.prontuario)
                    encontrado = True
                    break
                atual = atual.proximo
            if not encontrado:
                print("Paciente com prontuário", prontuario, "não encontrado.")


def main():
    lista_pacientes = ListaPacientes()

    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar paciente")
        print("2 - Listar pacientes por nome")
        print("3 - Buscar paciente por prontuário")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            nome = input("Nome do paciente: ")
            idade = int(input("Idade do paciente: "))
            prontuario = int(input("Número do prontuário: "))
            lista_pacientes.adicionar_paciente(nome, idade, prontuario)
            

        elif opcao == '2':
            print("\nListagem de pacientes:")
            lista_pacientes.listar_pacientes_por_nome()

        elif opcao == '3':
            prontuario = int(input("Informe o número do prontuário: "))
            lista_pacientes.buscar_paciente_por_prontuario(prontuario)

        elif opcao == '4':
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
