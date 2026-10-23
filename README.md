# Coffee Shop Analytics ☕

An interactive sales analytics dashboard built with Python and Streamlit using the Maven Analytics Coffee Shop Sales dataset.

## Overview

This application helps users explore coffee shop sales performance through interactive filters, key performance indicators, visualizations, and a rule-based question interface.

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

**Source:** [Maven Analytics – Coffee Shop Sales](https://mavenanalytics.io/data-playground/coffee-shop-sales)

The dataset contains transaction records for a fictional coffee shop operating across three New York City locations. It covers January through June 2023 and includes 149,116 records and 11 fields.

### Download and prepare the data

1. Open the [official Coffee Shop Sales dataset page](https://mavenanalytics.io/data-playground/coffee-shop-sales).
2. Sign in to your Maven Analytics account or create a free account if prompted.
3. Download the Excel dataset.
4. Create a folder named `data` in the root directory of this repository, if it does not already exist.
5. Place the downloaded Excel file inside that folder and ensure its filename is exactly:

   `Coffee Shop Sales.xlsx`

The expected path is:

`data/Coffee Shop Sales.xlsx`

The dataset is excluded from this repository. Each user must download it separately from the original source.

## Run Locally

Requirements: Python 3.9 or a compatible version.

### 1. Clone the repository

```bash
git clone https://github.com/juanf0714-stp/coffee-shop-analytics.git
cd coffee-shop-analytics
```

### 2. Download and prepare the dataset

Follow the instructions in the Dataset section above before launching the application.

### 3. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Launch the application

```bash
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
