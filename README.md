# Corona-Help-Bot-for-Building-Society
The **Corona Help Bot** is designed to provide helpful information about COVID-19 to residents of your building society. It can answer common queries, provide prevention tips, help you find hospitals nearby, and even send email and SMS alerts.

## Requirements
- **pyttsx3**==2.90
- **SpeechRecognition**==3.8.1
- **twilio**==7.0.0  # Required only if using the SMS feature

## Features

- **Voice Recognition**: The bot listens to your commands and provides answers.
- **Text-to-Speech**: The bot responds verbally to your queries.
- **Email & SMS Alerts**: Send important alerts via email or SMS (Twilio required for SMS).
- **COVID-19 Information**: Get symptoms, prevention tips, and nearby hospital details.

## Setup

### Prerequisites

1. **Python 3.x** installed on your system.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
