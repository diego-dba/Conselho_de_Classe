from app import app, db
from models import User

def create_user(username, password):
    with app.app_context():
        # Verifique se o usuário já existe
        user = User.query.filter_by(username=username).first()
        if user:
            print(f"Usuário '{username}' já existe.")
            return

        new_user = User(username=username)
        new_user.set_password(password)

        # Adicionar e confirmar a adição
        db.session.add(new_user)
        db.session.commit()
        print(f"Usuário '{username}' criado com sucesso.")

if __name__ == "__main__":
    create_user('teste8', 'teste8')  
