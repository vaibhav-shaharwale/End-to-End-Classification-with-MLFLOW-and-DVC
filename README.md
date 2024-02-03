# End-to-End-Classification-with-MLFLOW-and-DVC

## Create new virtual environment
```bash
conda create -n <name> python=<version>
conda activate <name>
```
utility : those functionality that will  be used frequently in code are called as utility related functionality

add "artifacts/*" in .gitignore # so that it not get commited

## Workflow

1. Update config.yaml
2. Update secrets.yaml [Optional] "credentials"
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

## Dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/vaibhav-shaharwale/End-to-End-Classification-with-MLFLOW-and-DVC.mlflow \
MLFLOW_TRACKING_USERNAME=vaibhav-shaharwale \
MLFLOW_TRACKING_PASSWORD=6402cccc2a9084b399ba652290d918ca3005ec55 \
python script.py


Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/vaibhav-shaharwale/End-to-End-Classification-with-MLFLOW-and-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=vaibhav-shaharwale

export MLFLOW_TRACKING_PASSWORD=6402cccc2a9084b399ba652290d918ca3005ec55
```
