import pandas as pd
import re as re
import sqlite3

filename = (r'Base para o teste.xlsx')
df = pd.read_excel(filename)

#Retirando os caracteres
df['Número'] = [col.replace("+", "") for col in df['Número']]
df['Número'] = [col.replace("(", "") for col in df['Número']]
df['Número'] = [col.replace(")", "") for col in df['Número']]

#Trabalhando os telefones sem o DDD ou sem o 9

numeros = df['Número']
print('Lista de números:')
for numero in numeros:
    if len(numero) != 14:
        print('-')
    else:
        print(numero)

#Trabalhando a coluna nome
print('Lista de Nomes:')
print(df['Nome'].str.capitalize())


#Banco de Dados
conectar = sqlite3.connect('novabase.db')
c = conectar.cursor() #executar consultas

def criar_tabela():
    c.execute('CREATE TABLE IF NOT EXISTS base (Nome text, Número text)')
criar_tabela()


#criando lista
lista = [
    ('Helena da silva', '558897890-4253'),
    ('Miguel de souza', '556295116-3513'),
    ('Arthur costa', '-'),
    ('Heitor dos santos','556791710-0573'),
    ('Bernardo  de oliveira','551897026-0776'),
    ('Davi pereira','-'),
    ('Théo rodrigues','556792377-7842'),
    ('Lorenzo almeida','554597248-1960'),
    ('Gabriel nascimento','555791369-3201'),
    ('Pedro lima','553895103-8581'),
    ('Benjamin araújo','555894802-0376'),
    ('Alice fernandes','-'),
    ('Laura de carvalho','558793944-4450'),
    ('Manuela gomes','-'),
    ('Valentina martins','552792678-3749'),
    ('Sophia da rocha','551595724-7080'),
    ('Isabella ribeiro','559791567-8443'),
    ('Heloísa alves','555298449-0391'),
    ('Luiza monteiro','557192745-1916'),
    ('Júlia mendes','551192178-8692'),
    ('Lorena araújo','-'),
    ('Matheus fernandes','-'),
    ('Lívia carvalho','556194767-4351'),
    ('Maria luiza gomes','-'),
    ('Cecília martins','555792044-1391'),
    ('Eloá rocha','-'),
    ('Giovanna ribeiro','-'),
    ('Maria clara alves','-'),
    ('Maria edaurda monteiro','-'),
    ('Mariana mendes','-'),
    ('Lara de barros','556792377-7842'),
    ('Beatriz freitas','553995341-4935'),
    ('Antonella barbosa','558096383-3426'),
    ('Maria júlia pinto','-'),
    ('Lucas moura','-'),
    ('Nicolas cavalcanti','-'),
    ('Joaquim dias','553293082-7984'),
    ('Samuel castro','-'),
    ('Henrique campos','-'),
    ('Rafael cardoso','555099775-8975'),
    ('Guilherme rocha','555298449-0391'),
    ('Enzo ribeiro','-'),
    ('Murilo alves','555392754-6327'),
    ('Benício monteiro','-'),
    ('Gustavo moura','-'),
    ('Isaac cavalcanti','-'),
    ('Emanuelly dias','-'),
    ('Isadora castro','-'),
    ('Ana clara da silva','555799079-4761'),
    ('Melissa souza','-'),
    ('Ana luiza costa','-'),
    ('Ana júlia santos','556994089-4792'),
    ('Esther oliveira','-'),
    ('Lavínia pereira','-'),
    ('Maitê rodrigues','-'),
    ('Maria cecília almeida','558095335-1726'),
    ('Maria alice nascimento','-'),
    ('Sarah lima','558292391-7081'),
    ('João moguel araújo','-'),
    ('Lucca rocha','-'),
    ('Enzo gabriel ribeiro','-'),
    ('Pedro henrique alves','559597951-1623'),
    ('Felipe monteiro','-'),
    ('João pedro mendes','-'),
    ('Pietro barros','556492588-1940'),
    ('Anthony freitas','-'),
    ('Daniel barbosa','-'),
    ('Bryan pinto','-'),
    ('Davi lucca moura','-'),
    ('Leonardo cavalcanti','-')]

c.executemany("""
INSERT INTO base (Nome, Número)
VALUES (?,?)
""",lista)


conectar.commit()
print('Dados inseridos com sucesso.')
conectar.close()