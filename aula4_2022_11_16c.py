#primeiro passo: importar a biblioteca sqlite3
import sqlite3

#PASSOS 2 E 3 VIRARÂO função conectar()
def conectar():
  #segundo passo: Vamos estabelecer uma conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")

  #terceiro passo: criar um objeto do tipo cursor
  cursor = conexao.cursor()

  return conexao, cursor