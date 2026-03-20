# LMS Telegram Bot: Development Plan

This development plan outlines the iterative approach to building the LMS Telegram bot. The architecture prioritizes testability by strictly decoupling the core command logic from the Telegram transport layer.

## Phase 1: Project Scaffolding (Task 1)
We will establish the project skeleton using `uv` for dependency management within a `pyproject.toml` file. The core feature will be a `bot.py` entry point that supports a `--test` CLI flag. This allows the isolated handler functions to be executed and verified directly via stdout without requiring an active Telegram connection or bot token. 

## Phase 2: Backend Integration (Task 2)
Building on the existing FastAPI LMS backend, we will connect the bot to the API. The isolated handlers will transition from returning placeholder text to fetching and formatting real data for slash commands like `/health`, `/labs`, and `/scores`.

## Phase 3: Intent-Based Natural Language Routing (Task 3)
We will integrate an LLM client to process plain text inputs from users. The backend API endpoints will be wrapped and exposed to the LLM as actionable tools, enabling natural language intent routing and dynamic, multi-step reasoning.

## Phase 4: Containerization and Deployment (Task 4)
Finally, the completed bot will be containerized using a `Dockerfile`. It will be added as a dependent service to the existing `docker-compose.yml` stack and deployed to the VM to run concurrently with the backend infrastructure.