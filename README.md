# Coffee Shop Analytics ☕

An interactive sales analytics dashboard built with Python and Streamlit, using the Maven Analytics Coffee Shop Sales dataset.

## Overview

This application helps users explore coffee shop sales performance through interactive filters, key performance indicators, visualizations, and a simple rule-based question interface.

## Features

- Revenue, transaction, units sold, and average ticket KPIs.
- Filters for date range, store, and product category.
- Monthly revenue trends.
- Revenue breakdown by product category.
- Top 10 products by revenue.
- Rule-based questions about revenue, categories, stores, and products.
- Questions use the complete dataset, independently of dashboard filters.

## Technology Stack

- Python
- Streamlit
- pandas
- Plotly
- openpyxl

## Dataset

Source: Maven Analytics Coffee Shop Sales dataset.

The dataset covers January to June 2023 and contains transaction dates, quantities, prices, store locations, and product information.

## Run Locally

Requirements: Python 3.9 or a compatible version.

1. Clone or download this repository.
2. Create and activate a virtual environment.
3. Install the dependencies.
4. Run the application.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m streamlit run test_app.py
```

Open `http://localhost:8501` in your browser.

## Analytical Definitions

- **Revenue:** transaction quantity multiplied by unit price, summed across rows.
- **Transaction:** one row represents one transaction, based on the observed dataset structure.
- **Average ticket:** total revenue divided by the number of unique transaction IDs.

## Limitations

The question interface uses predefined keyword rules rather than a large language model. It supports a limited set of question patterns and is not a general-purpose conversational AI system.

## Project Purpose

This project demonstrates an approach to interactive business intelligence, sales analysis, and accessible data exploration.
