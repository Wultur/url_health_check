#!/usr/bin/python
import requests
import boto3
from datetime import datetime

def check_website_health(url):
    try:
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            return False
        else:
            return True
    except:
        return True

def send_sns_notification(subject, message):
    sns = boto3.client('sns')
    topic_arn = 'AWS SNS ARN'
    response = sns.publish(
        TopicArn=topic_arn,
        Subject=subject,
        Message=message
    )
    return response

if __name__ == '__main__':
    url = "http://ip-apddress"
    if check_website_health(url):
        subject = 'The Service is down'
        message = 'The Service is down.'
        print(message)
        send_sns_notification(subject, message)
    else:
        current_date = datetime.now().date()
        print('The Service is up and running!   ' + current_date.strftime('%m/%d/%Y'))