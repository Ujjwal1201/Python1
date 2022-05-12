from flask import Flask, render_template,request,flash,redirect
app = Flask(__name__)
app.secret_key="secret"


@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="POST":
        question=request.form.get("question")
        op1=request.form.get('op1')
        op2  = request.form.get('op2')
        op3  = request.form.get('op3')
        op4  = request.form.get('op4')
        answer = request.form.get('ans')
        category = request.form.get('category')
        if not question or len(question) < 10:
            flash('Question is required and should be at least 10 characters long', 'danger')
            return redirect('/')
        elif not op1:
            flash('Option 1 is required', 'danger')
            return redirect('/')
        elif not op2:
            flash('Option 2 is required', 'danger')
            return redirect('/')
        
        elif not op3:
            flash('Option 3 required', 'danger')
            return redirect('/')
        
        elif not op4:
            flash('option 4 is required', 'danger')
            return redirect('/') 
        
        elif not answer:
            flash('answer is required', 'danger')
            return redirect('/')
        
        elif not category:
            flash('category is required', 'danger')
            return redirect('/')
        
        else:
            flash('Question added successfully', 'success')
            return redirect('/')
        
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')    

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
