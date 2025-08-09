# Resilience Testing of Celery: An Experimental Approach Using Fault Injection

This repository is a companion page for the following project:

> Resilience Testing of Celery: An Experimental Approach Using Fault Injection

It contains all the material required for replicating our experiments, including: the architecture, Docker-related files, the Celery tasks, and fault injection mechanisms, as well as supplementary tools. Some additional results, not included in the main documentation for the sake of space, are also provided.

## Experiment Results and Data

The results of the experiments are available in the `experiments/` directory.

## Experiment Replication

To replicate the experiment, follow these steps:

### Getting Started

1. **Clone the repository**

   ```sh
   git clone https://github.com/pccql/celery_chaos.git
   cd celery_chaos
   ```

2. **Start the environment using Docker Compose**

   ```sh
   docker compose up
   ```

### Running Experiments

#### 1. Configure Experiment Tasks

The script in `app/tasks/add_experiment_tasks_to_queue.py` is configured to create a predefined number of tasks every minute. You can modify this behavior in the script to change the task creation rate or amount as needed.

#### 2. Run Chaos Scenarios

To trigger chaos scenarios (fault injections), open your browser and visit [http://localhost:8000/docs](http://localhost:8000/docs) to access the FastAPI Swagger UI for the chaos service. From there, you can use the interactive API documentation to initiate fault injections such as CPU exhaustion, memory exhaustion, or network delay.

#### 3. Monitor with Grafana

1. Open Grafana in your browser at [http://localhost:3000](http://localhost:3000).
2. Log in with the default credentials (`admin` / `admin`).
3. Add Prometheus as a data source:
   - Go to **Configuration > Data Sources**.
   - Click **Add data source** and select **Prometheus**.
   - Set the URL to `http://prometheus:9090` and save.
4. Import the pre-configured dashboard:
   - Go to **Dashboards > Import**.
   - Upload the `celery-monitoring-grafana-dashboard.json` file from the repository.
   - Select the Prometheus data source you just created when prompted.
5. You can now visualize Celery and system metrics using the imported dashboard.

### Cleaning Up

To clean up Docker containers and volumes:

```sh
docker compose down -v
```

## Directory Structure

This is the root directory of the repository. The directory is structured as follows:

```
celery_chaos
 .
 |
 |--- app/           Celery app, task definitions, and experiment scripts.
 |    |--- tasks/    Individual task scripts (CPU, memory, request, etc.).
 |
 |--- chaos/         Chaos engineering faults for injection.
 |    |--- scenarios/  Scenario definitions.
 |
 |--- experiments/   Results of experiment executions.
 |
 |--- prometheus.yml Prometheus configuration for metrics scraping.
 |
 |--- docker-compose.yml  Docker Compose setup for the full environment.
 |
 |--- redis.Dockerfile   Dockerfile for Redis service.
 |
 |--- celery-monitoring-grafana-dashboard.json  Grafana dashboard for monitoring.
 |
 |--- README.md      This file.
```
