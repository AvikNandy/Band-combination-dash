import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import itertools

# Load data from CSV file
data = pd.read_csv('GPT_test.csv')

# Get all combinations of band ratios
bands = ['Ultra Blue', 'Blue', 'Green', 'Red', 'VNIR1', 'VNIR2', 'VNIR3', 'VNIR4', 'VNIR5', 'SWIR1', 'SWIR3', 'SWIR4']
combos = list(itertools.combinations(bands, 2))

# Create the app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Band Ratio vs. CHL(field)"),
    html.Div([
        html.Div([
            html.Label("Select Band Combination 1:"),
            dcc.Dropdown(
                id="band-combo-dropdown1",
                options=[{"label": "/".join(combo), "value": combo} for combo in combos],
                value=combos[0]
            ),
            dcc.Graph(id="scatter-plot1"),
        ], className="six columns"),
        html.Div([
            html.Label("Select Band Combination 2:"),
            dcc.Dropdown(
                id="band-combo-dropdown2",
                options=[{"label": "/".join(combo), "value": combo} for combo in combos],
                value=combos[1]
            ),
            dcc.Graph(id="scatter-plot2"),
        ], className="six columns"),
    ], className="row"),
    html.Div([
        html.Div([
            html.Label("Select Band Combination 3:"),
            dcc.Dropdown(
                id="band-combo-dropdown3",
                options=[{"label": "/".join(combo), "value": combo} for combo in combos],
                value=combos[2]
            ),
            dcc.Graph(id="scatter-plot3"),
        ], className="six columns"),
        html.Div([
            html.Label("Select Band Combination 4:"),
            dcc.Dropdown(
                id="band-combo-dropdown4",
                options=[{"label": "/".join(combo), "value": combo} for combo in combos],
                value=combos[3]
            ),
            dcc.Graph(id="scatter-plot4"),
        ], className="six columns"),
    ], className="row"),
], className="container")


# Define the callback functions
@app.callback(
    dash.dependencies.Output("scatter-plot1", "figure"),
    [dash.dependencies.Input("band-combo-dropdown1", "value")]
)
def update_scatter_plot1(combo):
    x = data[combo[0]] / data[combo[1]]
    y = data['CHL(field)']

    fig = px.scatter(x=x, y=y)
    fig.update_layout(
        title=f"{combo[0]} / {combo[1]} vs. CHL(field)",
        xaxis_title=f"{combo[0]} / {combo[1]}",
        yaxis_title="CHL(field)"
    )
    return fig

@app.callback(
    dash.dependencies.Output("scatter-plot2", "figure"),
    [dash.dependencies.Input("band-combo-dropdown2", "value")]
)
def update_scatter_plot2(combo):
    x = data[combo[0]] / data[combo[1]]
    y = data['CHL(field)']

    fig = px.scatter(x=x, y=y)
    fig.update_layout(
        title=f"{combo[0]} / {combo[1]} vs. CHL(field)",
        xaxis_title=f"{combo[0]} / {combo[1]}",
        yaxis_title="CHL(field)"
    )
    return fig

@app.callback(
    dash.dependencies.Output("scatter-plot3", "figure"),
    [dash.dependencies.Input("band-combo-dropdown3", "value")]
)
def update_scatter_plot3(combo):
    x = data[combo[0]] / data[combo[1]]
    y = data['CHL(field)']

    fig = px.scatter(x=x, y=y)
    fig.update_layout(
        title=f"{combo[0]} / {combo[1]} vs. CHL(field)",
        xaxis_title=f"{combo[0]} / {combo[1]}",
        yaxis_title="CHL(field)"
    )
    return fig

@app.callback(
    dash.dependencies.Output("scatter-plot4", "figure"),
    [dash.dependencies.Input("band-combo-dropdown4", "value")]
)
def update_scatter_plot4(combo):
    x = data[combo[0]] / data[combo[1]]
    y = data['CHL(field)']

    fig = px.scatter(x=x, y=y)
    fig.update_layout(
        title=f"{combo[0]} / {combo[1]} vs. CHL(field)",
        xaxis_title=f"{combo[0]} / {combo[1]}",
        yaxis_title="CHL(field)"
    )
    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=False)

