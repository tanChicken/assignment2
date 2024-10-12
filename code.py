import pandas as pd

# Your initial CSV data can be read using pandas
df = pd.read_csv("map_one.csv")

# Adding latitude and longitude manually
coords = {
    "United States of America": (37.0902, -95.7129),
    "United Kingdom": (55.3781, -3.4360),
    "France": (46.6034, 1.8883),
    "Japan": (36.2048, 138.2529),
    "Switzerland": (46.8182, 8.2275),
    "Australia": (-25.2744, 133.7751),
    "Canada": (56.1304, -106.3468),
    "Singapore": (1.3521, 103.8198),
    "Vietnam": (14.0583, 108.2772),
    "Cambodia": (12.5657, 104.9910),
    "New Zealand": (-40.9006, 174.8860),
    "Myanmar": (21.9162, 95.9560),
    "India": (20.5937, 78.9629),
    "Pakistan": (30.3753, 69.3451),
    "Nepal": (28.3949, 84.1240),
    "Thailand": (15.8700, 100.9925),
    "Philippines": (12.8797, 121.7740),
    "Taiwan": (23.6978, 120.9605),
    "South Korea": (35.9078, 127.7669),
    "Indonesia": (-0.7893, 113.9213),
    "China": (35.8617, 104.1954),
    "Brunei": (4.5353, 114.7277)
}

# Apply coordinates to the dataframe
df["Latitude"] = df["Country_Name"].map(lambda x: coords.get(x, (None, None))[0])
df["Longitude"] = df["Country_Name"].map(lambda x: coords.get(x, (None, None))[1])

# Saving the updated dataframe to a new CSV
df.to_csv("map_one.csv", index=False)