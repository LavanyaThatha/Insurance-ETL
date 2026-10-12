import os
import numpy as np
import pandas as pd

os.makedirs("data", exist_ok=True)
rng = np.random.default_rng(42)
n = 1000

df = pd.DataFrame({
    "age": rng.integers(18, 65, n),
    "sex": rng.choice(["male", "female"], n),
    "bmi": rng.normal(30, 6, n).round(1).clip(15, 50),
    "children": rng.integers(0, 5, n),
    "smoker": rng.choice(["yes", "no"], n, p=[0.2, 0.8]),
    "region": rng.choice(["northeast", "northwest", "southeast", "southwest"], n),
})

charges = (
    2000
    + df["age"] * 250
    + (df["bmi"] - 25).clip(lower=0) * 300
    + df["children"] * 400
    + (df["smoker"] == "yes") * 18000
    + rng.normal(0, 2500, n)
)
df["charges"] = charges.clip(lower=1000).round(2)

# Add messy data on purpose
df.loc[rng.choice(n, 20, replace=False), "region"] = " Northeast "
df.loc[rng.choice(n, 15, replace=False), "bmi"] = np.nan
df = pd.concat([df, df.sample(10, random_state=1)])  # duplicate rows

df.to_csv("data/insurance.csv", index=False)
print("Created data/insurance.csv with", len(df), "rows")