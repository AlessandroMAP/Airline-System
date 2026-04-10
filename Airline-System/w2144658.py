"""
****************************************************************************
Additional info
 1. I declare that my work contins no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID: w2144658
 4. Date: 23/11/2025
****************************************************************************

"""
from graphics import *  
import csv  
import math  

data_list = []   

def load_csv(CSV_chosen):
    """
    This function loads any csv file by name (set by the variable 'selected_data_file') into the list "data_list"
    YOU DO NOT NEED TO CHANGE THIS BLOCK OF CODE
    """
    with open(CSV_chosen, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            data_list.append(row)



#************************************************************************************************************

#EDIT THE CODE BELOW TO COMPLETE YOUR SUBMISSION

# Dictionary containing valid airport codes and their full names
valid_airports = {"LHR" : "London Heathrow",
           "MAD" : "Madrid Adolfo Suárez-Barajas",
           "CDG" : "Charles De Gaulle International",
           "IST" : "Istanbul Airport International",
           "AMS" : "Amsterdam Schiphol",
           "LIS" : "Lisbon Portela",
           "FRA" : "Frankfurt Main",
           "FCO" : "Rome Fiumicino",
           "MUC" : "Munich International",
           "BCN" : "Barcelona International"}

# Dictionary containing valid airline codes and their full names
valid_airlines = {"BA":"British Airways",
                  "AF":"Air France",
                  "AY":"Finnair",
                  "KL":"KLM",
                  "SK":"Scandinavian Airlines",
                  "TP":"TAP Air Portugal",
                  "TK":"Turkish Airlines",
                  "W6":"Wizz Air",
                  "U2":"easyJet",
                  "FR":"Ryanair",
                  "A3":"Aegean Airlines",
                  "SN":"Brussels Airlines",
                  "EK":"Emirates",
                  "QR":"Qatar Airways",
                  "IB":"Iberia",
                  "LH":"Lufthansa"}


# MAIN PROGRAM LOOP - Task E: Allows user to process multiple CSV files

while True:
    
    
    # TASK A - INPUT VALIDATION
   
    
    # Validate and accept city code input
    while True:
        city_code = input("Please enter a three-letter city code: ").upper()  # Get input and convert to uppercase
        
        if len(city_code) != 3:  # Check if length is not equal to 3
            print("Wrong code length - please enter a three-letter city code")  # Display error message
        elif city_code not in valid_airports:  # Check if city code exists in valid airports dictionary
            print("Unavailable city code - please enter a valid city code")  # Display error message
        else:
            break  # Exit loop if valid city code entered

    # Validate and accept year input
    while True:
        year = input("Please enter the year required in the format YYYY: ")  # Get year input
        
        if not year.isdigit() or len(year) != 4:  # Check if input is not a digit or length is not 4
            print("Wrong data type - please enter a four-digit year value")  # Display error message
        elif int(year) > 2025 or int(year) < 2000:  # Check if year is outside valid range
            print("Out of range - please enter a value from 2000 to 2025")  # Display error message
        else:
            break  # Exit loop if valid year entered
        
    # Construct the CSV filename by combining city code and year
    selected_data_file = f"data/{city_code}{year}.csv"

    # Display formatted header showing the selected file and airport information
    print("********************************************************************************")
    print(f"{selected_data_file} selected - Planes departing {valid_airports[city_code]} {year}")
    print("********************************************************************************")

    # Call function to load the selected CSV file into data_list
    load_csv(selected_data_file)

   
    # TASK B - OUTCOMES
   

    # Outcome 1: Calculate total number of departure flights in the 12-hour period
    total_flights = len(data_list)  # Get length of data_list (number of rows = number of flights)
    print(f"The total number of flights from this airport was {total_flights}")

    # Outcome 2: Calculate total number of flights departing from Terminal 2
    terminal2_count = 0  # Initialize counter
    for row in data_list:  # Loop through each flight record
        if row[8] == "2":  # Check if departure terminal (column 8) is "2"
            terminal2_count = terminal2_count + 1  # Increment counter

    print(f"The total number of flights departing Terminal Two was {terminal2_count}")

    # Outcome 3: Calculate total number of departures for flights under 600 miles
    under_600_counter = 0  # Initialize counter
    for row in data_list:  # Loop through each flight record
        if int(row[5]) < 600:  # Check if distance (column 5) is less than 600 miles
            under_600_counter = under_600_counter + 1  # Increment counter

    print(f"The total number of departures on flights under 600 miles was {under_600_counter}")

    # Outcome 4: Calculate total number of Air France flights
    AF_counter = 0  # Initialize counter
    for row in data_list:  # Loop through each flight record
        if row[1].startswith("AF"):  # Check if flight number (column 1) starts with "AF"
            AF_counter = AF_counter + 1  # Increment counter

    print(f"There were {AF_counter} Air France flights from this airport")

    # Outcome 5: Calculate total flights departing in temperatures below 15°C
    below_15_counter = 0  # Initialize counter
    for row in data_list:  # Loop through each flight record
        # Extract temperature from weather conditions (column 10) and convert to integer
        if int(row[10].split("Â")[0]) < 15:  # Check if temperature is below 15
            below_15_counter = below_15_counter + 1  # Increment counter

    print(f"There were {below_15_counter} flights departing in temperatures below 15 degrees")

    # Outcome 6: Calculate average British Airways departures per hour
    BA_counter = 0  # Initialize counter for BA flights
    hours = 12  # Total hours in the data period

    for row in data_list:  # Loop through each flight record
        if row[1].startswith("BA"):  # Check if flight number starts with "BA"
            BA_counter = BA_counter + 1  # Increment counter

    Average = BA_counter / hours  # Calculate average flights per hour

    print(f"There was an average of {round(Average,2)} British Airways flights per hour from this airport")

    # Outcome 7: Calculate percentage of British Airways flights
    BA_percentage = (BA_counter/total_flights) * 100  # Calculate percentage

    print(f"British Airways planes made up {round(BA_percentage,2)}% of all departures")

    # Outcome 8: Calculate percentage of delayed Air France flights
    AF_delayed_counter = 0  # Initialize counter for delayed AF flights

    for row in data_list:  # Loop through each flight record
        if row[1].startswith("AF"):  # Check if flight is Air France
            if row[2] != row[3]:  # Compare scheduled departure (column 2) with actual departure (column 3)
                AF_delayed_counter = AF_delayed_counter + 1  # Increment if times don't match (delayed)

    AF_delayed_percentage = (AF_delayed_counter/AF_counter) * 100  # Calculate percentage

    print(f"{round(AF_delayed_percentage, 2)}% of Air France departures were delayed")

    # Outcome 9: Calculate total hours with rain
    rain_hours = []  # Initialize empty list to store unique rain hours

    for row in data_list:  # Loop through each flight record
        if "rain" in row[10]:  # Check if "rain" appears in weather conditions (column 10)
            hour = row[2].split(":")[0]  # Extract hour from scheduled departure time
            if hour not in rain_hours:  # Check if this hour is not already recorded
                rain_hours.append(hour)  # Add hour to list

    print(f"There were {len(rain_hours)} hours in which rain fell")

    # Outcome 10: Find the least common destination(s)
    
    # Step 1: Count occurrences of each destination
    destination_counts = {}  # Initialize empty dictionary to store destination counts

    for row in data_list:  # Loop through each flight record
        destination = row[4]  # Get destination code from column 4
        
        if destination in destination_counts:  # Check if destination already in dictionary
            destination_counts[destination] = destination_counts[destination] + 1  # Increment count
        else:
            destination_counts[destination] = 1  # Add new destination with count of 1

    # Step 2: Find the minimum count
    min_count = min(destination_counts.values())  # Get the smallest count value

    # Step 3: Find all destinations with the minimum count
    least_common = []  # Initialize list for least common destination codes
    for destination, count in destination_counts.items():  # Loop through each destination and its count
        if count == min_count:  # Check if this destination has the minimum count
            least_common.append(destination)  # Add to list

    # Step 4: Convert airport codes to full names
    least_common_full_names = []  # Initialize list for full airport names
    for destination in least_common:  # Loop through least common destination codes
        full_name = valid_airports[destination]  # Look up full name in dictionary
        least_common_full_names.append(full_name)  # Add full name to list

    print(f"The least common destinations are {least_common_full_names}")

    
    # TASK C - SAVE RESULTS TO TEXT FILE
  
    
    # Open results.txt in append mode and write all outcomes
    with open("results.txt", "a") as file:
        file.write("********************************************************************************\n")
        file.write(f"{selected_data_file} selected - Planes departing {valid_airports[city_code]} {year}\n")
        file.write("********************************************************************************\n")
        file.write(f"The total number of flights from this airport was {total_flights}\n")
        file.write(f"The total number of flights departing Terminal Two was {terminal2_count}\n")
        file.write(f"The total number of departures on flights under 600 miles was {under_600_counter}\n")
        file.write(f"There were {AF_counter} Air France flights from this airport\n")
        file.write(f"There were {below_15_counter} flights departing in temperatures below 15 degrees\n")
        file.write(f"There was an average of {round(Average,2)} British Airways flights per hour from this airport\n")
        file.write(f"British Airways planes made up {round(BA_percentage,2)}% of all departures\n")
        file.write(f"{round(AF_delayed_percentage, 2)}% of Air France departures were delayed\n")
        file.write(f"There were {len(rain_hours)} hours in which rain fell\n")
        file.write(f"The least common destinations are {least_common_full_names}\n\n")

    print("Results saved to results.txt")


    # TASK D - HISTOGRAM

    
    # Validate and accept airline code for histogram
    while True:
        airline_code = input("Enter a two-character Airline code to plot a histogram: ").upper()  # Get input and convert to uppercase
        
        if airline_code not in valid_airlines:  # Check if airline code is valid
            print("Unavailable Airline code please try again")  # Display error message
        else:
            break  # Exit loop if valid airline code entered

    # Count flights per hour for the selected airline
    hourly_count = {}  # Initialize empty dictionary to store hourly flight counts

    for row in data_list:  # Loop through each flight record
        if row[1].startswith(airline_code):  # Check if flight belongs to selected airline
            hour = row[2].split(":")[0]  # Extract hour from scheduled departure time
            
            if hour in hourly_count:  # Check if hour already in dictionary
                hourly_count[hour] = hourly_count[hour] + 1  # Increment count
            else:
                hourly_count[hour] = 1  # Add new hour with count of 1

    # Find maximum flights in any single hour for scaling bars
    max_flights = max(hourly_count.values()) if hourly_count else 1  # Use 1 if no flights to avoid division by zero

    # Define window dimensions and margins
    window_width = 800  # Total window width in pixels
    window_height = 600  # Total window height in pixels
    margin_left = 100  # Left margin for Y-axis labels
    margin_right = 50  # Right margin
    margin_top = 80  # Top margin for title
    margin_bottom = 50  # Bottom margin

    # Calculate usable graph area
    graph_width = window_width - margin_left - margin_right  # Width available for bars
    graph_height = window_height - margin_top - margin_bottom  # Height available for bars
    bar_height = graph_height / 12  # Height for each horizontal bar

    # Create graphics window
    win = GraphWin("Flight Histogram", window_width, window_height)
    win.setBackground("white")  # Set background color to white

    # Draw title at top of window
    title = Text(Point(window_width / 2, 30), f"Departures by hour for {valid_airlines[airline_code]} from {valid_airports[city_code]} {year}")
    title.setSize(12)
    title.setStyle("bold")
    title.draw(win)

    # Draw "Hours" label on Y-axis
    hours_label = Text(Point(40, window_height / 2), "Hours")
    hours_label.setSize(10)
    hours_label.setStyle("bold")
    hours_label.draw(win)

    # Draw time range indicator
    time_range = Text(Point(40, window_height / 2 + 30), "00:00\n-\n12:00")
    time_range.setSize(8)
    time_range.draw(win)

    # Draw horizontal bars for each hour
    for hour in range(12):  # Loop through hours 0 to 11
        str_hour = str(hour).zfill(2)  # Convert hour to 2-digit string (e.g., "00", "05")
        count = hourly_count.get(str_hour, 0)  # Get flight count for this hour (0 if no flights)

        # Calculate bar width based on flight count (scaled proportionally)
        bar_width = (count / max_flights) * graph_width if count > 0 else 0

        # Calculate Y coordinates for bar position
        y1 = margin_top + (hour * bar_height)  # Top edge of bar
        y2 = y1 + bar_height - 5  # Bottom edge of bar (minus 5 for gap)

        # Calculate X coordinates for bar
        x1 = margin_left  # Left edge (all bars start at same position)
        x2 = margin_left + bar_width  # Right edge (varies based on count)

        # Create and draw the bar
        bar = Rectangle(Point(x1, y1), Point(x2, y2))
        bar.setFill("#E89CAE")  # Set fill color (pink)
        bar.setOutline("#D88BA0")  # Set outline color (darker pink)
        bar.draw(win)
        
        # Draw hour label on Y-axis
        hour_label = Text(Point(margin_left - 15, (y1 + y2) / 2), f"{str_hour}")
        hour_label.setSize(9)
        hour_label.draw(win)
        
        # Draw flight count at end of bar (only if count > 0)
        if count > 0:
            count_label = Text(Point(x2 + 15, (y1 + y2) / 2), str(count))
            count_label.setSize(10)
            count_label.setStyle("bold")
            count_label.draw(win)
    
    # Wait for mouse click to close window
    try:
        win.getMouse()  # Wait for user to click
        win.close()  # Close the window
    except GraphicsError:  # Handle case where window is closed manually
        pass

   
    # TASK E - LOOP TO PROCESS ANOTHER FILE
   
    
    # Ask user if they want to process another CSV file
    response = input("Do you want to select a new data file? Y/N: ").upper()  # Get input and convert to uppercase
    
    if response == "N":  # User does not want to continue
        print("Thank you. End of run")
        break  # Exit the main loop
    elif response == "Y":  # User wants to process another file
        data_list.clear()  # Clear data_list for next iteration
        # Loop continues automatically to beginning
    else:  # Invalid input
        print("Invalid input. Ending program.")
        break  # Exit the main loop
