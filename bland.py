import requests
import json

url = 'https://api.bland.ai/v1/calls'
authorization = '<authorization>'  # Replace with your actual authorization token
data = {
   'phone_number': '+12223334455',
   'task': 'A prompt up to 24k characters that instructs your phone agent what to do',
   'tools': ['A set of external APIs your phone agent can interact with during calls'],
   'transfer_phone_number': '+16667778899',
   'voice_id': 123
}

headers = {
   'Content-Type': 'application/json',
   'Authorization': authorization
}