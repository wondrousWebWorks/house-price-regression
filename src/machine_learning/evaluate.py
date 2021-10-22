from sklearn.metrics import mean_squared_log_error, mean_absolute_error
from sklearn.metrics import mean_squared_error, r2_score

import numpy as np


# Create function to output tne rmsle as sklearn doesn't have such an in-built function
def rmsle(y_test, y_predictions):
    return np.sqrt(mean_squared_log_error(y_test, y_predictions))


# Function for model evaluation
def show_scores(model):
    train_predictions = model.predict(X_train)
    val_predictions = model.predict(X_val)
    scores = {"Training MAE": mean_absolute_error(y_train, train_predictions),
              "Validation MAE": mean_absolute_error(y_val, val_predictions),
              "Training RMSLE": rmsle(y_train, train_predictions),
              "Validation RMSLE": rmsle(y_val, val_predictions),
              "Training R^2": model.score(X_train, y_train),
              "Validation R^2": model.score(X_val, y_val)}
    return scores


def evaluate_metrics(y_test, y_preds):
    mae = mean_absolute_error(y_test, y_preds)
    mse = mean_squared_error(y_test, y_preds)
    rmsle = np.sqrt(mean_squared_log_error(y_test, y_preds))
    r2 = r2_score(y_test, y_preds)

    return {
        "MAE": mae,
        "MSE": mse,
        "RMSLE": rmsle,
        "R2": r2
    }
