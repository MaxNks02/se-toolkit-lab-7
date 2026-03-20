# Use a slim Python image for efficiency
FROM python:3.12-slim

# Install uv for dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory inside the container
WORKDIR /app

# Copy dependency definition and lock file
COPY pyproject.toml uv.lock ./

# Install dependencies before copying code to optimize Docker cache
RUN uv sync --frozen --no-install-project

# Copy the bot source code
COPY . .

# Final installation of the project
RUN uv sync --frozen

# Start the bot
CMD ["uv", "run", "bot.py"]