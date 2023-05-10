import requests
import time

valid_tokens = []
invalid_tokens = []
locked_tokens = []
unknown_tokens = []

threads = int(input("Threads > "))

with open("tokens.txt") as f:
    tokens = f.readlines()

start_time = time.time()

for token in tokens:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Authorization": token.strip()
    }
    try:
        response = requests.get("https://discord.com/api/v9/users/@me/library", headers=headers)
        if response.status_code == 200:
            valid_tokens.append(token)
            print(f"[{time.strftime('%H:%M:%S')} Valid ({token[:32]}...)]")
        elif response.status_code == 401:
            invalid_tokens.append(token)
            print(f"[{time.strftime('%H:%M:%S')} Invalid ({token[:32]}...)]")
        elif response.status_code == 403:
            locked_tokens.append(token)
            print(f"[{time.strftime('%H:%M:%S')} Locked ({token[:32]}...)]")
        else:
            unknown_tokens.append(token)
            print(f"[{time.strftime('%H:%M:%S')} Unknown ({token[:32]}...)]")
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')} Error ({token[:32]}...): {e}]")

end_time = time.time()

print(f"\nResults:\n[-] Valid: {len(valid_tokens)}\n[-] Invalid: {len(invalid_tokens)}\n[-] Locked: {len(locked_tokens)}\n[-] Unknown: {len(unknown_tokens)}\n[-] Time Taken: {end_time - start_time:.2f} seconds")

with open("valid.txt", "w") as f:
    f.writelines(valid_tokens)

with open("invalid.txt", "w") as f:
    f.writelines(invalid_tokens)

with open("locked.txt", "w") as f:
    f.writelines(locked_tokens)

with open("unknown.txt", "w") as f:
    f.writelines(unknown_tokens)
