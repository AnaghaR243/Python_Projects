'''import requests
import json

city = input("Enter the name of the city: ")
api_key = 'ca676686ddf5447bbff03038242307'
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
r = requests.get(url)
wdic = json.loads(r.text)
print(wdic["temp_c"])
'''
import requests
import json
import os

def speak(text):
    # Construct a PowerShell command to speak the text
    command = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
              f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\');"'
    os.system(command)

# Get city input from the user
city = input("Enter the name of the city: ")

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'ca676686ddf5447bbff03038242307'
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

# Make the API request
r = requests.get(url)

# Check if the request was successful
if r.status_code == 200:
    try:
        # Parse the JSON data
        wdic = r.json()
        
        # Print the entire JSON response to understand its structure
        print("Weather Data:")
        print(json.dumps(wdic))
        
        # Extract the temperature in Celsius
        temp_c = wdic.get('current', {}).get('temp_c', 'Temperature data not found')
        
        # Prepare the message for speaking
        message = f"The temperature in {city} is {temp_c} degrees Celsius."
        print(message)
        
        # Call the speak function
        speak(message)
    except json.JSONDecodeError:
        print("Error: Unable to parse JSON response.")
else:
    print(f"Error: Unable to fetch weather data (status code: {r.status_code})")
