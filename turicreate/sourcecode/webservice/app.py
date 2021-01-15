import os
import flask
import turicreate as tc
from flask import jsonify, request

UPLOAD_FOLDER  = 'imagefolder'
ML_MODEL_PATH = '../model/turidogcatv2.model'
EXTENSIONS_ALLOWED = {'png', 'jpg'}

## App settings
app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ML_MODEL'] = ML_MODEL_PATH

# validate input files
def allowed_files(fileName):
  return '.' in fileName and fileName.rsplit('.', 1)[1].lower() in EXTENSIONS_ALLOWED


def get_classification(filename):
    modelPath = os.path.join(os.getcwd(),app.config['ML_MODEL'])
    print('Model Path : ', modelPath)
    model = tc.load_model(modelPath)
    print('Analysing image..')
    sfData = tc.image_analysis.load_images(filename, with_path=True)
    classify = model.classify(sfData)
    return classify

@app.route('/imageclasify', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(message = "No file found 1"), 404
    
    file = request.files['file']
    if file.filename == '':
        return jsonify(message = 'No file found'), 404

    if file and allowed_files(file.filename):
        filePath = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'], file.filename)
        print('get os path ', os.getcwd())
        print('\nUploading file to... ', filePath)
        
        file.save(filePath)

        # run Clasification
        classify = get_classification(filePath)

        return jsonify(classification = str(classify['class']), probability = str(classify['probability'])), 200
    
    return jsonify(message = "Unknown error contact support."), 500


app.run()