import pandas as pd, joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
df=pd.read_csv("ml_model/data/synthetic_results.csv")
X=df[["reservoir_level","breach_width","growth_time","manning","slope"]]
def train(t):
    y=df[t]
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.2,random_state=42)
    m=RandomForestRegressor(n_estimators=300,random_state=42,n_jobs=-1).fit(Xtr,ytr)
    import pathlib; pathlib.Path("ml_model/models").mkdir(parents=True, exist_ok=True)
    joblib.dump(m,f"ml_model/models/rf_{t}.joblib"); print(t,"R2=",m.score(Xte,yte))
for t in ["flooded_area","max_depth","arrival_time"]: train(t)
