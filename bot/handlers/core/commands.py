def handle_command(command_input: str) -> str:
    """
    Processes plain text commands for the --test mode.
    These are placeholder responses for Task 1.
    """
    command = command_input.strip().lower()

    if command.startswith("/start"):
        return "Welcome to the LMS Bot! Type /help to see what I can do."
    elif command.startswith("/help"):
        return "Available commands: /start, /help, /health, /labs, /scores <lab>"
    elif command.startswith("/health"):
        return "Backend status: UP (placeholder)"
    elif command.startswith("/labs"):
        return "Available labs: Lab 1, Lab 2 (placeholder)"
    elif command.startswith("/scores"):
        return f"Scores for requested lab: 100% (placeholder)"
    else:
        return "I don't understand that command."