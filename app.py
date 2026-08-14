import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Vehicle Dashboard",
    page_icon="🚗",
    layout="wide"
)

# Carregar os dados
car_data = pd.read_csv("vehicles_us_clean.csv")

# Título
st.title("🚗 Vehicle Dashboard")
st.write("Análise de anúncios de veículos usados")

# Visão geral
st.subheader("Visão geral dos dados")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total de veículos",
        f"{len(car_data):,}"
    )

with col2:
    st.metric(
        "Preço médio",
        f"${car_data['price'].mean():,.0f}"
    )

with col3:
    st.metric(
        "Ano médio",
        f"{car_data['model_year'].mean():.0f}"
    )

# Linha divisória
st.divider()

# Filtros
st.subheader("Filtros")

col1, col2, col3 = st.columns(3)

with col1:
    condition_selected = st.multiselect(
        "Condition",
        options=sorted(car_data["condition"].unique()),
        default=sorted(car_data["condition"].unique())
    )

with col2:
    type_selected = st.multiselect(
        "Type",
        options=sorted(car_data["type"].unique()),
        default=sorted(car_data["type"].unique())
    )

with col3:
    fuel_selected = st.multiselect(
        "Fuel",
        options=sorted(car_data["fuel"].unique()),
        default=sorted(car_data["fuel"].unique())
    )

# Aplicar filtros
filtered_data = car_data[
    car_data["condition"].isin(condition_selected)
    & car_data["type"].isin(type_selected)
    & car_data["fuel"].isin(fuel_selected)
]

st.write(
    f"**{len(filtered_data):,} veículos** correspondem aos filtros selecionados."
)

# Gráfico 1 - Distribuição dos preços
st.subheader("Distribuição dos preços")

fig_price = px.histogram(
    filtered_data,
    x="price",
    nbins=50,
    title="Distribuição dos preços dos veículos",
    labels={
        "price": "Price",
        "count": "Quantidade de veículos"
    }
)

st.plotly_chart(fig_price, use_container_width=True)

# Gráfico 2 - Ano do modelo x preço
st.subheader("Relação entre ano do modelo e preço")

fig_year = px.scatter(
    filtered_data,
    x="model_year",
    y="price",
    title="Relação entre ano do modelo e preço",
    labels={
        "model_year": "Model Year",
        "price": "Price"
    }
)

st.plotly_chart(fig_year, use_container_width=True)

# Gráfico 3 - Quilometragem x preço
st.subheader("Relação entre quilometragem e preço")

fig_odometer = px.scatter(
    filtered_data,
    x="odometer",
    y="price",
    title="Relação entre quilometragem e preço",
    labels={
        "odometer": "Odometer",
        "price": "Price"
    }
)

st.plotly_chart(fig_odometer, use_container_width=True)

# Gráfico 4 - Preço por condição
st.subheader("Distribuição dos preços por condição do veículo")

fig_condition = px.box(
    filtered_data,
    x="condition",
    y="price",
    title="Distribuição dos preços por condição",
    labels={
        "condition": "Condition",
        "price": "Price"
    }
)

st.plotly_chart(fig_condition, use_container_width=True)

# Gráfico 5 - Preço por tipo
st.subheader("Distribuição dos preços por tipo de veículo")

fig_type = px.box(
    filtered_data,
    x="type",
    y="price",
    title="Distribuição dos preços por tipo de veículo",
    labels={
        "type": "Type",
        "price": "Price"
    }
)

st.plotly_chart(fig_type, use_container_width=True)

# Gráfico 6 - Preço por combustível
st.subheader("Distribuição dos preços por tipo de combustível")

fig_fuel = px.box(
    filtered_data,
    x="fuel",
    y="price",
    title="Distribuição dos preços por tipo de combustível",
    labels={
        "fuel": "Fuel Type",
        "price": "Price"
    }
)

st.plotly_chart(fig_fuel, use_container_width=True)