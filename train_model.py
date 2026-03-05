import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib


def main():

    parser = argparse.ArgumentParser(description="Train baseline ML model")

    parser.add_argument("--data", required=True, help="CSV dataset")
    parser.add_argument("--target", required=True, help="Target column")
    parser.add_argument("--model_out", default="model.joblib")

    args = parser.parse_args()

    df = pd.read_csv(args.data)

    X = df.drop(columns=[args.target])
    y = df[args.target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=2000))
    ])

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, preds))
    print("\nClassification Report:")
    print(classification_report(y_test, preds))

    joblib.dump(model, args.model_out)

    print("\nModel saved to:", args.model_out)


if __name__ == "__main__":
    main()