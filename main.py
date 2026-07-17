import pandas as pd
import plotly.express as px

players = pd.read_csv("data/players.csv", sep=";")

top_scorers = players.sort_values(
    "Goals",
    ascending=False
).head(5)

best_players_by_rating = players.sort_values(
    "rating",
    ascending=False
)
top_assists=players.sort_values(
    "assists",
    ascending=False
)

print("Tout les joueurs de l'effecitf : ")
print(players)
print("5 joueurs avec la meilleure note generale de l'effectif : ")
print(best_players_by_rating.head(5))
print("5 meilleurs buteurs de l'effectif : ")
print(top_scorers.head(5))
print("5 meilleurs passeurs de l'effectif : ")
print(top_assists.head(5))
position_count = players["Position"].value_counts()
print(position_count)
total_players = len(players)
total_goals = players["Goals"].sum()
total_assists = players["assists"].sum()
average_rating = players["rating"].mean()
stats = {
    "Joueurs analysés": total_players,
    "Buts totaux": total_goals,
    "Passes décisives": total_assists,
    "Note moyenne": round(average_rating, 2)
}
print(stats)
attackers = players[
    players["Position"] == "Attaquant"
]

best_attackers=attackers.sort_values(
        "rating",
        ascending=False
    ).head(3)
defenders=players[
    players["Position"] == "Defenseur"
]
best_defenders=defenders.sort_values(
    "rating",
    ascending=False
).head(3)
midfielders=players[
    players["Position"]=="Milieu"
]
best_midfielders=midfielders.sort_values(
    "rating",
    ascending=False
).head(3)
fig = px.bar(
    top_scorers,
    x="Name",
    y="Goals",
    title="Top 5 buteurs - OM (+500min)"
)
fig.show()
fig = px.pie(
    position_count,
    values=position_count.values,
    names=position_count.index,
    title="Composition de l'effectif ayant +500min"
)
fig.show()
fig = px.scatter(
    players,
    x="Games",
    y="rating",
    size="Goals",
    hover_name="Name",
    title="Régularité et impact des joueurs"
)
fig.show()
