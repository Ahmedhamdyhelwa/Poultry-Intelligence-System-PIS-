# Poultry-Intelligence-System-PIS-
End to End Data Analytics Project for Poultry Farm Operations
<div align="center">

# 🐔 Riyadh Doha Poultry Analytics

### From Raw Data to Predictive Intelligence

**An end-to-end data analytics & machine learning project for a real working poultry farm**

![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-B8504E?style=for-the-badge&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Tableau](https://img.shields.io/badge/Tableau-1F77B4?style=for-the-badge&logo=tableau&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Netlify](https://img.shields.io/badge/Netlify-00C7B7?style=for-the-badge&logo=netlify&logoColor=white)

[🌐 **Live Website**](https://dohaafarm.netlify.app/) &nbsp;·&nbsp; [📊 **Tableau Dashboard**](https://public.tableau.com/app/profile/asmaa.elshazly/viz/PRODUCTIONKPIS/Dashboard1?publish=yes)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Headline Results](#-headline-results)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Repository Structure](#-repository-structure)
- [The Pipeline — Stage by Stage](#-the-pipeline--stage-by-stage)
  - [1. Excel — Data Modeling & Cleaning](#1-excel--data-modeling--cleaning)
  - [2. SQL Server — Database Design](#2-sql-server--database-design)
  - [3. Python — Cleaning & Analysis](#3-python--cleaning--analysis)
  - [4. Tableau — Public Dashboard](#4-tableau--public-dashboard)
  - [5. Power BI — Interactive Dashboards](#5-power-bi--interactive-dashboards)
  - [6. Machine Learning — XGBoost Model](#6-machine-learning--xgboost-model)
  - [7. Streamlit — Predictive Web App](#7-streamlit--predictive-web-app)
  - [8. Live Web Dashboard](#8-live-web-dashboard)
- [Getting Started](#-getting-started)
- [Dataset](#-dataset)
- [Key Findings](#-key-findings)
- [Future Work](#-future-work)
- [Documentation](#-documentation)
- [Contact](#-contact)

---

## 🎯 Overview

This project takes the daily operational records of a real commercial layer poultry farm — **Riyadh Doha**, a ~75,000-bird operation — and turns them into a complete analytics platform. We move data through eight clean stages, from a messy multi-sheet Excel workbook all the way to a deployed website and a live profit-forecasting model.

**The mission:**
- Consolidate fragmented operational data (Farm Data, Financial Data, Feed Suppliers) into a single source of truth.
- Build a normalized SQL Server database so the data can be queried, audited, and joined.
- Deliver interactive BI dashboards covering Production, Feed, Suppliers, and Finance.
- Train an ML model that forecasts **next-week net profit** with strong out-of-sample accuracy.
- Make the whole thing accessible through a Streamlit app and a public website.

The project covers **March 2019 → May 2026** — roughly **5,200+ daily records** and **60+ derived columns** after cleaning.

---

## 🏆 Headline Results

<div align="center">

| 🥚 Total Eggs | 💰 Total Revenue | 📈 Net Profit | 🎯 Model R² |
|:---:|:---:|:---:|:---:|
| **124M** | **316M EGP** | **312M EGP** | **0.82** |
| 2019 – 2026 | Cumulative | Cumulative | Held-out test set |

</div>

---

## 🏗️ System Architecture

```
┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐
│  Raw Excel │ → │   Python   │ → │ SQL Server │ → │   Python   │ → │  Power BI  │ → │  XGBoost   │
│  Workbook  │   │  Cleaning  │   │    (3NF)   │   │  Analysis  │   │  + Tableau │   │ + Streamlit│
│  3 sheets  │   │   Pandas   │   │ Star-style │   │   Seaborn  │   │ Dashboards │   │  Web App   │
└────────────┘   └────────────┘   └────────────┘   └────────────┘   └────────────┘   └────────────┘
                                                                                            ↓
                                                                              ┌────────────────────────┐
                                                                              │  🌐 dohaafarm.netlify  │
                                                                              │      .app website       │
                                                                              └────────────────────────┘
```

Each layer is independently runnable, version-controlled, and produces an artifact that becomes the input for the next layer.

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| **Data Source** | Microsoft Excel (multi-sheet workbook) |
| **Database** | Microsoft SQL Server (T-SQL) |
| **Data Processing** | Python 3 · Pandas · NumPy |
| **Visualization (Python)** | Matplotlib · Seaborn |
| **Business Intelligence** | Microsoft Power BI · Tableau Public |
| **Machine Learning** | XGBoost · scikit-learn · joblib |
| **Web App** | Streamlit |
| **Hosting** | Netlify (website) · Tableau Public |

---

## 📂 Repository Structure

```
poultry-farm-analytics/
│
├── 📊 data/
│   └── المشروع_النهائي_تم.xlsx          # Master workbook (3 operational sheets)
│
├── 🐍 python/
│   ├── farm_project.py                    # Cleaning, merging, EDA, 5-panel dashboard
│   ├── appGP.py                           # Streamlit predictive web app
│   └── GP.ipynb                           # ML training notebook
│
├── 🗄️ sql/
│   └── SQLQuery1.sql                      # FarmManagementSystem schema + ETL
│
├── 📈 dashboards/
│   ├── powerbi/                           # .pbix file + screenshots
│   └── tableau/                           # .twbx file
│
├── 🤖 models/
│   └── weekly_profit_model2_final.pkl     # Trained XGBoost regressor
│
├── 🌐 website/                            # Source for dohaafarm.netlify.app
│
├── 📄 docs/
│   ├── Riyadh_Doha_Poultry_Analytics_Documentation.docx
│   └── Riyadh_Doha_Poultry_Analytics_Documentation.pdf
│
├── 🖼️ assets/                             # Screenshots used in docs & README
│
├── requirements.txt
└── README.md
```

---

## 🔄 The Pipeline — Stage by Stage

### 1. Excel — Data Modeling & Cleaning

The project deliberately starts inside Excel because that is where the farm's data actually lives.

**What we did in Excel:**
- Removed merged cells and stray totals rows that broke pivot tables.
- Standardized date formats across all three operational sheets.
- Verified that per-size egg quantities (Bashayer / Small / Medium / Large / Double) sum to the daily total.
- Replaced text placeholders (`N/A`, `-`) with empty cells so Python reads them as `NaN`.
- Built validation pivot tables to confirm row counts per year and detect missing days.
- Prototyped the **Farm × Financial Data** join inside Power Query before moving to Python.

> 💡 **Why start in Excel?** It builds stakeholder trust. Farm operations could verify the data line-by-line in the tool they already know before any Python script touched it.

---

### 2. SQL Server — Database Design

A normalized `FarmManagementSystem` database in **Third Normal Form**.

**Tables:**
| Table | Role | Key Columns |
|---|---|---|
| `Suppliers` | Dimension | `SupplierID`, `SupplierName`, `ContactNumber` |
| `FeedTypes` | Dimension | `FeedID`, `FeedName`, `Unit` |
| `FinanceCategories` | Dimension | `CategoryID`, `CategoryName` |
| `Staging_DailyOperations` | Staging | Receives the wide flat file |
| `DailyOperations` | **Fact** | `OperationID`, `OpDate`, all FKs, `Quantity`, `UnitPrice`, `TotalAmount` |

**Design highlights:**
- Surrogate `IDENTITY` keys on every dimension.
- `TotalAmount AS (Quantity * UnitPrice) PERSISTED` — computed at insert time and indexed.
- Foreign-key constraints enforced on every fact-table reference.
- A staging table receives the wide CSV; ETL then explodes it into the normalized model.

```sql
CREATE TABLE DailyOperations (
    OperationID  INT PRIMARY KEY IDENTITY(1,1),
    OpDate       DATE,
    SupplierID   INT,
    FeedID       INT,
    CategoryID   INT,
    Quantity     DECIMAL(10,2),
    UnitPrice    DECIMAL(18,2),
    TotalAmount  AS (Quantity * UnitPrice) PERSISTED,
    Notes        NVARCHAR(MAX),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
    FOREIGN KEY (FeedID)     REFERENCES FeedTypes(FeedID),
    FOREIGN KEY (CategoryID) REFERENCES FinanceCategories(CategoryID)
);
```

---

### 3. Python — Cleaning & Analysis

The script **`farm_project.py`** is the analytical engine. It reads the three Excel sheets, harmonizes their schemas, merges them on the date column, validates, and produces a multi-panel dashboard.

**Pipeline steps:**
1. Load three sheets with `pandas.read_excel`.
2. `clean_header()` normalizes column names (lowercase, no spaces, no parentheses).
3. Coerce `date` columns with `pd.to_datetime` across all three frames.
4. Deduplicate `df_finance`; forward-fill `df_farm`.
5. Aggregate suppliers from per-invoice → per-day totals.
6. Three-way merge → export `poultry_cleaned_full.csv`.

**Validation checks built in:**
- Logical check on profit and production ranges.
- Duplicate-row count (must be zero after merge).
- Per-column missing-value inspection.

**Five-panel static dashboard:**
- Top 10 weeks by HD%.
- Top 10 weeks by Net Profit.
- Egg distribution donut (Bashayer / Small / Medium / Large / Double).
- Weekly feed consumption trend.
- Long-term production stability.

---

### 4. Tableau — Public Dashboard

> 🔗 **Live:** [public.tableau.com/app/profile/asmaa.elshazly/viz/PRODUCTIONKPIS](https://public.tableau.com/app/profile/asmaa.elshazly/viz/PRODUCTIONKPIS/Dashboard1?publish=yes)

A shareable, free-to-view production KPIs dashboard. Designed for executive review and external reviewers who don't have a Microsoft account.

**Features:**
- Daily HD% over time with a moving-average overlay.
- Egg-size mix as an interactive stacked bar by year.
- Mortality vs Stock dual-axis line for flock stability.
- Top-N week ranker with a parameter control.
- Drillable date filter (2019 – 2026).

---

### 5. Power BI — Interactive Dashboards

Five interconnected report pages, each focused on one business domain. A navigation panel lives on every page.

| Page | Focus | Audience |
|---|---|---|
| **Executive Overview** | Headline KPIs, mortality, feed vs water | Owner / Manager |
| **Eggs Production** | Size mix, broken-eggs trend, yearly breakdown | Production Lead |
| **Feed Optimization** | Received vs consumed, water trend, FCR | Feed Procurement |
| **Suppliers Analytics** | Invoices, paid/unpaid, price per ton | Procurement / Finance |
| **Financial Analytics** | Revenue, cost gap, per-egg margin, net profit | Finance / Owner |

---

### 6. Machine Learning — XGBoost Model

A **weekly net profit forecasting model**. Given the previous weeks' production and financial indicators, predict next week's net profit.

**Problem formulation:**
- **Task:** Supervised regression
- **Target:** `net_profit` (weekly aggregation)
- **Split:** Last 20% of weeks held out chronologically — **no shuffling**.

**Feature engineering:**
- `age_week = age_day // 7`
- **Lag features:** `profit_lag_{1,2,4}`, `hd_lag_{1,2,4}`
- **Rolling means:** `roll_profit_{2,4,6}`, `roll_hd_{2,4,6}`

**Hyperparameters:**

| Param | Value | Rationale |
|---|---|---|
| `n_estimators` | 250 | Enough trees, regularized below |
| `learning_rate` | 0.03 | Slow learning, avoid overfit |
| `max_depth` | 3 | Shallow trees |
| `min_child_weight` | 10 | Forces meaningful leaf support |
| `subsample` | 0.70 | Row sub-sampling |
| `colsample_bytree` | 0.70 | Column sub-sampling |
| `reg_alpha` (L1) | 4.0 | Drive unimportant weights to zero |
| `reg_lambda` (L2) | 8.0 | Smooth remaining weights |

**Performance:**

<div align="center">

| Train R² | Test R² | Train MAE | Test MAE |
|:---:|:---:|:---:|:---:|
| 0.953 | **0.816** | 11,564 EGP | 24,666 EGP |

</div>

**Top features (by importance):**
1. `profit_lag_1` — last week's profit dominates
2. `roll_profit_2` — 2-week momentum
3. `HD%` — current flock productivity
4. `roll_profit_4` — 4-week trend
5. `eggs_daily` — production volume

---

### 7. Streamlit — Predictive Web App

**`appGP.py`** turns the trained model into an interactive web app that anyone can use — no Python required.

**Features:**
- Sidebar sliders for `HD%` and `Mortality Rate`.
- Number inputs for `Stock`, `Feed Consumption`, `Eggs Produced`, `Age (days)`.
- **Real-time prediction** updates on every input change — no submit button.
- Live model performance cards (Train/Test MAE & R²).
- Actual-vs-predicted plot for the held-out test set.
- Feature importance chart and correlation heatmap.

**Run it:**
```bash
pip install -r requirements.txt
streamlit run python/appGP.py
```

---

### 8. Live Web Dashboard

> 🌐 **Live:** [dohaafarm.netlify.app](https://dohaafarm.netlify.app/)

A public, branded website hosted on Netlify. Mirrors the Power BI navigation but with a warm, farm-context palette. Mobile-responsive so farm staff can read it on phones in the field.

**Sections:**
- **Executive Overview** — headline KPIs and yearly trends
- **Production & Egg Quality** — size mix, broken-egg trend
- **Feed & Resource Optimization** — feed and water consumption
- **Suppliers Analytics** — invoice status, supplier ranking
- **Financial Analytics** — revenue, cost gap, profit

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Microsoft SQL Server (LocalDB or Express is fine)
- Power BI Desktop (for the `.pbix` file)
- Tableau Desktop / Tableau Reader (for the `.twbx` file)

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/poultry-farm-analytics.git
cd poultry-farm-analytics

# 2. Set up a Python environment
python -m venv .venv
source .venv/bin/activate          # on Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Run the cleaning pipeline
python python/farm_project.py

# 4. Launch the Streamlit web app
streamlit run python/appGP.py
```

### `requirements.txt`

```
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.12
openpyxl>=3.1
scikit-learn>=1.3
xgboost>=2.0
joblib>=1.3
streamlit>=1.28
```

### Database setup

```bash
# In SQL Server Management Studio (or Azure Data Studio):
# Open sql/SQLQuery1.sql and execute against your server.
# This will:
#   1. Create the FarmManagementSystem database
#   2. Create dimension + fact tables
#   3. Populate from Staging_DailyOperations
```

---

## 📊 Dataset

The master workbook contains three operational sheets:

| Sheet | Rows | Columns | Grain |
|---|---|---|---|
| **Farm Data** | ~5,237 | 20 | One row per day |
| **Financial Data** | ~5,217 | 33 | One row per day |
| **Feed Suppliers** | ~2,499 | 13 | One row per invoice |

**Key columns:**
- **Farm Data:** `date`, `Stock`, `HD%`, `eggs_daily`, `broken_eggs`, `bashayer`, `small`, `medium`, `large`, `double`, `Feed_consumption_kg`, `Water_consumption`, `temp_avg`
- **Financial Data:** `date`, per-size unit prices and revenues, `total_revenue`, `total_cost`, `net_profit`
- **Feed Suppliers:** `date`, `invoice_number`, `supplier_id`, `feed_type`, `quantity_tons`, `protein_pct`, `total_cost_egp`, `payment_status`

> 📅 **Time coverage:** March 2019 → May 2026 (≈7 production cycles).

---

## 🔍 Key Findings

- 🥚 **Medium + Large eggs = ~70%** of total production volume.
- 💵 **Large eggs alone contribute 41.19%** of total egg revenue.
- 📉 **Broken-egg counts decline year-on-year** — quality systems are working.
- 💰 **Net profit stays steady at 41M – 47M EGP per year** from 2019 through 2025.
- ⚠️ **39% of supplier invoices remain unpaid** — flagged to finance.
- 🌾 **Feed consumption peaks in 2022**, then declines with stock reductions.
- 🤖 **`profit_lag_1` is the strongest predictor** of next-week profit — operational momentum matters most.

---

## 🔮 Future Work

- [ ] Automate daily ingestion via **Airflow** or **Power Automate**.
- [ ] Add **month-ahead** and **quarter-ahead** forecasting horizons.
- [ ] Integrate **external features**: weather, regional feed-price indices, holiday calendars.
- [ ] Re-build dashboards on a **live SQL Server connection** instead of cached extracts.
- [ ] Extend the model into **anomaly detection** for daily HD% drift alerts.
- [ ] **Containerize** the Streamlit app and add role-based authentication.

---

## 📚 Documentation

A full **34-page project documentation book** is included in `/docs`:

- 📄 [`Riyadh_Doha_Poultry_Analytics_Documentation.docx`](docs/Riyadh_Doha_Poultry_Analytics_Documentation.docx)
- 📄 [`Riyadh_Doha_Poultry_Analytics_Documentation.pdf`](docs/Riyadh_Doha_Poultry_Analytics_Documentation.pdf)

The book covers every chapter of this README in depth, with code blocks, screenshots, KPI cards, and analytical commentary.

---

## 🔗 Links

| Resource | URL |
|---|---|
| 🌐 **Live Website** | https://dohaafarm.netlify.app/ |
| 📊 **Tableau Public Dashboard** | https://public.tableau.com/app/profile/asmaa.elshazly/viz/PRODUCTIONKPIS/Dashboard1 |
| 📄 **Project Documentation (PDF)** | `docs/Riyadh_Doha_Poultry_Analytics_Documentation.pdf` |

---

## 📬 Contact

For questions, feedback, or collaboration:

- 💼 Open an [Issue](../../issues) on this repository
- 📧 Reach out via the contact info on the [project website](https://dohaafarm.netlify.app/)

---

<div align="center">

### ⭐ If this project was helpful, please consider starring the repo!

**Riyadh Doha Poultry Analytics** &nbsp;·&nbsp; *From Raw Data to Predictive Intelligence* &nbsp;·&nbsp; 2026

Built with ❤️ — Excel · SQL · Python · Tableau · Power BI · XGBoost · Streamlit · Netlify

</div>
