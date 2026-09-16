import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def donor_segmentation(df, n_clusters=4):
    features = df.groupby("donor_type", as_index=False).agg(
        total_amount=("amount_inr", "sum"),
        avg_amount=("amount_inr", "mean"),
        donation_count=("donation_id", "count"),
        repeat_rate=("repeat_donor", "mean")
    )
    X = features[["total_amount", "avg_amount", "donation_count", "repeat_rate"]]
    Xs = StandardScaler().fit_transform(X)
    model = KMeans(n_clusters=min(n_clusters, len(features)), random_state=42, n_init=10)
    features["segment"] = model.fit_predict(Xs)
    return features, model

def beneficiary_risk_groups(df):
    out = df.copy()
    out["risk_group"] = pd.cut(
        out["outcome_score"],
        bins=[-1, 50, 70, 100],
        labels=["Needs Attention", "Moderate", "Positive"]
    )
    return out
