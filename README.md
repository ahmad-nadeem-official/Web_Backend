# 🌟 **WEB Backend Service** 🌟  

Welcome to **WEB Backend Service**, a robust and scalable Flask-based backend designed to power your web applications with seamless email notifications and database management! This project provides APIs for newsletter subscriptions, meeting scheduling, and contact form submissions, all integrated with PostgreSQL for data persistence and Gmail SMTP for email confirmations. Built with a focus on simplicity and efficiency, this backend is perfect for developers looking to deploy a reliable server-side solution! 🚀  

- 🔗 **Repository Name**: WEB Backend Service  
- 📅 **Last Updated**: June 09, 2025
- 👨‍💻 **Author**: Ahmad Nadeem 
- 🔗 **API URL**: `https://ahmadnadeem.vercel.app/`
  

---
## 🌐︎ endpoints of API
- 🔗 **1 endpoint**: `https://ahmadnadeem.vercel.app/meeting`
- 🔗 **2 endpoint**: `https://ahmadnadeem.vercel.app/contact`
- 🔗 **3 endpoint**: `https://ahmadnadeem.vercel.app/subscribe`

---
## 🚀 Key Features  

- **API Endpoints** 🌐: Handle subscriptions, meetings, and contact forms with ease.  
- **Email Notifications** 📧: Send instant confirmation emails using Flask-Mail and Gmail SMTP.  
- **Database Integration** 🗄️: Store data securely with SQLAlchemy and PostgreSQL.  
- **CORS Support** 🌍: Enable cross-origin requests for frontend integration.  
- **Debug Mode** 🛠️: Run with debug mode for development convenience.  

---

## 🛠️ Tech Stack  

Here’s the powerhouse of tools driving this backend!  

🛡️ Python ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)  
🛡️ Flask ![Flask](https://img.shields.io/badge/Flask-2.0%2B-green?logo=flask)  
🛡️ SQLAlchemy ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4%2B-orange?logo=sqlalchemy)  
🛡️ PostgreSQL ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-blue?logo=postgresql)  
🛡️ Flask-Mail ![Flask-Mail](https://img.shields.io/badge/Flask--Mail-SMTP-red)  
🛡️ Flask-CORS ![Flask-CORS](https://img.shields.io/badge/Flask--CORS-Cross%20Origin-yellow)  

---

## 📂 Project Structure  

Explore the organized layout of this repository:  

- **micro_services/**: Directory for microservice-related scripts.  
  - **env/**: Virtual environment folder (auto-generated, ignore in version control).  
  - **mail_t.py**: Utility script for email functionality testing.  
  - **main.py**: Core Flask application with all routes and logic.    
  - **test.py**: tests for the application.  
- **.gitignore**: Excludes unnecessary files (e.g., env) from version control.  
- **LICENSE**: Project license details.  
- **LICENSE.md**: Markdown version of the license.  
- **README.md**: You’re here! 😄  
- **requirements.txt**: List of dependencies to set up the project.  

---

## 🖥️ How to Get Started  

Get this backend up and running with these steps! 🚀  

### Prerequisites  
- Python 3.8 or higher 🐍  
- PostgreSQL installed and running 📊  
- A Gmail account for SMTP (enable "Less secure app access" or use App Password) 🔑  

### Step 1: Clone the Repository  
`https://github.com/ahmad-nadeem-official/Web_Backend.git`  
`cd WEB-Backend-Service`
`cd micro_services`  

### Step 2: Install Dependencies  
`pip install -r requirements.txt`  

### Step 3: Configure Environment  
- Update **app.config["SQLALCHEMY_DATABASE_URI"]** in **main.py** with your PostgreSQL credentials.  
- Replace **MAIL_USERNAME** and **MAIL_PASSWORD** in **main.py** with your Gmail credentials.  

### Step 4: Run the Application  
`python micro_services/main.py`  

The app will start in debug mode on `http://127.0.0.1:5000/`  

### Step 5: Test the APIs  
Use tools like Postman or curl or request to test the endpoints, 
or you can see test.py file for testing your api you will be guided there, 
- **POST /subscribe**: `{"email": "user@example.com"}`  
- **POST /meeting**: `{"name": "John", "email": "john@example.com", "date": "2025-06-10T10:00:00", "message": "Discuss project"}`  
- **POST /contact**: `{"name": "Jane", "email": "jane@example.com", "subject": "Support", "message": "Need help!"}`  

---

## 📊 How It Works  

1. **Initialize App** 🌐: Sets up Flask with CORS and SQLAlchemy.  
2. **Database Models** 🗄️: Defines Newsletter, Meeting, and Contact tables.  
3. **API Routes** 🔗: Handles POST requests for subscriptions, meetings, and contacts.  
4. **Email Sending** 📧: Uses Flask-Mail to send confirmation emails via Gmail SMTP.  
5. **Data Persistence** 💾: Saves user data to PostgreSQL with error handling.  

---

## 🧠 Why This Project Stands Out  

- **Production-Ready** 🚀: Includes error handling, email notifications, and database integration.  
- **Modular Design** 🧩: Easy to extend with new microservices or endpoints.  
- **Secure Setup** 🔒: Uses SSL for PostgreSQL and configurable email credentials.  
- **Developer-Friendly** 💻: Well-structured code with tests and documentation.  

---

## 🤝 Contributing  

Join the development journey! 🍴  
1. Fork the repository.  
2. Create a branch (git checkout -b feature/new-endpoint).  
3. Commit changes (git commit -m "Add new endpoint").  
4. Push and open a Pull Request 📬.  
Report issues or suggest features! 🤗  

---

## 📜 License  

Licensed under the Apache License See the LICENSE file for details.  

---

## 🙌 Acknowledgments  

- **Flask** for the amazing web framework.  
- **SQLAlchemy** for ORM simplicity.  
- **PostgreSQL** for reliable database management.  
- **Flask-Mail** for seamless email integration.  

---

🎉 **Thank you for exploring WEB Backend Service!** Power up your web apps with this backend today! 💻  