from flask import Flask
from db_config import init_app, db
import models  # importa models para registrar no SQLAlchemy

app = Flask(_name_)
app.config["SECRET_KEY"] = "sua_chave_aqui"

# inicializa com MySQL
app = init_app(app)

with app.app_context():
    db.create_all()

if _name_ == "_main_":
    app.run(debug=True)