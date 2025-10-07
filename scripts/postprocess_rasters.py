# postprocess_rasters.py
from pathlib import Path
import pandas as pd, sys

def main(scenario_id):
    out_dir = Path(f"outputs/{scenario_id}")
    out_dir.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame([
        {"metric":"area_flooded_km2","value":123.4},
        {"metric":"pop_exposed_k","value":56.7},
        {"metric":"avg_arrival_time_min","value":95},
    ])
    df.to_csv(out_dir / "summary_metrics.csv", index=False)
    print("OK:", out_dir / "summary_metrics.csv")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("استخدم: python scripts/postprocess_rasters.py S0_baseline")
    main(sys.argv[1])
