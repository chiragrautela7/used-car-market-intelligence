import pandas as pd
from pathlib import Path
RAW_PATH=Path("../data/raw/used_cars_raw.csv")
OUT_PATH=Path("../data/cleaned/used_cars_cleaned.csv")
df=pd.read_csv(RAW_PATH)
print("Raw shape:",df.shape)
df=df.drop_duplicates().copy()
for c in ["year","selling_price_lakh","km_driven","mileage_kmpl","engine_cc","max_power_bhp","seats"]: df[c]=pd.to_numeric(df[c],errors="coerce")
for c in ["mileage_kmpl","engine_cc","max_power_bhp"]: df[c]=df[c].fillna(df[c].median())
df=df[(df.selling_price_lakh>0)&(df.km_driven>=0)&df.year.between(2000,2025)].copy()
df["car_age"]=2025-df.year
df["price_per_10k_km"]=df.selling_price_lakh/(df.km_driven.clip(lower=1000)/10000)
df["price_segment"]=pd.cut(df.selling_price_lakh,[0,4,8,15,float("inf")],labels=["Budget","Mid-range","Premium","Luxury"])
df["mileage_category"]=pd.cut(df.mileage_kmpl,[0,12,18,25,float("inf")],labels=["Low","Medium","High","Very High"])
df["age_group"]=pd.cut(df.car_age,[-1,3,7,12,float("inf")],labels=["0-3 years","4-7 years","8-12 years","13+ years"])
OUT_PATH.parent.mkdir(exist_ok=True,parents=True); df.to_csv(OUT_PATH,index=False); print("Cleaned shape:",df.shape)
