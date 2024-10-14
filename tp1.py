import requests
import time

# TikTok account username you want to target
tiktok_username = "target_username"
report_url = f"https://www.tiktok.com/@{tiktok_username}/report"

# Your headers to mimic a browser request (Adjust if needed)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
}

# Function to send a report
def report_account():
    try:
        # Data to send in the report (you'll need to customize the reason and details)
        report_data = {
            'reason': 'Inappropriate Content',
            'details': 'This account is posting inappropriate content, violating community guidelines.',
            'reportType': 'Abuse'
        }

        # Make a POST request to submit the report
        response = requests.post(report_url, headers=headers, data=report_data)

        # Check response status
        if response.status_code == 200:
            print(f"Report successfully sent for {tiktok_username}")
        else:
            print(f"Failed to report {tiktok_username}. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to send multiple reports with delay
def mass_report(reports_count, delay):
    for _ in range(reports_count):
        report_account()
        time.sleep(delay)  # Delay between each report to avoid detection

# Customize how many reports and delay between them
mass_report(100, 5)  # Sends 100 reports, 5 seconds apart
