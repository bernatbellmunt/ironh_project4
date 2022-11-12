from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
import tools.sql_queries as esecuele
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# GET ENDPOINTS: SQL 
# SQL get everything
@app.route("/sql/")
def sql ():
    return jsonify(esecuele.get_everything())

@app.route("/sql/<name>", )
def lines_from_characters (name):
    return jsonify(esecuele.get_everything_from_character(name))

#all lines of a character-> we pass sentiment
@app.route("/sa/<name>/", )
def sa_from_character (name):
    everything = esecuele.get_just_dialogue(name)
    #return jsonify(everything)
    list_sentiment = [sia.polarity_scores(i["line"])["compound"] for i in everything]
    return jsonify(list_sentiment)

#avg sentiment all lines of a character-
@app.route("/avg_sa/<name>/", )
def avg_sa_from_character (name):
    everything = esecuele.get_just_dialogue(name)
    #return jsonify(everything)
    list_sentiment = [sia.polarity_scores(i["line"])["compound"] for i in everything]
    return jsonify(sum(list_sentiment)/len(list_sentiment))

#avg sentiment of all characters lines of a character
"""@app.route("/sa/all_characters", )
def all_sa ():
    everything = esecuele.get_lines_from_all()
    for """


####### POST
@app.route("/insertrow", methods=["POST"])
def try_post ():
    # Decoding params
    my_params = request.args
    season_no = my_params["season_no"]
    episode_no = my_params["episode_no"]
    episode_name = my_params["episode_name"]
    character_name = my_params["character_name"]
    line = my_params["line"]

    # Passing to my function: do the inserr
    esecuele.insert_one_row(season_no, episode_no, episode_name, character_name, line)
    return f"Query succesfully inserted"


if __name__ == "__main__":
    app.run(port=9000, debug=True)