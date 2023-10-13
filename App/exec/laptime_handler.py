from db.laptime_db import save_lap_time_to_db, get_lap_times_from_db

def save_lap_time(track_name, lap_time):
    #print("laptime_handler.py: savelaptime outside of try.")
    try:
        print("laptime_handler.py: Saving laptime:", lap_time, "at",track_name)
        # Call the function to save lap time to the database
        save_lap_time_to_db(track_name, lap_time)
        return "Lap time saved successfully!"
    except Exception as e:
        return f"Error: {str(e)}"
    pass

def display_lap_times():
    print("laptime_handler.py: Displaying laptimes")
    try:
        # Call the function to get lap times from the database
        lap_times = get_lap_times_from_db()
        
        if lap_times:
            # Process the lap times and display them in your GUI
            formatted_lap_times = "\n".join([f"Track: {track_name}, Lap Time: {lap_time}" for track_name, lap_time in lap_times])
            print("laptime_handler.py: Formatted lap times", formatted_lap_times)
            return formatted_lap_times
        else:
            return "No lap times found."
    except Exception as e:
        return f"Error: {str(e)}"
    pass
