# Example: Logging Events

def log_events(event_type, *messages):
    """Print an event type and any number of associated messages."""
    print(f"[{event_type.upper()}]")

    if messages: # only iterate if there are messages
        for msg in messages:
            print("-", msg)
    else:
        print("- No details provided")

if __name__ == "__main__":
    # Examples
    log_events("info", "User logged in", "IP 192.168.1.6")
    log_events("warning") # no message