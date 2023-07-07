# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:38:29 2023

@author: thepe
"""

from dash import Dash, html, dcc

import pandas as pd
import plotly.express as px


url = 'https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv'
df = pd.read_csv(url, nrows = 3000)

df2 = df.groupby(by = 'authors').mean().reset_index()
fig = px.bar(df2, x="authors", y="  num_pages")
fig.update_layout(
    title=dict(text="Nombre moyen de pages par auteur", font=dict(size=30), automargin=True, yref='paper'),
    font_color='#119DFF',
        title_font_color='#F71016',
        xaxis_title="Auteur",
    yaxis_title="Nombre de pages")





app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H4(children='Books'),
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    ),
    
    dcc.Markdown('''                   
               
                 
               
                 Choix de l'auteur :

'''), 
    # choix auteur
    dcc.Dropdown(list(df['authors'].unique())),
   
    dcc.Markdown('''
                   
                 
              
                 
Choix de la langue :

'''), 
    # choix langue
    dcc.RadioItems(list(df['language_code'].unique()), 'eng')
])

if __name__ == '__main__':
    app.run(debug=True)
