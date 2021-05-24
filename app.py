from flask import Flask
from utils import smart, ups


def create_app():
    
    app = Flask(__name__)

    app.register_blueprint(smart.bp)
    app.register_blueprint(ups.bp)


    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


