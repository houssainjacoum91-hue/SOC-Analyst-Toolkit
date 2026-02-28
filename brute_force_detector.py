import re
from collections import Counter

def detect_brute_force(log_file, threshold=3):
    with open(log_file, "r") as file:
        logs = file.readlines()

    ip_list = []

    for line in logs:
        match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
        if match:
            ip_list.append(match.group(1))

    ip_counts = Counter(ip_list)

    print("=== Brute Force Detection Report ===")
    for ip, count in ip_counts.items():
        if count >= threshold:
            print(f"[ALERT] Suspicious IP: {ip} | Attempts: {count}")
        else:
            print(f"[INFO] IP: {ip} | Attempts: {count}")

if __name__ == "__main__":
    detect_brute_force("sample_logs.txt")
