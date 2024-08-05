from flask import render_template, flash, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from models import User
from forms import LoginForm, RegistrationForm



# Página de registro
def register_routes(app):
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))  # Se o usuário já estiver autenticado, redireciona para o dashboard
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Conta criada com sucesso! Você pode agora fazer login.', 'success')  # Feedback para o usuário
            return redirect(url_for('login'))
        return render_template('register.html', form=form)

    # Rota para a página de login
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))  # Se já estiver logado, redireciona para o dashboard
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()  # Busca o usuário pelo nome de usuário
            if user and user.check_password(form.password.data):
                login_user(user)  
                flash('Login bem-sucedido!', 'success')  
                return redirect(url_for('dashboard'))
            else:
                flash('Nome de usuário ou senha incorretos.', 'danger')  
        return render_template('login.html', form=form)

   
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('login'))

    @app.route('/dashboard')
    @login_required
    def dashboard():
        return 'Bem-vindo ao Conselho de Classe!'