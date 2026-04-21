from sklearn.ensemble import IsolationForest

# Dummy feature conversion (we improve later)
def extract_features(log):
    return [
        len(log["event"]),                 # event length
        1 if log["severity"] == "high" else 0
    ]

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.2)
    
    def train(self, logs):
        features = [extract_features(log) for log in logs]
        self.model.fit(features)
    
    def predict(self, log):
        features = [extract_features(log)]
        result = self.model.predict(features)
        return "ANOMALY" if result[0] == -1 else "NORMAL"