from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.qq.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'qqid',
    MAIL_PASSWORD = 'password'
    )

mail = Mail(app)

@app.route("/")
def index():
    msg = Message(subject="Hello",
                  sender='you@qq.com',
                  recipients=['recipient@recipient_domain.com'])
    msg.html = "<b>testing</b> html"

    mail.send(msg)

    return '<h1>Sent</h1>'

if __name__ == '__main__':
    app.run(debug=True)
