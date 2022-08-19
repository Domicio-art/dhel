import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',database='agenda',user='root',password='')

    consulta_sql = "select * from usuarios"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount)

    print("\nMostrando os serviços agendados")
    for linha in linhas:
        print("Codigo:", linha[0])
        print("Serviço:", linha[1])
        print("Nome:", linha[2])
        print("Email:", linha[3])
        print("Telefone:", linha[4])
        print("Sexo:", linha[5])
        print("Data:", linha[6])
        print("Horário:", linha[7])
        print("Descrição:", linha[8],"\n")
except Error as e:
    print("Erro ao acessar tabela MySQL", e)
finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao MySQL encerrada")

