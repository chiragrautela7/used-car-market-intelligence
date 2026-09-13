# Used Car Market & Pricing Intelligence
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
df=pd.read_csv(Path("../data/cleaned/used_cars_cleaned.csv"))
print(df.shape); display(df.head()); display(df.isna().sum().sort_values(ascending=False).head())
# Q1 Price distribution
sns.histplot(df.selling_price_lakh,bins=40,kde=True); plt.title("Selling Price Distribution"); plt.show()
# Q2 Brand pricing
brand=df.groupby("brand").selling_price_lakh.agg(["count","mean","median"]).sort_values("median",ascending=False); display(brand)
# Q3 Age/depreciation
age=df.groupby("age_group",observed=True).selling_price_lakh.agg(["count","mean","median"]); display(age)
sns.scatterplot(data=df,x="car_age",y="selling_price_lakh",alpha=.35); sns.regplot(data=df,x="car_age",y="selling_price_lakh",scatter=False); plt.show()
# Q4 Mileage
sns.scatterplot(data=df,x="km_driven",y="selling_price_lakh",hue="price_segment",alpha=.4); plt.show()
# Q5 Transmission/fuel
display(df.groupby("transmission").selling_price_lakh.agg(["count","mean","median"]))
display(df.groupby("fuel").selling_price_lakh.agg(["count","mean","median"]))
# Q6 Brand x age retention
p=df.groupby(["brand","age_group"],observed=True).selling_price_lakh.median().unstack(); display(p)
sns.heatmap(p,annot=True,fmt=".1f"); plt.show()
# Q7 Segments
seg=df.groupby("price_segment",observed=True).agg(listings=("selling_price_lakh","size"),median_price=("selling_price_lakh","median"),median_km=("km_driven","median"),median_age=("car_age","median")); seg["share_%"]=seg.listings/len(df)*100; display(seg)
# Q8 correlations
display(df[["selling_price_lakh","car_age","km_driven","mileage_kmpl","engine_cc","max_power_bhp"]].corr()["selling_price_lakh"].sort_values(ascending=False))
