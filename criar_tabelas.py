# criar_tabelas.py
import os
from flask import Flask
from db_config import init_app, db
import models  # registra os modelos no metadata

# apague o banco antigo se quiser recriar do zero
DB_FILE = os.path.join(os.path.dirname(_file_), "sgb.db")
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

app = Flask(_name_)
init_app(app)

with app.app_context():
    db.create_all()
    print("Banco SQLite criado e tabelas geradas com sucesso.")