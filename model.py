import mlflow.pyfunc
import pandas as pd
import os
import logging

logger = logging.getLogger(name=__name__)

# vars is a dict that the client must provide
def predict(vars):
    model_path = _model_path_from_env()
    print(f"Model artifacts path is {model_path}")
    loaded_model = mlflow.pyfunc.load_model(model_path)
    print(f"Model loaded...")
    model_input = pd.DataFrame(vars)
    print(f"Model input is {model_input}")
    model_output = loaded_model.predict(model_input)
    print(f"Model output is {model_output}")
    return model_output


def _model_path_from_env():
    if "MLFLOW_ARTIFACTS_PATH" in os.environ:
        return os.getenv("MLFLOW_ARTIFACTS_PATH")
    model_owner = os.environ.get("MLFLOW_MODEL_OWNER", None)
    mlflow_run_id = os.environ.get("MLFLOW_RUN_ID", None)
    if model_owner and mlflow_run_id:
        return f"/artifacts/mlflow/{model_owner}/{mlflow_run_id}/artifacts/model"
    else:
        raise Exception(
            f"Cannot determine artifact path from owner={model_owner} and run id={mlflow_run_id}"
        )
