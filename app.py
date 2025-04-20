from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template(
        'index.html',
        title="Галерея",
    )

@app.route('/about')
def about():

    return render_template('about.html', title="о нас")

app.run(debug=True)