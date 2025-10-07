import streamlit as st, pathlib
st.set_page_config(page_title="Dam Failure Dashboard", layout="wide")
st.title("لوحة متابعة سيناريوهات انهيار السد")
scenario = st.selectbox("اختر السيناريو", ["S0_baseline","S1_pessimistic","S2_optimistic"])
out_dir = pathlib.Path("outputs") / scenario
st.subheader("ملفات المخرجات")
for name in ["depth.tif","velocity.tif","arrival_time.tif","hazard_index.tif","summary_metrics.csv","report.md"]:
    p = out_dir / name
    st.write(f"- {name}: {'✅' if p.exists() else '❌'}")
