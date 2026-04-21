import os
import activeornot 
import sqli
import xss
import ssrf
import outdated
import access_control
import crypto

# Clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# WAPT Banner
def banner():
    print("""
██╗    ██╗ █████╗ ██████╗ ████████╗
██║    ██║██╔══██╗██╔══██╗╚══██╔══╝
██║ █╗ ██║███████║██████╔╝   ██║   
██║███╗██║██╔══██║██╔═══╝    ██║   
╚███╔███╔╝██║  ██║██║        ██║   
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝        ╚═╝    

🛡️  Web Application Penetration Testing Tool
👨‍💻 Made by Deva
""")

def menu():
    while True:
        clear()
        banner()

        print("1. Active or Not (Website Status)")
        print("2. SQL Injection")
        print("3. Cross-Site Scripting (XSS)")
        print("4. Server-Side Request Forgery (SSRF)")
        print("5. Vulnerable & Outdated Components")
        print("6. Broken Access Control")
        print("7. Cryptographic Failures")
        print("0. Exit")

        choice = input("\n👉 Select an option: ")

        clear()

        if choice == "1":
            banner()
            activeornot.run()

        elif choice == "2":
            banner()
            sqli.run()

        elif choice == "3":
            banner()
            xss.run()

        elif choice == "4":
            banner()
            ssrf.run()

        elif choice == "5":
            banner()
            outdated.run()

        elif choice == "6":
            banner()
            access_control.run()

        elif choice == "7":
            banner()
            crypto.run()

        elif choice == "0":
            print("\n👋 Exiting WAPT... Stay Secure!\n")
            break

        else:
            print("❌ Invalid choice")

        input("\n🔁 Press Enter to return to menu...")

# Start tool
menu()