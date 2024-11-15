import pandas as pd


flight_data = pd.read_excel("JFK-SFO.xlsx")
weather_data = pd.read_excel("SFO.xlsx")


# Ensure Date and Scheduled_departure_time are in datetime format
flight_data['Date'] = pd.to_datetime(flight_data['Date'], format='%m/%d/%Y')
flight_data['Scheduled_arrival_time'] = pd.to_datetime(flight_data['Scheduled_arrival_time'], format='%H:%M:%S')

# Combine Date and Scheduled_departure_time columns
flight_data['Scheduled_arrival_time'] = pd.to_datetime(
    flight_data['Date'].dt.strftime('%Y-%m-%d') + ' ' + flight_data['Scheduled_arrival_time'].dt.strftime('%H:%M:%S')
)

# Ensure weather data is in datetime format
weather_data['DATE'] = pd.to_datetime(weather_data['DATE'])

# Round to the nearest hour
flight_data['Scheduled_arrival_time'] = flight_data['Scheduled_arrival_time'].dt.round('h')
weather_data['DATE'] = weather_data['DATE'].dt.round('h')

combined_data_jfk_sfo = pd.merge(
    flight_data, 
    weather_data, 
    left_on=['Destination_Airport', 'Scheduled_arrival_time'],  # Adjust column names as needed
    right_on=['STATION', 'DATE'],        # Adjust column names as needed
    how='left'  # Use 'left' to keep all flight data, even if no matching weather data
)

combined_data_jfk_sfo.drop(columns=['STATION', 'DATE'], inplace=True)
combined_data_jfk_sfo.to_excel("combined_data_jfk_sfo.xlsx", index=False)

combined_data_jfk_sfo.head()


flight_data = pd.read_excel("JFK-LAS.xlsx")
weather_data = pd.read_excel("LAS.xlsx")


# Ensure Date and Scheduled_departure_time are in datetime format
flight_data['Date'] = pd.to_datetime(flight_data['Date'], format='%m/%d/%Y')
flight_data['Scheduled_arrival_time'] = pd.to_datetime(flight_data['Scheduled_arrival_time'], format='%H:%M:%S')

# Combine Date and Scheduled_departure_time columns
flight_data['Scheduled_arrival_time'] = pd.to_datetime(
    flight_data['Date'].dt.strftime('%Y-%m-%d') + ' ' + flight_data['Scheduled_arrival_time'].dt.strftime('%H:%M:%S')
)

# Ensure weather data is in datetime format
weather_data['DATE'] = pd.to_datetime(weather_data['DATE'])

# Round to the nearest hour
flight_data['Scheduled_arrival_time'] = flight_data['Scheduled_arrival_time'].dt.round('h')
weather_data['DATE'] = weather_data['DATE'].dt.round('h')

combined_data_jfk_las = pd.merge(
    flight_data, 
    weather_data, 
    left_on=['Destination_Airport', 'Scheduled_arrival_time'],  # Adjust column names as needed
    right_on=['STATION', 'DATE'],        # Adjust column names as needed
    how='left'  # Use 'left' to keep all flight data, even if no matching weather data
)

combined_data_jfk_las.drop(columns=['STATION', 'DATE'], inplace=True)
combined_data_jfk_las.to_excel("combined_data_jfk_las.xlsx", index=False)

combined_data_jfk_las.head()
