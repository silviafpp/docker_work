from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello_world():
    r.incr('hits')
    count = r.get('hits').decode('utf-8')
    return f'Hello World! This page has been viewed {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



