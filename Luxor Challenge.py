import requests  # Import the requests library to handle HTTP requests
import schedule  # Import the schedule library to handle scheduling tasks
import time  # Import time library to handle sleep and time functions
from datetime import datetime  # Import datetime for handling date and time
from threading import Thread  # Import Thread to run tasks concurrentlyimport shedule  # Import the schedule library to handle scheduling tasks
import time  # Import time library to handle sleep and time functions
from datetime import datetime # Import datetime for handling date and time
from threading import Thread # Import Thread to run tasks concurrently

API_URL = "http://localhost:5000/api"  # DefineS the base URL for the API

#List the miner IP addresses you want to have 
MINERS = MINERS = [
    "192.168.1.100",
    "192.168.1.101",
    "192.168.1.102",
]


class Miner:
    def __init__(self, ip):
        """Initialize a Miner object with the given IP address."""
        self.ip = ip  # Store the miner's IP address
        self.token = None  # Initialize the token as None
        self.current_mode = None  # Initialize the current mode as None


    def login(self): # Logs in to the miner and retrieves the token.
        try: 
            #Send a post request to login and retrieve the token
            response = requests.post(f"{API_URL}/login", json={"miner_ip": self.ip})
            response.raise_for_status()  # Raise an exception for HTTP errors
            self.token = response.json().get("token")  # Extract token from the response
            print(f"Logged in to miner {self.ip}, token: {self.token}")  # Print login success message
        except requests.RequestException as e:
            # Handle exceptions during login
            print(f"Failed to log in to miner {self.ip}: {e}")
        except requests.RequestException as e:
            # Handle exceptions during login
            print(f"Failed to log in to miner {self.ip}: {e}")
    

    def logout(self):
        """Logs out of the miner."""
        try:
            if self.token:
                # Send a POST request to logout if token exists
                response = requests.post(f"{API_URL}/logout", json={"miner_ip": self.ip})
                response.raise_for_status()  # Raise an exception for HTTP errors
                print(f"Logged out of miner {self.ip}")  # Print logout success message
            self.token = None  # Reset the token
        except requests.RequestException as e:
            # Handle exceptions during logout
            print(f"Failed to log out of miner {self.ip}: {e}")


    def set_mode(self, mode):
        """Sets the miner's mode."""
        try:
            if mode in ["overclock", "normal", "underclock"]:
                # Send a POST request to set the miner's profile
                response = requests.post(f"{API_URL}/profileset", json={"token": self.token, "profile": mode})
                response.raise_for_status()  # Raise an exception for HTTP errors
            elif mode == "curtail":
                # Send a POST request to set the miner to curtail mode
                response = requests.post(f"{API_URL}/curtail", json={"token": self.token, "mode": "sleep"})
                response.raise_for_status()  # Raise an exception for HTTP errors
            self.current_mode = mode  # Update the current mode
            print(f"Miner {self.ip} set to {mode}")  # Print mode set success message
        except requests.RequestException as e:
            # Handle exceptions during mode setting
            print(f"Failed to set mode for miner {self.ip}: {e}")


    def schedule_miner_operations(miner):
        #Schedules the operations for a single miner based on the time of day.
        miner.login()  # Log in to the miner

    def set_overclock():
        Miner.set_mode("overclock")  # Set miner mode to overclock

    def set_normal():
        Miner.set_mode("normal")  # Set miner mode to normal

    def set_underclock():
        Miner.set_mode("underclock")  # Set miner mode to underclock

    def set_curtail():
        Miner.set_mode("curtail")  # Set miner mode to curtail


   # Schedule tasks for the miner at specific times
    schedule.every().day.at("00:00").do(set_overclock)  # Schedule overclock at midnight
    schedule.every().day.at("06:00").do(set_normal)  # Schedule normal mode at 6 AM
    schedule.every().day.at("12:00").do(set_underclock)  # Schedule underclock at noon
    schedule.every().day.at("18:00").do(set_curtail)  # Schedule curtail at 6 PM


    def main():
        threads = []  # List to hold threads for each miner
    for miner_ip in MINERS:
        miner = MINERS(miner_ip)  # Create a Miner object for each IP
        thread = Thread(target=schedule_miner_operations, args=(miner,))  # Create a new thread for miner operations
        thread.start()  # Start the thread
        threads.append(thread)  # Add thread to the list

    # Start the scheduler
    scheduler_thread = Thread(target = run_scheduler)  # Create a thread for the scheduler
    scheduler_thread.start()  # Start the scheduler thread

    # Join threads to ensure they complete
    for thread in threads:
        thread.join()  # Wait for miner operation threads to finish
    scheduler_thread.join()  # Wait for scheduler thread to finish

if __name__ == "__main__":
    main()  # Execute the main function if this script is run directly