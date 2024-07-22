import plotly.graph_objects as go
from typing import List


class ChartTable:
    def __init__(self, values: List[int | float], labels: List[str]) -> None:
        self.values = values
        self.labels = labels

    def generate_pie_chart(self):
        fig = go.Figure(data=go.Pie(labels=self.labels, values=self.values, hole=.7))
        fig.update_layout(
            title={
                'text': 'Taxas de Rendimento Escolar',
                'font': {
                    'color': '#F4F4F4',
                    },
            },
            colorway=['#00BDA8', '#FC346E', '#F9C926'],
            annotations=[
                dict(
                    text='Taxas',
                    x=0.5,
                    y=0.5, 
                    font_size=20, 
                    showarrow=False,
                    font=dict(
                        color='#F4F4F4'
                    )
                )
            ],
        )
        fig.update_traces(opacity=0.75)
        return fig

