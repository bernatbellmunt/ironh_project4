from flask import Flask, request, jsonify
import random
import operator
import numpy as np
import markdown.extensions.fenced_code
import tools.sql_queries as esecuele
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()



from wordcloud import WordCloud
from langdetect import detect
from textblob import TextBlob

import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt




app = Flask(__name__)

# Render the markdown - OK
@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# GET ENDPOINTS: SQL 
# SQL get everything - OK
@app.route("/everything/")
def sql ():
    return jsonify(esecuele.get_everything())

"""# I WANT TO GET THE SEASON_NO, EPISODE_NO AND EPISODE_NAME FROM MY DB
@app.route("/episodes")
def episodes ():
    return jsonify(esecuele.return_episodes_and_seasons())"""


# return all details from a Character -OK
@app.route("/details/<name>", )
def lines_from_characters (name):
    return jsonify(esecuele.get_everything_from_character(name))

#sentiment of each line - OK --> potser podria passarho a un grafic per veure quina es la seva evolució?
@app.route("/sa/<name>/", )
def sa_from_character (name):
    everything = esecuele.get_just_dialogue(name)
    #return jsonify(everything)
    list_sentiment = [sia.polarity_scores(i["line"])["compound"] for i in everything]
    return jsonify(list_sentiment)

#avg sentiment all lines of a character- OK
@app.route("/avg_sa/<name>/", )
def avg_sa_from_character (name):
    everything = esecuele.get_just_dialogue(name)
    #return jsonify(everything)
    list_sentiment = [sia.polarity_scores(i["line"])["compound"] for i in everything]
    return jsonify(sum(list_sentiment)/len(list_sentiment))

#avg sentiment of all characters lines of a character - OK
@app.route("/all_sentiments", )
def all_sa ():
    everything = esecuele.get_lines_from_char()
    new_d = {}
    for k, v in everything.items():
        list_sentiment = [sia.polarity_scores(i)["compound"] for i in v]
        avg_sent = sum(list_sentiment)/len(list_sentiment)
        new_d[k]=avg_sent
    return new_d

#returns all episodes
@app.route("/episodes", )
def all_episodes ():
    everything = esecuele.get_episodes()
    return jsonify(everything)

@app.route("/count_lines", )
def countlines ():
    everything = esecuele.get_lines_from_char()
    newd = {}
    sorted={}
    for key in everything:
        newd[key]=len(everything[key])
    
    return jsonify(newd)


#word cloud per character - does not work - processing a lot and 
"""@app.route("/wordcloud/<name>", )
def word_cloud_charac (name):
    everything = esecuele.get_lines_from_char()
    lines = everything[name]
    st=""
    for dialog in lines:
        st+=dialog
    wordcloud = WordCloud().generate(st)
    plt.figure(figsize=(10,10), facecolor="k")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    #plt.savefig('images/wordcloud.png', facecolor='k', bbox_inches='tight')
    plt.show();
    return wordcloud"""

####### POST -- DOES NOT WORK - METHOD NOT ALLOWED
@app.route("/post", methods=["POST"])
def insert_row ():
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