import httpx
import config


def _make_request(endpoint: str) -> dict | list | str:
    """
    Helper to make HTTP GET requests to the LMS backend.
    Returns the parsed JSON data, or a formatted error string if it fails.
    """
    url = f"{config.LMS_API_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {config.LMS_API_KEY}"
    }

    try:
        # Use a timeout so the bot doesn't hang forever if the backend is down
        with httpx.Client(timeout=5.0) as client:
            response = client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()

    except httpx.ConnectError:
        # P0.8: Friendly message with actual error for connection issues
        return f"Backend error: connection refused ({config.LMS_API_URL}). Check that the services are running."
    except httpx.HTTPStatusError as e:
        # P0.8: Friendly message with actual error for HTTP failures (e.g. 502 Bad Gateway)
        return f"Backend error: HTTP {e.response.status_code} {e.response.reason_phrase}. The backend service may be down."
    except Exception as e:
        # Catch-all for other unexpected errors without dumping a raw Traceback
        return f"Backend error: {str(e)}"


def get_health() -> str:
    """Calls GET /items/ and reports up/down status."""
    data = _make_request("/items/")

    # If the helper returned a string, it means an error occurred
    if isinstance(data, str):
        return data

    # If we got a list back, the backend is healthy
    if isinstance(data, list):
        return f"Backend is healthy. {len(data)} items available."

    return "Backend is responding, but returned unexpected data format."


def get_labs() -> str:
    """Calls GET /items/ and lists available labs."""
    data = _make_request("/items/")
    if isinstance(data, str):
        return data

    if isinstance(data, list):
        # Filter for items that are actually labs (assuming type="lab" or id contains "lab")
        labs = [item for item in data if item.get("type") == "lab" or "lab" in str(item.get("id", "")).lower()]

        if not labs:
            return "No labs found in the backend."

        lines = ["Available labs:"]
        for lab in labs:
            # Try to grab the title/name, fallback to ID
            name = lab.get("title") or lab.get("name") or lab.get("id") or "Unknown"
            lines.append(f"- {name}")
        return "\n".join(lines)

    return "Could not parse labs data."


def get_scores(lab_id: str) -> str:
    """Calls GET /analytics/pass-rates?lab=<lab_id> and formats the scores."""
    data = _make_request(f"/analytics/pass-rates?lab={lab_id}")
    if isinstance(data, str):
        return data

    if not data:
        return f"No pass rate data found for {lab_id}."

    lines = [f"Pass rates for {lab_id}:"]

    # Iterate through the dictionary/list returned by the analytics endpoint
    if isinstance(data, dict):
        for task_name, stats in data.items():
            # Adjust these keys based on your actual backend JSON structure
            pass_rate = stats.get("pass_rate", 0) * 100
            attempts = stats.get("attempts", 0)
            lines.append(f"- {task_name}: {pass_rate:.1f}% ({attempts} attempts)")
    elif isinstance(data, list):
        for item in data:
            task_name = item.get("task", "Unknown Task")
            pass_rate = item.get("pass_rate", 0) * 100
            attempts = item.get("attempts", 0)
            lines.append(f"- {task_name}: {pass_rate:.1f}% ({attempts} attempts)")

    return "\n".join(lines)