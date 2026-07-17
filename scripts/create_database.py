import sqlite3
import pandas as pd

players = pd.read_csv(
    "data/players.csv",
    sep=";"
)
connection = sqlite3.connect(
    "database/football.db"
)
players.to_sql(
    "players",
    connection,
    if_exists="replace",
    index=False
)
connection.close()
print("Base SQLite créée avec succès")