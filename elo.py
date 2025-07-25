# elo.py

# Retrieves a player's current elo based on their name. Called when updating match table and reporting elo
def retrieve_elo(df, name):
    name = str(name)
    row = df.loc[df["Player_Map"] == name, "Elo"] #Return elo if player found
    if not row.empty:
        return row.iloc[0]  # Returns first value if not empty. Row is a series.
    else:
        print(f"Error with {name}")


# Retrieves highest elo 
def retrieve_highest_elo(df, name):
    name = str(name)
    row = df.loc[df["Player_Map"] == name, "Highest Elo"]
    if not row.empty:
        return row.iloc[0]  # Get the first matching value
    else:
        print(f"Error with {name}")

# Updates current elo post-match
def update_elo(df, col, index, elo):
    df.loc[index, col] = elo

# Calculates an expected score given two ratings
def expected_score(ratingA, ratingB):
    ExpectedA = (1/(1 + 10**((ratingB-ratingA)/400)))
    return ExpectedA

# Rating post-game
def adjusted_rating(k, rating, expectedScore, score):
    adjustedRating = rating + k*(score-expectedScore)
    return adjustedRating

# Update elo for stats dataframe
def update_main_elo_table(df, playerName, newElo):
    if playerName in df['Player_Map'].values:
        df.loc[df['Player_Map'] == playerName, 'Elo'] = newElo
    else:
        print(f"Player '{playerName}' not found in the dataframe.")

# Updates highest ever elo
def update_main_highest_elo_table(df, playerName, newElo):
    if playerName in df['Player_Map'].values:
        df.loc[df['Player_Map'] == playerName, 'Highest Elo'] = newElo
    else:
        print(f"Player '{playerName}' not found in the dataframe.")