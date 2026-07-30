# 🏦 Pinnacle Bank – Enterprise Web Banking System

An end-to-end, full-stack enterprise banking portal engineered using **Python**, **Django**, and **PostgreSQL**. Designed around the Software Development Life Cycle (SDLC) to simulate a high-concurrency, secure FinTech platform.

![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge&logo=github)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 📖 Project Overview

Traditional banking platforms require unwavering precision, zero data loss, and immediate concurrency handling. Pinnacle Bank addresses these core requirements by providing an intuitive, modern dashboard to manage savings and checking accounts, execute atomic peer-to-peer transfers, and audit transactions seamlessly.

The platform combines a dynamic frontend built with HTML5, CSS3, and JavaScript with a robust Django backend that enforces row-level database locking and strict RBAC authorization.

---

## ✨ Core Features & Architectural Modules

### 🛡️ 1. Security & RBAC Framework

* **Multi-Tier Role-Based Access Control (RBAC):** Custom permissions distinguishing Customer, Branch Auditor, and SuperAdmin profiles.

* **PBKDF2 Password Hashing:** User credentials are encrypted using Django's default SHA-256 algorithm.

* **SQL Injection & XSS Defense:** Strict parameterization via Django ORM and auto-escaping templates.

* **CSRF Middleware:** Token validation on all mutable HTTP requests (POST, PUT, DELETE).

### ⚡ 2. Financial Ledger & Concurrency

* **ACID-Compliant Transfers:** Database rows are locked during processing using PostgreSQL’s `select_for_update()` to prevent double-spending race conditions.

* **Atomic Processing:** Wrapped in `transaction.atomic()` blocks; any failure during transfer instantly rolls back debit and credit operations.

* **Automated Account Generator:** Cryptographically random 10-digit account identification mechanism.

### 🎨 3. Modern UI/UX Experience

* **Responsive Banking Dashboard:** Standard HTML5/CSS3 frontend enhanced with dynamic JavaScript micro-interactions.

* **Custom Glassmorphic Cards:** Styled virtual debit cards displaying live account balances, card status (Active/Frozen), and card numbers.

* **Interactive Transaction Filters:** Instant client-side and server-side filtering by date range, transaction type, and status.

---

## 🛠️ Technology Stack

| Layer | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3, Vanilla JS | Dynamic user interface built with modern HTML/CSS and JS micro-interactions. |
| **Backend** | Python 3, Django | Enterprise MVT web framework handling business logic and routing. |
| **Database** | PostgreSQL | Server-side relational database providing ACID compliance and row-level locking. |
| **API Testing** | Postman, Thunder Client | REST API validation, payload inspection, and integration testing toolsets. |
| **Tools & VCS** | Git, GitHub | Codebase version control, issue tracking, and repository management. |

---

## 📡 API Reference Documentation

All API endpoints are validated through **Postman** and **Thunder Client** to verify HTTP status codes, authentication tokens, and error handling payloads.

| Endpoint | Method | Description | Request Payload |
| :--- | :--- | :--- | :--- |
| `/api/v1/auth/login/` | **POST** | Authenticates user & returns session token | `{"username": "...", "password": "..."}` |
| `/api/v1/accounts/` | **GET** | Retrieves user account balances & details | `None` |
| `/api/v1/transfer/` | **POST** | Processes an atomic fund transfer | `{"sender_account": "...", "receiver_account": "...", "amount": 1250.00}` |
| `/api/v1/transactions/` | **GET** | Fetches full financial ledger history | `None` |

---

## 🚀 Installation & Local Setup Guide

Follow these step-by-step instructions to run Pinnacle Bank locally on your machine.

### Step 1: Prerequisites

Ensure you have **Python 3.10+**, **PostgreSQL Server**, and **Git** installed on your system.

### Step 2: Clone Repository & Setup Workspace

Open your terminal and clone the repository using Git:

```bash
git clone [https://github.com/yourusername/pinnacle-bank.git](https://github.com/yourusername/pinnacle-bank.git)

cd pinnacle-bank
```


### Step 3: Create Database in PostgreSQL
Open your PostgreSQL command line tool (psql) and run the database initialization commands:
```sql
CREATE DATABASE pinnacle_bank_db;

CREATE USER pinnacle_admin WITH PASSWORD 'bank_password123';

GRANT ALL PRIVILEGES ON DATABASE pinnacle_bank_db TO pinnacle_admin;
```

### Step 4: Configure Project Settings
Update your pinnacle_bank/settings.py file to point to your local PostgreSQL instance:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pinnacle_bank_db',
        'USER': 'pinnacle_admin',
        'PASSWORD': 'bank_password123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Step 5: Run Migrations, Create Superuser & Start Server
Execute all core Django commands to initialize your schema, set up your admin profile, and start the development server:
```bash
# Apply database migrations
python manage.py makemigrations

python manage.py migrate

# Create administrator account
python manage.py createsuperuser

# Start local server
python manage.py runserver
```

Open your browser and navigate to http://127.0.0.1:8000/ to access the portal.

## 🧪 Postman & Thunder Client Testing Workflow
Integration tests are maintained via Postman and Thunder Client collections located in docs/PinnacleBank_Collection.json.
 * Valid Login (POST): Verifies user credentials and returns session tokens with a 200 OK status.
 * Invalid Login (POST): Blocks unauthorized credentials and returns a 401 Unauthorized state.
 * Get Accounts (GET): Fetches user account numbers and current balances.
 * Fund Transfer (POST): Deducts balance from the sender, credits the receiver, and logs transaction history with a 201 Created status.
 * Insufficient Funds Handling (POST): Intercepts transfers exceeding the balance and aborts the transaction with a 400 Bad Request error.
 * 
## 🎓 SDLC Adherence & Security Audit Matrix
This project strictly complies with all 10 core phases of the Software Development Life Cycle (SDLC):
 * Requirements Gathering: Analyzed modern retail banking requirements (Auth, Wallets, Ledgers, Audits).
 * System Architecture Design: Designed Django MVT architecture and PostgreSQL schema normalization (3NF).
 * Environment Setup: Configured PostgreSQL instance, environment parameters, and virtual workspaces.
 * Backend Implementation: Authored modular Django applications with custom middleware.
 * Frontend Development: Built responsive HTML5/CSS3 templates with dynamic JS micro-interactions.
 * API Engineering: Created REST endpoints tested systematically using Thunder Client and Postman.
 * Database Security: Enforced strict foreign key constraints, row-level locking, and indexing.
 * Quality Assurance: Unit tested atomic transfer logic and exception handling scenarios.
 * Documentation: Authored comprehensive README documentation and inline codebase comments.
 * Final Deployment Evaluation: Delivered a fully responsive, secure web banking system.
   
## 🔮 Future Scope & Roadmap
 * Real-World Payment Gateways: Integration with Stripe and Razorpay APIs for live payment processing.
 * PDF Statement Generator: Dynamic generation of downloadable monthly account statements.
 * Two-Factor Authentication (2FA): Time-based OTP verification for high-value fund transfers.
