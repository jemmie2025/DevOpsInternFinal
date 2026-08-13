# DevOps Intern Final Assessment

## Project Overview

This project demonstrates an end-to-end DevOps workflow for a Python application using **Linux/Ubuntu, Bash, Git/GitHub, Docker, GitHub Actions, HashiCorp Nomad, Grafana Alloy, Grafana Loki, and MLflow**.

The project covers application development, containerization, continuous integration, workload orchestration, centralized log monitoring, and optional experiment tracking.

---

## Project Structure

```text
DevOpsInternFinal/
├── .github/
│   └── workflows/
│       └── ci.yml
├── evidence/
│   ├── loki-verification.png
│   ├── mlflow-experiment.png
│   ├── nomad-allocation-status.png
│   ├── nomad-application-logs.png
│   └── nomad-job-status.png
├── mlflow/
│   └── dummy_experiment.py
├── monitoring/
│   ├── alloy-config.alloy
│   └── loki_setup.txt
├── nomad/
│   └── hello.nomad
├── scripts/
│   └── sysinfo.sh
├── Dockerfile
├── hello.py
└── README.md
```

---

## Architecture

```text
Git/GitHub
    ↓
GitHub Actions
    ↓
Python Application
    ↓
Docker
    ↓
Local Registry
    ↓
HashiCorp Nomad
    ↓
Grafana Alloy
    ↓
Grafana Loki
    ↓
Hello, DevOps!
```

MLflow is implemented separately as an optional experiment-tracking component.

---

## Task 1: Linux & Bash

The project was developed using **Ubuntu on Windows Subsystem for Linux (WSL)**.

Run the system information script:

```bash
chmod +x scripts/sysinfo.sh
./scripts/sysinfo.sh
```

Verify Python syntax:

```bash
python3 -m py_compile hello.py
```

**Result:** ✅ Linux environment and Bash script successfully verified.

---

## Task 2: Git & GitHub

Git and GitHub were used for source control and repository management.

```bash
git status
git add .
git commit -m "Complete Grafana Loki and Alloy monitoring setup"
git push origin main
```

**Result:** ✅ Project successfully version-controlled and pushed to GitHub.

---

## Task 3: Python Application

The application is defined in `hello.py`:

```python
import time

print("Hello, DevOps!", flush=True)

while True:
    time.sleep(60)
```

Application output:

```text
Hello, DevOps!
```

The application remains active so it can run as a Nomad-managed workload and generate container logs for monitoring.

**Result:** ✅ Python application successfully created and validated.

---

## Task 4: Docker Containerization

The Python application was containerized using Docker and made available through a local Docker registry.

Build the image:

```bash
docker build -t devops-hello:latest .
```

Tag and push the image:

```bash
docker tag devops-hello:latest localhost:5000/devops-hello:latest
docker push localhost:5000/devops-hello:latest
```

Verify Docker resources:

```bash
docker images devops-hello
docker ps
```

Nomad uses:

```text
localhost:5000/devops-hello:latest
```

**Result:** ✅ Docker image successfully built and made available for Nomad deployment.

---

## Task 5: GitHub Actions CI

The CI workflow is stored in:

```text
.github/workflows/ci.yml
```

The workflow runs on pushes to `main` and validates the Python application using:

```bash
python -m py_compile hello.py
```

Syntax validation is used because the application is designed to remain running continuously.

**Result:** 🟢 GitHub Actions completed successfully with a **GREEN / SUCCESS** status.

---

## Task 6: HashiCorp Nomad

The Dockerized application was deployed as a long-running Nomad service workload.

Nomad job specification:

```text
nomad/hello.nomad
```

Validate and deploy:

```bash
nomad job validate nomad/hello.nomad
nomad job run nomad/hello.nomad
nomad job status hello-devops
```

Final verified state:

```text
Type      = service
Status    = running
Running   = 1
Failed    = 0
Healthy   = 1
Unhealthy = 0
```

Verify the allocation:

```bash
nomad alloc status <allocation-id>
```

Verified allocation state:

```text
Client Status      = running
Client Description = Tasks are running
Deployment Health  = healthy
Task "hello"        = running
```

Retrieve application logs:

```bash
nomad alloc logs <allocation-id>
```

Output:

```text
Hello, DevOps!
```

### Deployment Evidence

**Nomad Job Status**

![Nomad Job Status](evidence/nomad-job-status.png)

