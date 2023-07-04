import datetime
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPE = ['https://www.googleapis.com/auth/calendar']


def main():

    cred = None

    if os.path.exists('token.json'):
        cred = Credentials.from_authorized_user_file('token.json')

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPE)
            cred = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(cred.to_json())

    try:
        service = build('calendar', 'v3', credentials=cred)

        now = datetime.datetime.now().isoformat() + 'Z'

        event_result = service.events().list(calendarId='primary', timeMin=now,
                                             maxResults=10, singleEvents=True, orderBy='startTime').execute()
        events = event_result.get('items', [])

        if not events:
            print('No upcoming events')
            return

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        print('An unexpected error has occured:', error)
