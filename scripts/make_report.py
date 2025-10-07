# make_report.py
from pathlib import Path, sys

TEMPLATE = "# تقرير محاكاة — {scenario}\n\n- نتائج الخرائط في المجلد outputs/{scenario}\n- ملخص: summary_metrics.csv\n"

def main(scenario_id):
    out_dir = Path(f"outputs/{scenario_id}")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "report.md").write_text(TEMPLATE.format(scenario=scenario_id), encoding="utf-8")
    print("OK:", out_dir / "report.md")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("استخدم: python scripts/make_report.py S0_baseline")
    main(sys.argv[1])
