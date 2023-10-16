import sqlite3
import os

def get_db_path():
    # Get the directory where the script is located
    script_dir = os.path.dirname(__file__)
    
    # Combine the directory path with the database file name
    db_path = os.path.join(script_dir, "../db/lap_times.db")
    
    return db_path

def init_database():
    # Check if the database file exists
    print("laptime_db: Checking database existance...")
    db_path = "db/lap_times.db"
    if not os.path.exists(db_path):
        print("laptime_db: Database doesn't exist")
        create_database()
    else :
        print("laptime_db: Database exists")

def create_database():
    # Create the database and necessary tables
    try:
        print("laptime_db: Creating database...")
        conn = sqlite3.connect("db/lap_times.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS lap_times (
                            track_name TEXT,
                            lap_time TEXT,
                            driver_name TEXT
                        )''')
        conn.commit()
        conn.close()
        print("laptime_db: Database created successfully")
    except Exception as e:
        print("laptime_db: Error creating the database:", str(e))

def save_lap_time_to_db(track_name, lap_time, driver_name):
    # Ensure the database exists
    init_database()

    print("laptime_db: Save_lap_time to db in laptime_db", driver_name, track_name, lap_time)
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lap_times ( track_name, lap_time, driver_name) VALUES (?, ?, ?)", (track_name, lap_time, driver_name))
    conn.commit()
    conn.close()
    print("laptime_db: Laptimes inserted into db")

def get_lap_times_from_db():
# Ensure the database exists
    init_database()
    print("laptime_db: Getting laptimes from db")
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("SELECT track_name, lap_time, driver_name TEXT FROM lap_times")
    lap_times = cursor.fetchall()
    conn.close()
    print("laptime_db: Recieved lap times:", lap_times)
    return lap_times