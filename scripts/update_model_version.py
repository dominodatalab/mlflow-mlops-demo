import os
import mlflow
import json
import sys

os.environ["MLFLOW_TRACKING_URI"] = "https://fsec.cs.domino.tech/mlflow-efs/"
domino_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkb21pbm9fYXBpX2tleSI6IjM3MDIyODEzYmVlZjIwNzUyMDQ0ZDFjMDU3MTI1ODc1MjRjZWMxZGY3MmEyY2ZiOGM1NTg4MjkzYjM4YWZhNjQiLCJkb21pbm9fcHJvamVjdF9uYW1lIjoibW9kZWwtZGVwbG95bWVudCIsImRvbWlub19ydW5faWQiOiJtb2RlbC1kZXBsb3llciIsInRhZ3MiOnt9fQ.4GfUjj5O7HDgrrbpKoh-RPCyEgG8gnAN1KN11oCoKB8"
#domino_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkb21pbm9fYXBpX2tleSI6IjE3ODU2MjA5NTg4NDg4ZTgiLCJkb21pbm9fcHJvamVjdF9uYW1lIjoibWxmbG93LW1sb3BzLWRlbW8iLCJkb21pbm9fcnVuX2lkIjoiLSIsInRhZ3MiOnsiZG9taW5vX3Byb2plY3RfaWQiOiI2MzE4Y2ZmOWY0ZDMwMTM0NGZmMGMxMWYifX0.iYCfOOjKWPYu9Gq3Vc0Kka6-ZZOpWJH37wYqjUfxNNI"   
os.environ["MLFLOW_TRACKING_TOKEN"] = domino_api_key
client = mlflow.tracking.MlflowClient()

with open(sys.argv[1], "r") as mv_file:
    model_versions = json.load(mv_file)
    for mv in model_versions:
        if ("stage" in mv) and (mv["stage"] in ["Production", "Archived"])
            client.transition_model_version_stage(name = mv["name"],
                        version = mv["version"],
                        stage = mv["stage"])
