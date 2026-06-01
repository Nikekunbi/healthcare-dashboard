# 🏥 Regional Healthcare Data Visualization

A Python-based data visualization project analyzing a regional healthcare system across **5 hospitals**, **5,000 patient visits**, and **full calendar year 2023**. The project covers clinical, operational, financial, and access-related analytics, culminating in an executive-level dashboard.

---

## 📋 Project Overview

| Item | Details |
|------|---------|
| **Dataset** | Regional Healthcare Data (synthetic) |
| **Rows** | 5,000 patient visits |
| **Date Range** | Jan 2023 – Dec 2023 |
| **Hospitals** | 5 (Apollo Regional, CityCare Hospital, GreenLife Hospital, Metro Health Center, Sunrise Medical) |
| **Tools** | Python · Pandas · Matplotlib · Seaborn |

---

## 📊 Key Findings

| KPI | Value |
|-----|-------|
| Total Patients Served | 5,000 |
| Total Revenue Generated | INR 75,109,920 |
| Average Satisfaction Score | 3.59 / 5 |
| 30-Day Readmission Rate | 17.18% |

---

## 🗂️ Project Structure

```
healthcare-dashboard/
├── data/
│   └── Regional_Healthcare_Data.csv      # Source dataset
├── src/
│   ├── eda.py                            # Exploratory data analysis
│   └── analysis.py                       # All charts + dashboard generator
├── outputs/
│   ├── charts/                           # Individual task visualizations
│   │   ├── task1_kpis.png
│   │   ├── task2_visit_types.png
│   │   ├── task3_revenue_by_hospital.png
│   │   ├── task4_revenue_insurance_stacked.png
│   │   ├── task5_revenue_visit_stacked.png
│   │   ├── task6_geospatial_map.png
│   │   ├── task7_insurance_pie.png
│   │   └── task8_readmission_line.png
│   └── dashboard/
│       └── executive_dashboard.png       # Part 2 executive dashboard
├── docs/
│   └── insights.md                       # Written analysis & insights
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/healthcare-dashboard.git
cd healthcare-dashboard
```

### 2. Set up a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the EDA
```bash
python src/eda.py
```

### 5. Generate all charts and the dashboard
```bash
python src/analysis.py
```

Charts are saved to `outputs/charts/` and the dashboard to `outputs/dashboard/`.

---

## 📈 Visualizations

### Part 1 – Individual Analytics Tasks

| Task | Visualization | Description |
|------|--------------|-------------|
| 1 | KPI Scorecards | Total patients, revenue, satisfaction, readmission rate |
| 2 | Bar Chart | Patient visit volume by type (OPD / IPD / Emergency) |
| 3 | Bar Chart | Total revenue by hospital |
| 4 | Stacked Bar Chart | Revenue by hospital broken down by insurance type |
| 5 | Stacked Bar Chart | Revenue by hospital broken down by visit type |
| 6 | Bubble Map | Hospital locations with visit volume encoded as bubble size |
| 7 | Pie Chart | Cost distribution across insurance types |
| 8 | Line Chart | Monthly 30-day readmission rate by visit type |

### Part 2 – Executive Dashboard

A single integrated dashboard combining KPI cards, visit volume, revenue by hospital, and monthly readmission trends — designed for healthcare leadership decision-making.

---

## 💡 Key Insights

- **OPD dominates** visit volume (53%), but **IPD drives the highest revenue per visit** due to longer stays and higher billing.
- **Metro Health Center** leads in total revenue (INR 15.9M), while **Apollo Regional** records the lowest (INR 14.4M).
- **Private insurance** accounts for the largest share of total revenue (~45%), followed by Government and Self-pay.
- **30-day readmission rate** is notably higher for OPD patients (18.0%) than for Emergency (16.6%) or IPD (16.1%), suggesting a gap in post-visit follow-up for outpatients.
- Revenue distribution is relatively balanced across hospitals, indicating uniform patient load sharing across the network.

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Pandas** – data loading, cleaning, aggregation
- **Matplotlib** – all chart rendering
- **Seaborn** – style and color palette support
- **NumPy** – numerical operations

---

## 📄 License

This project uses a synthetic dataset generated for educational purposes. All code is available under the [MIT License](LICENSE).
