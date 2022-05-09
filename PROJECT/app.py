from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, request, flash, redirect, session, url_for
app = Flask(__name__)
app.secret_key = 'thisisaverysecretkey'

def opendb():
    engine = create_engine("sqlite:///db.sqlite")
    Session = sessionmaker(bind=engine)
    return Session()

@app.route('/', methods=['GET','POST'])
def login ():
    if request.method == 'POST':
        email = request.form.get('email')
        Password  = request.form.get('Password')
        if not email or len(email) < 11:
            flash("Enter correct email", 'danger')
            return redirect('/')
        elif not Password:
            flash('Password is required', 'danger')
            return redirect('/')
        # more like this
        else:
            session['isauth'] = True
            session['id'] = True
            session['name'] = True

            flash('Login Successfull', 'success')
            return redirect('/')

    return render_template('login.html')


@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/uploads',methods=['GET','POST'])
def upload():
    return render_template('upload.html')


@app.route('/logout',methods=['GET','POST'])
def logout():
    if "isauth" in session:
        session.pop('isauth')
    return redirect ("/")

if __name__ == '__main__':
  app.run(debug=True)





 

