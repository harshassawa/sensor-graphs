import pandas as pd
import plotly.express as px

# Read the text file into a pandas DataFrame
df = pd.read_csv('Temperature_Data_Log_2.txt', delim_whitespace=True, header=None, names=['SR.NO.', 'DATE', 'TIME', 'TEMPERATURE', 'BATTERY'])

# Calculate the TIME(SEC) column using the formula
df['TIME(SEC)'] = df['TIME'].apply(lambda x: pd.Timedelta(x).seconds)

# Calculate the ABS TIME(SEC) column using the formula
time_sec = df['TIME(SEC)'].values
abs_time_sec = [0]
for i in range(1, len(time_sec)):
    if time_sec[i] >= time_sec[i-1]:
        abs_time_sec.append(time_sec[i] - time_sec[i-1])
    else:
        abs_time_sec.append(24*3600 - (time_sec[i-1]))
df['ABS TIME(SEC)'] = abs_time_sec

# Calculate the ABS TIME(HRS) column using the formula
df['ABS TIME(HRS)'] = df['ABS TIME(SEC)'] / 3600

# Calculate the CUM(HRS) column using the formula
cum_hrs = [0]
for i in range(1, len(df)):
    cum_hrs.append(df.at[i, 'ABS TIME(HRS)'] + cum_hrs[i-1])
df['CUM(HRS)'] = cum_hrs

# Calculate the TTF column using the formula
df['TTF'] = df['ABS TIME(HRS)'] * df['TEMPERATURE']

# Calculate the CUM TTF column using the formula
cum_ttf = [0]
for i in range(1, len(df)):
    cum_ttf.append(df.at[i, 'TTF'] + cum_ttf[i-1])
df['CUM TTF'] = cum_ttf

# Format the TIME(SEC), ABS TIME(HRS), CUM(HRS), and TTF columns as floats with two decimal places
df['TIME(SEC)'] = df['TIME(SEC)'].apply(lambda x: '{:.2f}'.format(x))
df['ABS TIME(HRS)'] = df['ABS TIME(HRS)'].apply(lambda x: '{:.2f}'.format(x))
df['CUM(HRS)'] = df['CUM(HRS)'].apply(lambda x: '{:.2f}'.format(x))
df['TTF'] = df['TTF'].apply(lambda x: '{:.2f}'.format(x))
df['CUM TTF'] = df['CUM TTF'].apply(lambda x: '{:.2f}'.format(x))

# Convert the DataFrame to an Excel file
df.to_excel('output_file.xlsx', index=False)


fig = px.line(df, x='CUM(HRS)', y='TEMPERATURE', hover_data=['SR.NO.'])
fig.show()

fig = px.line(df, x='CUM(HRS)', y='CUM TTF', hover_data=['SR.NO.'])
fig.show()