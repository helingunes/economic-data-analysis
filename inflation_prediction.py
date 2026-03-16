import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import statsmodels.api as sm

# Veri yükleme
df = pd.read_excel("turkiye_buyume.xlsx")

print("Veri boyutu:", df.shape)


# Lag (gecikmeli) değişkenler oluşturma
df["Enflasyon_lag1"] = df["Enflasyon tüketici fiyatları (%yıllık)"].shift(1)
df["Yatırım_lag1"] = df["Gayri safi sermaya oluşumu (%GSYİH)"].shift(1)
df["Kamu_lag1"] = df["Genel hükümet nihai tüketim harcamaları (%GSYİH)"].shift(1)
df["Sanayi_lag1"] = df["Sanayi katma değer (%GSYİH)"].shift(1)
df["Cari_lag1"] = df["Cari hesap dengesi (%GSYİH)"].shift(1)


# Eksik değerleri temizleme
df = df.dropna()

print("Lag sonrası veri boyutu:", df.shape)


# Bağımlı ve bağımsız değişkenler
y = df["Enflasyon tüketici fiyatları (%yıllık)"]

X = df[
    [
        "Enflasyon_lag1",
        "Yatırım_lag1",
        "Kamu_lag1",
        "Sanayi_lag1",
        "Cari_lag1",
    ]
]


# Train / Test ayrımı (zaman bazlı)
train = df[df["Yıl"] <= 2021]
test = df[df["Yıl"] >= 2022]

X_train = train[X.columns]
X_test = test[X.columns]

y_train = train["Enflasyon tüketici fiyatları (%yıllık)"]
y_test = test["Enflasyon tüketici fiyatları (%yıllık)"]

print("Train size:", len(X_train))
print("Test size:", len(X_test))


# OLS (Ekonometrik model)
X_train_ols = sm.add_constant(X_train)

ols_model = sm.OLS(y_train, X_train_ols).fit()

print("\nOLS SONUÇLARI\n")
print(ols_model.summary())


# Random Forest modeli
rf = RandomForestRegressor(random_state=42)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)


# XGBoost modeli
xgb = XGBRegressor()

xgb.fit(X_train, y_train)

xgb_pred = xgb.predict(X_test)


# Model değerlendirme fonksiyonu
def evaluate(true, pred):

    rmse = np.sqrt(mean_squared_error(true, pred))
    mae = mean_absolute_error(true, pred)
    r2 = r2_score(true, pred)

    return rmse, mae, r2


rf_rmse, rf_mae, rf_r2 = evaluate(y_test, rf_pred)
xgb_rmse, xgb_mae, xgb_r2 = evaluate(y_test, xgb_pred)


# Model karşılaştırması
results = pd.DataFrame(
    {
        "Model": ["Random Forest", "XGBoost"],
        "RMSE": [rf_rmse, xgb_rmse],
        "MAE": [rf_mae, xgb_mae],
        "R2": [rf_r2, xgb_r2],
    }
)

print("\nMODEL KARŞILAŞTIRMASI\n")
print(results)


# Gerçek vs tahmin
forecast = pd.DataFrame(
    {
        "Yıl": test["Yıl"],
        "Gerçek Enflasyon": y_test,
        "RF Tahmin": rf_pred,
        "XGB Tahmin": xgb_pred,
    }
)

print("\nTAHMİN SONUÇLARI\n")
print(forecast)
