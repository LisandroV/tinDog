from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    context = {
        'message': 'hola',
        'items': [
            {'name': 'Lisandro', 'age': 19},
            {'name': 'Pablo', 'age': 20}
        ]
    }
    return render_template('index.html', **context)

if __name__ == "__main__":
    app.run()
