from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'sneha singh 2201330100263'

if __name__ == '__main__':
    app.run(port=5000)
