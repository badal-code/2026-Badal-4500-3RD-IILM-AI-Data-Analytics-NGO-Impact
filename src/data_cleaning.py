import pandas as pd

def clean_donations(path="data/donations.csv"):
    df = pd.read_csv(path)
    df["donation_date"] = pd.to_datetime(df["donation_date"], errors="coerce")
    df["amount_inr"] = pd.to_numeric(df["amount_inr"], errors="coerce")
    df = df.drop_duplicates().dropna(subset=["donation_date", "amount_inr"])
    df = df[df["amount_inr"] > 0].copy()
    df["month"] = df["donation_date"].dt.to_period("M").astype(str)
    return df

def clean_beneficiaries(path="data/beneficiaries.csv"):
    df = pd.read_csv(path)
    for col in ["age", "attendance_rate", "outcome_score"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df.drop_duplicates().dropna()

def clean_volunteers(path="data/volunteers.csv"):
    df = pd.read_csv(path)
    df["hours_contributed"] = pd.to_numeric(df["hours_contributed"], errors="coerce")
    df["months_active"] = pd.to_numeric(df["months_active"], errors="coerce")
    return df.drop_duplicates().dropna()
