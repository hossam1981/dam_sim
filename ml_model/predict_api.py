import streamlit as st, joblib, numpy as np, os
st.set_page_config(page_title="Flood ML Predictor", layout="centered")
st.title("تقدير سريع بالموديل (بدون تشغيل محاكاة)")
rl=st.slider("Reservoir Level (m)",170.0,180.0,176.0,0.1)
bw=st.slider("Breach Width (m)",100.0,800.0,400.0,10.0)
gt=st.slider("Breach Growth Time (h)",1.0,6.0,3.0,0.1)
mn=st.slider("Manning n",0.03,0.08,0.05,0.005)
sl=st.slider("Downstream Slope",0.0001,0.0020,0.0006,0.0001)
def load(p):
    try: return joblib.load(p)
    except Exception: st.warning("⚠️ شغّل تدريب النماذج أولاً."); return None
area=load("ml_model/models/rf_flooded_area.joblib")
depth=load("ml_model/models/rf_max_depth.joblib")
arr=load("ml_model/models/rf_arrival_time.joblib")
if all([area,depth,arr]):
    x=np.array([[rl,bw,gt,mn,sl]])
    st.success(f"🌊 Flooded Area ≈ {area.predict(x)[0]:.1f} km²")
    st.success(f"📏 Max Depth ≈ {depth.predict(x)[0]:.2f} m")
    st.success(f"⏱️ Arrival Time ≈ {arr.predict(x)[0]:.0f} min")
else:
    st.info("أوامر التشغيل:")
    st.code("python -m pip install scikit-learn joblib\npython ml_model/generate_synthetic.py\npython ml_model/train_model.py")
