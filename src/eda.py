"""
Healthcare Data – Exploratory Data Analysis (EDA)
Run this script first to understand the dataset before generating visualizations.
"""

import pandas as pd
import numpy as np
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "Regional_Healthcare_Data.csv")
df = pd.read_csv(DATA_PATH)
df["visit_date"] = pd.to_datetime(df["visit_date"])

print("=" * 60)
print("REGIONAL HEALTHCARE DATASET – EDA SUMMARY")
print("=" * 60)

print(f"\n📦 Shape          : {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"📅 Date range     : {df['visit_date'].min().date()} → {df['visit_date'].max().date()}")
print(f"🏥 Hospitals      : {df['hospital_id'].nunique()} ({', '.join(sorted(df['hospital_id'].unique()))})")
print(f"🧑 Unique patients: {df['patient_id'].nunique():,}")

print("\n── Missing values ──────────────────────────────────────")
missing = df.isnull().sum()
print(missing[missing > 0] if missing.any() else "  None – dataset is complete ✓")

print("\n── Visit type distribution ─────────────────────────────")
print(df["visit_type"].value_counts().to_string())

print("\n── Insurance type distribution ─────────────────────────")
print(df["insurance_type"].value_counts().to_string())

print("\n── Chronic condition breakdown ─────────────────────────")
print(df["chronic_condition"].value_counts().to_string())

print("\n── Numeric summary ─────────────────────────────────────")
print(df[["age", "length_of_stay", "total_bill_amount",
          "lab_tests_ordered", "satisfaction_score"]].describe().round(2).to_string())

print("\n── Revenue by hospital ─────────────────────────────────")
rev = df.groupby("hospital_name")["total_bill_amount"].agg(["sum", "mean", "count"])
rev.columns = ["Total Revenue (INR)", "Avg Bill (INR)", "Visit Count"]
rev["Total Revenue (INR)"] = rev["Total Revenue (INR)"].map("{:,.0f}".format)
rev["Avg Bill (INR)"]      = rev["Avg Bill (INR)"].map("{:,.0f}".format)
print(rev.to_string())

print("\n── Readmission rate overall ────────────────────────────")
rate = (df["readmitted_30_days"] == "Yes").mean() * 100
print(f"  {rate:.2f}%")

print("\n── Readmission by visit type ───────────────────────────")
rt = df.groupby("visit_type").apply(
    lambda x: (x["readmitted_30_days"] == "Yes").mean() * 100
).round(2)
print(rt.to_string())

print("\n" + "=" * 60)
print("EDA complete.")
