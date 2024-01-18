# End-to-End-Classification-with-MLFLOW-and-DVC

## Create new virtual environment
'''bash
conda create -n <name> python=<version>
conda activate <name>
'''
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
