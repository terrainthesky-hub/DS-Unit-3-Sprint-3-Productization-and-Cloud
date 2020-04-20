# web_app/__init__.py

from flask import Flask

from models import db, migrate
from web_app.routes.tweet_routes import tweet_routes

# application factory pattern
def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitoff_13.db"
   # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////C:\Users\lesle\Desktop\twitoff_13\twitoff-13\twitoff_13.db"
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(tweet_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
