#!pip install pyresparser
#!python -m spacy download en_core_web_sm
#!pip install nltk
#!python -m nltk.downloader words
#!pip intall flask
#!pip intall flask_restful
#!pip install -U flask-cors


# pyresparser
# nltk
# flask
# flask_restful
# flask-cors
# spacy3.5.0
# https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0-py3-none-any.whl

import nltk
nltk.download("stopwords")

from pyresparser import ResumeParser
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from fileinput import filename
import tempfile

app = Flask(__name__)
api = Api(app)
CORS(app)
class Resume(Resource):

    def post(self):
        f = request.files["resume"]
        tf = tempfile.NamedTemporaryFile()

        finalName = tf.name + "_" + f.filename
        f.save(finalName)  
        data = ResumeParser(finalName).get_extracted_data()
        response = jsonify(data)

        return response


api.add_resource(Resume, '/api/resume')

if __name__ == '__main__':
    app.run(debug=True,port=5678,host='0.0.0.0')  # run our Flask app
