import plotly.graph_objects as go

CORES = {
    "Itaú": "#FF6B00",
    "Bradesco": "#CC0000",
    "Nubank": "#820AD1",
    "Vale": "#007A4D",
    "Petrobras": "#009C3B",
}


def grafico_cotacao(frames):
    fig = go.Figure()
    for nome, df in frames.items():
        preco = df["Close"].squeeze()
        fig.add_trace(go.Scatter(
            x=preco.index,
            y=preco.values,
            name=nome,
            line=dict(color=CORES.get(nome), width=2),
            hovertemplate=f"<b>{nome}</b><br>Data: %{{x|%d/%m/%Y}}<br>Preço: R$ %{{y:.2f}}<extra></extra>",
        ))
    fig.update_layout(
        title="Cotação Histórica 2025 (Preço de Fechamento)",
        xaxis_title="Data",
        yaxis_title="Preço (R$)",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_dark",
    )
    return fig


def grafico_performance(perf):
    fig = go.Figure()
    for nome, serie in perf.items():
        fig.add_trace(go.Scatter(
            x=serie.index,
            y=serie.values,
            name=nome,
            line=dict(color=CORES.get(nome), width=2),
            hovertemplate=f"<b>{nome}</b><br>Data: %{{x|%d/%m/%Y}}<br>Performance: %{{y:.2f}}%<extra></extra>",
        ))
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    fig.update_layout(
        title="Performance no Ano 2025 (%)",
        xaxis_title="Data",
        yaxis_title="Retorno (%)",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_dark",
    )
    return fig


def grafico_volume(frames, acao_selecionada):
    df = frames[acao_selecionada]
    volume = df["Volume"].squeeze()
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=volume.index,
        y=volume.values,
        name=acao_selecionada,
        marker_color=CORES.get(acao_selecionada),
        hovertemplate=f"<b>{acao_selecionada}</b><br>Data: %{{x|%d/%m/%Y}}<br>Volume: %{{y:,.0f}}<extra></extra>",
    ))
    fig.update_layout(
        title=f"Volume Negociado — {acao_selecionada} 2025",
        xaxis_title="Data",
        yaxis_title="Volume",
        template="plotly_dark",
    )
    return fig
