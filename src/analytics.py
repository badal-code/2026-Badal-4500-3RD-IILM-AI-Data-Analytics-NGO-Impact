import pandas as pd

def donation_summary(df):
    return {
        "total_donations": len(df),
        "total_amount_inr": float(df["amount_inr"].sum()),
        "average_donation_inr": float(df["amount_inr"].mean()),
        "repeat_donor_share": float(df["repeat_donor"].mean() * 100),
    }

def donations_by_program(df):
    return df.groupby("program", as_index=False)["amount_inr"].sum().sort_values("amount_inr", ascending=False)

def donations_by_state(df):
    return df.groupby("state", as_index=False)["amount_inr"].sum().sort_values("amount_inr", ascending=False)

def monthly_donations(df):
    out = df.groupby("month", as_index=False)["amount_inr"].sum()
    return out.sort_values("month")

def beneficiary_summary(df):
    return df.groupby("program", as_index=False).agg(
        beneficiaries=("beneficiary_id", "count"),
        avg_attendance=("attendance_rate", "mean"),
        avg_outcome=("outcome_score", "mean")
    ).sort_values("avg_outcome", ascending=False)

def volunteer_summary(df):
    return df.groupby("program", as_index=False).agg(
        volunteers=("volunteer_id", "count"),
        total_hours=("hours_contributed", "sum"),
        avg_months_active=("months_active", "mean")
    ).sort_values("total_hours", ascending=False)
