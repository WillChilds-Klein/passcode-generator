import flask
import random
import time

app = flask.Flask(__name__)

PAGE_FMT = '''
<h1>{}</h1>
'''

PERIOD = 60*60*24*7             # 1 week in seconds
LENGTH = 4                      # screentime uses 4 ordinals
ALPHABET = map(str, range(10))  # screentime uses digits 0-9

@app.route('/')
def root():
    return PAGE_FMT.format(generate_code(time.time()))

def generate_code(s, period=PERIOD, length=LENGTH, alphabet=ALPHABET):
    random.seed(int(s) / period)
    return ''.join([
        alphabet[random.randint(0, len(alphabet)-1)] for _ in range(length)
    ])

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
