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