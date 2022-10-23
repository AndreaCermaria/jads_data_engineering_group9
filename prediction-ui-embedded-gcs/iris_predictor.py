import json

import pandas as pd
from keras.models import load_model
import os
import pickle #extra add to read the model

class IrisPredictor:
    def __init__(self):
        self.model = None

    def predict_single_record(self, df):
        model_name = os.environ.get('MODEL_NAME', 'Specified environment variable is not set.')
        if self.model is None:
            self.model = pickle.load(open(model_name, 'rb')) #extra add to read the model
#            self.model = load_model(model_name)

        y_pred = self.model.predict(df)
        print(y_pred[0])
        status = (y_pred[0])
        return status
