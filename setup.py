from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
	'packages': [
        'requests',
        'rumps'
    ],
    'plist': {
        'CFBundleName': 'Currency Ticker',
        'CFBundleIdentifier': 'com.mqul.currency.ticker',
        'LSPrefersPPC': True,
        'LSUIElement': True,
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)