import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

st.set_page_config(
    page_title="Dashboard de Indicadores Econômicos do Brasil",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).parent

CAMINHO_DADOS = (
    BASE_DIR
    / "dados"
    / "simulacao_indicadores_economicos_brasil.csv"
)

CAMINHO_BANCO = (
    BASE_DIR
    / "database"
    / "indicadores_economicos.sqlite"
)


sns.set_theme(style="whitegrid")


@st.cache_data
def carregar_dados_csv():

    df = pd.read_csv(CAMINHO_DADOS)

    # Garantir que o ano seja numérico
    if "ano" in df.columns:
        df["ano"] = pd.to_numeric(
            df["ano"],
            errors="coerce"
        )

        df = df.sort_values("ano")

    return df

def criar_banco_sqlite(df):

    CAMINHO_BANCO.parent.mkdir(
        exist_ok=True
    )

    engine = create_engine(
        f"sqlite:///{CAMINHO_BANCO}"
    )

    df.to_sql(
        "indicadores_economicos",
        engine,
        if_exists="replace",
        index=False
    )

    return engine


df = carregar_dados_csv()
engine = criar_banco_sqlite(df)

st.title(
    "Dashboard de Indicadores Econômicos do Brasil"
)

st.write("""
Este dashboard apresenta uma análise dos principais indicadores
econômicos brasileiros entre 2015 e 2024.

A aplicação integra Pandas, visualização de dados, SQLAlchemy,
SQLite e Streamlit para explorar a evolução dos indicadores,
identificar períodos críticos e investigar relações entre
variáveis econômicas.
""")

st.sidebar.header("Filtros")


# Filtro de ano
if "ano" in df.columns:

    anos = sorted(
        df["ano"]
        .dropna()
        .unique()
    )

    anos_selecionados = st.sidebar.multiselect(
        "Ano",
        options=anos,
        default=anos
    )

else:

    anos_selecionados = []

df_filtrado = df.copy()

if "ano" in df.columns and anos_selecionados:

    df_filtrado = df[
        df["ano"].isin(
            anos_selecionados
        )
    ]
    
# Filtro de período

anos_disponiveis = sorted(
    df["ano"].dropna().unique()
)

ano_inicio, ano_fim = st.sidebar.slider(
    "Período",
    min_value=int(min(anos_disponiveis)),
    max_value=int(max(anos_disponiveis)),
    value=(
        int(min(anos_disponiveis)),
        int(max(anos_disponiveis))
    ),
    step=1
)

# Filtro de nível econômico

niveis = [
    "Crise",
    "Estabilidade",
    "Crescimento"
]

nivel_selecionado = st.sidebar.multiselect(
    "Nível econômico",
    options=niveis,
    default=niveis
)


# Filtro de Período

anos_disponiveis = sorted(
    df["ano"].dropna().unique()
)

ano_inicio, ano_fim = st.sidebar.slider(
    "Período",
    min_value=int(min(anos_disponiveis)),
    max_value=int(max(anos_disponiveis)),
    value=(
        int(min(anos_disponiveis)),
        int(max(anos_disponiveis))
    ),
    step=1
)

df_filtrado = df[
    (df["ano"] >= ano_inicio) &
    (df["ano"] <= ano_fim)
].copy()

if df_filtrado.empty:

    st.warning(
        "Nenhum registro encontrado para os filtros selecionados."
    )

    st.stop()





def encontrar_coluna(possiveis_nomes):

    for coluna in df.columns:

        nome = coluna.lower().strip()

        for termo in possiveis_nomes:

            if termo in nome:
                return coluna

    return None


coluna_pib = encontrar_coluna(
    ["pib"]
)

coluna_inflacao = encontrar_coluna(
    ["inflacao", "inflação", "ipca"]
)

coluna_desemprego = encontrar_coluna(
    ["desemprego", "desocupacao", "desocupação"]
)

coluna_juros = encontrar_coluna(
    ["juros", "selic"]
)

coluna_dolar = encontrar_coluna(
    ["dolar", "dólar", "cambio", "câmbio"]
)

coluna_renda = encontrar_coluna(
    ["renda", "rendimento"]
)

coluna_consumo = encontrar_coluna(
    ["consumo"]
)

coluna_crescimento = encontrar_coluna(
    ["crescimento"]
)

