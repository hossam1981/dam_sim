import numpy as np, pandas as pd, pathlib
rng = np.random.default_rng(42)
N=2000
rl = rng.uniform(170,180,N); bw=rng.uniform(100,800,N); gt=rng.uniform(1,6,N)
mn=rng.uniform(0.03,0.08,N); sl=rng.uniform(0.0001,0.002,N)
flooded_area = (rl-168)*(bw/200)*(1.5-sl*500)*(0.9+0.2*(0.06/mn)); flooded_area=np.maximum(flooded_area,0)*1.2
max_depth = (rl-169)*(bw/600)*(0.8+0.4*(0.06/mn)); max_depth=np.clip(max_depth,0,None)
arrival_time = 120/(sl*1000+0.2)*(gt/3)*(0.9+0.2*(mn/0.05)); arrival_time=np.clip(arrival_time,10,600)
df=pd.DataFrame(dict(reservoir_level=rl,breach_width=bw,growth_time=gt,manning=mn,slope=sl,
                     flooded_area=flooded_area,max_depth=max_depth,arrival_time=arrival_time))
path=pathlib.Path("ml_model/data"); path.mkdir(parents=True, exist_ok=True)
df.to_csv(path/"synthetic_results.csv", index=False); print("Saved", path/"synthetic_results.csv")
