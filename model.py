import mlflow.pyfunc
import pandas as pd
import os

# vars is a dict that the client must provide
def predict(vars):
    model_path = _model_path_from_env()
    loaded_model = mlflow.pyfunc.load_model(model_path)
    model_input = pd.DataFrame.from_dict(vars)
    model_output = loaded_model.predict(model_input)
    return model_output


def _model_path_from_env():
    if "MLFLOW_ARTIFACTS_PATH" in os.environ:
        return os.getenv("MLFLOW_ARTIFACTS_PATH")
    project_owner = os.environ.get("DOMINO_MODEL_PROJECT_OWNER", None)
    mlflow_run_id = os.environ.get("MLFLOW_RUN_ID", None)
    if project_owner and mlflow_run_id:
        return f"/artifacts/mlflow/{project_owner}/{mlflow_run_id}/artifacts/"
    else:
        raise Exception(
            f"Cannot determine artifact path from owner={project_owner} and run id={mlflow_run_id}"
        )
