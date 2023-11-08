import json
import os
import requests

def lambda_handler(event, context):
    # Verify the GitHub webhook event type
    headers = event['headers']
    if 'X-GitHub-Event' in headers and headers['X-GitHub-Event'] == 'issues':
        # Deserialize the incoming JSON payload
        input_json = json.loads(event['body'])
        issue_url = input_json['issue']['html_url']

        # Prepare Slack message payload
        slack_payload = {
            'text': f'Issue Created: {issue_url}'
        }

        # Send the message to Slack
        response = requests.post(os.environ['SLACK_URL'], json=slack_payload)

        # Check the response from Slack
        if response.status_code == 200:
            return {
                'statusCode': 200,
                'body': json.dumps('Message sent successfully to Slack!')
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': json.dumps('Failed to send message to Slack!')
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid GitHub webhook event!')
        }
