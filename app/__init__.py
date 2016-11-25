from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views

# @app.route("/")
# def main():
#    return "Welcome!"

if __name__ == "__main__":
    app.run()

