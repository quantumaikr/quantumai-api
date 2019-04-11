from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

from app import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from Model import db
db.init_app(app)


if __name__ == "__main__":
    app.run()
