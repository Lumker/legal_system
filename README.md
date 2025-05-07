### **Legal System for South African Law Firms**  
**A Django-based case management system for small law firms in South Africa**  

This system automates **case tracking**, **document management**, **deadline alerts**, and **billing** while ensuring **POPIA compliance** and usability by non-technical attorneys. Built for rapid deployment on **cPanel** (with fallback to Celery/Redis for development).

---

### **Key Features**
- ✅ **Case Management**: Track cases, clients, and lawyers.
- ✅ **Deadline Alerts**: Automated email/SMS reminders using Celery (or cron for cPanel).
- ✅ **Document Uploads**: Secure PDF/document uploads with encryption.
- ✅ **Billing & Time Tracking**: Auto-generate invoices and track billable hours.
- ✅ **Dashboard**: Visualize case status, billing efficiency, and pro bono impact.
- ✅ **Multilingual Support**: English, isiXhosa, Afrikaans (via Django `i18n`).
- ✅ **POPIA Compliance**: Field-level encryption, audit logs, and data retention policies.
- ✅ **cPanel Deployment Ready**: Lightweight and optimized for shared hosting.

---

### **Tech Stack**
- **Backend**: Django, Python 3.10+, PostgreSQL/MySQL
- **Frontend**: Bootstrap 5, Chart.js, Jinja2 templates
- **Task Queue**: Celery + Redis (development), cron (cPanel)
- **Security**: `django-cryptography`, `django-simple-history`
- **Compliance**: POPIA, Legal Practice Act of South Africa

---

### **Getting Started**

#### **1. Clone the Repository**
```bash
git clone https://github.com/lumker/legal_system.git
cd legal_system
```

#### **2. Set Up Virtual Environment**
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
```

#### **3. Configure Settings**
Create a `.env` file in the root:
```env
SECRET_KEY=your-secret-key
DEBUG=True
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.office365.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your@outlook.com
EMAIL_HOST_PASSWORD=your-app-password
CLICKATELL_API_KEY=your-sms-api-key
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

#### **4. Migrate Database**
```bash
python manage.py makemigrations
python manage.py migrate
```

#### **5. Run Redis (Development Only)**
Use Docker:
```bash
docker run -p 6379:6379 redis
```

#### **6. Start Celery Worker (Windows)**
```bash
celery -A config worker --loglevel=info --pool solo
```

#### **7. Schedule Daily Deadline Checks**
Run Celery Beat in a new terminal:
```bash
celery -A config beat --loglevel=info
```

#### **8. Launch Development Server**
```bash
python manage.py runserver
```

---

### **Deploy on cPanel**
For production on cPanel (no background workers):
1. Replace Celery with a **cron job**:
   ```bash
   0 8 * * * /home/yourusername/virtualenv/public_html/legal_system/venv/bin/python /home/yourusername/public_html/legal_system/manage.py run_deadline_check
   ```
2. Use **MySQL** instead of SQLite.
3. Set `STATIC_ROOT` and run `collectstatic`.
4. Use `.env` for secrets (via cPanel’s environment variable manager).

---

### **Contributing**
We welcome contributions from:
- **South African legal tech developers**
- **Law students** (for legal workflow testing)
- **Community advocates** (for isiXhosa/Afrikaans translations)

#### **How to Contribute**
1. Fork the repo.
2. Create a new branch (`git checkout -b feature/document-ocr`).
3. Commit changes (`git commit -m "Add OCR support"`).
4. Push to GitHub (`git push origin feature/document-ocr`).
5. Submit a pull request.

---

### **License**
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

### **Contact**
- **Project Lead**: Lumkile Mawethu (lumker@example.com)
- **GitHub**: [github.com/lumker/legal_system](https://github.com/lumker/legal_system)

---

### **Acknowledgments**
- Special thanks to the **Law Society of South Africa** for compliance guidance.
- Localized testing with **PythonZA** and **GirlCode** communities.
- Feedback from **rural law firms** in **Soweto**, **Stellenbosch**, and **Grahamstown**.

---

### **Support Local Legal Tech**
This project empowers small South African law firms to digitize workflows without sacrificing compliance or affordability.  
Join us in bridging the legal tech gap in underserved communities.

---

### **Need Help With?**
Let me know if you'd like help:
- Adding **document OCR** with `pytesseract`.
- Setting up **SMS alerts** via Clickatell.
- Training local developers on the codebase.
- Expanding to **pro bono case tracking**.

This README ensures your project is **accessible**, **compliant**, and **ready for real-world use** by small South African law firms. 🚀
