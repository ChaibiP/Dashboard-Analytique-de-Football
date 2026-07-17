import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="OM Data Analytics",
    layout="wide"
)

connection = sqlite3.connect(
    "database/football.db"
)

players = pd.read_sql_query(
    "SELECT * FROM players",
    connection
)

connection.close()
st.sidebar.success("Données chargées depuis SQLite")

st.title("OM Data Analytics Dashboard 25/26")
st.write(
    "Analyse des performances des joueurs ayant joué plus de 500 minutes."
)
total_players = len(players)
total_goals = players["Goals"].sum()
total_assists = players["assists"].sum()
average_rating = players["rating"].mean()
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Joueurs analysés",
    total_players
)
col2.metric(
    "Buts",
    total_goals
)
col3.metric(
    "Passes décisives",
    total_assists
)
col4.metric(
    "Note moyenne",
    round(average_rating,2)
)
top_scorers = players.sort_values(
    "Goals",
    ascending=False
).head(5)
top_scorers_graph = px.bar(
    top_scorers,
    x="Name",
    y="Goals",
    title="Top 5 buteurs"
)
top_assists=players.sort_values(
    "assists",
    ascending=False
).head(5)
st.plotly_chart(top_scorers_graph)
top_assists_graph=px.bar(
    top_assists,
    x="Name",
    y="assists",
    title="Top 5 passeurs"
)
st.plotly_chart(top_assists_graph)
position_count = players["Position"].value_counts()
lineup_graph = px.pie(
    position_count,
    values=position_count.values,
    names=position_count.index,
    title="Composition de l'effectif ayant +500min"
)
st.plotly_chart(lineup_graph)
rating_consistency_graph = px.scatter(
    players,
    x="Games",
    y="rating",
    size="Goals",
    hover_name="Name",
    title="Régularité et impact des joueurs"
)
st.plotly_chart(rating_consistency_graph)
