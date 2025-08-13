# crud_aluno.py
from db_config import conectar
from hashlib import sha256

def hash_senha(senha):
    return sha256(senha.encode('utf-8')).hexdigest()

def criar_aluno(nome, email, senha, status='ativo'):
    try:
        conn = conectar()
        cursor = conn.cursor()
        senha_h = hash_senha(senha)
        cursor.execute(
            "INSERT INTO Aluno (nome, email, senha, serie, status) VALUES (%s, %s, %s, %s,%s)",
            (nome, email, senha_h, serie, status)
        )
        conn.commit()
        return{"status":"sucesso","mensagem":"Aluno criado.","id":cursor.lastrowid}
    except Exception as e:
        return {"status":"erro","mensagem":str(e)}
    finally:
        try: conn.close()
        except: pass

def listar_alunos():
    try:
        conn = conectar()
        cursor = conn.cursor(ditictionary=True)
        cursor.execute("SELECT id, nome, email, serie, status FROM Aluno")
        return cursor.fetchall()
    except Exception as e:
        return {"status":"erro","mensagem":str(e)}
    finally:
        try: conn.close()
        except: pass

def obter_aluno(id_aluno):
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nome, emaill, serie, status FROM Aluno WHERE id=%s", (id_aluno,))
        row = cursor.fetchone()
        if not row:
            return {"status":"aviso","mensagem":"Aluno não encontrado."}
        return row
    except Exception as e:
        return {"status":"erro","mensagem":str(e)}
    finally:
        try: conn.close()
        except: pass

def atualizar_aluno(id_aluno, nome=None, email=None, senha=None, serie=None, status=None):
    try:
        conn = conectar()
        cursor = conn.cursor()
        campos = []
        valores = []
        if nome is not None:
            campos.append("nome=%s"); valores.append(nome)
        if email is not None:
            campos.append("email=%s"); valores.append(email)
        if nome is not None:
            campos.append("senha=%s"); valores.append(hash_senha(senha))
        if nome is not None:
            campos.append("serie=%s"); valores.append(serie)
        if nome is not None:
            campos.append("status=%s"); valores.append(status)
        if not campos:
           return {"status":"aviso","mensagem":"Nada para atualizar."}
        sql = "UPDATE Aluno SET " + ", ".join(campos) + "WHERE id=%s"
        valores.append(id_aluno)
        cursor.execute(sql, tuple(valores))
        conn.commit()
        if cursor.rowcount==0:
            return {"status":"sucesso","mensagem":str(e)}
    finally:
            try: conn.close()
            except: pass

def deletar_aluno(id_aluno):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Aluno WHERE id=%s", (id_aluno,))
        conn.commit()
        if cursor.rowcount==0:
            return {"status":"aviso","mensagem":"Aluno não encontrado."}
        return {"status":"sucesso","mensagem":"Aluno excluido."}
    except Exception as e:
            return {"status":"erro","mensagem":}                

                                
