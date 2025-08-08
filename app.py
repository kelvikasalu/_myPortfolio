from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact-form')
def contact_form():
    return render_template('contact_form.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = 'kelvinkasalu20@gmail.com'  # Your email address
        msg['Subject'] = f"Portfolio Contact: {subject}"
        
        # Create the email body
        body = f"""
        Name: {name}
        Email: {email}
        Subject: {subject}
        
        Message:
        {message}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            # Configure your email server settings here
            # For Gmail, you'll need to use an App Password
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('your-email@gmail.com', 'your-app-password')  # Replace with your email and app password
            server.send_message(msg)
            server.quit()
            
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash('There was an error sending your message. Please try again later.', 'error')
            print(f"Error sending email: {str(e)}")
        
        return redirect(url_for('contact_form'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 