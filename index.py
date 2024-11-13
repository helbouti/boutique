from flask import Flask , render_template , request
import psycopg2
from flask import jsonify

from flask_wtf import FlaskForm,RecaptchaField
from wtforms import (StringField,SelectField, TextAreaField, IntegerField, BooleanField, RadioField)
from wtforms.validators import InputRequired, Length , NumberRange , Regexp


app = Flask(__name__)
app.config['SECRET_KEY'] = 'lablam.2017'
#app.config['RECAPTCHA_USE_SSL']= False
#app.config['RECAPTCHA_PUBLIC_KEY']='enter_your_public_key'
#app.config['RECAPTCHA_PRIVATE_KEY']='enter_your_private_key'
#app.config['RECAPTCHA_OPTIONS']= {'theme':'black'}


def connectDB():
    return psycopg2.connect(
        host = "127.0.0.1",
        user ="root" ,
        password ="",
        database = "test"
    )


#my wtf formclass
class commandForm(FlaskForm):
    nom = StringField('nom', validators=[InputRequired()])
    prenom = StringField('prenom', validators=[InputRequired()])
    addr = StringField('addr', validators=[InputRequired()] )
    qt = IntegerField('qt', validators=[NumberRange(min=1, max=20,  message='enter 1 et 20 ')] , render_kw={"value":"1"} )
    tel = StringField('tel', validators=[InputRequired('Required'), Length(min=10, max=10),Regexp(r'^(05|06|07)\d{8}$')] )

    #Regexp(r'^(05|06|07)\d{8}$')
    #from wtforms import (StringField,SelectField...)
    #language = SelectField(u'Programming Language',choices=[('cpp', 'C++'),('py', 'Python'),('text', 'Plain Text')])#select for color
    #color = SelectField(u'Color Choice',choices=[('#FF0000', 'red'),('#00FF00','green'),('#0000FF','blue')])


#home page
@app.route("/",methods=['GET','POST'])
def index():
    form = commandForm() # wtf

    return render_template("index.html", form =form  )


@app.route("/del")
def delete_cmd():
    conn = connectDB()
    delcur = conn.cursor()
    delcur.execute("delete from clients where personid > 13 ;")
    conn.commit()
    delcur.close()
    conn.close()#closing
    return  jsonify({"deleted":"ok"})


@app.route("/mydb")
def Liste_command():
    conn = connectDB()
    cur = conn.cursor()
    cur.execute("select  * from  clients ")
    results = cur.fetchall()
    cur.close()
    conn.close() #closing
    return render_template('command.html' , results = results)


def add_client(nom ,prenom ,addr , phone ,qt):
    quey = "INSERT INTO clients (nom ,prenom ,addr , phone ,qt) VALUES (%s ,%s ,%s ,%s ,%s);"
    values= (nom ,prenom ,addr , phone ,qt)
    conn = connectDB()
    cur = conn.cursor()
    cur.execute(quey,values)
    cur.close()
    conn.commit()
    conn.close()#closing


@app.route('/handle_data', methods=['POST'])
def handle_data():
    form = commandForm() 

    if form.validate():
        return jsonify({"data":form.data})
    return jsonify({"error":form.errors})

if __name__=="__main__":
    app.run(debug=True)