# Slack AI Data Bot MVP

A minimal Slack bot that converts natural language questions into SQL
using LangChain, executes them on a PostgreSQL database, and returns
results directly in Slack.

------------------------------------------------------------------------

## Overview

This project implements a Slack-based AI data assistant. Users can ask
questions about sales data in natural language, and the bot will:

1.  Convert the question to SQL using a Large Language Model via
    LangChain.
2.  Execute the SQL query on a PostgreSQL database.
3.  Return the results back to Slack.

Example query in Slack:

    /ask-data show revenue by region for 2025-09-01

Example response:

    Region | Revenue
    -----------------
    North  | 125000.50
    South  | 54000.00
    West   | 40500.00

------------------------------------------------------------------------

## Architecture

    Slack Slash Command
            ↓
    FastAPI Backend
            ↓
    LangChain (NL → SQL)
            ↓
    PostgreSQL Database
            ↓
    Formatted Result → Slack

Components:

-   Slack Slash Command `/ask-data`
-   FastAPI backend server
-   LangChain SQL generation
-   PostgreSQL query execution

------------------------------------------------------------------------

## Project Structure

    slack-ai-data-bot
    │
    ├── app
    │   ├── main.py
    │   │
    │   ├── database
    │   │   └── postgres.py
    │   │
    │   ├── llm
    │   │   └── sql_generator.py
    │   │
    │   └── pipeline
    │       └── query_pipeline.py
    │
    ├── scripts
    │   └── seed_db.sql
    │
    ├── tests
    │   ├── test_llm.py
    │   └── test_pipeline.py
    │
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## Setup Instructions

### 1. Clone the repository

    git clone <your-repo-url>
    cd slack-ai-data-bot

### 2. Install dependencies

    pip install -r requirements.txt

### 3. Configure environment variables

Create a `.env` file:

    OPENAI_API_KEY=your_api_key
    DB_HOST=localhost
    DB_NAME=analytics
    DB_USER=postgres
    DB_PASSWORD=your_password

### 4. Setup PostgreSQL database

Run:

    psql -U postgres -f scripts/seed_db.sql

------------------------------------------------------------------------

## Running the Application

Start the FastAPI server:

    uvicorn app.main:app --reload --port 3000

Expose it using ngrok:

    ngrok http 3000

Use the HTTPS URL provided by ngrok when configuring Slack.

------------------------------------------------------------------------

## Slack Integration

Create a Slack app and add a slash command:

Command:

    /ask-data

Request URL:

    https://<your-ngrok-url>/ask-data

Example:

    /ask-data show revenue by region for 2025-09-01

------------------------------------------------------------------------

## Features

-   Natural language → SQL generation using LangChain
-   PostgreSQL query execution
-   Slack slash command interface
-   Clean formatted output
-   Error handling for failed queries

------------------------------------------------------------------------

## Stretch Goals (Not Implemented)

Possible future improvements:

-   Export results as CSV
-   Generate charts for date range queries
-   Query result caching
-   SQL validation and security safeguards

------------------------------------------------------------------------

## Tech Stack

-   Python
-   FastAPI
-   LangChain
-   PostgreSQL
-   Slack API
-   ngrok

------------------------------------------------------------------------

## Author

Jewel Jain