**Nomad Allocation Status**

![Nomad Allocation Status](evidence/nomad-allocation-status.png)

**Nomad Application Logs**

![Nomad Application Logs](evidence/nomad-application-logs.png)

**Result:** 🟢 Application successfully deployed as a healthy Nomad-managed Docker workload.

---

## Task 7: Grafana Alloy & Loki Monitoring

Monitoring configuration:

```text
monitoring/
├── alloy-config.alloy
└── loki_setup.txt
```

### Loki Verification

Check Loki readiness:

```bash
curl -sS http://localhost:3100/ready
```

Successful response:

```text
ready
```

### Alloy Verification

Grafana Alloy was configured to:

- Discover Docker containers.
- Select the Nomad-managed `hello-*` container.
- Collect application logs.
- Apply `job="nomad"` and `source="docker"` labels.
- Forward collected logs to Grafana Loki.

Validate the Alloy configuration:

```bash
docker run --rm \
  -v /mnt/c/Users/godsw/DevOpsInternFinal/monitoring/alloy-config.alloy:/etc/alloy/config.alloy:ro \
  grafana/alloy:latest \
  validate /etc/alloy/config.alloy
```

The configuration validated successfully.

### End-to-End Log Verification

Query the application log directly from Loki:

```bash
curl -G -sS "http://localhost:3100/loki/api/v1/query_range" \
  --data-urlencode 'query={job="nomad"} |= "Hello, DevOps!"' \
  --data-urlencode 'start=2026-08-12T23:15:00Z' \
  --data-urlencode 'end=2026-08-12T23:25:00Z' \
  --data-urlencode 'limit=10' | python3 -m json.tool
```

Successful response included:

```text
"status": "success"
"job": "nomad"
"source": "docker"
"Hello, DevOps!"
```

### Monitoring Evidence

**Loki Log Verification**

![Loki Verification](evidence/loki-verification.png)

**Result:** 🟢 Complete monitoring pipeline successfully verified:

```text
Python → Docker/Nomad → Grafana Alloy → Grafana Loki → Hello, DevOps!
```

---

## Extra Credit: MLflow Tracking

MLflow was deployed as an isolated Docker tracking server and used to record a dummy experiment without modifying the existing CI/CD pipeline.

The experiment implementation is stored in:

```text
mlflow/dummy_experiment.py
```

Run the experiment:

```bash
python3 mlflow/dummy_experiment.py
```

Successful execution:

```text
MLflow experiment logged successfully.
```

The MLflow Tracking API confirmed the completed run:

```text
Run Name: wise-dog-975
Status: FINISHED

Metrics:
accuracy = 0.95
deployment_success = 1.0

Parameters:
environment = devops-assessment
tool = mlflow
```

### MLflow Evidence

![MLflow Experiment](evidence/mlflow-experiment.png)

**Result:** 🟢 MLflow successfully recorded and retrieved the experiment, parameters, and metrics.

---

## Final Verification

| Component | Status |
|---|---|
| Linux / Bash | ✅ Complete |
| Git & GitHub | ✅ Complete |
| Python Application | ✅ Verified |
| Docker | ✅ Complete |
| Local Registry | ✅ Working |
| GitHub Actions CI | 🟢 Success |
| Nomad Deployment | 🟢 Healthy |
| Nomad Application Logs | 🟢 `Hello, DevOps!` |
| Grafana Alloy | 🟢 Running |
| Grafana Loki | 🟢 Ready |
| Alloy → Loki | 🟢 Verified |
| Loki Log Query | 🟢 `Hello, DevOps!` |
| MLflow Tracking | 🟢 Experiment Verified |

---

## Conclusion

This assessment successfully demonstrates an end-to-end DevOps workflow covering **Linux, Bash, Git/GitHub, Python, Docker, GitHub Actions CI, HashiCorp Nomad orchestration, Grafana Alloy log collection, Grafana Loki log aggregation, and MLflow experiment tracking**.

The primary DevOps pipeline is:

```text
Git/GitHub → GitHub Actions → Docker → Nomad → Grafana Alloy → Grafana Loki
```

The successful Loki query returning **`Hello, DevOps!`** confirms that the application was deployed and its logs were successfully collected, forwarded, and queried through the monitoring pipeline.

The optional MLflow implementation additionally demonstrates experiment tracking by successfully recording and retrieving a completed run with associated parameters and metrics.