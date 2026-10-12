import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("insurance.db")

by_age = pd.read_sql("""
    SELECT age_group, ROUND(AVG(charges), 2) AS avg_charges, COUNT(*) AS policies
    FROM policies
    GROUP BY age_group
    ORDER BY age_group
""", conn)

by_region = pd.read_sql("""
    SELECT region, ROUND(AVG(charges), 2) AS avg_charges
    FROM policies
    GROUP BY region
    ORDER BY avg_charges DESC
""", conn)

by_smoker = pd.read_sql("""
    SELECT smoker, ROUND(AVG(charges), 2) AS avg_charges
    FROM policies
    GROUP BY smoker
""", conn)
conn.close()

print(by_age)
print(by_region)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

def draw(ax, labels, values, title):
    bars = ax.bar(labels, values)
    ax.set_title(title)
    ax.set_ylabel("Average charges")
    ax.bar_label(bars, labels=[f"{v:,.0f}" for v in values], padding=2)
    ax.set_ylim(0, max(values) * 1.15)

age_labels = [f"{g}\n(n={n})" for g, n in zip(by_age["age_group"], by_age["policies"])]
draw(axes[0], age_labels, by_age["avg_charges"], "Average charges by age group")
draw(axes[1], by_region["region"], by_region["avg_charges"], "Average charges by region")
draw(axes[2], by_smoker["smoker"], by_smoker["avg_charges"], "Average charges by smoker status")

plt.tight_layout()
plt.savefig("charts.png", dpi=150)
print("Saved charts.png")