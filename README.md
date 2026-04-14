🏦 Sistema Bancário em Python com POO

📌 Descrição

Desafio da DIO (Digital Innovation One) para desenvolver uma nova versão do sistema bancário, desta vez aplicando os conceitos de Programação Orientada a Objetos (POO) em Python. Nesta etapa, o foco está na organização do código por meio de classes e objetos, tornando a aplicação mais estruturada e reutilizável.

🚀 Evolução do Projeto

Esta versão representa a evolução das implementações anteriores, incorporando:

Estrutura baseada em POO

Melhor organização e reutilização de código

Uso de classes abstratas para transações

Maior clareza e manutenção do sistema

🎯 Objetivos do Projeto

Aplicar conceitos de Programação Orientada a Objetos (POO)

Estruturar melhor o código 

Simular um sistema bancário mais próximo do mundo real

Evoluir de uma abordagem procedural para orientada a objetos

🧠 Conceitos de POO Aplicados

Classes e objetos

Herança (ContaCorrente → Conta)

Encapsulamento (uso de atributos privados)

Abstração com classes abstratas (Transacao)

Polimorfismo (Saque e Deposito)

Separação de responsabilidades

🏗️ Arquitetura do Sistema

Nesta versão final, o projeto deixou de ser um conjunto de funções para se tornar um sistema inteligente. Apliquei os pilares da POO para dar 'vida' aos componentes do banco. Agora a aplicação não apenas processa dados, ela modela o mundo real: clientes, contas e transações interagem através de contratos inteligentes, garantindo que o sistema seja modular, escalável e extremamente seguro.

Modelagem de Domínio: Utilizei Abstração e Herança para criar entidades como PessoaFisica e ContaCorrente, reaproveitando lógica e definindo comportamentos específicos para cada perfil.

Polimorfismo em Ação: Através de uma interface comum de Transacao, operações de Saque e Depósito seguem o mesmo protocolo, mas executam regras distintas, tornando o código elegante e fácil de expandir.

Encapsulamento Estratégico: Protegi a integridade financeira do sistema usando propriedades privadas e métodos de acesso, garantindo que o saldo e o histórico só sejam alterados através de fluxos validados.

⚙️ Funcionalidades

O sistema permite:

👤 Cadastro de clientes

🏦 Criação de contas bancárias

💰 Depósito

💸 Saque (com validações)

📄 Extrato de transações

🔄 Gerenciamento de contas e usuários

📋 Menu interativo via terminal

🧠 Explicação da Arquitetura

A classe Conta representa a base do sistema, sendo responsável pelas operações essenciais como depósito e saque, além de manter o saldo e o histórico de transações.

A classe ContaCorrente, que herda de Conta, implementa regras específicas de negócio, como limite de valor por saque e quantidade máxima de saques diários, demonstrando o uso de herança e polimorfismo.

O controle das transações foi modelado por meio de uma classe abstrata Transacao, que define um contrato para operações financeiras. A partir dela, foram implementadas as classes Saque e Deposito, responsáveis por executar e registrar cada operação, promovendo maior organização e flexibilidade no sistema.

O Historico armazena todas as transações realizadas, incluindo tipo, valor e data, permitindo a geração de extratos detalhados.

Já a classe Cliente, juntamente com sua especialização PessoaFisica, gerencia os dados dos usuários e suas contas, permitindo o relacionamento entre cliente e múltiplas contas.

🛠️ Tecnologias Utilizadas

Python

VSCode

🚀 Como Executar

🔹 Pré-requisitos

Python instalado

🔹 Passos

Clone o repositório: git clone https://github.com/seu-usuario/seu-repositorio.git

Acesse a pasta do projeto: cd seu-repositorio

Execute o programa: python sistema_bancario.py

💻 Exemplo de Uso

Bem-vindo(a) ao Banco Python!

[d] Depositar

[s] Sacar

[e] Extrato

[nc] Nova Conta

[lc] Listar Contas

[nu] Novo Usuário

[q] Sair

📚 Aprendizados

Aplicação prática de Programação Orientada a Objetos

Organização de sistemas mais complexos

Separação de responsabilidades entre classes

Evolução de código procedural para orientado a objetos

💡 Melhorias Futuras

Interface gráfica (GUI)

Persistência de dados (banco de dados)

Sistema de autenticação

API REST para operações bancárias

Suporte a múltiplas contas por cliente

📌 Conclusão

Este projeto mostra como a POO e uma boa modelagem transformam um sistema simples em uma aplicação robusta. Foi uma ótima experiência sair de um script básico para uma estrutura completa em POO.

