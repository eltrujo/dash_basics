#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Source: https://www.datacamp.com/community/tutorials/learn-build-dash-python
Markdown:
    To include a block of text in the HTML
"""

# # # Markdown # # #

import dash
import dash_core_components as dcc  # it has the Graph class
import dash_html_components as html  # it has all the HTML tags

app = dash.Dash()

markdown_text = """
### Dash and Markdown
A lot of text
"""

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
    app.run_server(debug=True)