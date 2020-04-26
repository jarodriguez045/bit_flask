from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Jose"
    name = "Rodriguez"
    return render_template('index.html', author=author, name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run configured for running out of docker