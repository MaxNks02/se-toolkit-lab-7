import sys
from services.api import get_health, get_labs, get_scores
from services.llm import process_natural_language

def handle_command(command_input: str) -> str:
    text = command_input.strip()
    print(f"DEBUG: handle_command received: '{text}'", file=sys.stderr)
    
    if not text:
        return "I didn't catch that. Try /help."

    if text.startswith("/"):
        parts = text.split()
        command = parts[0].lower()
        if command == "/start":
            return "Welcome! Ask me anything about labs or scores."
        elif command == "/help":
            return "/start, /help, /health, /labs, /scores <lab>"
        elif command == "/health":
            return get_health()
        elif command == "/labs":
            return get_labs()
        elif command == "/scores":
            if len(parts) < 2: return "Usage: /scores <lab>"
            return get_scores(parts[1])
        else:
            return f"Unknown command: {command}"
    
    
    else:
        print("DEBUG: Forwarding to LLM service...", file=sys.stderr)
        return process_natural_language(text)
