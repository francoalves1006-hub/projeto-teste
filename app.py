import streamlit as st
from data import carregar_dados, calcular_performance, ACOES
from charts import grafico_cotacao, grafico_performance, grafico_volume

st.set_page_config(
    page_title="Dashboard de Ações 2025",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Dashboard de Ações Brasileiras — 2025")
st.caption("Itaú · Bradesco · Nubank · Vale · Petrobras")

with st.spinner("Carregando dados do mercado..."):
    frames = carregar_dados()
    perf = calcular_performance(frames)

# Cards de resumo
st.subheader("Resumo")
cols = st.columns(len(frames))
for col, (nome, df) in zip(cols, frames.items()):
    preco = df["Close"].squeeze()
    cotacao_atual = preco.iloc[-1]
    variacao_ano = ((preco.iloc[-1] / preco.iloc[0]) - 1) * 100
    maxima = preco.max()
    minima = preco.min()
    with col:
        st.metric(
            label=nome,
            value=f"R$ {cotacao_atual:.2f}",
            delta=f"{variacao_ano:+.2f}% no ano",
        )
        st.caption(f"Máx: R$ {maxima:.2f} | Mín: R$ {minima:.2f}")

st.divider()

# Gráfico de cotação
st.plotly_chart(grafico_cotacao(frames), use_container_width=True)

# Gráfico de performance
st.plotly_chart(grafico_performance(perf), use_container_width=True)

st.divider()

# Gráfico de volume
st.subheader("Volume Negociado")
acao_selecionada = st.selectbox("Selecione a ação:", list(frames.keys()))
st.plotly_chart(grafico_volume(frames, acao_selecionada), use_container_width=True)
