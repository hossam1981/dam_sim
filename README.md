# dam-failure-sim — قالب محاكاة انهيار السد العالي (مع 3D + ML)

## تشغيل سريع
1) ضع ملف DEM الخام: `data/dem/raw.tif`
2) ثبّت الحزم:
   ```bash
   pip install rasterio geopandas pandas pyyaml xarray rich streamlit pydeck pillow scikit-learn joblib
   ```
3) تجهيز DEM:
   ```bash
   python scripts/preprocess_dem.py
   ```
4) (اختياري) توليد مخرجات تجريبية Placeholder:
   ```bash
   python scripts/run_hecras.py scenarios/s0_baseline.yaml
   python scripts/postprocess_rasters.py S0_baseline
   python scripts/make_report.py S0_baseline
   ```
5) لوحة الملفات:
   ```bash
   streamlit run dashboard/app.py
   ```

## عرض 3D تفاعلي
- صدّر GeoTIFFs من محرك المحاكاة إلى `outputs/S*_*/` بالاسم `depth_0001.tif ...` أو `depth.tif`.
- ثم:
  ```bash
  streamlit run dashboard/app_3d.py
  ```

## نموذج ML سريع
```bash
python ml_model/generate_synthetic.py
python ml_model/train_model.py
streamlit run ml_model/predict_api.py
```

> ملاحظة: ملفات GeoTIFF الحالية في `outputs/*` هي Placeholders – استبدلها بنتائج المحرك (HEC-RAS/Telemac/LISFLOOD-FP).
