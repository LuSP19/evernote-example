import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    def __init__(self):
        self.EVERNOTE_CONSUMER_KEY = os.getenv('EVERNOTE_CONSUMER_KEY')
        self.EVERNOTE_CONSUMER_SECRET = os.getenv('EVERNOTE_CONSUMER_SECRET')
        self.EVERNOTE_PERSONAL_TOKEN = os.getenv('EVERNOTE_PERSONAL_TOKEN')
        self.JOURNAL_TEMPLATE_NOTE_GUID = os.getenv('JOURNAL_TEMPLATE_NOTE_GUID')
        self.JOURNAL_NOTEBOOK_GUID = os.getenv('JOURNAL_NOTEBOOK_GUID')
        self.INBOX_NOTEBOOK_GUID = os.getenv('INBOX_NOTEBOOK_GUID')
