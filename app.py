from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/mes2311', methods=['GET'])
def mes2311():
    return render_template('mes2311.html')

if __name__ == '__main__':
    app.run()
