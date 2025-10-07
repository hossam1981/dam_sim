# 3D interactive viewer using pydeck
import streamlit as st, rasterio, numpy as np, pydeck as pdk, pathlib, glob, tempfile
from PIL import Image

st.set_page_config(page_title="3D Flood Dashboard", layout="wide")
st.title("لوحة 3D تفاعلية لسيناريوهات الفيضان")

scenarios = ["S0_baseline","S1_pessimistic","S2_optimistic"]
scenario = st.sidebar.selectbox("اختر السيناريو", scenarios, index=0)
out_dir = pathlib.Path("outputs") / scenario

candidates = sorted(glob.glob(str(out_dir / "depth_*.tif")))
if not candidates and (out_dir / "depth.tif").exists():
    candidates = [str(out_dir / "depth.tif")]
if not candidates:
    st.warning("لا توجد خرائط عمق بعد في " + str(out_dir))
    st.stop()

frame_idx = 0
if len(candidates) > 1:
    frame_idx = st.sidebar.slider("الإطار الزمني", 0, len(candidates)-1, 0, 1)
depth_path = pathlib.Path(candidates[frame_idx])
st.write(f"الملف المختار: **{depth_path.name}**")

def raster_to_png_with_bounds(path):
    with rasterio.open(path) as src:
        arr = src.read(1, masked=True).astype("float32")
        # تطبيع القيم إلى 0-255
        finite = np.isfinite(arr)
        vmax = np.nanpercentile(arr[finite], 99) if finite.any() else 1.0
        scale = 255.0/max(vmax,1e-6)
        img = np.clip(arr*scale, 0, 255).filled(0).astype("uint8")
        rgb = np.stack([img,img,img], axis=-1)
        left, bottom, right, top = src.bounds.left, src.bounds.bottom, src.bounds.right, src.bounds.top
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    Image.fromarray(rgb).save(tmp.name)
    return tmp.name, [[left, bottom], [right, bottom], [right, top], [left, top]]

png_path, bounds = raster_to_png_with_bounds(depth_path)

view_state = pdk.ViewState(latitude=(bounds[0][1]+bounds[2][1])/2,
                           longitude=(bounds[0][0]+bounds[2][0])/2,
                           zoom=7, pitch=50, bearing=20)

layer = pdk.Layer("BitmapLayer", data=None, image=png_path, bounds=bounds, opacity=0.8)
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, map_style="mapbox://styles/mapbox/satellite-v9"))
st.caption("لعرض تضاريس فعلية ثلاثية الأبعاد استخدم TerrainLayer مع تبليط COG أو Cesium/MapLibre.")
