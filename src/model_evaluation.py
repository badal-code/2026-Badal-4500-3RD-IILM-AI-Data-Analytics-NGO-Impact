from sklearn.metrics import silhouette_score

def cluster_quality(model, X_scaled):
    labels = model.labels_
    if len(set(labels)) < 2:
        return None
    return silhouette_score(X_scaled, labels)
