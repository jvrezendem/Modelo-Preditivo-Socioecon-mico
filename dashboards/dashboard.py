import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent  # volta da pasta dashboards/ para a raiz
DATA_DIR = BASE_DIR / "data"

st.set_page_config(
    page_title="Dashboard Socioeconômico MG",
    layout="wide"
)

st.title("Análise Socioeconômica e Predição do IDH")
st.markdown("Este dashboard apresenta os **resultados finais** do modelo de Machine Learning desenvolvido para avaliar e prever o **IDH das Regiões Integradas de Segurança Pública (RISP)**.")

dfPredict = pd.read_csv(DATA_DIR/"predict.csv", sep = ";")
dfLofo = pd.read_csv(DATA_DIR/"importance_lofo.csv", sep = ";")
dfPremut = pd.read_csv(DATA_DIR/"importnce_permut.csv", sep = ";")
dfImportance = pd.read_csv(DATA_DIR/"dataset_importance.csv", sep = ";")

with open(DATA_DIR/"metrics.json") as f:
    metrics = json.load(f)


st.subheader("Métricas do Modelo (Cross validation)")

col1, col2, col3 = st.columns(3)

col1.metric(
    "R² médio (Cross validation)",
    f"{metrics['R2_mean']:.2f}",
    f"± {metrics['R2_std']:.2f}"
)


col2.metric(
    "MAE médio",
    f"{metrics['MAE_mean']:.4f}",
    f"± {metrics['MAE_std']:.4f}"
)

col3.metric("Modelo", metrics["modelo"])

st.subheader("Métricas do Modelo (Split Fixo)")

col1, col2, col3 = st.columns(3)

col1.metric(
    "R² ",
    f"{metrics['R2_splitFixo']:.2f}",
)


col2.metric(
    "MAE",
    f"{metrics['MAE_splitFixo']:.4f}",
)

col3.metric("Modelo", metrics["modelo"])

st.subheader("Qualidade das previsões")

fig, ax = plt.subplots(figsize=(8,6))

ax.scatter(dfPredict["IDH real"], dfPredict["Previsão(Cross-Validation)"], label="Cross-Validation")
ax.scatter(dfPredict["IDH real"], dfPredict["Previsão(Split Fixo)"], label="Split Fixo")

min_val = min(dfPredict["IDH real"].min(),
              dfPredict["Previsão(Cross-Validation)"].min(),
              dfPredict["Previsão(Split Fixo)"].min())

max_val = max(dfPredict["IDH real"].max(),
              dfPredict["Previsão(Cross-Validation)"].max(),
              dfPredict["Previsão(Split Fixo)"].max())

ax.plot([min_val, max_val], [min_val, max_val], "r--", label="Previsão perfeita")

ax.set_xlabel("IDH Real")
ax.set_ylabel("IDH Previsto")
ax.legend()
ax.grid(True)   

st.pyplot(fig)

st.subheader("Importância das Variáveis")

st.text("Pelo método LOFO")

fig2, ax2 = plt.subplots(figsize=(8,6))

ax2.barh(dfLofo["Variável"], dfLofo["Diferença de Erro"])
ax2.axvline(0, color='k', linestyle='--')
ax2.set_xlabel("∆MAE")
ax2.set_title("Impacto das variáveis socioeconômicas com base na técnica LOFO")

st.pyplot(fig2)

st.text("Pelo método de Importância por Permutação")

fig3, ax3 = plt.subplots(figsize=(8,6))

ax3.barh(dfPremut["Variável"], dfPremut["Diferença de mae (Permutação)"], color='green')
ax3.axvline(0, color='k', linestyle='--')
ax3.set_xlabel("∆MAE")
ax3.set_title("Impacto das variáveis socioeconômicas com base na técnica de importância por Permutação")

st.pyplot(fig3)

st.text("Pela média dos dois métodos")

fig4, ax4 = plt.subplots(figsize=(8,6))

ax4.barh(dfImportance["Variável"], dfImportance["Média ∆MAE (Importância)"], color='orange')
ax4.axvline(0, color='k', linestyle='--')
ax4.set_xlabel("∆MAE")
ax4.set_title("Impacto das variáveis socioeconômicas com base na média dos dois métodos")

st.pyplot(fig4)

st.subheader("Insights")

st.markdown("Entre os modelos de aprendizado de máquina avaliados neste estudo, o Ridge Regressor apresentou o melhor desempenho preditivo para o conjunto de dados analisado, tanto em termos de coeficiente de determinação (R² médio) quanto de erro médio absoluto (MAE). Esse resultado reforça a adequação de modelos de regressão regularizados para bases de dados reduzidas, nas quais o risco de sobreajuste é elevado.")

st.markdown("A análise de importância das variáveis, conduzida por meio dos métodos Leave-One-Feature-Out (LOFO) e Importância por Permutação, revelou que a educação é o fator de maior relevância na determinação do Índice de Desenvolvimento Humano (IDH) das regiões analisadas. Esse resultado pode ser observado pelo aumento expressivo do erro de previsão quando a variável taxa de analfabetismo é removida ou permutada, indicando que a informação contida nessa variável é essencial para o desempenho do modelo.")

st.markdown("Em seguida, os fatores relacionados à saúde, representados pela expectativa de vida, e à renda, expressa pela renda média da população, também demonstraram elevada importância socioeconômica, uma vez que a degradação dessas variáveis resultou em perdas significativas na capacidade preditiva do modelo.")

st.markdown("Esses achados sugerem que, no contexto analisado, políticas públicas voltadas à educação possuem potencial impacto estrutural mais profundo sobre o desenvolvimento humano, sendo complementadas de forma relevante por ações na área da saúde e da distribuição de renda. Ressalta-se, entretanto, que os resultados refletem associações estatísticas aprendidas pelo modelo, não implicando necessariamente relações de causalidade direta.")