import os
import mlflow
import json

domino_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkb21pbm9fYXBpX2tleSI6IjM3MDIyODEzYmVlZjIwNzUyMDQ0ZDFjMDU3MTI1ODc1MjRjZWMxZGY3MmEyY2ZiOGM1NTg4MjkzYjM4YWZhNjQiLCJkb21pbm9fcHJvamVjdF9uYW1lIjoibW9kZWwtZGVwbG95bWVudCIsImRvbWlub19ydW5faWQiOiJtb2RlbC1kZXBsb3llciIsInRhZ3MiOnt9fQ.4GfUjj5O7HDgrrbpKoh-RPCyEgG8gnAN1KN11oCoKB8"
os.environ["MLFLOW_TRACKING_URI"] = "https://fsec.cs.domino.tech/mlflow-efs/#"
os.environ["MLFLOW_TRACKING_TOKEN"] = domino_api_key   
client = mlflow.tracking.MlflowClient()

with open("model_version.json", "r") as mv_file:
    model_versions = json.load(mv_file)
    for mv in model_versions:
        client.update_model_version(name = mv["name"],
                      version = mv["version"],
                      stage = mv["stage"])
