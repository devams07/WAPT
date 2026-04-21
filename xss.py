import requests
from urllib.parse import urlencode

def run():
    print("\n🧪 Cross-Site Scripting (XSS) Scanner\n")

    # Step 1: Get URL
    url = input("Enter URL (example: http://example.com/search): ")

    # Step 2: Multiple payloads
    payloads = [
        "<script>alert(1)</script>",
        "\"><script>alert(1)</script>",
        "'><script>alert(1)</script>",
        "<img src=x onerror=alert(1)>"
    ]

    # Step 3: Loop through payloads
    for payload in payloads:
        try:
            # Step 4: Encode parameters
            params = {'q': payload}
            full_url = url + "?" + urlencode(params)

            print(f"\n➡️ Testing payload: {payload}")

            # Step 5: Send request
            r = requests.get(full_url, timeout=5)

            # Step 6: Check reflection
            if payload in r.text:
                print("⚠️ Possible XSS vulnerability detected!")
            else:
                print("✅ No reflection detected")

        except requests.exceptions.RequestException as e:
            print(f"❌ Error: {e}")


# 🔒 Prevent auto execution when imported
if __name__ == "__main__":
    run()