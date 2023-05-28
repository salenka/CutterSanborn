from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_mysql_connector import MySQL



app = Flask(__name__)
app.config['SECRET_KEY'] = 'chavesecreta'

app.config['MYSQL_USER'] = 'Salenka'
app.config['MYSQL_DATABASE'] = 'Salenka$cutter'
app.config['MYSQL_HOST'] = 'Salenka.mysql.pythonanywhere-services.com'
app.config['MYSQL_PASSWORD'] = 'univesp2023'

bootstrap = Bootstrap(app)
mysql = MySQL(app)


class CutterForm(FlaskForm):
    entrada = StringField("Digite a Entrada Principal no formato 'Sobrenome, Nome'", validators=[DataRequired()])
    submit = SubmitField('Gerar código Cutter')

@app.route('/', methods=['GET', 'POST'])
def index():
    session['entrada'] = None
    session['codigo'] = None
    form=CutterForm()
    if form.validate_on_submit():
        session['entrada'] = form.entrada.data
        session['codigo'] = retorna_codigo(session['entrada'])
        return render_template('index.html', form=form, entrada=session['entrada'], codigo=session['codigo'])
    return render_template('index.html', form=form, entrada=session['entrada'])


def retorna_codigo(entrada):
    entrada = entrada.replace(' ', '');
    consulta = f"SELECT codigo FROM CutterSanborn WHERE Sobrenome <= '{entrada}' AND ProximoNome > '{entrada}';"
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute(consulta)
    output = cur.fetchall()[0][0]
    return str(output)

