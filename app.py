import os
from flask import Flask, request, jsonify, render, render_template
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline


os.putenv('LANG', "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "input_image.jpg"
        self.classifier = PredictionPipeline(self.filename)



@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def train_route():
    os.system("python main.py")
    os.system("dvc repro")      # for running dvc pipeline
    return "Training done Successfully....!!!"


@app.route("/predict", methods=['POST'])
@cross_origin()
def predict_route():
    image = request.json['image']
    decodeImage(image, clAPP.filename)
    result = clAPP.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    clAPP = ClientApp()
    app.run(host='0.0.0.0', port=8080)  #local host
    # app.run(host='0.0.0.0', port=8080)  #for AWS
    # app.run(host='0.0.0.0', port=80)    #for AZURE