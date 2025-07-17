from abc import ABC, abstractmethod
from datetime import datetime



class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    
    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            
        elif valor > 0:
            self._saldo -= valor
            return True
        else:
            print("Operação falhou! O valor informado é inválido.") 
        
        return False     

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False
        
        return True

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes    

    def adicionar(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y")
        })

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar(self)
            print(f"Saque de R$ {self.valor:.2f} realizado com sucesso!")
        

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar(self)
            print(f"Depósito de R$ {self.valor:.2f} realizado com sucesso!")

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite 
        self.limite_saques = limite_saques

    
    def sacar(self, valor):
        numero_saques = len([t for t in self.historico.transacoes if t["tipo"] == Saque.__name__])
        
        excedeu_limite = valor > self.limite    
        excedeu_saques = numero_saques >= self.limite_saques
        
        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários atingido.")
        else:
            return super().sacar(valor)
        
        return False

    def __str__(self):
        return (f"Agência: {self.agencia}\n"
                f"C/C: {self.numero}\n"
                f"Titular: {self.cliente.nome}\n"
        )  
              
              
              
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, transacao, conta):
        if conta in self.contas:
            transacao.registrar(conta)
        else:
            print("Conta não encontrada.")    

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, endereco, data_nascimento, cpf):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

def menu():
    menu = """\n

    Bem-vindo(a) ao Banco Python!
    Escolha uma opção:

    [d] Depositar
    [s] Sacar
    [e] Extrato 
    [nc] Novo Conta
    [lc] Lista Contas
    [nu] Novo Usuário
    [q] Sair

    => """

    return input(menu)

def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None
    
def recuperar_conta(cliente):
    if not cliente:
        print("Cliente não encontrado.")
        return 
    

    if not cliente.contas:
        print("Nenhuma conta encontrada para o cliente.")
        return 
    return cliente.contas[0]  

def depositar(clientes):
   cpf = input("Informe o CPF do cliente: ")
   cliente = filtrar_clientes(cpf, clientes)     
   if not cliente:
       print("Cliente não encontrado. Cadastre o cliente primeiro.")
       return
   valor = float(input("Informe o valor do depósito: "))
   transacao = Deposito(valor)
   conta = recuperar_conta(cliente)
   if not conta:
       print("Conta não encontrada. Cadastre a conta primeiro.")
       return
   cliente.realizar_transacao(transacao, conta)
   
   
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    
    if not cliente:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")
        return
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    conta = recuperar_conta(cliente)
    if not conta:
        print("Conta não encontrada. Cadastre a conta primeiro.")
        return
    cliente.realizar_transacao(transacao, conta)    

def exibir_extrato(clientes):   
        cpf = input("Informe o CPF do cliente: ")
        cliente = filtrar_clientes(cpf, clientes)   

        if not cliente:
            print("Cliente não encontrado. Cadastre o cliente primeiro.")
            return
        

        conta = recuperar_conta(cliente)
        if not conta:
            print("Conta não encontrada. Cadastre a conta primeiro.")
            return
            
        if conta:
                print("\n================ EXTRATO ================\n")
                for transacao in conta.historico.transacoes:
                    print(f"{transacao['tipo']}: R$ {transacao['valor']:.2f} - {transacao['data']}")
                print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
                print("\n==========================================\n")


def criar_cliente(clientes):
        cpf = input("Informe o CPF (somente números): ")
        cliente = filtrar_clientes(cpf, clientes)
        
        if cliente:
            print("Cliente já cadastrado.")
            return 
        
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        
        cliente = PessoaFisica(nome = nome, endereco = endereco, data_nascimento = data_nascimento, cpf = cpf)
        clientes.append(cliente)
        
        print(f"Cliente {nome} cadastrado com sucesso!")

def criar_conta(numero_conta, clientes, contas):
        cpf = input("Informe o CPF do cliente: ")
        cliente = filtrar_clientes(cpf, clientes)
        
        if not cliente:
            print("Cliente não encontrado. Cadastre o cliente primeiro.")
            return
        
        conta = ContaCorrente.nova_conta(numero = numero_conta, cliente = cliente)
        contas.append(conta)
        cliente.contas.append(conta)
        print(f"Conta criada com sucesso! Número da conta: {conta.numero}")
         

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    
    print("\nLista de Contas:")
    for conta in contas:
        print(str(conta))



def main():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == 'd':
            depositar(clientes)
        
        elif opcao == 's':
            sacar(clientes)
        
        elif opcao == 'e':
            exibir_extrato(clientes)

        elif opcao == 'nu':
            criar_cliente(clientes)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)    

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            print("Obrigado por usar o Banco Python! Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")        

main()            