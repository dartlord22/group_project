from flask_app import app
from flask_app.controller import users, shows


if __name__ == '__main__':
    app.run(debug=True)