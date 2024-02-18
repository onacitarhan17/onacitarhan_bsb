from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('name')
    surname = request.form.get('surname')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    login_type = True if request.form.get('login_type') == 'LMU Login' else False
    morning = True if request.form.get('morning') == 'True' else False
    afternoon = True if request.form.get('afternoon') == 'False' else False
    print(name, surname, email, username, password, login_type)
    from deneme import main
    main(name, surname, email, username, password, login_type)
    return "Code is working"