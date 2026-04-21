import requests
import time

def run():
    print("\n🌐 Active or Not + Basic Info Scanner\n")

    url = input("Enter URL (with http/https): ")

    try:
        # Step 1: Send request and measure time
        start = time.time()
        r = requests.get(url, timeout=5)
        end = time.time()

        # Step 2: Basic info
        print("\n🔍 BASIC INFO")
        print("Status Code:", r.status_code)
        print("Response Time:", round(end - start, 2), "seconds")
        print("Response Length:", len(r.text))

        # Step 3: Server info
        print("\n🖥️ SERVER INFO")
        print("Server:", r.headers.get("Server", "Not disclosed"))
        print("Powered By:", r.headers.get("X-Powered-By", "Not disclosed"))

        # Step 4: Security headers check
        print("\n🔐 SECURITY HEADERS")
        security_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Strict-Transport-Security"
        ]

        for header in security_headers:
            if header in r.headers:
                print(f"✅ {header} is present")
            else:
                print(f"⚠️ {header} is missing")

        # Step 5: Content check
        print("\n📄 CONTENT CHECK")
        if "login" in r.text.lower():
            print("🔑 Login page detected")
        if "admin" in r.text.lower():
            print("⚠️ Admin-related content found")
        if "<form" in r.text.lower():
            print("📝 Form detected (possible input points)")

    except requests.exceptions.RequestException as e:
        print("❌ Error:", e)


# 🔒 Prevent auto-execution when imported
if __name__ == "__main__":
    run()