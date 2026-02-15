import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("data/solar_data.csv")

X = df[['shortwave_radiation_backwards_sfc',
        'temperature_2_m_above_gnd',
        'relative_humidity_2_m_above_gnd',
        'wind_speed_10_m_above_gnd',
        'total_cloud_cover_sfc',
        'angle_of_incidence',
        'zenith']]

y = df['generated_power_kw']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

model = RandomForestRegressor(
    n_estimators=500,
    max_depth=20,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("MAE:", mae)
print("RMSE:", rmse)
print("Max Power:", y.max())
print("Min Power:", y.min())

joblib.dump(model, "models/solar_model.pkl")
print("Model saved successfully!")

feature_importances = model.feature_importances_
features = X.columns

plt.figure(figsize=(8,5))
plt.barh(features, feature_importances)
plt.xlabel("Importance")
plt.title("Feature Importance")
plt.tight_layout()
plt.show()