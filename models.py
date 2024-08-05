from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Define o modelo de usuário
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID único para cada usuário
    username = db.Column(db.String(150), unique=True, nullable=False)  # Nome de usuário deve ser único
    password_hash = db.Column(db.String(128))  # Hash da senha para segurança

    # Método para definir a senha (armazena o hash da senha)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Método para verificar a senha
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))