import os
import mlflow
domino_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkb21pbm9fYXBpX2tleSI6IjM3MDIyODEzYmVlZjIwNzUyMDQ0ZDFjMDU3MTI1ODc1MjRjZWMxZGY3MmEyY2ZiOGM1NTg4MjkzYjM4YWZhNjQiLCJkb21pbm9fcHJvamVjdF9uYW1lIjoibW9kZWwtZGVwbG95bWVudCIsImRvbWlub19ydW5faWQiOiJtb2RlbC1kZXBsb3llciIsInRhZ3MiOnt9fQ.4GfUjj5O7HDgrrbpKoh-RPCyEgG8gnAN1KN11oCoKB8"
os.environ["MLFLOW_TRACKING_URI"] = "https://fsec.cs.domino.tech/mlflow-efs/#"
os.environ["MLFLOW_TRACKING_TOKEN"] = domino_api_key   
client = mlflow.tracking.MlflowClient()
##Read the {PROJECT_ROOT}/mlflow_models/production/{model_name}-{model_version}.json from the project root folder
client.update_model_version(name = "Name",
                    version = version
                    stage = "Production")
##Read the {PROJECT_ROOT}/mlflow_models/archive/{model_name}-{model_version}.json
client.update_model_version(name = "Name",
                    version = version
                    stage = "Archived"
