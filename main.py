import pandas as pd

players = pd.read_csv("data/players.csv", sep=";")

top_scorers = players.sort_values(
    "Goals",
    ascending=False
)
print(players)
print(players.head())
print(top_scorers.head(5))
players.info()