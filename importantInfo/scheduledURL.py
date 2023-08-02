import sched
import time
import subprocess

# Define the time intervals for running the file
intervals = ['06:00', '12:00', '18:00', '00:00']

def run_file():
    # Replace 'filename.py' with the name of your file
    subprocess.call(['python', 'updatingURLTest.py'])

def schedule_file():
    s = sched.scheduler(time.time, time.sleep)
    for interval in intervals:
        # Convert the interval to seconds since epoch
        scheduled_time = time.mktime(time.strptime(interval, '%H:%M'))

        # Schedule the task to run at the specified time
        s.enterabs(scheduled_time, 1, run_file)

    # Run the scheduler
    s.run()

# Schedule the file to run
schedule_file()
