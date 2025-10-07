# preprocess_dem.py
from pathlib import Path
import rasterio
from rasterio.fill import fillnodata

IN_DEM = Path("data/dem/raw.tif")
OUT_DEM = Path("data/dem/clean.tif")

def main():
    if not IN_DEM.exists():
        raise SystemExit("ملف DEM الخام غير موجود: data/dem/raw.tif ضع ملفك أولاً.")
    with rasterio.open(IN_DEM) as src:
        profile = src.profile
        data = src.read(1)
        filled = fillnodata(data, mask=(data==src.nodata) if src.nodata is not None else None,
                            max_search_distance=50, smoothing_iterations=0)
        profile.update(nodata=None)
        with rasterio.open(OUT_DEM, "w", **profile) as dst:
            dst.write(filled, 1)
    print("تم إنتاج:", OUT_DEM)

if __name__ == "__main__":
    main()
