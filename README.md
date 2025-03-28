Sistema Bancário Simples - README

📝 Descrição

Este é um programa Python que simula operações básicas de um sistema bancário, permitindo ao usuário:

- Realizar depósitos

- Efetuar saques

- Visualizar extrato

- Sair do sistema

⚙️ Funcionalidades

💰 Depósito
Aceita apenas valores positivos

Atualiza o saldo e registra no extrato

💵 Saque
Limite de 3 saques diários

Valor máximo por saque: R$ 500,00

Verifica se há saldo suficiente

Aceita apenas valores positivos

Atualiza o saldo e registra no extrato

📊 Extrato
Exibe todas as movimentações (depósitos e saques)

Mostra o saldo atual

Informa quando não há movimentações

📋 Variáveis do Sistema
saldo: Armazena o saldo atual (inicia em R$ 0,00)

limite: Valor máximo por saque (R$ 500,00)

extrato: String que acumula o histórico de transações

numero_saque: Contador de saques realizados

LIMITE_SAQUE: Número máximo de saques permitidos (3)

🚀 Como Executar
Certifique-se de ter Python instalado (versão 3.x recomendada)

Copie o código para um arquivo com extensão .py (ex: banco.py)

Execute o arquivo no terminal/comando:

bash
Copy
python banco.py

🖥️ Interface
O sistema apresenta um menu simples com opções:

Selecione uma das opções abaixo:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>

📌 Regras de Negócio
- Depósitos:

Apenas valores positivos são aceitos

- Saques:

Máximo de 3 saques por dia

Valor máximo de R$ 500,00 por saque

Não pode sacar mais que o saldo disponível

- Extrato:

Mostra todas as transações na ordem em que ocorreram

Exibe o saldo atual no final

💡 Melhorias para acrescentar

Adicionar sistema de autenticação de usuário

Implementar persistência de dados (salvar em arquivo ou banco de dados)

Adicionar opção de transferência entre contas

Criar interface gráfica (GUI)

🛠️ Tecnologias Utilizadas

Python (linguagem de programação)

Estruturas de controle (if/elif/else)

Loop while para manter o sistema em execução

Formatação de strings (f-strings)
