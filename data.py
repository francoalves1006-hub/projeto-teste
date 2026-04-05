import yfinance as yf
import pandas as pd
import streamlit as st

ACOES = {
    "Itaú": "ITUB4.SA",
    "Bradesco": "BBDC4.SA",
    "Nubank": "ROXO34.SA",
    "Vale": "VALE3.SA",
    "Petrobras": "PETR4.SA",
}

INICIO_2025 = "2025-01-01"


@st.cache_data(ttl=3600)
def carregar_dados():
    frames = {}
    for nome, ticker in ACOES.items():
        df = yf.download(ticker, start=INICIO_2025, auto_adjust=True, progress=False)
        if not df.empty:
            df.index = pd.to_datetime(df.index)
            frames[nome] = df
    return frames


def calcular_performance(frames):
    perf = {}
    for nome, df in frames.items():
        preco = df["Close"].squeeze()
        perf[nome] = ((preco / preco.iloc[0]) - 1) * 100
    return perf
