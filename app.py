#||||||||||||||||||||||||||||||||||||||| INDEX.JS |||||||||||||||||||||||||||||||||||||||||

# TO RUN THE APP LOCALLY, USE THE ENVIRONMENT SETUP:

#           . venv/bin/activate

#  When you’re done, to deactivate the flask environment: 

#           deactivate

#__________________________________ IMPORT SETUP ___________________________________________

import os
import sys
import re
import requests
import bs4
from flask import Flask, jsonify , request, abort, make_response
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS





app = Flask(__name__)
CORS(app)
api = Api(app)



class songWiki(Resource):
    def get(self, artist):
        # URL
        URL = "https://en.wikipedia.org/wiki/" 
        # send the request to Wikipedia song page.
        response = requests.get(URL + artist)
        # parse the response
        soup = bs4.BeautifulSoup(response.text, 'html.parser') 
        # we have to find artist title.
        title = soup.find('h1', {'class': 'firstHeading'})
        # getting the intro paragraph.
        paragraphs = soup.select("p")
        # just grab the text up to contents as stated in question
        intro_paragraph = '\n'.join([ para.text for para in paragraphs[0:2]])
        intro_paragraph = re.sub(r'\[[0-9]*\]',' ', intro_paragraph)
        #intro_paragraph = re.sub(r'\s+',' ', intro_paragraph)
        #intro_paragraph = intro_paragraph.strip('\\\\') # does not work yet.
        #intro_paragraph = re.sub(r'\n','', intro_paragraph)
        # get it all together
        tune_scout = {
                        "Artist": title.text,
                        "About": intro_paragraph
                    }

        # printing the whole thing.
        return jsonify(tune_scout)

api.add_resource(songWiki, "/<string:artist>")






if __name__ == "__main__":
    app.run(debug=True)
