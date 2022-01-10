from flask import Flask, render_template

app = Flask(__name__)

# app.config["SECRET_KEY"] =
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site_data.db'

posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)
    # return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return render_template("about.html")
    # return "<h1>About Page</h1>"


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


# app name
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    # defining function
    return f"<h1>Page not found: <br><br> {e}<h1>"
