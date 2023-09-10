import urllib.request, json

url = "https://xkcd.com/info.0.json"
response = urllib.request.urlopen(url)
data = response.read()
dict = json.loads(data)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", datum=dict)

@app.route("/<name>")
def hello_name(name):
    return "Hello "+ name

@app.route("/contact")
def home():
    return render_template("contact.html")

@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Michaela" 
    return render_template("about.html", aboutName=name)   

if __name__ == "__main__":
    app.run()

app.run(debug=True)

