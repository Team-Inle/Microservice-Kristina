
#||||||||||||||||||||||||||||||||||||||| INDEX.JS |||||||||||||||||||||||||||||||||||||||||




#__________________________________ IMPORT SETUP ___________________________________________

import os
import sys
import json
import requests
import bs4
from flask import Flask, jsonify , request, abort, make_response
import json
from flask_restful import Api, Resource, reqparse





app = Flask(__name__)
api = Api(app)



class songWiki(Resource):
    def get(self, song, artist):
        return grab_info(artist)

api.add_resource(songWiki, "/<string:song>/<string:artist>")

#________________________________OTHER CODE________________________________



def grab_info(song, artist):
    # URL
    URL = "https://en.wikipedia.org/wiki/" + artist
    # send the request to Wikipedia song page.
    response = requests.get(URL)
    # parse the response
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # get the infobox
    infobox = soup.find('table', {'class': 'infobox'})
    # getting First row element tr
    first_tr = infobox.find_all('tr')[0]
    # from first_tr we have to find artist title.
    title = first_tr.th.div
    # getting 4th row element tr
    fourth_tr = infobox.find_all('tr')[3]
    # from first_tr we have to find artist's origin.
    origin = fourth_tr.td.a
    # getting 5th row element tr
    fifth_tr = infobox.find_all('tr')[4]
    # from first_tr we have to find artist's genre.
    genre_list = fifth_tr.td.ul
    genre = []
    for tag in genre_list:
        genre = genre.append(genre.li.a)
    # get it all together
    tune_scout = {
                    "artist": title.text,
                    "origin": origin.text,
                    "genre" : genre.text        
                }

    # printing the whole thing.
    return json.dumps(tune_scout)


















@app.errorhandler(400)
def not_found(error=None):
    message = {
        'status': 400,
        'message': 'Bad Request: ' + request.url
    }
    response = jsonify(message)
    response.status_code = 400
    return response

def ok(data):
    response = jsonify(data)
    response.status_code = 200
    return response











if __name__ == "__main__":
    app.run(debug=True)


