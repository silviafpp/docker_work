from flask import Flask, render_template
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello_world():
    r.set('comida', 'banana')
    r.set('xpto', 'teste')
    keys = [key.decode() for key in r.keys()] # convert the key values from bytes literals (redis python client default) to strings
    values = [value.decode() for value in r.mget(keys)]
    return render_template('index.html', keys=keys, values=values)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

# from flask import Flask, request, render_template
# import redis

# app = Flask(__name__)
# r = redis.Redis(host='localhost', port=6379, db=0)

# @app.route('/submit', methods=['POST'])
# def submit():
#     key = request.form['key']
#     value = request.form['value']
#     r.set(key, value)
#     return 'Key-Value pair submitted: {}={}'.format(key, value)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')


# from flask import Flask, render_template, request
# import redis

# app = Flask(__name__)
# r = redis.Redis(host='localhost', port=6379)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/register', methods=['POST'])
# def register():
#     name = request.form['name']
#     age = request.form['age']
#     r.set(name, age)
#     return 'Registration successful!'

# if __name__ == '__main__':
#     app.run(debug=True)



