import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import pandas as pd


ndvi_data = {
    'Antarctica': 0.23,
    'Australia': 0.42,
    'Asia': 0.55,
    'Africa': 0.36,
    'Europe': 0.62,
    'North America': 0.52,
    'South America': 0.58,


}


df = pd.DataFrame(list(ndvi_data.items()), columns=['Continent', 'NDVI'])


plt.figure(figsize=(10, 5))
plt.bar(df['Continent'], df['NDVI'], color='green')
plt.xlabel('Continent')
plt.ylabel('NDVI')
plt.title('Average NDVI by Continent')
plt.ylim(0, 0.9)
plt.show()

data = [
    {"Continent": "Asia", "Years": 2018, "Mean NDVI": 0.5642, "Standard Deviation": 0.1319},
    {"Continent": "Asia", "Years": 2019, "Mean NDVI": 0.5634, "Standard Deviation": 0.1352},
    {"Continent": "Asia", "Years": 2020, "Mean NDVI": 0.5566, "Standard Deviation": 0.1392},
    {"Continent": "Australia", "Years": 2018, "Mean NDVI": 0.4250, "Standard Deviation": 0.2138},
    {"Continent": "Australia", "Years": 2019, "Mean NDVI": 0.4209, "Standard Deviation": 0.2107},
    {"Continent": "Australia", "Years": 2020, "Mean NDVI": 0.4177, "Standard Deviation": 0.2089},
    {"Continent": "Africa", "Years": 2018, "Mean NDVI": 0.3534, "Standard Deviation": 0.1452},
    {"Continent": "Africa", "Years": 2019, "Mean NDVI": 0.3567, "Standard Deviation": 0.1421},
    {"Continent": "Africa", "Years": 2020, "Mean NDVI": 0.3695, "Standard Deviation": 0.1400},
    {"Continent": "Europe", "Years": 2018, "Mean NDVI": 0.5211, "Standard Deviation": 0.1098},
    {"Continent": "Europe", "Years": 2019, "Mean NDVI": 0.5299, "Standard Deviation": 0.1075},
    {"Continent": "Europe", "Years": 2020, "Mean NDVI": 0.5341, "Standard Deviation": 0.1053},
    {"Continent": "Antarctica", "Years": 2018, "Mean NDVI": 0.2301, "Standard Deviation": 0.1912},
    {"Continent": "Antarctica", "Years": 2019, "Mean NDVI": 0.2322, "Standard Deviation": 0.1933},
    {"Continent": "Antarctica", "Years": 2020, "Mean NDVI": 0.2344, "Standard Deviation": 0.1954},
    {"Continent": "North America", "Years": 2018, "Mean NDVI": 0.6243, "Standard Deviation": 0.1555},
    {"Continent": "North America", "Years": 2019, "Mean NDVI": 0.6272, "Standard Deviation": 0.1532},
    {"Continent": "North America", "Years": 2020, "Mean NDVI": 0.6300, "Standard Deviation": 0.1509},
    {"Continent": "South America", "Years": 2018, "Mean NDVI": 0.5897, "Standard Deviation": 0.1741},
    {"Continent": "South America", "Years": 2019, "Mean NDVI": 0.5918, "Standard Deviation": 0.1719},
    {"Continent": "South America", "Years": 2020, "Mean NDVI": 0.5940, "Standard Deviation": 0.1697}
]

# Create DataFrame
df = pd.DataFrame(data)

# Set up the figure and axis
fig, ax = plt.subplots(2, 1, figsize=(10, 12), sharex=True)

# Plot Mean NDVI for each continent
for continent in df['Continent'].unique():
    subset = df[df['Continent'] == continent]
    ax[0].plot(subset['Years'], subset['Mean NDVI'], marker='o', label=continent)

# Plot Standard Deviation for each continent
for continent in df['Continent'].unique():
    subset = df[df['Continent'] == continent]
    ax[1].plot(subset['Years'], subset['Standard Deviation'], marker='o', label=continent)

# Setting titles, labels and legend
ax[0].set_title('Mean NDVI by Year and Continent')
ax[0].set_ylabel('Mean NDVI')
ax[0].legend()

ax[1].set_title('Standard Deviation by Year and Continent')
ax[1].set_ylabel('Standard Deviation')
ax[1].set_xlabel('Years')
ax[1].legend()

# Display the plot
plt.tight_layout()
plt.show()

data = {
    'Continent': ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia', 'Antarctica'],
    'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Freshwater_Content_Percent': [0.03, 0.12, 0.07, 0.1, 0.1, 0.02, 0.56],
    'NDVI': [0.36, 0.55, 0.62, 0.52, 0.58, 0.42, 0.23],
    'St_Dev': [0.1452, 0.1352, 0.1075, 0.1532, 0.1719, 0.2138, 0.0933]
}
df = pd.DataFrame(data)

#graphs the correltaion between freshwater and ndvi
def analyze_freshwater_effect(df):
    correlation = df['Freshwater_Content_Percent'].corr(df['NDVI'])
    print(f"Correlation between freshwater content and NDVI: {correlation}")
    df.plot(kind='scatter', x='NDVI', y='Freshwater_Content_Percent')
    plt.title('Freshwater Content vs NDVI')
    plt.show()

#compares freshwater with each continent
def show_freshwater(df):
  plt.title('Freshwater Content % Per Continent')
  plt.pie(df['Freshwater_Content_Percent'], labels = df['Continent'])
  plt.show()

#determines how likely a continent's NDVI will fluctuate (ex: seasonal change)
def grade_std_deviation(df):
    volatility_grades = []
    for val in df['St_Dev']:
        if val > 0.2:
            volatility_grades.append('Volatile')
        elif 0.1 < val <= 0.2:
            volatility_grades.append('Moderate')
        else:
            volatility_grades.append('Stable')

    df['Volatility_Grade'] = volatility_grades

    print(df[['Continent', 'St_Dev', 'Volatility_Grade']])

grade_std_deviation(pd.DataFrame(data))

show_freshwater(df)

analyze_freshwater_effect(df)
