# Vehicle Dashboard

Projeto de análise exploratória de dados (EDA) e desenvolvimento de um dashboard interativo para explorar anúncios de veículos usados.

# Sobre o projeto

Este projeto tem como objetivo analisar um conjunto de dados com informações sobre anúncios de veículos usados e identificar padrões relacionados a preço, características dos veículos e tempo de permanência dos anúncios.

A análise foi realizada utilizando Python e bibliotecas de análise e visualização de dados. Após o tratamento e a exploração dos dados, foi desenvolvido um dashboard interativo utilizando Streamlit.
##  Dashboard

O dashboard interativo está disponível no Render:

 [Acessar o Vehicle Dashboard](https://vehicle-dashboard-ms5y.onrender.com)
# Dataset

O dataset contém **51.525 anúncios de veículos usados** e **13 variáveis**, incluindo:

- `price` — preço do veículo
- `model_year` — ano do modelo
- `model` — modelo do veículo
- `condition` — condição do veículo
- `cylinders` — número de cilindros
- `fuel` — tipo de combustível
- `odometer` — quilometragem
- `transmission` — tipo de transmissão
- `type` — tipo de veículo
- `paint_color` — cor do veículo
- `is_4wd` — indicação de tração 4x4
- `date_posted` — data de publicação do anúncio
- `days_listed` — número de dias em que o anúncio permaneceu ativo

## Análise exploratória

Durante a EDA foram analisadas:

- Estrutura e tipos das variáveis
- Valores ausentes
- Estatísticas descritivas
- Distribuição dos preços
- Distribuição das variáveis categóricas
- Valores extremos e possíveis outliers
- Relação entre ano do modelo e preço
- Relação entre quilometragem e preço
- Distribuição dos preços por condição
- Distribuição dos preços por tipo de veículo
- Distribuição dos preços por combustível
- Distribuição dos preços por transmissão
- Tempo de permanência dos anúncios

## Tratamento dos dados

Foram identificados e tratados valores ausentes e inconsistentes.

Entre os principais tratamentos realizados:

- Valores ausentes de `is_4wd` foram preenchidos com `0`.
- Valores ausentes de `model_year` foram tratados utilizando a mediana.
- Valores ausentes de `cylinders` foram preenchidos utilizando a mediana.
- Valores ausentes e registros com `odometer = 0` foram tratados utilizando a mediana.
- Valores ausentes de `paint_color` foram substituídos pela categoria `unknown`.
- Valores extremos de `price` e `odometer` foram analisados e mantidos quando não havia evidência suficiente para classificá-los como erros.

Após o tratamento, o dataset não apresenta valores ausentes.

## Dashboard

Após a conclusão da EDA, foi desenvolvido um dashboard interativo com Streamlit.

O dashboard apresenta:

- Total de veículos
- Preço médio
- Ano médio dos veículos
- Distribuição dos preços
- Relação entre ano do modelo e preço
- Relação entre quilometragem e preço
- Distribuição dos preços por condição
- Distribuição dos preços por tipo de veículo
- Distribuição dos preços por combustível

O usuário também pode utilizar filtros interativos por:

- `Condition`
- `Type`
- `Fuel`

Os gráficos são atualizados de acordo com os filtros selecionados.

## Tecnologias utilizadas

- Python
- Pandas
- Plotly
- Streamlit
- Jupyter Notebook
- Git
- GitHub

## Estrutura do projeto

```text
vehicle-dashboard/
│
├── app.py
├── vehicles_us.csv
├── vehicles_us_clean.csv
├── requirements.txt
├── README.md
├── .gitignore
│
└── notebooks/
    └── EDA.ipynb
