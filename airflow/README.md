# Airpulse 🌬️

End-to-end air quality data pipeline for India, built with a modern open-source DE stack.

## Architecture

Raw CSV (India AQI) → Python Ingest → Postgres → dbt (DuckDB) → Airflow DAG

## Stack

| Tool | Purpose |
|------|---------|
| Python + Pandas | Data ingestion |
| PostgreSQL | Raw data storage |
| DuckDB + dbt Core | Transformation layer |
| Apache Airflow | Orchestration & scheduling |
| Docker | Containerization |

## Pipeline

- `stg_air_quality` — cleans raw AQI readings, casts types, removes nulls
- `mart_city_pollution` — city-level pollution summary by pollutant

## dbt Tests

- `not_null` on city, pollutant_id, avg_pollution
- `accepted_values` on pollutant_id (SO2, NO2, OZONE, CO, PM2.5, PM10, NH3)

## How to Run

### 1. Start Airflow
```bash
cd airflow && docker compose up -d
```

### 2. Access Airflow UI
URL: http://localhost:8080
Username: airflow
Password: airflow

### 3. Trigger the DAG
Enable and trigger `airpulse_pipeline` in the UI.

## Project Structure

airpulse/
├── airflow/          # Airflow DAGs + Docker setup
├── data/             # Raw AQI CSV (gitignored)
├── ingest/           # Python ingestion scripts
└── transform/        # dbt project (models, tests, schema)

## Data Source

India Real-Time Air Quality Index — https://data.gov.in