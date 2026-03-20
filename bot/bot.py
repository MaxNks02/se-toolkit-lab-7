from services.api import get_health, get_labs, get_scores
from services.llm import process_natural_language


def handle_command(command_input: str) -> str:
    """
    Processes both slash commands and natural language intent routing.
    """
    text = command_input.strip()
    if not text:
        return "I didn't catch that. Try /help."

    # Process standard slash commands
    if text.startswith("/"):
        parts = text.split()
        command = parts[0].lower()

        if command == "/start":
            return "Welcome to the LMS Bot! I can help you check system health, browse labs, and view scores. You can also just ask me questions in plain English!"
        elif command == "/help":
            return (
                "Here are the commands you can use:\n"
                "/start - Welcome message\n"
                "/help - Lists all available commands\n"
                "/health - Check if the backend is up and running\n"
                "/labs - List all available labs\n"
                "/scores <lab_id> - Get pass rates for a specific lab (e.g., /scores lab-04)"
            )
        elif command == "/health":
            return get_health()
        elif command == "/labs":
            return get_labs()
        elif command == "/scores":
            if len(parts) < 2:
                return "Please specify a lab. Usage: /scores <lab_id> (e.g., /scores lab-04)"
            return get_scores(parts[1])
        else:
            return f"Unknown command: {command}. Type /help to see what I can do."

    # P1.1: Intent-Based Natural Language Routing
    # If it is not a slash command, send it to the LLM to figure out what to do!
    else:
        return process_natural_language(text)