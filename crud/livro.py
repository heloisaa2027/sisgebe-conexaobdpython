# crud_livro.py
from db_config import conectar

def criar_livro(titulo, autor, isbn=None, sinopse=None, capa=None, quantidade=1, categoria_id=None):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Livro (titulo, autor, isnb, sinopse, capa, quantidade, categoria_id) VALUES (%s, %s, %s, %s, %s, %s, %s,)",
            (titulo, author_or_none(autor), isbn, sinopse, capa, quantidade, categoria_id)
        )
        conn.commit()
        return {"status":"sucesso","mensagem":"Livro criado com sucesso.","id":cursor.lastrowid}
    except Exception as e:
        return {"status":"erro","mensagem":str(e)}
    finally:
        try: conn.close()
        except: pass

def author_or_none(a):
    return a if a is not None else ""

def listar_livros():
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Livro")
        return cursor.fechall()
    except Exception as e:
        return {"status":"erro","mensagem":str(e)}
    finally:
        try: conn.close()
        except: pass

def obter_livro(id_livro):
    try:
        conn = conectar()                    
