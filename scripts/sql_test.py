import sqlite3

connection = sqlite3.connect(
    "database/football.db"
)
cursor = connection.cursor()
cursor.execute("""
SELECT Name, Goals, rating
FROM players
ORDER BY Goals DESC
LIMIT 5
""")
results = cursor.fetchall()
for player in results:
    print(player)

connection.close()