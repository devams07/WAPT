# 🛡️ Web Application Penetration Testing Tool (WAPT)

A Python-based tool designed to perform automated security testing on web applications.
This tool helps identify common vulnerabilities based on OWASP Top 10.

---

## 🚀 Features

* 🔍 **Active Status Check** – Verify if the target is reachable
* 💉 **SQL Injection Detection** – Basic payload-based testing
* ⚡ **Cross-Site Scripting (XSS)** – Detect reflected XSS vulnerabilities
* 🌐 **SSRF Testing** – Identify Server-Side Request Forgery issues
* 🔐 **Broken Access Control** – Test restricted endpoints
* 📉 **Outdated Components Check** – Identify old/unsafe technologies
* 🔑 **Cryptographic Failures** – Detect weak security practices

---

## 🧰 Tech Stack

* Python 3
* `requests`
* `BeautifulSoup`
* `urllib`
* `re`

---

## 📁 Project Structure

```
WAPT/
│── main.py
│── activeornot.py
│── sqli.py
│── xss.py
│── ssrf.py
│── outdated.py
│── access_control.py
│── crypto.py
│── .gitignore
```

---

## ▶️ Usage

Run the tool:

```bash
python main.py
```

You will see a menu like this:

```
[1] Active or Not
[2] SQL Injection
[3] XSS
[4] SSRF
[5] Broken Access Control
[6] Outdated Components
[7] Cryptographic Failures
[8] Scan All
```

Select an option and then enter the target URL:

```
Enter target URL: http://example.com
```

---

## 🧪 Example Output

```
[2] SQL Injection Selected

Enter target URL: http://testphp.vulnweb.com

🔍 Testing SQL Injection...
⚠️ Possible SQL Injection vulnerability detected!

✅ Scan Completed!
```

---

## ⚠️ Disclaimer

This tool is created for **educational purposes only**.
Do not use this tool on websites without proper authorization.

---

📌 Note

⚠️ This is a basic-level (foundation) penetration testing tool, developed for learning and understanding web security concepts.
It is not intended to replace professional-grade tools.



## 📌 Future Improvements

* 🔄 Advanced crawling engine
* 📂 Payload management system
* 📊 HTML report generation
* 🧠 Smarter vulnerability detection
* 🔐 Authentication support

---

## 👨‍💻 Author

**Deva M S**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
