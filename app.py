from flask import Flask,render_template
from flask_bootstrap import Bootstrap


app=Flask(__name__)
Bootstrap(app)

posts=[
    {
        'author':'copy Schafer',
        'title':'Blog Post1',
        'content': 'First Post Content',
        'date_post':'April 20,2018'
    },
    {
        'author': 'jone Doe',
        'title':'Blog Post2',
        'content':'Second Post',
        'date_post':'April 21,2018'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title=title)
@app.route("/mahi")
def mahi():
    return render_template('mahi.html')

if __name__=='__main__':
    app.run(debug=True)
