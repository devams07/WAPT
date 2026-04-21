import requests
import re

def run():
    print("\n🔐 Cryptographic Failure Scanner\n")

    url = input("Enter website URL (with http/https): ")

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        content = response.text

        print("\n🔍 BASIC CHECKS\n")

        # 1. HTTPS Check
        if url.startswith("https://"):
            print("✅ Using HTTPS")
        else:
            print("❌ Not using HTTPS (Data can be intercepted!)")

        # 2. Weak Crypto Detection
        print("\n🔍 Checking for weak cryptographic algorithms...")
        weak_patterns = ["md5", "sha1"]

        for pattern in weak_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                print(f"⚠️ Possible weak crypto usage detected: {pattern.upper()}")

        # 3. Sensitive Data Exposure
        print("\n🔍 Checking for sensitive data exposure...")
        sensitive_patterns = [
            r"password\s*=\s*['\"]?.+['\"]?",
            r"api[_-]?key\s*=\s*['\"]?.+['\"]?",
            r"secret\s*=\s*['\"]?.+['\"]?"
        ]

        for pattern in sensitive_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                print("🚨 Possible sensitive data exposed!")

        # 4. Security Headers
        print("\n🔍 Checking security headers...")

        if "Strict-Transport-Security" in headers:
            print("✅ HSTS Enabled")
        else:
            print("❌ Missing HSTS")

        if "Content-Security-Policy" in headers:
            print("✅ CSP Present")
        else:
            print("❌ Missing CSP")

        # 5. Cookie Security
        print("\n🔍 Checking cookies...")

        cookies = response.cookies

        for cookie in cookies:
            if not cookie.secure:
                print(f"⚠️ Cookie '{cookie.name}' is not Secure")
            if not cookie.has_nonstandard_attr('HttpOnly'):
                print(f"⚠️ Cookie '{cookie.name}' is not HttpOnly")

    except requests.exceptions.RequestException as e:
        print("❌ Error:", e)


# 🔒 Prevent auto execution when imported
if __name__ == "__main__":
    run()