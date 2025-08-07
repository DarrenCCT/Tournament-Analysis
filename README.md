# EUAC Data Analytics (In-Progress)

EUAC (European ARMS Competitive) is a video game tournament series for the Nintendo Switch game ARMS. This project is a Python-based data analytics toolset designed to gather, process, and analyse tournament, match, and player data from the EUAC events.

## Project Overview

This project collects and merges data from multiple APIs (start.gg and challonge.com), engineering tournament data for further analysis and insights.
There are currently three notebook in the EUAC series: Data Collection, Data Cleaning, and Data Analysis. Also one .py file.

The files included:

**EUAC - Data Collection:** Showing how the data was gathered and merged into one dataframe from the two APIs. It also demonstrates how any roadblocks were dealt it (such as tournament urls that were not crawlable by bots).  
  
**EUAC - Data Cleaning:** How the data was cleaned. This includes stuff like data types and dealing with player account inconsistencies between the two APIs. 
  
**EUAC - Data Analysis:** Data visualisations, statistical information and tests, and general analysis. Tournament tidbits. Some unsupervised machine learning (K-Means clustering) to group players into tiers. Creation of an Elo system to rank player strength.  
  
**elo.py:** A .py file to contain the functions necessary for Elo calculations. Specifically written for this project. 

### Features

- Automated data collection from start.gg and challonge.com APIs
- Data engineering and merging to unify tournament/match/player info
- Data analysis-ready output for further exploration

### Future Additions

- Interactive Dashboard
- Discord Bot for querying tournament/player statistics
- Automated processing for other tournament series

## Technologies Used

- Python
- Pandas
- GraphQL

## Getting Started

1. **Open Notebooks**:
    ```bash
    jupyter lab
    ```
    - Start with `EUAC - Data Collection.ipynb`
    - Then explore `EUAC - Data Cleaning.ipynb`
    - Finally, run `EUAC = Data Analysis.ipynb`
  
## 📉 Disclaimer

> **The notebooks are currently only intended to be viewed**, as to run these notebooks, you would require API keys and tokens for both Challonge and Start.gg.

## Data Sources

- [start.gg](https://start.gg)
- [Challonge](https://challonge.com)
- [ARMS Wiki](https://armswiki.org/wiki/EU_ARMS_Challenge)

## About EUAC

The European ARMS Competitive (EUAC) is a community-run tournament series for ARMS on Nintendo Switch, featuring players from across Europe.

## Contributing

Contributions are welcome! If you have suggestions or want to add features, feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.

---

*If you have questions or want to enhance this README with more sections (e.g., examples, data schema, API authentication), just let me know!*
