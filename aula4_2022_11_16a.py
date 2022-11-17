#primeiro passo: importar a biblioteca sqlite3
import sqlite3

#segundo passo: Vamos estabelecer uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#terceiro passo: criar um objeto do tipo cursor
cursor = conexao.cursor()

#quarto passo: Comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#quinto passo: Executar o comando SQL no SQLite (no cursor)
cursor.execute(sql)

#sexto passo: Exibir a consulta com todos os nomes de heróis e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")