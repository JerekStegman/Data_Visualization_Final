import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
import numpy as np

file_path = "thyroid_cancer_risk_data.csv"  
df = pd.read_csv(file_path)

sns.set_style("whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

sns.countplot(data=df, x="Thyroid_Cancer_Risk", hue="Thyroid_Cancer_Risk", order=["Low", "Medium", "High"], palette="coolwarm", ax=axes[0, 0], legend=False)
axes[0, 0].set_title("Thyroid Cancer Risk Distribution", fontsize=14)
axes[0, 0].set_ylabel("Count")

risk_factors = ["Family_History", "Radiation_Exposure", "Iodine_Deficiency", "Smoking", "Obesity", "Diabetes"]
df_melted = df.melt(id_vars=["Thyroid_Cancer_Risk"], value_vars=risk_factors, var_name="Risk Factor", value_name="Presence")

sns.histplot(data=df_melted[df_melted["Presence"] == "Yes"], x="Risk Factor", hue="Thyroid_Cancer_Risk",
             multiple="stack", palette="coolwarm", ax=axes[0, 1])
axes[0, 1].set_title("Risk Factors and Thyroid Cancer Risk", fontsize=14)
axes[0, 1].set_ylabel("Count")
axes[0, 1].tick_params(axis='x', rotation=45)

sns.boxplot(data=df, x="Thyroid_Cancer_Risk", y="TSH_Level", hue="Thyroid_Cancer_Risk", palette="coolwarm", ax=axes[1, 0], legend=False)
axes[1, 0].set_title("TSH Levels Across Cancer Risk Categories", fontsize=14)

sns.boxplot(data=df, x="Diagnosis", y="Nodule_Size", hue="Diagnosis", palette="coolwarm", ax=axes[1, 1], legend=False)
axes[1, 1].set_title("Nodule Size Comparison: Benign vs. Malignant", fontsize=14)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x="Thyroid_Cancer_Risk", y="TSH_Level", hue="Gender", split=True, palette="Spectral")
plt.title("Violin Plot of TSH Levels by Cancer Risk and Gender", fontsize=16)
plt.xlabel("Thyroid Cancer Risk Level")
plt.ylabel("TSH Level")
plt.legend(title="Gender", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()








