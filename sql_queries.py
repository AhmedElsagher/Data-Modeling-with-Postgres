# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs ;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time ;"

# CREATE TABLES
# 'user_id','first_name','last_name', 'gender','level'
user_table_create = ("""
CREATE TABLE  IF  NOT EXISTS  users
(
    user_id VARCHAR(50)  PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL, 
    last_name VARCHAR(50) NOT NULL, 
    gender  CHARACTER(1) NOT NULL, 
    level VARCHAR(10) check(level in('free','paid'))
);
""")


# artist_id, name, location, latitude, longitude

artist_table_create = ("""
CREATE TABLE  IF  NOT EXISTS  artists
(
    artist_id  VARCHAR(50)  PRIMARY KEY,
    name VARCHAR(100) NOT NULL, 
    location  VARCHAR(100), 
    latitude NUMERIC,
    longitude NUMERIC
);
""")

#   song_id, title, artist_id, year, duration
song_table_create = ("""
CREATE TABLE  IF  NOT EXISTS  songs
(
    song_id  VARCHAR(50)  PRIMARY KEY,
    title VARCHAR(100), 
    artist_id VARCHAR(50), 
    year INT,
    duration  NUMERIC
--    CONSTRAINT fk_artist
--       FOREIGN KEY(artist_id) 
--        REFERENCES artists(artist_id)
);
""")

#    songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

songplay_table_create = ("""
CREATE TABLE IF  NOT EXISTS songplays 
(
    songplay_id SERIAL PRIMARY KEY,
    start_time NUMERIC UNIQUE NOT NULL,
    user_id  VARCHAR(50) NOT NULL,
    level VARCHAR(10)  check(level in('free','paid')), 
    song_id VARCHAR(50)  ,
    artist_id VARCHAR(50)  ,
    session_id INT NOT NULL,
    location  VARCHAR(50) ,
    user_agent TEXT
--   CONSTRAINT fk_artist
--      FOREIGN KEY(artist_id) 
--        REFERENCES artists(artist_id),
--    CONSTRAINT fk_user
--        FOREIGN KEY(user_id) 
--        REFERENCES users(user_id)
--    CONSTRAINT fk_song
--       FOREIGN KEY(user_id) 
--       REFERENCES users(user_id)
);
""")



# timestamp, hour, day, week of year, month, year, and weekday
time_table_create = ("""
CREATE TABLE  IF  NOT EXISTS  time
(
    timestamp NUMERIC PRIMARY KEY,
    hour INT,
    day INT,
    weekofyear INT,
    month INT,
    year INT,
    weekday INT
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays ( start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
                 VALUES (%s, %s,%s, %s, %s,%s, %s, %s ) ON CONFLICT DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO users (user_id,first_name,last_name, gender,level) 
                 VALUES (%s, %s, %s,%s, %s)ON CONFLICT(user_id) DO UPDATE SET level = excluded.level;
""")

song_table_insert = ("""
INSERT INTO songs (  song_id, title, artist_id, year, duration) 
                 VALUES (%s, %s, %s,%s, %s )ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) 
                 VALUES (%s, %s, %s,%s, %s)ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (timestamp, hour, day, weekofyear, month, year,  weekday) 
                 VALUES (%s, %s, %s,%s, %s, %s, %s)ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""
 SELECT  songs.song_id, artists.artist_id FROM songs FULL OUTER  JOIN artists 
 ON
 songs.artist_id = artists.artist_id
 WHERE songs.title = %s AND
     artists.name = %s AND
     songs.duration = %s ;
 """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create,
                        song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
