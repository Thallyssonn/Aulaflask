from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Kevinha minha esposinha linda <3!"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')