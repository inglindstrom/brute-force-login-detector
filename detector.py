from collections import defaultdict

# Maximum number of failed attempts before generating an alert
ALERT_THRESHOLD = 5

# Simulated authentication events
login_events = [
    ("admin", "FAIL"),
    ("ingrid", "SUCCESS"),
    ("admin", "FAIL"),
    ("admin", "FAIL"),
    ("user01", "FAIL"),
    ("admin", "FAIL"),
    ("admin", "FAIL"),
]

# Store the number of failed attempts for each user
failed_attempts = defaultdict(int)

print("=== Authentication Security Monitor ===\n")

for user, status in login_events:

    if status == "FAIL":
        failed_attempts[user] += 1

        print(
            f"[FAILED LOGIN] User: {user} | "
            f"Attempts: {failed_attempts[user]}"
        )

        if failed_attempts[user] >= ALERT_THRESHOLD:
            print(
                f"[HIGH ALERT] Possible brute-force attack "
                f"detected against user: {user}"
            )

    elif status == "SUCCESS":
        print(f"[SUCCESS] User: {user}")

        # Successful login resets the failed-attempt counter
        failed_attempts[user] = 0