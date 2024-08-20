import pickle
import os

import mlflow
from mlflow.tracking import MlflowClient

from flask import Flask, request, jsonify

os.environ["AWS_PROFILE"] = "user"

MLFLOW_TRACKING_URI='http://ec2-3-76-206-134.eu-central-1.compute.amazonaws.com:5000'
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)
# path = client.download_artifacts(run_id=RUN_ID, path='preprocessor', dst_path='.')
# print(f'####### downloading the model artifacts artifact to {path}')

# with open(path, 'rb') as f_in:
#     dv = pickle.load(f_in)

RUN_ID = os.environ.get('RUN_ID', '72651ede7ade4627895b829cfe507516')
logged_model = f'runs:/{RUN_ID}/model'
model = mlflow.pyfunc.load_model(logged_model)

def prepare_features(ride_dto):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride_dto['PULocationID'], ride_dto['DOLocationID'])
    features['trip_distance'] = ride_dto['trip_distance']

    return features

def predict(features):
    predictions = model.predict(features)

    return predictions

app = Flask('bike-customer-segment-prediction')

@app.route('/predict', methods=['POST'])
def predict_controller():
    ride = request.get_json()
    print(ride)

    pred = predict(ride)
    print(pred)

    result = {
        'user_type': float(pred[0]) > 0.5,
        'model_version': RUN_ID
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)