<h1>Edge Finder</h1>
<h3>Scrape real time odds data in the NBA season. With GUI for user interaction and historical data analysis on odds movement</h3>

This project is designed for the NBA season and tracking, analyzing, and displaying real-time odds movement across different sportsbooks in the United States

Requirments in order to fully utilize: 
  - SQL database (tested on local MySQL DB - but queries will function correctly on any similar entities)

After DB Creations - Credentials must be stored somewhere for softare to access - placeholders are made in the current code (not recommended - use environment variables etc.)

- /tests folder contains the main files for functionality

- Step 1: Populating DB will game schedule information
  - Must run 'updatingURLTest.py' - will populate DB will schedule information for the given season. ONLY NEEDS TO BE RUN ONCE TO UPDATE THE DB AND STORED INDEFINITELY

- Step 2: Actually gathering real-time data
  - 'multithreadTest.py' will execute the scripts on the available sportsbooks (currently just FanDuel and DraftKings)
  - Odds data will be scraped and stored in DB for further analysis to be done

- For user interaction in the /interface directory - run 'home.py' to view the GUI built around the functionalities.


.spec files have been created, as home.py was created into EdgeFinder the desktop application version. Easily converted into .exe file


The scraper will not scrape anythign in the off season - as the only data that gets scraped and stored is about currently available games scheduled on the sportsbook. The main usability of this project is from 
late October -> June of the next year. That is the regular season and playoffs for the NBA


<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">
    <img width="250" alt="how_to_step1" src="https://github.com/ParkerG19/EdgeFinder-NBA-Odds-Scraper-Analysis/assets/36928533/34a47d0d-adec-4020-98b8-0fde5b5d1f24">
    <img width="250" alt="how_to_step2" src="https://github.com/ParkerG19/EdgeFinder-NBA-Odds-Scraper-Analysis/assets/36928533/4247628d-e9ef-475d-b028-86af67706d05">
    <img width="250" alt="how_to_step3" src="https://github.com/ParkerG19/EdgeFinder-NBA-Odds-Scraper-Analysis/assets/36928533/8a3e1cce-4dde-4ad3-a28e-98414fbf46af">
</div>
