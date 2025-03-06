# Cricket Analysis Dashboard Documentation

## Overview
This project features a dynamic Tableau dashboard that provides in-depth insights into ODI cricket matches from **2002 to 2023**. Using over **1.2 million rows** of ball-by-ball data, the dashboard highlights key trends, team performances, and individual player statistics.

## Project Structure

- **README.md:** An overview of the project.
- **LICENSE:** The MIT License file.
- **Dashboard.twbx:** The packaged Tableau workbook.
- **docs/Documentation.md:** Detailed project documentation.
- **.gitignore:** Specifies files to exclude from version control.
- **data/**: Contains sample data files or data preparation scripts (if applicable).

## Data Description

- **Dataset:** ODI Men's Cricket Match Data (2002-2023)
- **Source:** Kaggle  
  [Dataset Link](https://www.kaggle.com/datasets/utkarshtomar736/odi-mens-cricket-match-data-2002-2023)
- **Volume:** Over **1.2 million rows** of detailed match records.
- **Key Fields:**  
  - `match_id`: Unique match identifier.
  - `season`: Season or year of the match.
  - `start_date`: Date when the match began.
  - `venue`: Stadium or ground where the match was held.
  - `innings`: Innings number.
  - `ball`: Ball number within an innings.
  - `batting_team`: Team batting.
  - `bowling_team`: Team bowling.
  - *(Additional fields are available as per the dataset.)*

## Dashboard Features & KPIs

The dashboard includes several interactive visualizations that track crucial performance metrics:

- **🏆 Top Batsmen:**  
  - Total runs scored.
  - Average runs per match.
  - Strike rates.
- **🎯 Leading Bowlers:**  
  - Total wickets taken.
  - Economy rates.
  - Strike rates.
- **📈 Team Performance:**  
  - Scoring averages.
  - Consistency and performance trends across seasons.
- **📍 Venue Impact:**  
  - Comparison of home vs. away performance.
- **⏳ Seasonal Trends:**  
  - Analysis of match outcomes and performance shifts over time.

## Tools & Methodology

- **Tools Used:**
  - **Tableau Desktop:** For dashboard creation and visualization.
  - **Tableau Public/Reader:** For sharing and viewing the dashboard.
  - **Kaggle:** Source for the dataset.
  - **GitHub:** Repository management and version control.

- **Methodology:**
  1. **Data Acquisition:**  
     - Downloaded the dataset from Kaggle.
     - Performed an initial data exploration to understand the structure.
  2. **Data Preparation:**  
     - Cleaned and transformed the raw ball-by-ball data.
     - Aggregated key metrics and handled missing values.
  3. **Dashboard Development:**  
     - Designed interactive visualizations using Tableau Desktop.
     - Implemented filters to allow dynamic exploration by teams, seasons, and venues.
  4. **Validation & Iteration:**  
     - Refined visualizations through iterative testing and feedback.
  5. **Deployment:**  
     - Packaged the final workbook as a TWBX file for easy sharing and publication.

## Usage Instructions

- **Viewing the Dashboard:**  
  - Open the `Dashboard.twbx` file using **Tableau Desktop** or **Tableau Reader**.
  - When publishing to Tableau Public, ensure that the data source is set to use an extract.
- **Interacting with the Dashboard:**  
  - Use interactive filters to explore specific teams, seasons, or venues.
  - Hover over data points for detailed match insights.

## Future Enhancements

- **Data Automation:**  
  - Explore ways to automate data updates for real-time analysis.
- **Enhanced KPIs:**  
  - Integrate additional metrics, such as player efficiency and weather impact.
- **User Feedback:**  
  - Continuously refine the dashboard based on user interactions and suggestions.

## Contributing

This project is a personal academic endeavor. However, suggestions for improvements or enhancements are welcome. Feel free to open issues or submit pull requests.