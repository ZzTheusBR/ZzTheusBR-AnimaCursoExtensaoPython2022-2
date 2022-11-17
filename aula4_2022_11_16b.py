#primeiro passo: importar a biblioteca sqlite3
import sqlite3

#segundo passo: Vamos estabelecer uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#terceiro passo: criar um objeto do tipo cursor
cursor = conexao.cursor()
#quarto passo: comando para inserir um herói/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

#quinto passo: Executar o comando SQL
cursor.execute(sql)

#sexto passo: Confirmar o INSERT com commit() e fechar o banco 
conexao.commit()
conexao.close()

#voltar para o arquivo "aula4_2022_11_16a.py" para ver o comando INSERT INTO funcionando