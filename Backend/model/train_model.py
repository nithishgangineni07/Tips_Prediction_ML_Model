import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def train_model(df):
    """Train a machine learning model using the provided DataFrame."""

    # Separate features and target
    X = df.drop('tip', axis=1)
    y = df['tip']

    # Correctly identify categorical & numerical columns
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns
    numerical_cols = X.select_dtypes(exclude=['object', 'category']).columns

    # Preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', 'passthrough', numerical_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False),
             categorical_cols)
        ]
    )

    # Pipeline
    model = Pipeline(
        steps=[
            ('preprocessor', preprocessor),
            ('regression', RandomForestRegressor(
                n_estimators=100,
                random_state=42
            ))
        ]
    )

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train
    model.fit(X_train, y_train)

    return model
