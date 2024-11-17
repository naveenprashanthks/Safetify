import requests
import geocoder
import datetime

# Simulated Crime Data for Coimbatore Areas (Use real data in production)
crime_data = {
    "racecourse": {"incidents": 3, "last_reported": "2024-11-05", "safety_score": 60},
    "peelamedu": {"incidents": 1, "last_reported": "2024-11-10", "safety_score": 85},
    "saravanampatti": {"incidents": 5, "last_reported": "2024-11-01", "safety_score": 50},
    "sungam": {"incidents": 2, "last_reported": "2024-11-07", "safety_score": 70},
    "RS Puram": {"incidents": 0, "last_reported": "2024-11-12", "safety_score": 90},
    "RSPuram": {"incidents": 0, "last_reported": "2024-11-12", "safety_score": 90},
    "TidelPark": {"incidents": 0, "last_reported": "2024-11-08", "safety_score": 95},
    "Tidel Park": {"incidents": 0, "last_reported": "2024-11-08", "safety_score": 95},
    "Kalapatti": {"incidents": 4, "last_reported": "2024-10-29", "safety_score": 55},
    "Coimbatore_Central": {"incidents": 3, "last_reported": "2024-11-01", "safety_score": 65},
    "Gandhipuram": {"incidents": 2, "last_reported": "2024-11-03", "safety_score": 70},
    "pollachi": {"incidents": 2, "last_reported": "2024-11-02", "safety_score": 75},
    "marudamalai": {"incidents": 1, "last_reported": "2024-10-30", "safety_score": 80},
    "udumalpet": {"incidents": 3, "last_reported": "2024-11-06", "safety_score": 65},
    "sira": {"incidents": 1, "last_reported": "2024-11-04", "safety_score": 85},
    "tidelpark south": {"incidents": 0, "last_reported": "2024-11-10", "safety_score": 95},
    "tidelparksouth": {"incidents": 0, "last_reported": "2024-11-10", "safety_score": 95},
    "peelamedu_south": {"incidents": 0, "last_reported": "2024-11-09", "safety_score": 90},
    "kovaipudur": {"incidents": 4, "last_reported": "2024-11-03", "safety_score": 60},
    "kinathukadavu": {"incidents": 3, "last_reported": "2024-11-04", "safety_score": 65},
    "malumichampatti": {"incidents": 2, "last_reported": "2024-11-05", "safety_score": 70},
    "othakalmandapam": {"incidents": 1, "last_reported": "2024-11-03", "safety_score": 80},
    "townhall": {"incidents": 1, "last_reported": "2024-11-11", "safety_score": 80},
    "town hall": {"incidents": 1, "last_reported": "2024-11-11", "safety_score": 80},
    "brookefields": {"incidents": 0, "last_reported": "2024-11-12", "safety_score": 90},
    "fun mall": {"incidents": 0, "last_reported": "2024-11-10", "safety_score": 85},
    "broadway cinemas": {"incidents": 1, "last_reported": "2024-11-08", "safety_score": 75},
    "legends mall": {"incidents": 1, "last_reported": "2024-11-09", "safety_score": 80},
    "kg mall": {"incidents": 0, "last_reported": "2024-11-07", "safety_score": 90},
    "city centre mall": {"incidents": 1, "last_reported": "2024-11-06", "safety_score": 78},
    "fun republic mall": {"incidents": 0, "last_reported": "2024-11-05", "safety_score": 88},
    "brookefields mall": {"incidents": 0, "last_reported": "2024-11-11", "safety_score": 90},
    "inox cinemas": {"incidents": 0, "last_reported": "2024-11-05", "safety_score": 90},
    "pvr cinemas": {"incidents": 1, "last_reported": "2024-11-09", "safety_score": 80},
    "sri vijaya cinemas": {"incidents": 1, "last_reported": "2024-11-04", "safety_score": 85},
    "alliances cinemas": {"incidents": 0, "last_reported": "2024-11-12", "safety_score": 88},
    "sree theatre": {"incidents": 1, "last_reported": "2024-11-03", "safety_score": 75},
    "shree theatre": {"incidents": 1, "last_reported": "2024-11-08", "safety_score": 77},
    "cinema max": {"incidents": 0, "last_reported": "2024-11-02", "safety_score": 90},
    "ram theatre": {"incidents": 1, "last_reported": "2024-11-10", "safety_score": 75},
    "balaji theatre": {"incidents": 0, "last_reported": "2024-11-06", "safety_score": 85},
    "miraj cinemas": {"incidents": 0, "last_reported": "2024-11-10", "safety_score": 88},
    "GH": {"incidents": 0, "last_reported": "2024-11-12", "safety_score": 90},  # Added GH
    "ramanathapuram": {"incidents": 2, "last_reported": "2024-11-09", "safety_score": 80},  # Added Ramanathapuram
    "singanallur": {"incidents": 3, "last_reported": "2024-11-08", "safety_score": 70},  # Added Singanallur
    "shanthi gears": {"incidents": 1, "last_reported": "2024-11-07", "safety_score": 75},  # Added Shanthi Gears
    "ondipudur": {"incidents": 4, "last_reported": "2024-11-06", "safety_score": 65},  # Added Ondipudur
    "irugur": {"incidents": 2, "last_reported": "2024-11-05", "safety_score": 80}  # Added Irugur


     # Added Town Hall location
  # Added Town Hall location
}

# Function to check safety based on the location
def check_safety(query):
    # Convert the query to lowercase for case-insensitive matching
    query = query.lower()

    # Loop through the crime data to check if the location is mentioned in the query
    for area in crime_data:
        if area.lower() in query:
            crime_info = crime_data[area]
            safety_report = f"Alright, let's take a look at the safety details for {area.capitalize()}."

            safety_report += f"\nIncidents reported in the past month: {crime_info['incidents']}."
            safety_report += f"\nThe most recent incident was reported on: {crime_info['last_reported']}."
            safety_report += f"\nSafety Score: {crime_info['safety_score']} out of 100."

            # Get current time and decide on warning based on time
            current_time = datetime.datetime.now()
            if current_time.hour >= 19 or current_time.hour < 6:
                safety_report += "\nIt's currently nighttime, which can be risky. Please be extra cautious if you're in this area after dark."
            else:
                safety_report += "\nDuring daytime, the area seems to be safe. Just stay alert."

            # Safety message based on score
            if crime_info["safety_score"] < 60:
                safety_report += "\nHowever, with a low safety score, it might be wise to avoid unnecessary visits here."
            else:
                safety_report += "\nBased on the safety score, this area is generally safe, but it's always good to stay aware of your surroundings."

            return safety_report
    
    return "Sorry, I couldn't find safety data for the area you mentioned. Could you check the name again?"

# Main function for user interaction
def main():
    print("Hello! I'm here to help you check the safety of various areas in Coimbatore.")
    query = input("Please ask me about any area, like 'Is Peelamedu safe?' or 'Tell me about safety in Gandhipuram': ").lower()

    safety_report = check_safety(query)
    print("\n" + safety_report)

if __name__ == "__main__":
    main()
