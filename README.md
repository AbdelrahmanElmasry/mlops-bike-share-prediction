# mlops-bike-share-prediction
This project uses data from the Bay Wheels bike-sharing program to create a model to predict whether a rider departing from a certain station is most likely a returnung member or a casual user. Bay Wheels could leverage these insights to tailor campaigns to users at particular stations during selected times which's may increase more member acqusition.


## Configure aws credentials
```bash
aws configure --profile "user"
```

or set the AWS environment variables
```bash
export AWS_ACCESS_KEY_ID=

export AWS_SECRET_ACCESS_KEY=
export AWS_DEFAULT_REGION=eu-central-1
```

 Start remote MLflow tracking server
 ```bash
 mlflow server -h 0.0.0.0 -p 5000 --backend-store-uri postgresql://mlflow:mlflow5000@mlflowdb.ch2aoukmao7z.eu-central-1.rds.amazonaws.com:5432/mlflow --default-artifact-root s3://mlflow-artifacts-data-store/mlflow/ --artifacts-destination s3://mlflow-artifacts-data-store/
```

Create deployment pipenv with the exact dependencies versions

```bash
pipenv install scikit-learn==1.5.1 flask requests gunicorn --python=3.9
```