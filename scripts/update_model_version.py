import os
import mlflow
import json
import sys

os.environ["MLFLOW_TRACKING_URI"] = "https://fsec.cs.domino.tech/mlflow-efs/"
client = mlflow.tracking.MlflowClient()
tokens = json.loads(os.getenv("PROJECT_TOKENS"))

with open(sys.argv[1], "r") as mv_file:
    model_versions = json.load(mv_file)
    for project_id in model_versions:
        tracking_token = tokens[f"PROJECT_ID_{project_id}"]
        if not tracking_token:
            raise Exception(f"Toekn not found for project id {project_id}")
        os.environ["MLFLOW_TRACKING_TOKEN"] = tracking_token
        for name_ver in model_versions[project_id]:
            client.transition_model_version_stage(
                name=name_ver["name"],
                version=str(name_ver["version"]),
                stage="Production",
            )
