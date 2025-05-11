import plotly.graph_objects as go

def generate_plots(scores, glc, bert, dic):
    shifts, values = zip(*scores)
    line_chart = go.Figure()
    line_chart.add_trace(go.Scatter(x=shifts, y=values, mode='lines+markers', name='Pontuação'))
    line_chart.update_layout(title="Pontuação por Shift", xaxis_title="Shift", yaxis_title="Score")

    pie_chart = go.Figure(data=[go.Pie(labels=['GLC', 'BERT', 'Dicionário'], values=[glc, bert, dic])])
    pie_chart.update_layout(title="Distribuição de Confiança por Validação")

    return line_chart, pie_chart