st.subheader(
    "Indicadores-chave de desempenho"
)

kpis = {}


if coluna_pib:
    kpis["PIB médio"] = (
        df_filtrado[coluna_pib].mean()
    )


if coluna_inflacao:
    kpis["Inflação média"] = (
        df_filtrado[coluna_inflacao].mean()
    )


if coluna_desemprego:
    kpis["Desemprego médio"] = (
        df_filtrado[coluna_desemprego].mean()
    )


if coluna_juros:
    kpis["Juros médio"] = (
        df_filtrado[coluna_juros].mean()
    )


if coluna_dolar:
    kpis["Dólar médio"] = (
        df_filtrado[coluna_dolar].mean()
    )


if coluna_crescimento:

    kpis["Crescimento médio"] = (
        df_filtrado[coluna_crescimento].mean()
    )


colunas_kpi = st.columns(
    len(kpis)
)


for coluna, (nome, valor) in zip(
    colunas_kpi,
    kpis.items()
):

    coluna.metric(
        nome,
        f"{valor:,.2f}"
    )


st.divider()

aba1, aba2, aba3, aba4, aba5 = st.tabs(
    [
        "Visão Geral",
        "Relações Econômicas",
        "Períodos Críticos",
        "Consulta SQL",
        "Dados"
    ]
)

with aba1:

    st.subheader(
        "Evolução dos indicadores econômicos"
    )


    if coluna_pib and "ano" in df.columns:

        fig, ax = plt.subplots(
            figsize=(12, 5)
        )

        sns.lineplot(
            data=df_filtrado,
            x="ano",
            y=coluna_pib,
            marker="o",
            linewidth=2.5,
            ax=ax
        )

        ax.set_title(
            "Evolução do PIB"
        )

        ax.set_xlabel("Ano")
        ax.set_ylabel("PIB")

        st.pyplot(fig)


    if coluna_inflacao and "ano" in df.columns:

        fig, ax = plt.subplots(
            figsize=(12, 5)
        )

        sns.lineplot(
            data=df_filtrado,
            x="ano",
            y=coluna_inflacao,
            marker="o",
            color="red",
            ax=ax
        )

        ax.set_title(
            "Evolução da Inflação"
        )

        ax.set_xlabel("Ano")
        ax.set_ylabel("Inflação")

        st.pyplot(fig)


    if coluna_desemprego and "ano" in df.columns:

        fig, ax = plt.subplots(
            figsize=(12, 5)
        )

        sns.lineplot(
            data=df_filtrado,
            x="ano",
            y=coluna_desemprego,
            marker="o",
            color="orange",
            ax=ax
        )

        ax.set_title(
            "Evolução do Desemprego"
        )

        ax.set_xlabel("Ano")
        ax.set_ylabel("Desemprego")

        st.pyplot(fig)

with aba2:

    st.subheader(
        "Relações entre indicadores econômicos"
    )

    if coluna_inflacao and coluna_desemprego:

        st.markdown(
            "### Inflação × Desemprego"
        )

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.scatterplot(
            data=df_filtrado,
            x=coluna_desemprego,
            y=coluna_inflacao,
            hue="ano" if "ano" in df.columns else None,
            s=120,
            ax=ax
        )

        ax.set_xlabel(
            "Taxa de desemprego"
        )

        ax.set_ylabel(
            "Inflação"
        )

        ax.set_title(
            "Relação entre Inflação e Desemprego"
        )

        st.pyplot(fig)


        correlacao = (
            df_filtrado[
                [
                    coluna_inflacao,
                    coluna_desemprego
                ]
            ]
            .corr()
            .iloc[0, 1]
        )

        st.info(
            f"Correlação entre inflação e desemprego: "
            f"{correlacao:.2f}"
        )

    if coluna_juros and coluna_consumo:

        st.markdown(
            "### Juros × Consumo"
        )

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.scatterplot(
            data=df_filtrado,
            x=coluna_juros,
            y=coluna_consumo,
            hue="ano" if "ano" in df.columns else None,
            s=120,
            ax=ax
        )

        ax.set_xlabel(
            "Taxa de juros"
        )

        ax.set_ylabel(
            "Consumo"
        )

        ax.set_title(
            "Relação entre Juros e Consumo"
        )

        st.pyplot(fig)


        correlacao = (
            df_filtrado[
                [
                    coluna_juros,
                    coluna_consumo
                ]
            ]
            .corr()
            .iloc[0, 1]
        )

        st.info(
            f"Correlação entre juros e consumo: "
            f"{correlacao:.2f}"
        )

