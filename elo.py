# elo.py

def retrieve_elo(df, name):
    """
    Retrieves an elo rating for a given name.

    Parameters:
    df (pandas dataframe): The dataset.
    name (string): The player's name.

    Returns: 
    An integer that is the player's current elo rating.
    """
    name = str(name)
    row = df.loc[df["Player_Map"] == name, "Elo"] #Return elo if player found
    if not row.empty:
        return row.iloc[0]  # Returns first value if not empty. Row is a series.
    else:
        print(f"Error with {name}")



def retrieve_highest_elo(df, name):
    """
    Retrieves the highest elo rating achieved for a given player name.

    Parameters:
    df (pandas dataframe): The dataset containing the column's "Player_Map" and "Highest Elo".
    name (string): The player's name.

    Returns: 
    An integer that is the player's highest ever elo rating.
    """
    name = str(name)
    row = df.loc[df["Player_Map"] == name, "Highest Elo"]
    if not row.empty:
        return row.iloc[0]  # Get the first matching value
    else:
        print(f"Error with {name}")


def update_elo(df, col, index, elo):
    """
    Updates a player's new adjusted elo rating after a match. Given the dataframe, index position, column, and elo rating.
    Used for updating the match table dataframe.

    Parameters:
    df (pandas dataframe): The dataset.
    col (string): Column to be updated (e.g., "Player 1 Adjusted Elo")
    index (integer): Position in the dataframe.
    elo (integer): The player's elo.

    Returns: None.
    This function does not return a value.
    """
    df.loc[index, col] = elo


def expected_score(ratingA, ratingB):
    """
    Calculates the expected score given two ratings.
    Expected score for Player A is defined as:

        E_A = 1/(1 + 10^((R_B-R_A)/400))

    Where E_A is a positive number ranging from 0 to 1.
    Representing Player A's odds of beating Player B.

    Player B's odds (E_B) can be calculated as 1 - E_A

    Parameters:
        ratingA (float): The elo rating of Player A.
        ratingB (float): The elo rating of Player B.

    Returns:
        A float between 0 and 1 that represents the expected score for Player A.
        Player B's expected score can be calculated as 1 - the returned value
    """
    ExpectedA = (1/(1 + 10**((ratingB-ratingA)/400)))
    return ExpectedA


def adjusted_rating(k, rating, expectedScore, score):
    """
    Calculates the adjusted elo rating after a set. 
    Given the k-factor (k), rating to be adjusted (R_A), expected score (E_A), and actual score (S_A).
    Adjusted rating is defined as:

    R'_A = R_A + k(S_A - E_A)

    Parameters:
        k (integer): The K-Factor. 
        rating(float): The current rating to be adjusted.
        expectedScore(float): The expected score.
        score(float): The actual score.

    Returns: 
        A float representing the updated elo rating after a match.
        The K-Factor determines the impact on the result of the rating.
        """
    adjustedRating = rating + k*(score-expectedScore)
    return adjustedRating


def update_main_elo_table(df, playerName, newElo):
    """
    Updates the current rating in a pandas dataframe that contains the columns "Player_Map" and "Elo".

    Parameters:
    df (pandas dataframe): The dataset. 
    playerName (string): The player's name.
    newElo (integer): Current elo to be updated.

    Returns: None.
    This function does not return a value.
    """
    if playerName in df['Player_Map'].values:
        df.loc[df['Player_Map'] == playerName, 'Elo'] = newElo
    else:
        print(f"Player '{playerName}' not found in the dataframe.")


def update_main_highest_elo_table(df, playerName, newElo):
    """
    Updates the highest ever achieved elo rating for a player given the dataset, player name, and elo rating.
    The dataframe should contain the columns "Player_Map" and "Highest_Elo".

    This function is only called if the player achieves a new highest rating.
    Does not handle the check to see if the given score is higher than the entry in the dataframe.

    Parameters:
    df (pandas dataframe): The dataset.
    playerName (string): The player's name
    newElo (integer): The player's highest elo.

    Returns: None.
    This function does not return a value.

    """
    if playerName in df['Player_Map'].values:
        df.loc[df['Player_Map'] == playerName, 'Highest Elo'] = newElo
    else:
        print(f"Player '{playerName}' not found in the dataframe.")