
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_mysql_connector import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'senha que gera chave secreta (campo oculto) para cada sessão do usuário'

app.config['MYSQL_USER'] = 'Salenka'
app.config['MYSQL_DATABASE'] = 'Salenka$cutter'
app.config['MYSQL_HOST'] = 'Salenka.mysql.pythonanywhere-services.com'
app.config['MYSQL_PASSWORD'] = 'univesp2023'

bootstrap = Bootstrap(app)
mysql = MySQL(app)


class NameForm(FlaskForm):
    name = StringField('Digite a Entrada Principal', validators=[DataRequired()])
    submit = SubmitField('Gerar código Cutter')


@app.route('/')
def index():
    '''form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))'''
    return render_template('index.html')

GERA_CODIGO = 'select codigo from CutterSanborn where sobrenome="Smit"'

@app.route('/mysql_test')
def mysql_test():
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute(GERA_CODIGO)
    output = cur.fetchall()[0][0]
    return str(output)

