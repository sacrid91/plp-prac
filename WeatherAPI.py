# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

print("🌍 Welcome to the Weather Data Analysis Tool!\n")

# -------------------------------
# 1. NumPy: Create array 1-10 and calculate mean
# -------------------------------
numbers = np.arange(1, 11)  # [1, 2, ..., 10]
mean_value = np.mean(numbers)
print(f"🔢 NumPy: Mean of numbers 1 to 10 = {mean_value}\n")

# -------------------------------
# 2. Fetch Real Weather Data from Open-Meteo API (Free & No Key Needed)
# -------------------------------
print("📡 Fetching weather data for Nairobi, Kenya...\n")

# Public weather API (no API key required)
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": -1.2833,   # Nairobi
    "longitude": 36.8167,
    "hourly": "temperature_2m",
    "forecast_days": 1     # Only today
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Check if request succeeded
    data = response.json()

    # Extract hourly temperatures
    times = data['hourly']['time'][:24]  # Next 24 hours
    temps = data['hourly']['temperature_2m'][:24]

    print(f"✅ Success! Retrieved {len(temps)} hourly temperature readings.\n")

except requests.exceptions.RequestException as e:
    print(f"❌ Error fetching data: {e}")
    print("Using sample data instead for learning...\n")
    # Fallback sample data
    times = [f"{h:02d}:00" for h in range(24)]
    temps = np.random.normal(22, 3, 24).round(1)  # Simulated temps

# -------------------------------
# 3. Load into Pandas DataFrame and Show Summary
# -------------------------------
df = pd.DataFrame({
    'Time': times,
    'Temperature (°C)': temps
})

print("📊 Weather Data Sample (First 5 Rows):")
print(df.head())

print("\n📈 Summary Statistics:")
print(df.describe())

# Bonus: Use NumPy on DataFrame column
max_temp = np.max(temps)
min_temp = np.min(temps)
avg_temp = np.mean(temps)
print(f"\n🌡️  Today's Forecast:")
print(f"   → High: {max_temp:.1f}°C")
print(f"   → Low:  {min_temp:.1f}°C")
print(f"   → Avg:  {avg_temp:.1f}°C")

# -------------------------------
# 4. Plot Temperature Trend with Matplotlib
# -------------------------------
plt.figure(figsize=(12, 6))
plt.plot(df['Time'], df['Temperature (°C)'], marker='o', linestyle='-', color='tab:blue', linewidth=2)
plt.title('Hourly Temperature Forecast for Nairobi', fontsize=16, fontweight='bold')
plt.xlabel('Time of Day')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Add horizontal lines for min, avg, max
plt.axhline(avg_temp, color='red', linestyle='--', alpha=0.6, label=f'Average ({avg_temp:.1f}°C)')
plt.axhline(max_temp, color='darkred', linestyle=':', alpha=0.6, label=f'Max ({max_temp:.1f}°C)')
plt.axhline(min_temp, color='navy', linestyle=':', alpha=0.6, label=f'Min ({min_temp:.1f}°C)')
plt.legend()

plt.show()

# -------------------------------
# 5. Bonus: Save to CSV (Real-world workflow)
# -------------------------------
df.to_csv('nairobi_weather_today.csv', index=False)
print("\n💾 Data saved to 'nairobi_weather_today.csv'")

print("\n🎉 Learning Complete! You've practiced:")
print("   • requests → Fetch real data from web")
print("   • pandas → Load and analyze data")
print("   • numpy → Calculate stats")
print("   • matplotlib → Visualize trends")
print("   • Error handling → Robust code")