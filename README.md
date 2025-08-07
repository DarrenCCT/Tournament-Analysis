# EUAC Data Analytics (In-Progress)

EUAC (European ARMS Competitive) is a video game tournament series for the Nintendo Switch game ARMS. This project is a Python-based data analytics toolset designed to gather, process, and analyse tournament, match, and player data from the EUAC events.

## Project Overview

This project collects and merges data from multiple APIs (start.gg and challonge.com), engineering tournament data for further analysis and insights.

### Features

- Automated data collection from start.gg and challonge.com APIs
- Data engineering and merging to unify tournament/match/player info
- Data analysis-ready output for further exploration

### Future Additions

- Interactive Dashboard
- Discord Bot for querying tournament/player statistics

## Technologies Used

- Python
- Pandas
- GraphQL

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/DarrenCCT/EUAC.git
   cd EUAC
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script (replace `main.py` with the entrypoint if different):
   ```bash
   python main.py
   ```

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
