# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the App

```bash
pip install -r requirements.txt
streamlit run app.py
```

## GitHub Auto-Sync

This project is linked to a GitHub repository. Every time Claude Code modifies a file, the changes are automatically committed and pushed via a `PostToolUse` hook configured in `.claude/settings.local.json`.

**To set up the remote (first time only):**
```bash
git remote add origin https://github.com/FrancoJR/<repo-name>.git
git branch -M main
git push -u origin main
```

**Hook behavior:** After every Edit/Write tool call, Claude runs:
```bash
git add -A && git commit -m "auto: <timestamp>" && git push
```

If push fails (e.g., no remote configured), the hook exits silently — your local git history is still saved.

## Architecture

This is a single-page Streamlit dashboard tracking Brazilian stock prices (Itaú, Bradesco, Nubank, Vale, Petrobras) for 2025.

**Module responsibilities:**
- `data.py` — fetches OHLCV data from Yahoo Finance via `yfinance`, caches results for 1 hour with `@st.cache_data`. Defines `ACOES` (ticker map) and `INICIO_2025`. The two functions are `carregar_dados()` → `dict[str, DataFrame]` and `calcular_performance(frames)` → `dict[str, Series]`.
- `charts.py` — pure Plotly functions that receive the data dicts and return `go.Figure` objects. Uses the `CORES` dict for brand colors per company. Three chart types: line (cotação), line (performance %), bar (volume).
- `app.py` — Streamlit entry point. Calls data functions, renders summary metric cards, then embeds the three charts.
