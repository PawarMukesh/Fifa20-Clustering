from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "The default route shown by slash"

@app.route('/project')
def fifa20():
    return "Fifa20 Clustering"

if __name__ == "__main__":
    app.run()