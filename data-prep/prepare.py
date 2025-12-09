import pandas as pd
import numpy as np

class MatchDataProcessor:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.input_file, low_memory=False)
        return self

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()
        return self

    def drop_missing(self):
        self.df = self.df.dropna(subset=["HomeTeam", "AwayTeam", "FTHome", "FTAway"])
        return self

    def replace_empty_strings(self):
        str_cols = self.df.select_dtypes(include=["object"]).columns
        self.df[str_cols] = self.df[str_cols].replace("", np.nan)
        return self

    def drop_columns(self):
        cols_to_drop = ["MatchTime", "MaxHome", "MaxAway", "MaxDraw", "Over25", "Under25", "MaxOver25", "MaxUnder25", "HandiSize", "HandiHome", "HandiAway"]
        self.df = self.df.drop(columns=cols_to_drop, errors="ignore")
        return self

    def convert_scores_to_numeric(self):
        self.df["FTHome"] = pd.to_numeric(self.df["FTHome"], errors="coerce")
        self.df["FTAway"] = pd.to_numeric(self.df["FTAway"], errors="coerce")
        self.df = self.df.dropna(subset=["FTHome", "FTAway"])
        return self

    @staticmethod
    def get_match_result(row):
        if row["FTHome"] > row["FTAway"]:
            return "Win"
        elif row["FTHome"] == row["FTAway"]:
            return "Draw"
        return "Loss"

    def add_features(self):
        self.df["match_result"] = self.df.apply(self.get_match_result, axis=1)
        self.df["total_goals"] = self.df["FTHome"] + self.df["FTAway"]
        self.df["over25_binary"] = (self.df["total_goals"] > 2.5).astype(int)
        return self

    def save(self, output_file: str):
        self.df.to_csv(output_file, index=False)
        return self

    def run_all(self, output_file="matches-prepared.csv"):
        (
            self.load_data()
            .remove_duplicates()
            .drop_missing()
            .replace_empty_strings()
            .drop_columns()
            .convert_scores_to_numeric()
            .add_features()
            .save(output_file)
        )

if __name__ == "__main__":
    processor = MatchDataProcessor("matches.csv")
    processor.run_all()