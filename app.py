from flask import Flask, request, render_template, redirect, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # The SMTP server
app.config['MAIL_PORT'] = 587  # SMTP server port
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'borank55@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'dpgo nfrw qpxc ifzh'  # Your email account password
app.config['MAIL_DEFAULT_SENDER'] = 'borank55@gmail.com'  # Default sender

mail = Mail(app)

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/news_detail')
def news_detail():
    return render_template('news_detail.html')

# Contact form route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form.get('first-name')
            name = request.form.get('last-name')
            email = request.form.get('email')
            message = request.form.get('message')
            recipients = ['recipient-email@example.com']  # Change to your recipient email address

            msg = Message(
                "New Contact Form Submission",
                recipients=recipients,
                body=f"Name: {name}\nEmail: {email}\nMessage: {message}"
            )

            # Send the message
            mail.send(msg)

            # Return a success response
            return jsonify({'status': 'success', 'message': 'Message sent successfully!'})
        except Exception as e:
            # Return an error response
            return jsonify({'status': 'error', 'message': 'Failed to send message.'}), 500

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)