
from flask import Blueprint, jsonify, request, render_template, redirect #, flash

from models import Twitter, parse_records, db

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_tweets():
    tweet_records = Twitter.query.all()
    print(tweet_records)
    tweets = parsed_records(tweet_records)
    return jsonify(tweets)

@tweet_routes.route("/tweets")
def list_tweets_for_humans():
    tweet_records = Twitter.query.all()
    print(tweet_records)
    return render_template("tweets.html", message="Here's some tweets", tweets=tweet_records)

@tweet_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))

    new_tweet = Twitter(tweet=request.form["Tweet"], user=request.form["User_Name"])
    db.session.add(new_book)
    db.session.commit()

    #return jsonify({
    #    "message": "BOOK CREATED OK (TODO)",
    #    "book": dict(request.form)
    #})
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    return redirect(f"/tweets")