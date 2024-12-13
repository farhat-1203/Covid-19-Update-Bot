# Covid-19 Update Bot

A simple Python-based COVID-19 update bot that provides real-time notifications about the current confirmed cases, deaths, and recoveries worldwide. The bot runs in the background and shows notifications every hour with the latest statistics.

## Features
- Get real-time COVID-19 statistics (confirmed cases, deaths, recoveries).
- Notification feature that shows updates every hour.
- A simple and user-friendly GUI for displaying the information.
- Supports fetching data for specific countries (modifiable in the code).

## Tech Stack
- Backend: Python 3.x
- Libraries: `requests`, `win10toast`, `tkinter` (for GUI)
- API: `https://coronavirus-19-api.herokuapp.com/` (for fetching COVID-19 data)

## Setup Instructions

### Prerequisites
- Python 3.11 or higher installed on your system.
- pip package manager.

### Steps to Run the Project

1. **Clone the repository:**
    ```bash
    git clone https://github.com/farhat-1203/Covid-19-Update-Bot.git
    cd Covid-19-Update-Bot
    ```

2. **Set up a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows use: venv\Scripts\activate
    ```

3. **Install required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the bot:**
    ```bash
    python corona.py
    ```

5. **Enjoy the notifications!**

### Project Structure
```plaintext
Covid-19-Update-Bot/
├── mycovidenv             # virtual enironment folder 
├── corona.py              # Main script for fetching and displaying updates
├── LICENSE                # License information (optional)
├── requirements.txt       # Required libraries for the project
