from biblioteca import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nome=form.nome.data).first()
    
    if usuario and check_password_hash(usuario.senha, form.senha.data):
        session['usuario_logado'] = usuario.nome
        flash(f'{usuario.nome} logado com sucesso!')
        proxima_pagina = request.form.get('proxima', url_for('index'))  # Redireciona para a index se não houver próxima
        return redirect(proxima_pagina)
    else:
        flash('Usuário ou senha inválidos.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)  # Remover o usuário da sessão
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))
