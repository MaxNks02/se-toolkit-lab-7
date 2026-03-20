from services.api import get_health, get_labs, get_scores


def handle_command(command_input: str) -> str:
    """
    Processes plain text commands for the --test mode and the Telegram bot.
    Now integrated with real LMS backend data.
    """
    # Split the input into parts (e.g., "/scores lab-04" -> ["/scores", "lab-04"])
    parts = command_input.strip().split()
    if not parts:
        return "I didn't catch that. Try /help."

    command = parts[0].lower()

    # P0.3: /start — welcome message
    if command == "/start":
        return "Welcome to the LMS Bot! I can help you check system health, browse labs, and view scores."

    # P0.4: /help — lists all available commands
    elif command == "/help":
        return (
            "Here are the commands you can use:\n"
            "/start - Welcome message\n"
            "/help - Lists all available commands\n"
            "/health - Check if the backend is up and running\n"
            "/labs - List all available labs\n"
            "/scores <lab_id> - Get pass rates for a specific lab (e.g., /scores lab-04)"
        )

    # P0.5: /health — calls backend, reports status
    elif command == "/health":
        return get_health()

    # P0.6: /labs — lists available labs
    elif command == "/labs":
        return get_labs()

    # P0.7: /scores <lab> — per-task pass rates
    elif command == "/scores":
        # Edge case handling: ensure the user actually provided a lab ID
        if len(parts) < 2:
            return "Please specify a lab. Usage: /scores <lab_id> (e.g., /scores lab-04)"

        lab_id = parts[1]
        return get_scores(lab_id)

    # Handle unknown commands gracefully
    else:
        return f"Unknown command: {command}. Type /help to see what I can do."