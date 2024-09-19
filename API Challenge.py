# Make sure your Flask server is running and reachable. 
# Once confirmed, run your control script (Luxor Challenge.py) and observe the outputs.
# Always make sure your syntax is clean.

import argparse  # Use this to test your arguments within the script. Will ensure automation works.
import requests  # Import the requests library to handle HTTP requests.
import schedule  # Import the schedule library to handle scheduling tasks.
import time  # Import the time library to handle sleep and time functions.
from datetime import datetime  # Import datetime for handling date and time.
from threading import Thread  # Import Thread to run tasks concurrently.

API_URL = "http://localhost:5000/api"  # Base URL for the API.

class Miner:
    def __init__(self, ip):
        self.ip = ip  # IP address of the miner.
        self.token = None  # Token for the miner's session.
        self.current_mode = None  # Current mode of the miner.

    def login(self):
        try:
            response = requests.post(f"{API_URL}/login", json={"miner_ip": self.ip})  # Send a POST request to the login endpoint.
            response.raise_for_status()  # Raise an exception for HTTP errors.
            self.token = response.json().get("token")  # Retrieve the token from the response.
            print(f"Logged in to miner {self.ip}, token: {self.token}")  # Print the login success message.
        except requests.RequestException as e:
            print(f"Failed to log in to miner {self.ip}: {e}")  # Print the error message if login fails.

    def set_mode(self, mode):
        try:
            if mode in ["overclock", "normal", "underclock"]:
                response = requests.post(f"{API_URL}/profileset", json={"token": self.token, "profile": mode})  # Set the profile mode.
                response.raise_for_status()  # Raise an exception for HTTP errors.
            elif mode == "curtail":
                response = requests.post(f"{API_URL}/curtail", json={"token": self.token, "mode": "sleep"})  # Set the curtail mode.
                response.raise_for_status()  # Raise an exception for HTTP errors.
            self.current_mode = mode  # Update the current mode of the miner.
            print(f"Miner {self.ip} set to {mode}")  # Print the mode change success message.
        except requests.RequestException as e:
            print(f"Failed to set mode for miner {self.ip}: {e}")  # Print the error message if mode change fails.

def schedule_miner_operations(miner):
    """Schedules the operations for a single miner based on the time of day."""
    miner.login()  # Log in to the miner.

    def set_overclock():
        miner.set_mode("overclock")  # Set miner mode to overclock.
        print(f"Set miner {miner.ip} to overclock")  # Print the mode change message.

    def set_normal():
        miner.set_mode("normal")  # Set miner mode to normal.
        print(f"Set miner {miner.ip} to normal")  # Print the mode change message.

    def set_underclock():
        miner.set_mode("underclock")  # Set miner mode to underclock.
        print(f"Set miner {miner.ip} to underclock")  # Print the mode change message.

    def set_curtail():
        miner.set_mode("curtail")  # Set miner mode to curtail.
        print(f"Set miner {miner.ip} to curtail")  # Print the mode change message.

    print(f"Scheduling tasks for miner {miner.ip}")  # Print the scheduling message.
    schedule.every().day.at("0:00").do(set_overclock)  # Schedule overclock at 00:00.
    schedule.every().day.at("6:00").do(set_normal)  # Schedule normal mode at 06:00.
    schedule.every().day.at("12:00").do(set_underclock)  # Schedule underclock at 12:00.
    schedule.every().day.at("18:00").do(set_curtail)  # Schedule curtail at 18:00.

def run_scheduler():
    """Runs the scheduler to execute pending tasks."""
    while True:
        schedule.run_pending()  # Run pending scheduled tasks.
        time.sleep(60)  # Sleep for a minute before checking again.

def main():
    MINERS = ["192.168.1.100", "192.168.1.101", "192.168.1.102"]  # List of miner IP addresses.
    threads = []  # Initialize the threads list.

    for miner_ip in MINERS:
        miner = Miner(miner_ip)  # Create a Miner object for each IP.
        thread = Thread(target=schedule_miner_operations, args=(miner,))  # Create a Thread to handle each miner.
        thread.start()  # Start the thread.
        threads.append(thread)  # Add each thread to the list.

    # Start the scheduler in its own thread.
    scheduler_thread = Thread(target=run_scheduler)
    scheduler_thread.start()

    # Join miner threads to ensure they complete.
    for thread in threads:
        thread.join()

    # Join the scheduler thread to ensure it completes.
    scheduler_thread.join()

if __name__ == "__main__":
    main()  # Execute the main function if this script is run directly.
