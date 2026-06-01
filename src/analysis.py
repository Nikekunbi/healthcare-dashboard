"""
Healthcare Data Visualization - Analysis Script
Generates all KPIs and charts for the assignment.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np
import os

# ── Setup ──────────────────────────────────────────────────────────────────────
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "Regional_Healthcare_Data.csv")
CHARTS_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs", "charts")
DASHBOARD_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs", "dashboard")
os.makedirs(CHARTS_DIR, exist_ok=True)
os.makedirs(DASHBOARD_DIR, exist_ok=True)

PALETTE = {
    "primary":   "#1B4F8A",
    "secondary": "#2E86AB",
    "accent":    "#E84855",
    "green":     "#3BB273",
    "orange":    "#F78C6B",
    "light":     "#EEF4FB",
    "gray":      "#6B7280",
}

INSURANCE_COLORS = {
    "Government": "#1B4F8A",
    "Private":    "#2E86AB",
    "Self-pay":   "#E84855",
}

VISIT_COLORS = {
    "OPD":       "#1B4F8A",
    "IPD":       "#2E86AB",
    "Emergency": "#E84855",
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})

# ── Load data ─────────────────────────────────────────────────────────────────
df = pd.read_csv(DATA_PATH)
df["visit_date"] = pd.to_datetime(df["visit_date"])
df["year_month"] = df["visit_date"].dt.to_period("M")

print(f"Dataset loaded: {len(df):,} rows, {df.shape[1]} columns")

# ══════════════════════════════════════════════════════════════════════════════
# TASK 1 – KPIs
# ══════════════════════════════════════════════════════════════════════════════

total_patients    = df["patient_id"].nunique()
total_revenue     = df["total_bill_amount"].sum()
avg_satisfaction  = df["satisfaction_score"].mean()
readmission_rate  = (df["readmitted_30_days"] == "Yes").mean() * 100

kpis = {
    "Total Patients Served":         (f"{total_patients:,}",        "#1B4F8A", "PATIENTS"),
    "Total Revenue (INR)":           (f"INR {total_revenue:,.0f}",  "#3BB273", "REVENUE"),
    "Avg Satisfaction Score":        (f"{avg_satisfaction:.2f} / 5", "#F78C6B", "SATISFACTION"),
    "30-Day Readmission Rate":       (f"{readmission_rate:.1f}%",   "#E84855", "READMISSION"),
}

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
fig.patch.set_facecolor("#F0F4F8")

for ax, (label, (value, color, icon)) in zip(axes, kpis.items()):
    ax.set_facecolor("white")
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    ax.text(0.5, 0.72, icon, ha="center", va="center", fontsize=10,
            fontweight="bold", color=color, alpha=0.4, transform=ax.transAxes)
    ax.text(0.5, 0.45, value, ha="center", va="center", fontsize=22,
            fontweight="bold", color=color, transform=ax.transAxes)
    ax.text(0.5, 0.18, label, ha="center", va="center", fontsize=10,
            color=PALETTE["gray"], transform=ax.transAxes, wrap=True)
    ax.add_patch(mpatches.FancyBboxPatch((0.02, 0.02), 0.96, 0.96,
        boxstyle="round,pad=0.02", linewidth=2,
        edgecolor=color, facecolor="white", transform=ax.transAxes, zorder=-1))
    ax.add_patch(mpatches.FancyBboxPatch((0.02, 0.02), 0.96, 0.04,
        boxstyle="round,pad=0", linewidth=0,
        facecolor=color, transform=ax.transAxes, zorder=-1))

fig.suptitle("Healthcare System – Key Performance Indicators", fontsize=14,
             fontweight="bold", color=PALETTE["primary"], y=1.01)
plt.tight_layout(pad=1.5)
plt.savefig(os.path.join(CHARTS_DIR, "task1_kpis.png"), bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.close()
print("✅ Task 1 – KPIs saved")

# ══════════════════════════════════════════════════════════════════════════════
# TASK 2 – Visit Types Bar Chart
# ══════════════════════════════════════════════════════════════════════════════

visit_counts = df["visit_type"].value_counts().reindex(["OPD", "IPD", "Emergency"])

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(visit_counts.index, visit_counts.values,
              color=[VISIT_COLORS[v] for v in visit_counts.index],
              width=0.5, edgecolor="white", linewidth=1.5)

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 30,
            f"{int(bar.get_height()):,}", ha="center", va="bottom",
            fontsize=11, fontweight="bold", color=PALETTE["primary"])

ax.set_title("Patient Visit Volume by Visit Type", fontsize=14,
             fontweight="bold", color=PALETTE["primary"], pad=15)
ax.set_xlabel("Visit Type", fontsize=11, labelpad=8)
ax.set_ylabel("Number of Visits", fontsize=11, labelpad=8)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax.set_facecolor(PALETTE["light"])
fig.patch.set_facecolor("white")
ax.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "task2_visit_types.png"), bbox_inches="tight")
plt.close()
print("✅ Task 2 – Visit types bar chart saved")

# ══════════════════════════════════════════════════════════════════════════════
# TASK 3 – Financial Performance by Hospital
# ══════════════════════════════════════════════════════════════════════════════

rev_by_hospital = (df.groupby("hospital_name")["total_bill_amount"]
                   .sum().sort_values(ascending=False))

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(rev_by_hospital.index, rev_by_hospital.values / 1e6,
              color=PALETTE["primary"], width=0.5, edgecolor="white", linewidth=1.5)

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
            f"₹{bar.get_height():.1f}M", ha="center", va="bottom",
            fontsize=10, fontweight="bold", color=PALETTE["primary"])

ax.set_title("Total Revenue by Hospital", fontsize=14,
             fontweight="bold", color=PALETTE["primary"], pad=15)
ax.set_xlabel("Hospital", fontsize=11, labelpad=8)
ax.set_ylabel("Total Revenue (₹ Millions)", fontsize=11, labelpad=8)
ax.set_facecolor(PALETTE["light"])
fig.patch.set_facecolor("white")
ax.grid(axis="y", linestyle="--", alpha=0.5)
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "task3_revenue_by_hospital.png"), bbox_inches="tight")
plt.close()
print("✅ Task 3 – Revenue by hospital saved")

# ══════════════════════════════════════════════════════════════════════════════
# TASK 4 – Stacked Bar: Revenue by Hospital × Insurance Type
# ══════════════════════════════════════════════════════════════════════════════

rev_ins = (df.groupby(["hospital_name", "insurance_type"])["total_bill_amount"]
           .sum().unstack(fill_value=0) / 1e6)
rev_ins = rev_ins.loc[rev_by_hospital.index]  # sort by total revenue

fig, ax = plt.subplots(figsize=(11, 6))
bottom = np.zeros(len(rev_ins))
for ins_type in ["Government", "Private", "Self-pay"]:
    if ins_type in rev_ins.columns:
        ax.bar(rev_ins.index, rev_ins[ins_type], bottom=bottom,
               label=ins_type, color=INSURANCE_COLORS[ins_type],
               width=0.5, edgecolor="white", linewidth=1)
        bottom += rev_ins[ins_type].values

ax.set_title("Total Revenue by Hospital and Insurance Type", fontsize=14,
             fontweight="bold", color=PALETTE["primary"], pad=15)
ax.set_xlabel("Hospital", fontsize=11, labelpad=8)
ax.set_ylabel("Revenue (₹ Millions)", fontsize=11, labelpad=8)
ax.legend(title="Insurance Type", bbox_to_anchor=(1.01, 1), loc="upper left")
ax.set_facecolor(PALETTE["light"])
fig.patch.set_facecolor("white")
ax.grid(axis="y", linestyle="--", alpha=0.5)
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "task4_revenue_insurance_stacked.png"), bbox_inches="tight")
plt.close()
print("✅ Task 4 – Revenue × Insurance stacked bar saved")

# ══════════════════════════════════════════════════════════════════════════════
# TASK 5 – Stacked Bar: Revenue by Hospital × Visit Type
# ══════════════════════════════════════════════════════════════════════════════

rev_visit = (df.groupby(["hospital_name", "visit_type"])["total_bill_amount"]
             .sum().unstack(fill_value=0) / 1e6)
rev_visit = rev_visit.loc[rev_by_hospital.index]

fig, ax = plt.subplots(figsize=(11, 6))
bottom = np.zeros(len(rev_visit))
for vtype in ["OPD", "IPD", "Emergency"]:
    if vtype in rev_visit.columns:
        ax.bar(rev_visit.index, rev_visit[vtype], bottom=bottom,
               label=vtype, color=VISIT_COLORS[vtype],
               width=0.5, edgecolor="white", linewidth=1)
        bottom += rev_visit[vtype].values

ax.set_title("Revenue Impact of Visit Type by Hospital", fontsize=14,
             fontweight="bold", color=PALETTE["primary"], pad=15)
ax.set_xlabel("Hospital", fontsize=11, labelpad=8)
ax.set_ylabel("Revenue (₹ Millions)", fontsize=11, labelpad=8)
ax.legend(title="Visit Type", bbox_to_anchor=(1.01, 1), loc="upper left")
ax.set_facecolor(PALETTE["light"])
fig.patch.set_facecolor("white")
ax.grid(axis="y", linestyle="--", alpha=0.5)
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "task5_revenue_visit_stacked.png"), bbox_inches="tight")
plt.close()
print("✅ Task 5 – Revenue × Visit Type stacked bar saved")

# ══════════════════════════════════════════════════════════════════════════════
# TASK 6 – Geospatial Map (Bubble Chart)
# ══════════════════════════════════════════════════════════════════════════════

hospital_geo = (df.groupby(["hospital_name", "latitude", "longitude"])
                .size().reset_index(name="visit_volume"))

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_facecolor("#D6EAF8")
fig.patch.set_facecolor("white")

scatter = ax.scatter(
    hospital_geo["longitude"], hospital_geo["latitude"],
    s=hospital_geo["visit_volume"] / 3,
    c=PALETTE["primary"], alpha=0.7, edgecolors="white", linewidth=2, zorder=5
)

for _, row in hospital_geo.iterrows():
    ax.annotate(
        f"{row['hospital_name']}\n({row['visit_volume']:,} visits)",
        (row["longitude"], row["latitude"]),
        textcoords="offset points", xytext=(10, 8),
        fontsize=8.5, color=PALETTE["primary"], fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8, edgecolor=PALETTE["secondary"])
    )

# Legend for bubble size
for size in [300, 700, 1100]:
    ax.scatter([], [], s=size / 3, c=PALETTE["primary"], alpha=0.7,
               label=f"{size} visits", edgecolors="white", linewidth=1.5)

ax.legend(title="Visit Volume", loc="lower left", fontsize=9, title_fontsize=9)
ax.set_title("Geospatial Healthcare Access – Hospital Locations & Patient Volume",
             fontsize=13, fontweight="bold", color=PALETTE["primary"], pad=15)
ax.set_xlabel("Longitude", fontsize=10)
ax.set_ylabel("Latitude", fontsize=10)
ax.grid(True, linestyle="--", alpha=0.4, zorder=0)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "task6_geospatial_map.png"), bbox_inches="tight")
plt.close()
print("✅ Task 6 – Geospatial map saved")

# ══════════════════════════════════════════════════════════════════════════════
# TASK 7 – Insurance Distribution Pie Chart
# ══════════════════════════════════════════════════════════════════════════════

ins_rev = df.groupby("insurance_type")["total_bill_amount"].sum()
colors  = [INSURANCE_COLORS[k] for k in ins_rev.index]

fig, ax = plt.subplots(figsize=(7, 6))
wedges, texts, autotexts = ax.pie(
    ins_rev.values,
    labels=ins_rev.index,
    autopct="%1.1f%%",
    colors=colors,
    startangle=140,
    pctdistance=0.75,
    wedgeprops=dict(edgecolor="white", linewidth=2),
    explode=[0.04] * len(ins_rev),
)
for t in autotexts:
    t.set_fontsize(11)
    t.set_fontweight("bold")
    t.set_color("white")
for t in texts:
    t.set_fontsize(11)

# Centre annotation
ax.text(0, 0, f"Total\n₹{ins_rev.sum()/1e6:.1f}M",
        ha="center", va="center", fontsize=11, fontweight="bold",
        color=PALETTE["primary"])

ax.set_title("Cost Distribution by Insurance Type", fontsize=14,
             fontweight="bold", color=PALETTE["primary"], pad=15)
fig.patch.set_facecolor("white")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "task7_insurance_pie.png"), bbox_inches="tight")
plt.close()
print("✅ Task 7 – Insurance pie chart saved")

# ══════════════════════════════════════════════════════════════════════════════
# TASK 8 – Monthly Readmission Rate by Visit Type (Line Chart)
# ══════════════════════════════════════════════════════════════════════════════

df["readmitted_bin"] = (df["readmitted_30_days"] == "Yes").astype(int)
monthly_readmit = (df.groupby(["year_month", "visit_type"])["readmitted_bin"]
                   .mean().reset_index())
monthly_readmit["year_month_str"] = monthly_readmit["year_month"].astype(str)
monthly_readmit["rate_pct"] = monthly_readmit["readmitted_bin"] * 100

fig, ax = plt.subplots(figsize=(13, 5))
for vtype, grp in monthly_readmit.groupby("visit_type"):
    grp = grp.sort_values("year_month")
    ax.plot(grp["year_month_str"], grp["rate_pct"],
            marker="o", markersize=5, linewidth=2,
            label=vtype, color=VISIT_COLORS[vtype])

ax.set_title("Monthly 30-Day Readmission Rate by Visit Type", fontsize=14,
             fontweight="bold", color=PALETTE["primary"], pad=15)
ax.set_xlabel("Month", fontsize=11, labelpad=8)
ax.set_ylabel("Readmission Rate (%)", fontsize=11, labelpad=8)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:.0f}%"))
ax.legend(title="Visit Type", fontsize=10)
ax.set_facecolor(PALETTE["light"])
fig.patch.set_facecolor("white")
ax.grid(axis="y", linestyle="--", alpha=0.5)
plt.xticks(rotation=45, ha="right", fontsize=8)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "task8_readmission_line.png"), bbox_inches="tight")
plt.close()
print("✅ Task 8 – Readmission line chart saved")

# ══════════════════════════════════════════════════════════════════════════════
# PART 2 – Executive Dashboard (single figure)
# ══════════════════════════════════════════════════════════════════════════════

fig = plt.figure(figsize=(20, 14), facecolor="#EEF4FB")
fig.suptitle("Regional Healthcare System – Executive Dashboard",
             fontsize=18, fontweight="bold", color=PALETTE["primary"], y=0.97)

gs = fig.add_gridspec(3, 4, hspace=0.45, wspace=0.35,
                       top=0.92, bottom=0.05, left=0.05, right=0.97)

# ── Row 0: KPI Cards ──────────────────────────────────────────────────────────
kpi_data = [
    ("Total Patients", f"{total_patients:,}", PALETTE["primary"]),
    ("Total Revenue", f"INR {total_revenue/1e6:.1f}M", PALETTE["green"]),
    ("Avg Satisfaction", f"{avg_satisfaction:.2f} / 5", PALETTE["orange"]),
    ("30-Day Readmission", f"{readmission_rate:.1f}%", PALETTE["accent"]),
]
for col, (label, value, color) in enumerate(kpi_data):
    ax = fig.add_subplot(gs[0, col])
    ax.set_facecolor("white")
    for sp in ax.spines.values(): sp.set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    ax.text(0.5, 0.60, value, ha="center", va="center", fontsize=18,
            fontweight="bold", color=color, transform=ax.transAxes)
    ax.text(0.5, 0.20, label, ha="center", va="center", fontsize=9,
            color=PALETTE["gray"], transform=ax.transAxes)
    for spine in ["top", "left", "right", "bottom"]:
        ax.spines[spine].set_visible(True)
        ax.spines[spine].set_color(color)
        ax.spines[spine].set_linewidth(1.5)

# ── Row 1 Left: Visit Volume by Visit Type ────────────────────────────────────
ax2 = fig.add_subplot(gs[1, :2])
bars = ax2.bar(visit_counts.index, visit_counts.values,
               color=[VISIT_COLORS[v] for v in visit_counts.index],
               width=0.45, edgecolor="white")
for bar in bars:
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 20,
             f"{int(bar.get_height()):,}", ha="center", fontsize=9,
             fontweight="bold", color=PALETTE["primary"])
ax2.set_title("Visit Volume by Type", fontsize=11, fontweight="bold",
              color=PALETTE["primary"])
ax2.set_facecolor(PALETTE["light"])
ax2.grid(axis="y", linestyle="--", alpha=0.4)
ax2.spines["top"].set_visible(False); ax2.spines["right"].set_visible(False)

# ── Row 1 Right: Revenue by Hospital ─────────────────────────────────────────
ax3 = fig.add_subplot(gs[1, 2:])
h_bars = ax3.barh(rev_by_hospital.index, rev_by_hospital.values / 1e6,
                  color=PALETTE["secondary"], edgecolor="white")
for bar in h_bars:
    ax3.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2,
             f"₹{bar.get_width():.1f}M", va="center", fontsize=9,
             fontweight="bold", color=PALETTE["primary"])
ax3.set_title("Revenue by Hospital (₹M)", fontsize=11, fontweight="bold",
              color=PALETTE["primary"])
ax3.set_facecolor(PALETTE["light"])
ax3.grid(axis="x", linestyle="--", alpha=0.4)
ax3.spines["top"].set_visible(False); ax3.spines["right"].set_visible(False)
ax3.invert_yaxis()

# ── Row 2: Monthly Readmission Lines ─────────────────────────────────────────
ax4 = fig.add_subplot(gs[2, :])
for vtype, grp in monthly_readmit.groupby("visit_type"):
    grp = grp.sort_values("year_month")
    ax4.plot(grp["year_month_str"], grp["rate_pct"],
             marker="o", markersize=4, linewidth=2,
             label=vtype, color=VISIT_COLORS[vtype])
ax4.set_title("Monthly 30-Day Readmission Rate by Visit Type",
              fontsize=11, fontweight="bold", color=PALETTE["primary"])
ax4.set_ylabel("Readmission Rate (%)")
ax4.legend(title="Visit Type", fontsize=9, loc="upper right")
ax4.set_facecolor(PALETTE["light"])
ax4.grid(axis="y", linestyle="--", alpha=0.4)
ax4.spines["top"].set_visible(False); ax4.spines["right"].set_visible(False)
plt.setp(ax4.get_xticklabels(), rotation=45, ha="right", fontsize=7)

plt.savefig(os.path.join(DASHBOARD_DIR, "executive_dashboard.png"),
            bbox_inches="tight", facecolor=fig.get_facecolor(), dpi=150)
plt.close()
print("✅ Part 2 – Executive dashboard saved")
print("\n🎉 All outputs generated successfully!")
