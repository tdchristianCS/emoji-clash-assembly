from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    link="<a href='/about'>About Page</a>"
    return render_template('home.html', name='User')

@app.route('/about')
def about_page():
    link="<a href='/'>Back to home Page</a>"
    return render_template("about.html")




if __name__ == '__main__':
    app.run()