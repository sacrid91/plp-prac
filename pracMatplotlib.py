import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Bar Chart: Countries & Population
# -------------------------------

# Data
countries = ['India', 'China', 'USA', 'Indonesia', 'Pakistan']
populations = np.array([1428, 1425, 331, 275, 240])  # in millions

# Create DataFrame
df_pop = pd.DataFrame({
    'Country': countries,
    'Population (M)': populations
})

# Plot
plt.figure(figsize=(10, 6))
plt.bar(df_pop['Country'], df_pop['Population (M)'], color='skyblue', edgecolor='navy', linewidth=1)
plt.title('Population of 5 Countries (in millions)', fontsize=16, fontweight='bold')
plt.xlabel('Country')
plt.ylabel('Population (Millions)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# -------------------------------
# 2. Pie Chart: Student's 24-Hour Day
# -------------------------------

# Data (in hours)
activities = ['Study', 'Sleep', 'Classes', 'Exercise', 'Meals', 'Leisure', 'Commute']
hours = np.array([6, 8, 5, 1, 2, 1.5, 0.5])  # Total = 24

# Validate total
assert np.isclose(np.sum(hours), 24), "Hours must add up to 24!"

# Create DataFrame
df_day = pd.DataFrame({
    'Activity': activities,
    'Hours': hours
})

# Plot
plt.figure(figsize=(8, 8))
colors = plt.cm.Pastel1(np.linspace(0, 1, len(activities)))
plt.pie(df_day['Hours'], labels=df_day['Activity'], autopct='%1.1f%%', startangle=90, colors=colors, explode=[0.05]*len(activities))
plt.title("How a Student Spends 24 Hours", fontsize=16, fontweight='bold')
plt.show()

# -------------------------------
# 3. Line Chart: Temperature During the Day
# -------------------------------

# Time points (4 key times)
times = ['Morning (6 AM)', 'Noon (12 PM)', 'Evening (6 PM)', 'Night (12 AM)']
temperature_c = np.array([18, 28, 24, 20])  # in Celsius

# Add some smoothness with NumPy interpolation (simulate hourly data)
time_numeric = np.arange(0, len(times))
time_smooth = np.linspace(0, len(times)-1, 100)
temp_smooth = np.interp(time_smooth, time_numeric, temperature_c)  # Linear interpolation

# Create DataFrame
df_temp = pd.DataFrame({
    'Time': times,
    'Temperature (°C)': temperature_c
})

# Plot
plt.figure(figsize=(10, 6))
plt.plot(time_smooth, temp_smooth, color='orange', linewidth=2, label='Temperature')
plt.scatter(time_numeric, temperature_c, color='red', zorder=5)  # Mark actual points
plt.xticks(time_numeric, times, rotation=15)
plt.title('Temperature Changes During the Day', fontsize=16, fontweight='bold')
plt.ylabel('Temperature (°C)')
plt.xlabel('Time of Day')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()


# -------------------------------
# Optional: Display DataFrames
# -------------------------------
print("📊 Country Populations:")
print(df_pop)

print("\n⏰ Student Daily Routine:")
print(df_day)

print("\n🌡️  Temperature Data:")
print(df_temp)