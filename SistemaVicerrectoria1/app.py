from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def usuario():
    return render_template('usuario.html')

if __name__ == '__main__':
    app.run(debug=True)

