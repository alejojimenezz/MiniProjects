# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyshorteners"
# ]
# ///


import pyshorteners

s = pyshorteners.Shortener(api_key='YOUR_KEY')
s.bitly.short('http://www.google.com')
s.bitly.expand('https://bit.ly/TEST')

# Requires API KEY