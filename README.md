# dam-failure-sim — Dam Failure Simulation Template (3D + ML)

## Quick Start Checklist
1. Choose your operating system and follow the environment setup guide below.
2. Place your raw DEM at `data/dem/raw.tif`.
3. Preprocess the DEM:
   ```bash
   python scripts/preprocess_dem.py
   ```
4. (Optional) Generate placeholder outputs:
   ```bash
   python scripts/run_hecras.py scenarios/s0_baseline.yaml
   python scripts/postprocess_rasters.py S0_baseline
   python scripts/make_report.py S0_baseline
   ```
5. Launch the 2D dashboard:
   ```bash
   streamlit run dashboard/app.py
   ```

## Environment Setup

### macOS Workflow
1. Open the project folder in Cursor or VS Code.
2. (Optional) create a virtual environment:
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   ```
3. Run the automated task sequence:
   - From the menu choose `Terminal → Run Task → 🚀 Run All (Setup → Train → 3D)`.
   - This installs packages from `requirements_macos.txt` with `--only-binary ":all:"`, trains the ML models, and launches the 3D dashboard.
4. Alternatively, run the shell script:
   ```bash
   chmod +x setup_mac.sh
   ./setup_mac.sh
   ```
   - The script builds `.venv`, upgrades pip/setuptools/wheel, installs the macOS requirements, trains ML models, and starts the 3D dashboard.

### Windows 10/11 Workflow (PowerShell)
1. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Upgrade packaging tools and install dependencies:
   ```powershell
   python -m pip install --upgrade pip setuptools wheel
   pip install -r requirements.txt
   ```
3. Launch the 3D dashboard:
   ```powershell
   streamlit run dashboard/app_3d.py
   ```
4. Troubleshooting GIS packages:
   - If `rasterio`, `fiona`, or similar packages fail to install, install OSGeo4W dependencies or download prebuilt `.whl` files from Christoph Gohlke’s repository.

## 3D Flood Viewer
- Export GeoTIFFs from HEC-RAS / LISFLOOD / other engines into `outputs/S*_*/` named `depth_0001.tif` (or `depth.tif`).
- Launch the viewer:
  ```bash
  streamlit run dashboard/app_3d.py
  ```

## Quick ML Pipeline
```bash
python ml_model/generate_synthetic.py
python ml_model/train_model.py
streamlit run ml_model/predict_api.py
```

> Note: Sample GeoTIFFs in `outputs/*` are placeholders—replace them with your simulation results.
