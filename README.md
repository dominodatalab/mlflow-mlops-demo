# mlflow-mlops-demo
Demonstration of MLOps using MLflow and Domino Model Endpoint

We use this project to demonstrate one possible lifecycle of MLFlow models, from development to testing and deployment to production. MLFlow keeps track of the models and artifacts, with Domino deploying them as Model APIs. The MLFlow models are transitioned to Staging before deployment. When the model APIs have been tested, the code is moved to the main branch, at which point the MLFlow model is transitioned to Production.

For simplicity and demonstration purposes, the transition to staging is done from the workspace using the MLFlow version of the model. This reflects the iterative nature of the development process.

Using MLFlow in Domino
It is expected that this git repository will be used to create a git based project in Domino, with the user positioned to develop in the right branch ('dev' in this case). A workspace using the Domino environment, 'MLflow-Stage-Transition--Workspace' and the JupyterLab IDE must be used for the proper setup of OS environment variables and connection to the proxy. 

The mlflow-model.ipynb notebook shows how to use the MLFlow client to create experiments and runs and to register models. The environment variables required for the client to function properly, like 'MLFLOW_TRACKING_URI' are already populated within the workspace. Some familiarity with these MLFlow specific environment variables is assumed.

Once the models are created, they can be viewed by launching the Tracking UI from the workspace launcher (the MLFLOW icon under the Notebook section of the launcher)

Testing the model
Once the model has been developed and registered with MLFlow, it can be tested by deploying it as a model API in Domino. In order to do that, use the deploy-to-staging.ipynb notebook. You will notice that the project name is the same as the current project. The environment ID reflects a Domino environment that was created specifically to run the model (in this case, the environment named 'domino_mlflow_api_endpoint'). We would like to have created the environment using the requirements file stored as part of the model artifacts, but the model API container is locked down.

Only an invocation by the project owner or the use of a service token will enable the transition to Staging and deployment of the model API.

If all goes well, a Domino model API will be deployed with a model ID and model version ID. The Domino model will have environment variables set to reflect the MLFLOW_MODEL_NAME, MLFLOW_MODEL_OWNER, MLFLOW_MODEL_VERSION and MLFLOW_RUN_ID. These variables are crucial to mount the model artifacts during deployment and locate them when the model is running. 

The MLFlow model will be transitioned to Staging, with tags set to reflect the corresponding DOMINO_MODEL_ID and DOMINO_MODEL_VERSION_ID. These tags can be used to formulate the Domino model API URL and access it.

Transition to production
Once the model has been satisfactorily tested, update the scripts/model_version.json file to indicate which models are ready for production use. The models are grouped by their project ID.

Within github, repository secrets are stored for each project ID. The name of the secret is PROJECT_ID_{project_id} and the value is a service token generated specifically for that project ID. This token is also stored as a kubernetes secret with the name {project_id}.apikey

When a stage transition is requested, the mlflow proxy checks for a service token and matches the value provided in the API call with the apikey file stored as a kubernetes secret.

Service tokens are typically for use by clients like github, in order to avoid user credential propagation.

When the code is merged to the 'main' branch of this repository, a git action is triggered, which will invoke the MLFlow endpoint with the right token for the project ID in model_version.json and transition the MLFlow model to production.


