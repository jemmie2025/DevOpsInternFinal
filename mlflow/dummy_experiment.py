import mlflow

mlflow.set_tracking_uri("http://localhost:5001")
mlflow.set_experiment("devops-extra-credit")

with mlflow.start_run():
    mlflow.log_param("environment", "devops-assessment")
    mlflow.log_param("tool", "mlflow")
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_metric("deployment_success", 1)

    print("MLflow experiment logged successfully.")
