from conectar import connect

def inserir(mydb, nome, email, senha, cpf):
        mycursor = mydb.cursor()

        sql = 'INSERT INTO usuario (nome, email, senha, cpf) VALUES (%s, %s, %s, %s)'
        val = (nome, email, senha, cpf)

        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "Cadastrado com sucesso!")

        mycursor.close()



def autenticar(mydb, email, senha):
        mycursor = mydb.cursor()
        sql = ('SELECT email, senha FROM usuario WHERE email = %s AND senha = %s')
        val = (email, senha)
        mycursor.execute(sql, val)
        resultado = mycursor.fetchall()

        for i, x in resultado:
                
            if email == i and senha == x:
                 print ( mycursor.rowcount,' Login aceito!')
                 return True
                 
        mycursor.close()
      
       