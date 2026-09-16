import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd
import plotly.express as px
import streamlit as st
from analytics import donation_summary

st.set_page_config(page_title="NGO Impact Analytics", layout="wide")
st.title("NGO Impact & Donation Analytics Dashboard")
st.caption("Synthetic demonstration dashboard — not based on confidential organizational records.")

don = pd.read_csv("data/donations.csv")
ben = pd.read_csv("data/beneficiaries.csv")
vol = pd.read_csv("data/volunteers.csv")
prog = pd.read_csv("data/programs.csv")

with st.sidebar:
    st.header("Filters")
    selected_states = st.multiselect("State", sorted(don["state"].unique()), default=list(don["state"].unique()))
    selected_programs = st.multiselect("Program", sorted(don["program"].unique()), default=list(don["program"].unique()))

fd = don[don["state"].isin(selected_states) & don["program"].isin(selected_programs)].copy()
summary = donation_summary(fd)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Donations", f'{summary["total_donations"]:,}')
c2.metric("Funds Raised", f'₹{summary["total_amount_inr"]:,.0f}')
c3.metric("Avg Donation", f'₹{summary["average_donation_inr"]:,.0f}')
c4.metric("Repeat Donor Share", f'{summary["repeat_donor_share"]:.1f}%')

tab1, tab2, tab3 = st.tabs(["Donations", "Beneficiary Impact", "Volunteers & Programs"])

with tab1:
    a, b = st.columns(2)
    by_program = fd.groupby("program", as_index=False)["amount_inr"].sum()
    a.plotly_chart(px.bar(by_program, x="program", y="amount_inr", title="Funds by Program"), use_container_width=True)
    monthly = fd.assign(donation_date=pd.to_datetime(fd["donation_date"])).groupby(
        fd.assign(donation_date=pd.to_datetime(fd["donation_date"]))["donation_date"].dt.to_period("M").astype(str),
        as_index=False
    )["amount_inr"].sum().rename(columns={"donation_date":"month"})
    b.plotly_chart(px.line(monthly, x="month", y="amount_inr", markers=True, title="Monthly Donation Trend"), use_container_width=True)

with tab2:
    impact = ben.groupby("program", as_index=False).agg(
        beneficiaries=("beneficiary_id","count"),
        avg_attendance=("attendance_rate","mean"),
        avg_outcome=("outcome_score","mean")
    )
    st.dataframe(impact.round(2), use_container_width=True)
    st.plotly_chart(px.scatter(impact, x="avg_attendance", y="avg_outcome", size="beneficiaries",
                               hover_name="program", title="Attendance vs Outcome Score"),
                    use_container_width=True)

with tab3:
    vsummary = vol.groupby("program", as_index=False).agg(
        volunteers=("volunteer_id","count"),
        total_hours=("hours_contributed","sum")
    )
    st.plotly_chart(px.bar(vsummary, x="program", y="total_hours", title="Volunteer Hours by Program"),
                    use_container_width=True)
    st.dataframe(prog.round(2), use_container_width=True)
