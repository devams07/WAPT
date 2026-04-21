import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs, urlencode, urlunparse
import re

def run():
    print("\n🔐 Advanced Broken Access Control Scanner\n")

    target = input("Enter target URL (e.g., http://localhost:3000): ")

    session = requests.Session()

    # ---------------- LOGIN SUPPORT ----------------
    use_login = input("Does the site require login? (y/n): ").lower()

    if use_login == "y":
        login_url = input("Enter login URL: ")
        username = input("Username: ")
        password = input("Password: ")

        data = {
            "email": username,
            "password": password
        }

        try:
            res = session.post(login_url, data=data)
            print("🔐 Login attempted. Status:", res.status_code)
        except requests.exceptions.RequestException:
            print("❌ Login failed")

    # ---------------- CRAWLER ----------------
    visited = set()
    to_visit = [target]

    def extract_links(url):
        links = []
        try:
            r = session.get(url, timeout=5)
            soup = BeautifulSoup(r.text, "html.parser")

            for a in soup.find_all("a", href=True):
                full = urljoin(url, a["href"])
                if target in full:
                    links.append(full)
        except:
            pass
        return links

    # ---------------- RESPONSE ANALYSIS ----------------
    def is_interesting_response(base, test):
        if abs(len(base.text) - len(test.text)) > 50:
            return True

        if "application/json" in test.headers.get("Content-Type", ""):
            if base.text != test.text:
                return True

        return False

    # ---------------- IDOR TEST (PARAM) ----------------
    def test_params(url):
        parsed = urlparse(url)
        params = parse_qs(parsed.query)

        if not params:
            return

        try:
            baseline = session.get(url, timeout=5)
        except:
            return

        print(f"\n🔍 Testing Parameters: {url}")

        for param in params:
            val = params[param][0]

            if val.isdigit():
                test_values = [str(int(val)+1), "9999"]
            else:
                test_values = ["admin", "1"]

            for t in test_values:
                new_params = params.copy()
                new_params[param] = t

                new_query = urlencode(new_params, doseq=True)
                new_url = urlunparse(parsed._replace(query=new_query))

                try:
                    r = session.get(new_url, timeout=5)
                    print(f"➡️ {param}={t} | {r.status_code}")

                    if r.status_code == 200 and is_interesting_response(baseline, r):
                        print("⚠️ Possible IDOR detected!")
                except:
                    pass

    # ---------------- REST ID TEST ----------------
    def test_rest_ids(url):
        match = re.search(r"/(\d+)", url)
        if not match:
            return

        original_id = match.group(1)

        try:
            baseline = session.get(url, timeout=5)
        except:
            return

        print(f"\n🔍 Testing REST ID: {url}")

        for new_id in [str(int(original_id)+1), "9999"]:
            new_url = url.replace("/" + original_id, "/" + new_id)

            try:
                r = session.get(new_url, timeout=5)
                print(f"➡️ {new_url} | {r.status_code}")

                if r.status_code == 200 and is_interesting_response(baseline, r):
                    print("⚠️ Possible REST IDOR detected!")
            except:
                pass

    # ---------------- RESTRICTED PATH TEST ----------------
    def test_restricted(base):
        paths = ["/admin", "/api/users", "/dashboard", "/account"]

        print("\n🔐 Testing Restricted Paths...\n")

        for p in paths:
            url = urljoin(base, p)
            try:
                r = session.get(url, timeout=5)
                print(f"{p} → {r.status_code}")

                if r.status_code == 200:
                    print("⚠️ Possible Unauthorized Access!")
            except:
                pass

    # ---------------- MAIN LOOP ----------------
    depth = 0
    max_depth = 2

    while to_visit and depth < max_depth:
        current = to_visit.pop(0)

        if current in visited:
            continue

        visited.add(current)

        print(f"\n🌐 Crawling: {current}")

        links = extract_links(current)

        for link in links:
            if link not in visited:
                to_visit.append(link)

            test_params(link)
            test_rest_ids(link)

        depth += 1

    # Base URL extraction
    parsed = urlparse(target)
    base_url = f"{parsed.scheme}://{parsed.netloc}"

    test_restricted(base_url)

    print("\n✅ Scan Completed!\n")


# 🔒 Prevent auto-execution when imported
if __name__ == "__main__":
    run()