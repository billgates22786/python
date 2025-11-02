
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
df=pd.DataFrame(
    {
        'Location':['Canada','New-York','Austin','Canada'],
        'Price':[30000,20000,10000,670000]
    }
) 
app=dash.Dash(__name__)
app.title='Property Prices'
app.layout = html.Div([
    html.H2("Property Prices Dashboard",style={'textAlign':'center'}),

    dcc.Dropdown(
        id='Prices-Dropdown',
        options=[{'label':Location,'value':Location} for Location in df['Location'].unique()],
        placeholder="Please select from below",
        clearable=False 
    ),
    dcc.Graph(id='Location-graph')
])

@app.callback(
    Output('Location-graph','figure'),
    Input('Location dropdown','value')
)

def update_chart(selected):
  filtered_df=df[df['Location']== selected]
  summary=filtered_df.groupby('Location', as_index=False)['Price'].sum()

  fig= px.bar(summary,x='Location',y='Price', title=f"Total sales for {selected}")
  return fig
  # app.run(mode='inline')
  if __name__ == '__main__':
    app.run(debug=True)