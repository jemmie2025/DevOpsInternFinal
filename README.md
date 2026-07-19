# DevOps Intern Final Assessment

*Name:* Jemimah Godswill  
*Date:* July 19, 2026  

## Project Description

This project shows a DevOps workflow that uses an open-source tools including Linux, Git, Docker, GitHub Actions, Nomad, and Grafana Loki.

my  goal is to build a small automated pipeline that covers scripting, containerization, CI/CD, deployment, and monitoring.

## Project Structure

text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── monitoring/
│   └── loki_setup.txt
├── nomad/
│   └── hello.nomad
├── scripts/
│   └── sysinfo.sh
├── hello.py
├── Dockerfile
└── README.md


## Prerequisites

- Git
- Python 3
- Docker
- Nomad
- Grafana Loki

## Running the Python Script

Run:

bash
python hello.py


Expected output:

text
Hello, DevOps!


## Linux System Information Script

The script displays:
- Current user
- Current date
- Disk usage

Run:

bash
./scripts/sysinfo.sh


## Running the Docker Container

Build the Docker image:

bash
docker build -t hello-app .


Run the container:

bash
docker run hello-app


## GitHub Actions CI/CD

The GitHub Actions workflow is located at:

text
.github/workflows/ci.yml


The workflow automatically runs hello.py whenever code is pushed to the main branch.

## Running the Nomad Job

Run:

bash
nomad job run nomad/hello.nomad


The Nomad job deploys the Docker container using the configured CPU and memory resources.

## Monitoring with Grafana Loki

Loki setup instructions are available in:

text
monitoring/loki_setup.txt


The file contains instructions for starting Loki, checking Loki status, and viewing logs.

## Author

Jemimah Godswill