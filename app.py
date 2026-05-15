from flask import Flask
app = Flask(__name__)

@app.route('/a')
def home():
    return 'Hello Dosto, from Flask and Docker World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
