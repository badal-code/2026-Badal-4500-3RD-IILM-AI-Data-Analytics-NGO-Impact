# System Architecture

```text
                ┌─────────────────────┐
                │ Synthetic CSV Data  │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │ Data Cleaning       │
                │ & Validation        │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │ Exploratory         │
                │ Data Analysis       │
                └──────────┬──────────┘
                           ↓
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
   Donation Analysis  Impact Analysis  Volunteer Analysis
          └────────────────┼────────────────┘
                           ↓
                ┌─────────────────────┐
                │ ML / Segmentation   │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │ Plotly + Streamlit  │
                └─────────────────────┘
```
