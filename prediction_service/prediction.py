import yaml
import os
import json
import joblib
import numpy as np

params_path = "params.yaml"


def read_params(config_path=params_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data).tolist()[0]
    return prediction


def api_response(request):
    data = request.get_json(force=True)
    print(data)