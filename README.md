
This application automates miner operations, ensuring each miner runs in a specific mode based on the time of day. 
I provide an overview of how this application functions, its features, and setup instructions.

The control application is an advanced tool that schedules different operating modes for a fleet of miners based on a predefined time schedule. 
This time-based scheduling allows miners to switch between different operational modes, such as overclocking, normal operation, underclocking, and curtailing.

In order to run an application that interacts with your machines, you need to build a virtual server and you need to run a script that operates accordingly with the server. 

Automated commands to be implemented:
#Overclock: From midnight to 6:00 AM, miners operate at maximum capacity, utilizing off-peak hours to maximize performance.
#Normal: From 6:00 AM to noon, miners switch to normal mode, balancing performance and power consumption.
#Underclock: From noon to 6:00 PM, miners reduce power consumption, aligning with higher daytime electricity rates.
#Curtail: From 6:00 PM to midnight, miners enter curtail mode to conserve energy during peak demand times.

Prerequisites:
Install the latest version of python or version that is compatible with your OS
Type "pip install requests" in the terminal
type in "pip install flask" in the terminal

A couple of notes I'd like to emphasize: 

Make sure your Flask server is running and reachable. 
Once confirmed, run your control script (Luxor Challenge.py) and observe the outputs.
Always make sure your syntax is clean.
Use 'impoprt argparse' to test your arguments within the script. Will ensure automation works.
This application was built in the VS code IDE
