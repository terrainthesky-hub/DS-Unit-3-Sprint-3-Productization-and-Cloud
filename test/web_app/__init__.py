# web_app/__init__.py

from flask import Flask

from web_app.models import db, migrate
from web_app.routes.tweet_routes import tweet_routes
from web_app.routes.home_routes import home_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.admin_routes import admin_routes
from web_app.routes.stats_routes import stats_routes

# application factory pattern
def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitoff.db"
   # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////C:\Users\lesle\Desktop\twitoff_13\twitoff-13\twitoff_13.db"
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(tweet_routes)
    app.register_blueprint(home_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(stats_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
