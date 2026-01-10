# Football Match Predictions

This project aims to predict football match outcomes and scores using machine learning techniques, specifically leveraging the **FLAML** (Fast and Lightweight AutoML) library.

## Features

- **Data Preprocessing**: Automated cleaning and feature engineering of match data.
- **Score Regression**: Predicting the number of goals scored by the home and away teams.
- **High-Score Classification**: Binary classification to predict if a match will have more than 2.5 goals.
- **AutoML Integration**: Using FLAML for efficient model selection and hyperparameter tuning.

## Project Structure

```text
football-match-predictions/
├── data-prep/          # Data preparation scripts
│   ├── prepare.py      # Main preprocessing script
│   └── matches.csv     # Raw dataset (input)
├── models/             # Machine learning notebooks
│   ├── match_results_regression.ipynb    # Score prediction
│   └── Klasyfikacja_binarna_wysoki_wynik.ipynb # Over 2.5 goals classification
├── analysis/           # Analysis results and visualizations
└── README.md           # Project documentation
```

## Getting Started

### Prerequisites

Ensure you have Python installed. It is recommended to use a virtual environment.

```bash
pip install pandas numpy flaml matplotlib seaborn notebook
```

### Usage

1. **Prepare the Data**:
   Place your `matches.csv` in the `data-prep/` directory and run the preprocessing script:
   ```bash
   python data-prep/prepare.py
   ```
   This will generate `matches-prepared.csv`.

2. **Train Models**:
   Open the Jupyter notebooks in the `models/` directory to train and evaluate the models:
   ```bash
   jupyter notebook models/match_results_regression.ipynb
   ```

## Methodology

- **Regression**: Separate models are trained for `FTHome` and `FTAway` scores using FLAML's `AutoML` regressor.
- **Classification**: A binary classifier is used to predict the `over25_binary` target, indicating if the total goals exceed 2.5.
- **Feature Engineering**: Includes creating match results (Win/Draw/Loss), total goals, and binary indicators for betting-related predictions.

## License

This project is for educational purposes.