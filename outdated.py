import requests
from bs4 import BeautifulSoup
import re

def run():
    print("\n🌐 Website Vulnerability Scanner (Auto Version Detection)\n")

    url = input("Enter website URL (with http/https): ")

    try:
        r = requests.get(url, timeout=5)

        print("\n🔍 BASIC INFO")
        print("Status Code:", r.status_code)

        soup = BeautifulSoup(r.text, "html.parser")
        scripts = soup.find_all("script")

        print("\n📦 JS LIBRARY ANALYSIS\n")

        found = False

        for script in scripts:
            src = script.get("src")

            if src:
                # 🔹 Detect jQuery
                if "jquery" in src.lower():
                    found = True
                    print("Found jQuery:", src)

                    # 🔹 Extract version using regex
                    match = re.search(r'jquery[-\.](\d+\.\d+\.\d+)', src, re.IGNORECASE)

                    if match:
                        version = match.group(1)
                        print("Detected Version:", version)

                        # 🔹 Compare versions
                        vulnerable_versions = ["1.12.4", "2.2.4"]

                        if version in vulnerable_versions:
                            print("⚠️ Vulnerable jQuery version detected!")
                        else:
                            print("✅ Version looks safer (but verify with CVE DB)")

                    else:
                        print("⚠️ Version not found in URL (might be hidden)")

        if not found:
            print("No jQuery detected")

        print("\n✅ Scan Complete!")

    except requests.exceptions.RequestException as e:
        print("❌ Error:", e)


# 🔒 Prevent auto execution when imported
if __name__ == "__main__":
    run()