import pandas as pd

flight_data = pd.read_excel("flight/2014-2023.xlsx")
weather_data = pd.read_excel("weather/JFK.xlsx")

# Ensure Date column is in datetime format
flight_data['Date'] = pd.to_datetime(flight_data['Date'], format='%m/%d/%Y')

# Combine Date and Scheduled_departure_time columns
flight_data['Scheduled_departure_time'] = pd.to_datetime(
    flight_data['Date'].dt.strftime('%Y-%m-%d') + ' ' + flight_data['Scheduled_departure_time'].dt.strftime('%H:%M:%S')
)
weather_data['DATE'] = pd.to_datetime(weather_data['DATE'])

flight_data['Scheduled_departure_time'] = flight_data['Scheduled_departure_time'].dt.round('h')

weather_data['DATE'] = weather_data['DATE'].dt.round('h')

combined_data = pd.merge(
    flight_data, 
    weather_data, 
    left_on=['Origin Airport', 'Scheduled_departure_time'],  # Adjust column names as needed
    right_on=['STATION', 'DATE'],        # Adjust column names as needed
    how='left'  # Use 'left' to keep all flight data, even if no matching weather data
)

combined_data.drop(columns=['STATION', 'DATE'], inplace=True)

print("Missing values in combined dataset:\n", combined_data.isnull().sum())

# Optionally, handle missing values if necessary
# Here we're using forward fill as an example; adjust based on your needs
combined_data.fillna(method='ffill', inplace=True)

# Step 6: Save the Combined Data (Optional)
# Save the final combined dataset to a new Excel file
combined_data.to_excel("combined_flight_weather_data.xlsx", index=False)

# Display the first few rows of the combined data to verify
combined_data.head()
