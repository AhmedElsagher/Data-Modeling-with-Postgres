# Sparkify
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.
## Database Design
Using the song and log datasets, i created a star schema optimized for queries on song play analysis. This includes the following tables.

#### Fact Table

1.  **songplays** - records in log data associated with song plays i.e. records with page `NextSong`
    -   _songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent_

#### Dimension Tables

2.  **users** - users in the app
    -   _user_id, first_name, last_name, gender, level_
3.  **songs** - songs in music database
    -   _song_id, title, artist_id, year, duration_
4.  **artists** - artists in music database
    -   _artist_id, name, location, latitude, longitude_
5.  **time** - timestamps of records in **songplays** broken down into specific units
    -   _start_time, hour, day, week, month, year, weekday_
## ETL Pipeline
1.  **create_tables** script is responsible for create the schema 
2.    **etl** script is responsible for loading json files and populating the tables .
3. test notebook for testing the scripts

## How to Run 
1. install Postgres and its wrapper in python psycopg2
2. Create tables   `python create_tables.py`
3.   Populate tables  `python etl.py`
