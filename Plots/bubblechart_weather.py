import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')


# Preparing data
data = [
    go.Scatter(x=df['average_min_temp'],
               y=df['average_max_temp'],
               text=df['month'],
               mode='markers',
               marker=dict(size=df['average_max_temp'],color=df['average_min_temp'], showscale=True))
]

# Preparing layout
layout = go.Layout(title='Average Min and Max Temperature Over 2014-2015', xaxis_title='Min Temp',
                   yaxis_title='Max Temp', hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart_weather.html')