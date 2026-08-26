
# Flask URL Shortener API

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Licence:MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
---

a lightweight, beginner-friendly RESTful API built with **Python** and **Flask** that turns long, unwieldy web links into clean, shareable short URLs 

---

## 📝 Features

* **URL Shortening ('POST'):** Accepts any longer URL and generates a unique 6-character alphanumeric short code.
* **Smart URL Normalization:** Automatically handles URLs provided without an 'http://' or 'https://' prefix.
* **Collision Safety:** Guarantees every generated short code is strictly unique using loop validation.
* **Instant Redirection ('GET'):** Performs a '302 Redirect' to send a visitors directly to their original destination.
* **Dynamic Host Detection**: Works seamlessly across local development servers ('localhost) and deployed production domains.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** Flask 3.x
* **Storage:** In-Memory Hash Map (Dictionary)

---

## 📁 Repository Structure 
```text
flask-url-shortener/
│
├── app.py              # Main Flask application logic & routing
├── requirements.txt    # Project dependencies
├── .gitignore          # Files excluded from version control
└── README.md           # Project documentation
```
---

### 2. Clean Git Commands (Run these in VS Code Terminal)

After saving your 4 files (`app.py`, `requirements.txt`, `.gitignore`, `README.md`), run these exact lines in your terminal:

```bash
git init
git add .
git commit -m "Initial commit: Flask URL Shortener API"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/flask-url-shortener.git
git push -u origin main
