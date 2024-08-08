#By leveraging a custom API, this application automates miner operations, ensuring each miner runs in the most efficient mode based on the time of day. 
#I provide an overview of how this application functions, its features, and setup instructions.

#The miner control application is an advanced tool that schedules various operating modes for a fleet of miners based on a predefined time schedule. 
#This time-based scheduling allows miners to switch between different operational modes, such as overclocking, normal operation, underclocking, and curtailing, at specific times throughout the day. 
#Here’s a detailed breakdown of the modes:
#Overclock: From midnight to 6:00 AM, miners operate at maximum capacity, utilizing off-peak hours to maximize performance.
#Normal: From 6:00 AM to noon, miners switch to normal mode, balancing performance and power consumption.
#Underclock: From noon to 6:00 PM, miners reduce power consumption, aligning with higher daytime electricity rates.
#Curtail: From 6:00 PM to midnight, miners enter curtail mode to conserve energy during peak demand times.
#This application manages multiple miners concurrently, ensuring that each miner follows the schedule without the need for manual intervention. 
#Furthermore, the application logs every operation and mode change, providing a clear and detailed record of the fleet’s activities for transparency and accountability.

#Prerequisites
#Python 3.6+
#type in "pip install requests" 
#type in "pip install flask"

