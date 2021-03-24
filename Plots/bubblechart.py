import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Creating mean, min, max of temperature group by month column
new_df = df.groupby(['month']).agg(
    {'actual_mean_temp' : 'mean', 'average_min_temp' : 'min', 'average_max_temp' : 'max'}).reset_index()

# Preparing data
data = [
     go.Scatter(x=new_df['average_min_temp'],
                y=new_df['average_max_temp'],
                text=new_df['month'],
                mode='markers',
                marker=dict(size=new_df['actual_mean_temp'] /
                            0.5,color=new_df['actual_mean_temp'] / 0.5, showscale=True))
    ]

# Preparing layout
layout = go.Layout(title="Average min and max temperature of each month in weather statistics", xaxis_title="Average"
                                                                     " min temperature",
                   yaxis_title="Average max temperature", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')