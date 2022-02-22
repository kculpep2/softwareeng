import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['month'] = pd.to_datetime(df['date'])

df = df.groupby(['month']).agg({'actual_max_temp': 'max'}).reset_index()

# Preparing data: setting x to month and y to the temp data. the line will show fluctuation of max temp
data = [go.Scatter(x=df['month'], y=df['actual_max_temp'], mode='lines', name='temp')]

# Preparing layout
layout = go.Layout(title='Max Temperature by Month (In Alphabetical Order) 2014-2015', xaxis_title='Month',
                   yaxis_title='Temperature')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart_weather.html')