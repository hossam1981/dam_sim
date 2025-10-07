# run_hecras.py (Placeholder pipeline runner)
from pathlib import Path
import sys, yaml, time

def main(cfg_path):
    cfg = yaml.safe_load(Path(cfg_path).read_text(encoding="utf-8"))
    out_dir = Path(f"outputs/{cfg['scenario_id']}")
    out_dir.mkdir(parents=True, exist_ok=True)
    # Placeholders
    for name in ["depth.tif","velocity.tif","arrival_time.tif","hazard_index.tif"]:
        (out_dir / name).write_text("PLACEHOLDER: استبدل بخريطة GeoTIFF من المحرك", encoding="utf-8")
    print("تم تنفيذ سيناريو:", cfg["scenario_id"], "->", out_dir)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("استخدم: python scripts/run_hecras.py scenarios/s0_baseline.yaml")
    main(sys.argv[1])