with aba3:

    st.subheader(
        "Identificação de períodos críticos"
    )


    if coluna_crescimento:

        df_criticos = df_filtrado[
            df_filtrado[coluna_crescimento] < 0
        ]

        st.write(
            "Anos com crescimento econômico negativo:"
        )

        st.dataframe(
            df_criticos,
            use_container_width=True
        )


        if not df_criticos.empty:

            st.warning(
                f"Foram identificados "
                f"{len(df_criticos)} períodos "
                f"com crescimento negativo."
            )


    elif coluna_pib:

        df_analise = df_filtrado.copy()

        df_analise[
            "crescimento_calculado"
        ] = (
            df_analise[coluna_pib]
            .pct_change()
            * 100
        )

        df_criticos = df_analise[
            df_analise[
                "crescimento_calculado"
            ] < 0
        ]

        st.write(
            "Anos com queda do PIB:"
        )

        st.dataframe(
            df_criticos[
                [
                    "ano",
                    "crescimento_calculado"
                ]
            ],
            use_container_width=True
        )

with aba4:

    st.subheader("Consulta SQL com SQLAlchemy")

    st.write("""
    Os dados tratados foram armazenados em um banco SQLite utilizando
    SQLAlchemy. A consulta abaixo demonstra como utilizar SQL para
    calcular os indicadores econômicos.
    """)

    # Mostra as colunas realmente existentes na tabela
    st.write("Colunas disponíveis na tabela:")

    st.code(
        ", ".join(df.columns),
        language="text"
    )

    # Monta a consulta somente com colunas existentes
    consultas = []

    if coluna_pib:
        consultas.append(
            f'AVG("{coluna_pib}") AS pib_medio'
        )

    if coluna_inflacao:
        consultas.append(
            f'AVG("{coluna_inflacao}") AS inflacao_media'
        )

    if coluna_desemprego:
        consultas.append(
            f'AVG("{coluna_desemprego}") AS desemprego_medio'
        )

    if coluna_juros:
        consultas.append(
            f'AVG("{coluna_juros}") AS juros_medio'
        )

    if coluna_dolar:
        consultas.append(
            f'AVG("{coluna_dolar}") AS dolar_medio'
        )

    if consultas:

        consulta = f"""
        SELECT
            {", ".join(consultas)}
        FROM indicadores_economicos;
        """

        resultado_sql = pd.read_sql(
            consulta,
            engine
        )

        st.dataframe(
            resultado_sql,
            use_container_width=True
        )

        st.code(
            consulta,
            language="sql"
        )

    else:

        st.warning(
            "Nenhuma coluna econômica foi identificada "
            "para realizar a consulta SQL."
        )

engine = create_engine(
    f"sqlite:///{CAMINHO_BANCO}"
)

df = pd.read_sql(
    "SELECT * FROM indicadores_economicos",
    engine
)

with aba5:

    st.subheader("Dados armazenados no SQLite")

    consulta_dados = """
    SELECT *
    FROM indicadores_economicos
    """

    dados_sql = pd.read_sql(
        consulta_dados,
        engine
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Registros",
        len(dados_sql)
    )

    col2.metric(
        "Colunas",
        len(dados_sql.columns)
    )

    st.dataframe(
        dados_sql,
        use_container_width=True
    )


st.divider()

st.subheader(
    "Conclusão"
)

st.write("""
A análise permite acompanhar a evolução dos principais indicadores
econômicos brasileiros entre 2015 e 2024.

O dashboard possibilita investigar o comportamento do PIB, inflação,
desemprego, taxa de juros, câmbio, renda e consumo, além de identificar
períodos de maior crescimento, retração e instabilidade.

As análises de correlação permitem investigar relações entre variáveis
econômicas, sempre considerando que correlação não significa necessariamente
causalidade.

A integração entre Pandas, SQLAlchemy, SQLite, Matplotlib, Seaborn e
Streamlit transforma a base de dados em uma ferramenta interativa de
análise econômica.
""")
