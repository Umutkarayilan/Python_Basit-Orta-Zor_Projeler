# Proje Açıklaması: Plotly Dash kullanarak etkileşimli bir veri görselleştirme dashboard'u oluşturun.

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Örnek veri seti
df = pd.DataFrame({
    "Ülke": ["Türkiye", "Almanya", "Fransa", "İtalya", "İspanya"],
    "Nüfus": [84, 83, 67, 60, 47],
    "Yüzölçümü": [783562, 357022, 551695, 301340, 505990]
})

# Dash uygulamasını başlatır
app = dash.Dash(__name__)

# Uygulama layout'u
app.layout = html.Div([
    html.H1("Ülkelerin Nüfusu ve Yüzölçümü"),
    dcc.Dropdown(
        id='x-axis',
        options=[
            {'label': 'Nüfus', 'value': 'Nüfus'},
            {'label': 'Yüzölçümü', 'value': 'Yüzölçümü'}
        ],
        value='Nüfus'
    ),
    dcc.Graph(id='bar-chart'),
])

# Callback ile grafiği günceller
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('x-axis', 'value')]
)
def update_graph(selected_x):
    fig = px.bar(df, x='Ülke', y=selected_x, title=f'Ülkelere Göre {selected_x}')
    return fig

# Uygulamayı çalıştırır
if __name__ == '__main__':
    app.run_server(debug=True)



# Plotly Dash ile etkileşimli web tabanlı veri görselleştirme dashboard'ları oluşturulur.
# Dropdown ve Graph bileşenleri kullanılarak kullanıcı etkileşimi sağlanır.
# Callback fonksiyonları ile interaktif grafikler dinamik olarak güncellenir.
# Plotly Express ile kolayca görsel grafikler oluşturulur.