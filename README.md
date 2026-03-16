# economic-data-analysis
Economic data analysis and regression modeling with Python
# Türkiye Enflasyon Tahmin Modeli

Bu proje Python kullanarak Türkiye'deki ekonomik göstergelerden yararlanarak enflasyon tahmini yapmayı amaçlamaktadır.

Çalışmada ekonomik değişkenler kullanılarak hem ekonometrik hem de makine öğrenmesi modelleri kurulmuş ve performansları karşılaştırılmıştır.

## Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Statsmodels
- Scikit-learn
- XGBoost

## Kullanılan Modeller

Bu projede üç farklı model uygulanmıştır:

- OLS (Ordinary Least Squares) ekonometrik modeli
- Random Forest regresyon modeli
- XGBoost regresyon modeli

## Veri İşleme Adımları

Proje kapsamında:

- Ekonomik veri setleri yüklenmiştir
- Lag (gecikmeli) değişkenler oluşturulmuştur
- Eksik değerler temizlenmiştir
- Eğitim ve test veri setleri ayrılmıştır

## Model Değerlendirme

Modeller aşağıdaki metriklerle karşılaştırılmıştır:

- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score

## Amaç

Amaç ekonomik göstergeler kullanılarak enflasyonun tahmin edilmesi ve farklı model yaklaşımlarının performanslarının karşılaştırılmasıdır.
## Not

Ekonomik veri setleri genellikle sınırlı gözlem sayısına sahiptir ve makroekonomik değişkenler yüksek oynaklık gösterebilir. Bu nedenle tahmin performansı sınırlı olabilir.

Bu çalışma model doğruluğundan ziyade veri hazırlama süreci, farklı model yaklaşımlarının uygulanması ve performanslarının karşılaştırılmasına odaklanmaktadır.ß
