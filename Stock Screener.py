import yfinance as yf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Function to check if options flow is bullish or bearish
def check_options_flow(ticker, expiration_date):
    try:
        # Fetch options data for the specified ticker and expiration date
        options_data = yf.Ticker(ticker).option_chain(expiration_date)

        # Calculate total call and put volume
        call_volume = options_data.calls['volume'].sum()
        put_volume = options_data.puts['volume'].sum()

        # Determine if options flow is bullish or bearish
        if call_volume > put_volume:
            return "Bullish"
        elif put_volume > call_volume:
            return "Bearish"
        else:
            return "Neutral"
    except Exception as e:
        print(f"Error checking options flow for {ticker}: {e}")
        return "Error"


# Function to send email alert
def send_email_alert(subject, body):
    sender_email = "stockscreener2024@gmail.com"  # Your Gmail address
    receiver_email = "istanford@liberty.edu"  # Replace with recipient's email address
    password = "eohb kniw wlgh exok"  # Your Gmail app password

    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to SMTP server and send email using SSL
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred while sending email: {e}")


# Main function
def main():
    # Define the ticker symbol to monitor (SPY in this example)
    ticker = "SPY"
    expiration_date = '2024-04-12'  # Specify the desired expiration date

    # Check options flow for the specified ticker
    options_flow = check_options_flow(ticker, expiration_date)

    # Send email alert based on options flow
    subject = f"{ticker} Options Flow Alert"
    body = f"The options flow for {ticker} expiring on {expiration_date} is {options_flow}."
    send_email_alert(subject, body)


if __name__ == "__main__":
    main()