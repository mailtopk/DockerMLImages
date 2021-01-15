# Train a ML model using turicreate fromwork

## Goal

Train a model to identify an given image if its a cat or a dog and test and build a web service to use the trained mode and responce back with classification and probability

### Prereqisit

- Anaconda
    This can be installed from [Anaconda](https://www.anaconda.com)

- Data Set

 Download data set from [Kaggle Cats and Dogs Dataset](https://www.microsoft.com/en-us/download/details.aspx?id=54765) to turicreate/dataset folder

- Postman

## Create conda 

Conda environment file is under turicreate/env folder. 

``` shell_session
    $cd turicreat/env
    $conda env create -f environment.yml
```

Activate environment

```shell_session
  $ 
  $conda activate turienv
```

## Folder struture 

turicreat
    env
    sourcecode
        model
        webservice
        mlmodel

_model_ folder contain code to create ml model using turicreate framework. This code help to build ML model using turicreate framework

_webservice_ folder has web service code which uses the trined model to predict given image (cat or dog).

_mlmodel_ folder contain trainned model.


## Running webservice

``` shell_session
    $cd turicreate/sourcecode/webservice
    $python app.py
```

Output should look something like

```shell_session
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Postman settings

POST http://127.0.0.1:5000/imageclasify

Request

```json
    file: dogsamplefile.jpg
```

Response body

``` json
    {
        "classification": "['Dog']",
        "probability": "[0.9999999052977787]"
    }
```
