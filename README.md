# 📧 Email AI Autoresponder

**Email AI Autoresponder** is a smart automation tool that automatically responds to incoming emails using OpenAI's advanced language model. 

This bot reads unread emails, analyzes their content, and generates customized replies.

## 🚀 Features

- ✅ **AI-Powered Responses**: Automatically generate intelligent and context-aware replies using OpenAI.
- ✅ **Multi-Platform Support**: Works seamlessly with **Gmail** and **Outlook**.
- ✅ **Customizable**: Easily tailor the responses to fit your needs.
- ✅ **Fully Automated**: Automatically checks inboxes and sends replies without manual intervention.

## 📂 Project Structure

```
email-ai-autoresponder/
├── main.py              # Main bot logic
├── config.py            # Email credentials and configuration
├── requirements.txt     # Required dependencies
└── README.md            # Project documentation
```

## 🛠️ Prerequisites

- Python 3.8 or later
- OpenAI API key
- Email account (Gmail or Outlook)

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/email-ai-autoresponder.git
cd email-ai-autoresponder
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

Update the `config.py` file with your credentials and settings:

```python
# config.py

EMAIL_ADDRESS = 'your_email@example.com'    # Your email address
EMAIL_PASSWORD = 'your_password'            # Your email password

# IMAP and SMTP settings
IMAP_SERVER = 'imap.gmail.com'              # For Gmail, or 'imap-mail.outlook.com' for Outlook
SMTP_SERVER = 'smtp.gmail.com'              # For Gmail, or 'smtp.office365.com' for Outlook

# OpenAI API key
OPENAI_API_KEY = 'your_openai_api_key'
```

🔔 **Note**: If you're using **Gmail** with 2-step verification, you must generate an [App Password](https://myaccount.google.com/apppasswords).

## ▶️ Running the Bot

To start the bot:

```bash
python main.py
```

## 📬 Testing the Bot

1. Send a test email to the address configured in `config.py`.
2. Verify that the bot responds with an AI-generated reply.

## 📊 Customizing the Bot

- Modify the `generate_response()` function in `main.py` to customize the AI replies.
- Adjust the frequency of inbox checks by wrapping the `check_inbox()` function in a loop with a delay.

## 🧰 Troubleshooting

- **Authentication Error**: Ensure that the email address, password, and IMAP/SMTP access are correctly configured.
- **No Replies Sent**: Verify that IMAP access is enabled and the correct servers are used.
- **OpenAI API Error**: Confirm that your API key is valid and has sufficient usage limits.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the project.

---

💡 **Empower your email communication with smart AI-driven automation!**

