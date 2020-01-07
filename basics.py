#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Source: https://www.datacamp.com/community/tutorials/learn-build-dash-python
Dash App Layout:
    dash_html_components has all HTML tags
    dash_core_components has the Graph class that will be used to create a graph on our layout
    Graph renders data using plotly.js
Server:
    Dash is built on top of Flask
"""

# # # Dash App Layout # # #

import dash

# Import libraries to enable us to generate HTML content with Python
import dash_core_components as dcc  # it has the Graph class
import dash_html_components as html  # it has all the HTML tags


app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5],
                    'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
