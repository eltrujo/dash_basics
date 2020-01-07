#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Source: https://www.datacamp.com/community/tutorials/learn-build-dash-python
Scatter:
    We need to import graph_objs form Plotly
    We pass as 'mode' attribute the value 'markers' to define the scatter plot
"""

# # # Generating Scatter Plots # # #

import dash
import dash_core_components as dcc  # it has the Graph class
import dash_html_components as html  # it has all the HTML tags
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/' +
    'gdp-life-exp-2007.csv')

app.layout = html.Div([
    dcc.Graph(
        id = 'life-exp-vs-gdp',
        figure = {
            'data': [
                go.Scatter(
                    x = df[df['continent'] == i]['gdp per capita'],
                    y = df[df['continent'] == i]['life expectancy'],
                    text = df[df['continent'] == i]['country'],
                    mode = 'markers',
                    opacity = 0.8,
                    marker = {
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name = i
                ) for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis = {'type': 'log', 'title': 'GDP Per Capita'},
                yaxis = {'title': 'Life Expectancy'},
                margin = {'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend = {'x': 0, 'y': 1},
                hovermode = 'closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)