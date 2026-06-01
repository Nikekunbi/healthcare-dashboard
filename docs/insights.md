# Healthcare Analytics – Key Insights

## Dataset Overview

The Regional Healthcare Dataset covers 5,000 patient visits across 5 hospitals in 4 Indian cities (Chennai, Kochi, Pune, Delhi, Mumbai) during the full calendar year 2023. Each row represents a single patient visit with clinical, operational, and financial attributes.

---

## Task 1 – Key Performance Indicators

| KPI | Value |
|-----|-------|
| Total Patients Served | 5,000 |
| Total Revenue | INR 75,109,920 (~INR 75.1M) |
| Average Satisfaction Score | 3.59 / 5.0 |
| 30-Day Readmission Rate | 17.18% |

**Insight:** The satisfaction score of 3.59/5 is below the healthcare industry benchmark of 4.0, indicating room for improvement in patient experience. The 17.18% readmission rate is above the typical target of ≤15%, warranting further clinical review.

---

## Task 2 – Visit Type Analysis

| Visit Type | Count | Share |
|-----------|-------|-------|
| OPD | 2,672 | 53.4% |
| IPD | 1,521 | 30.4% |
| Emergency | 807 | 16.1% |

**Insight:** Over half of all visits are outpatient (OPD). This is expected for a multi-hospital system. However, Emergency accounts for 16%, which may indicate a need for stronger primary care to prevent emergency escalations.

---

## Task 3 – Financial Performance by Hospital

| Hospital | Total Revenue (INR) |
|----------|-------------------|
| Metro Health Center | 15,923,524 |
| GreenLife Hospital | 15,071,384 |
| Sunrise Medical | 15,062,397 |
| CityCare Hospital | 14,650,887 |
| Apollo Regional | 14,401,728 |

**Insight:** Revenue is distributed fairly evenly across hospitals (range: INR 1.5M), suggesting balanced patient distribution. Metro Health Center leads, likely due to a higher proportion of IPD admissions with longer stays.

---

## Task 4 – Insurance Type Breakdown by Hospital

**Insight:** Private insurance consistently contributes the largest revenue share (~45%) across all hospitals. Self-pay patients represent the smallest share but carry the highest financial risk for collections. Hospitals should consider targeted financial counseling for self-pay patients to reduce bad debt.

---

## Task 5 – Visit Type Revenue by Hospital

**Insight:** IPD visits, despite lower volume, generate disproportionately higher revenue due to multi-day stays and higher billing. All hospitals show similar IPD/OPD revenue split, confirming system-wide consistency. Emergency revenue is the smallest segment, as many emergency visits may be short or triaged to OPD.

---

## Task 6 – Geospatial Healthcare Access

**Insight:** The five hospitals span India's major metros (Chennai, Kochi, Pune, Delhi, Mumbai), with roughly equal patient volumes per location (~1,000 visits each). Geographic distribution is well spread, though urban concentration remains a limitation — rural patients may have limited access.

---

## Task 7 – Insurance and Payment Distribution

| Insurance Type | Revenue Share |
|---------------|--------------|
| Private | ~45% |
| Government | ~39% |
| Self-pay | ~15% |

**Insight:** Government insurance patients form a significant proportion (39%), highlighting the hospital network's public health role. The 15% self-pay share should be monitored for payment defaults.

---

## Task 8 – Monthly Readmission Rate Trends

**Insight:** OPD readmission rates (avg ~18%) consistently exceed IPD and Emergency rates throughout the year. This is counterintuitive — outpatients are readmitted more often than inpatients — pointing to potential gaps in discharge planning, follow-up care, or care continuity for outpatient visits. Peaks in certain months (e.g., winter months) may correlate with seasonal illness spikes.

---

## Part 2 – Executive Dashboard Design Rationale

The executive dashboard places KPI scorecards at the top for immediate at-a-glance awareness, followed by visit volume and revenue charts for operational context, and the readmission trend line at the bottom to highlight the most actionable clinical metric. This layout mirrors the natural decision flow of healthcare leadership: first understand scale (KPIs), then understand distribution (charts), then identify risk trends (readmission). A consistent blue color palette reinforces institutional trust and readability.
