
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user_name = request.form['user_name']
        if user_name == '':
            return render_template('index.html', message='Por favor, digite um nome de usuário.')
        return render_template('thank-you.html', value=user_name)

if __name__ == "__main__":
    app.run(debug=True)