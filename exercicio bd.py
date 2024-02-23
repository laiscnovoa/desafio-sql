import sqlite3

#conexao do arquivo python com o banco de dados
conexao = sqlite3.connect('banco')
#conexao para uma nova variável
cursor = conexao.cursor()

# 1. criação da tabela
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

""""
2. inserindo dados
cursor.execute('INSERT INTO alunos( id, nome, idade, curso) VALUES (50, "Márcia", 20, "Português")')
cursor.execute('INSERT INTO alunos( id, nome, idade, curso) VALUES (51, "Cyntia", 23, "História")')
cursor.execute('INSERT INTO alunos( id, nome, idade, curso) VALUES (52, "Luiz Gabriel", 25, "Estatística")')
cursor.execute('INSERT INTO alunos( id, nome, idade, curso) VALUES (53, "Julia", 32, "Geografia")')
cursor.execute('INSERT INTO alunos( id, nome, idade, curso) VALUES (54, "Vanessa", 12, "História")')
cursor.execute('INSERT INTO alunos( id, nome, idade, curso) VALUES (55, "Davi", 22, "Engenharia")')
cursor.execute('INSERT INTO alunos( id, nome, idade, curso) VALUES (56, "Bin Laden", 30, "Engenharia")')
cursor.execute('INSERT INTO alunos( id, nome, idade, curso) VALUES (57, "Rodriguinho", 19, "Matemática")')
"""

""" 
3. 
selecionar todos os registros da tabela alunos
dados = cursor.execute('SELECT * FROM alunos')

selecionar o nome e a idade dos alunos com mais de 20 anos
dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

selecionar alunos do curso de engenharia em ordem alfabética
dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC')

contar número total de alunos na tabela
dados = cursor.execute('SELECT COUNT(id) FROM alunos')
"""

"""
4. 
atualizar a idade de um aluno específico na tabela
dados = cursor.execute('UPDATE alunos SET idade = 21 WHERE id = 54')

remover aluno pelo id
dados = cursor.execute('DELETE FROM alunos WHERE id = 50')
"""
"""
dados = cursor.execute('SELECT * FROM alunos')
#mostrar cada um dos dados
for alunos in dados:
    print(alunos)
"""


"""
5. criar tabela e inserir dados

cursor.execute('CREATE TABLE clientes(id_cliente INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')
cursor.execute('INSERT INTO clientes( id_cliente, nome, idade, saldo) VALUES (1, "Ingrid", 51, 7327.0)')
cursor.execute('INSERT INTO clientes( id_cliente, nome, idade, saldo) VALUES (2, "Barry", 38, 50.0)')
cursor.execute('INSERT INTO clientes( id_cliente, nome, idade, saldo) VALUES (3, "September", 61, 4821.0)')
cursor.execute('INSERT INTO clientes( id_cliente, nome, idade, saldo) VALUES (4, "Olivia", 39, 6288.0)')
cursor.execute('INSERT INTO clientes( id_cliente, nome, idade, saldo) VALUES (5, "Dora", 34, 5898.0)')
cursor.execute('INSERT INTO clientes( id_cliente, nome, idade, saldo) VALUES (6, "Ruby", 18, 8098.0)')
cursor.execute('INSERT INTO clientes( id_cliente, nome, idade, saldo) VALUES (7, "Bradley", 46, 5470.0)')
"""

"""
6.
selecionar nome e idade dos clientes com idade > 30
saldo = cursor.execute('SELECT * FROM clientes WHERE idade > 30')

calcular saldo médio dos cliente
saldo = cursor.execute('SELECT AVG(saldo) FROM clientes')

cliente com maior saldo
saldo = cursor.execute('SELECT nome, MAX(saldo) FROM clientes')

qtd de cliente com saldo > 1000
saldo = cursor.execute('SELECT COUNT(saldo) FROM clientes WHERE saldo > 1000')
"""

"""
7.
atulizar saldo de um cliente específico
cursor.execute('UPDATE clientes SET saldo = 890.50 WHERE id_cliente = 4')

remover cliente pelo id
cursor.execute('DELETE FROM clientes WHERE id_cliente = 7')
"""

"""
saldo = cursor.execute('SELECT * FROM clientes')
#mostrar dados
for clientes in saldo:
    print(clientes)
"""
"""
8.
criar tabela de compras
cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor FLOAT, FOREIGN KEY(cliente_id) REFERENCES clientes(id_cliente))')

inserção de dados
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, 2, "computador", 74.0)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, 2, "mouse sem fio", 38.0)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3, 1, "café", 19.9)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (4, 5, "aspirador de pó", 131.8)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (5, 3, "tapete", 127.5)')
"""
#consulta com o nome do cliente, produto, valor de cada compra
shop = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM compras LEFT JOIN clientes ON clientes.id_cliente = compras.cliente_id')
#mostrar dados
for compras in shop:
    print(compras)

#vão ser enviadas as informações até chegar nesse comando
conexao.commit()
#não dar conflito no sistema gerenciador
conexao.close