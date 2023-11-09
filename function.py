import json
import os
import requests

def lambda_handler(event, context):
    # Assuming event is a JSON object
    input_data = json.loads(event)

    # Extract the URL of the created issue
    issue_url = input_data.get("issue", {}).get("html_url", "")

    # Construct the payload for Slack
    payload = {
        "text": f"Issue Created: {issue_url}"
    }

    # Send data to Slack using webhook URL
    slack_url = os.environ.get("SLACK_URL")
    response = requests.post(slack_url, json=payload)

    # Return the response from Slack as the result of the Lambda function
    return {
        "statusCode": response.status_code,
        "body": response.text
    }
