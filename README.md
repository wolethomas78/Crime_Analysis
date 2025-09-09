
![alt image](https://github.com/wolethomas78/Crime_Analysis/blob/0b739e09d3b566190af8057bd6a6cf5f2e750302/lapd_crime.png)

# Crime Data Dashboard & Public Safety Insights  
**Data Source**: LAPD Crime Data (2020–Present)  
**Metadata Updated**: July 12, 2025

This project features a dynamic and interactive dashboard that analyzes crime trends across Los Angeles from 2020 to the present. Using official LAPD crime report data, the dashboard empowers public safety professionals, policymakers, and community members with clear, data-driven insights.

---

## Table of Content
   - [Project Overview](#project-overview)
   - [Tools & Technologies](#tools--technologies)
   - [Data Source](#data-source)
   - [Important Notes](#important-notes)
   - [Target Audience](#target-audience)
   - [KPI](#kpi)
   - [Gendered Crime Tren ds](#gendered-crime-trends)
   - [Top 5 Crime Types (2020–2025)](#top-5-crime-types-2020-2025)
   - [Crime Committed by Status (2020–2025)](#crime-committed-by-status-2020-2025)
   - [Methodology](#methodology)
   - [Contact Me](#contact-me)



 



## Project Overview

### Goal  
Build a user-friendly, interactive dashboard to:

- Track and compare crime trends over time  
- Visualize crime types, frequencies, and locations  
- Identify affected victims based on gender and weapons used for crime  
- Support data-informed public safety decisions  

---

## Tools & Technologies

- **Python (Pandas)** – For data cleaning, transformation, and preprocessing  
- **Power BI** – For interactive visualization and dashboard development  
- **Excel** – For initial data handling and formatting  

---

## Data Source

- **Source**: LAPD crime reports (2020–Present)  
- Includes incident types, dates, times, and generalized locations (nearest hundred block)  
- Some fields may contain missing or redacted values (e.g., `(0°, 0°)` for location)  

---

## Important Notes

- On **March 7, 2024**, LAPD began transitioning to a new **NIBRS-compliant Records Management System**  
- Crime updates have temporarily shifted from **weekly** to **bi-weekly** as part of this transition  
- Data accuracy may vary due to transcription from original paper-based reports

  ## Target Audience

- Public safety officials and law enforcement analysts  
- City policymakers and planning departments  
- Journalists, researchers, and civic groups  
- Concerned residents and neighborhood organizations  

- ---

![alt image](https://github.com/wolethomas78/Crime_Analysis/blob/aec6be49626887f00ecafca1466e13d198a79767/kpiCrime.png)
## KPI: 
### YTD vs PYTD Crime and Reporting Lag (2020–2025)

This section tracks **Year-to-Date (YTD)** vs **Previous Year-to-Date (PYTD)** crime volumes and **Average Report Lag Days**, filtered by year and crime severity (`Not Severe`, `Severe`).

---

### KPI Visual Setup

- **KPI Cards**:
  -  Crime YTD & PYTD
  -  Avg Report Lag Days (YTD & PYTD)
- **Slicers**:
  - Year (2020–2025)
  - Crime Severity (Severe / Not Severe)

---

### Key Insights

- 🔸 **Lag Time Improvement**:  
  Report lag has decreased dramatically from 2020 to 2025 in both crime categories (e.g., Not Severe from 32.15 → 1.31 days).
  
- 🔸 **Crime Volume Trends**:  
  - From 2020–2023, crime counts steadily increased.
  - In **2024–2025**, both Not Severe and Severe crimes dropped sharply.

---

### Interpretation

- Decreasing report lag suggests operational efficiency gains and improved data systems.
- Sudden crime drops in 2024–2025 may reflect **NIBRS system transition**, **underreporting**, or **reporting delays**, not necessarily lower crime.

---

### Recommendations

1. **Enhance Real-Time Reporting**  
   → Expand mobile/digital tools to maintain low report lag times.

2. **Audit 2024–2025 Data Drops**  
   → Validate if declines are due to system change or real reductions.

3. **Create Monitoring Thresholds**  
   → Set automated alerts for major changes in crime count or lag time.



---
  ## Gendered Crime Trends
### Gender-Based Crime Victim Analysis (2020–2025)

This section of the dashboard analyzes gender distribution among crime victims from 2020 to 2025, categorized by **crime severity** (`Severe` vs `Not Severe`), using official LAPD data.

---

### Chart Referenced

![alt image](https://github.com/wolethomas78/Crime_Analysis/blob/8568ad54f4f8f5206d6114f3e2e6b69eb1390d1c/victim_gender.png)
- **Visual**: Single Pie Chart  
- **Slicers**:  
  - `Year` (2020–2025)  
  - `Crime Severity` (Severe / Not Severe)  
- **Values**: Victim Gender (%)

The pie chart dynamically updates to show the male-to-female ratio for the selected year and crime type.

---

### Key Observations

- **Not Severe Crimes (2020–2024)**: Female victims consistently outnumbered males.
- **Not Severe Crimes (2025)**: Reversal — male victims increased to 53.57%.
- **Severe Crimes**: Male victims dominate every year, peaking at **87.5% in 2025**.
- The **2025 severe crime gender split** is unusually extreme.

---

### Interpretation

- Not severe crimes affect **females more often**, especially in earlier years.
- Severe crimes are consistently **male-dominated**, suggesting higher male exposure to violent crime.
- The **2025 spike in male severe crime victims** and drop in female victims likely signals a data shift, reporting issue, or social trend.

---

### Impact

- Gender-targeted crime prevention policies may need to be **rebalanced**.
- Sudden changes in 2025 indicate a need to **validate reporting quality** after LAPD’s switch to the **NIBRS system**.
- Community safety strategies must adapt to **shifting victim profiles**.

---

### Recommendations

1. **Audit 2025 severe crime data** to verify anomaly or real trend shift.
2. **Adjust community programs**: Support women for minor crime prevention, target men for violence prevention.
3. **Monitor male victimization trends** — especially in 2025.
4. **Use this interactive pie chart** for ongoing crime pattern reviews.
5. **Document data limitations post-NIBRS transition** to maintain transparency.

---

![alt image](https://github.com/wolethomas78/Crime_Analysis/blob/20d9ec27ed5ebc48ea20b7cdc042bf821087bcdf/mnthlycrime.png)

## Monthly Crime Trend Analysis (2020–2025)

This section analyzes monthly crime volumes by severity type using slicers for year and crime classification (Not Severe vs Severe). It reveals key seasonal trends, reporting irregularities, and system-driven data gaps.

---

### Key Insights

#### Not Severe Crimes
- **Consistent seasonality (2020–2023)**: Higher crime in spring–fall; dips in winter months.
- **Sharp decline in 2024–2025**: Monthly volumes drop significantly; 2025 data nearly absent.

#### Severe Crimes
- **Strong upward trend (2020–2023)** with sustained high volumes.
- **Abrupt collapse in 2024–2025**, suggesting **reporting or system-level issues**.

---

### Interpretation

- Monthly patterns until 2023 suggest **predictable crime cycles** that can support seasonal policing strategies.
- The **abrupt drop** in 2024–2025 across both categories aligns with the **LAPD’s transition to NIBRS**, indicating **data disruption or delayed reporting**, not necessarily a real decline in crime.

---

### Recommendations

1. **Investigate RMS Transition Effects on 2024–2025 Data**
   - Confirm if low volumes stem from **technical disruptions, delayed integration**, or **data entry backlogs** caused by the NIBRS-compliant system transition.

2. **Use 2020–2023 Seasonality for Predictive Safety Planning**
   - Apply historical monthly trends to **pre-position law enforcement resources** in high-activity months (e.g., summer & holidays).

3. **Align Stakeholders on Data Transition Status**
   - Communicate clearly with policy teams, law enforcement, and community stakeholders that **2024–2025 data gaps are transitional**, not indicative of real-world crime reduction.

---


## Top 5 Crime Types (2020–2025)
![alt image](https://github.com/wolethomas78/Crime_Analysis/blob/b286589143cfd89cd905c20a2548a00c33671c26/top5.png)

### Chart Referenced
**Bar Chart** showing the **Top 5 crime types per year**, filtered using slicers for:
- **Year**
- **Crime Severity (Not Severe / Severe)**

---

### Observation

- **Not Severe Crimes (2020–2023):**
  - Consistently high: `Battery - Simple Assault`, `Vandalism (Felony)`, and `Theft of Identity`.
  - Notable increase in **identity theft**, peaking at **22.2K in 2022**.
  - `Intimate Partner - Simple Assault` also ranks high.
  - Sudden volume drop in **2024–2025** across all crimes.

- **Severe Crimes (2020 data shown):**
  - Top 5: `Vehicle Theft (20.8K)`, `Burglary`, `Assault with Deadly Weapon`, `Burglary from Vehicle`, and `Petty Theft`.
  - These represent **property and violent crimes** with the greatest social and economic impact.

---

### Interpretation

- **Criminal behavior patterns** remain consistent in earlier years, suggesting repeat-offense environments and persistent social factors.
- The **2024–2025 drop** likely reflects **reporting system transition issues (RMS/NIBRS)**, not actual crime reduction.
- **Vehicle-related crimes and assault** dominate severe categories, showing need for focused deterrents.

---

### Impact

- **Strategic planning risks** if stakeholders misinterpret 2024–2025 data as real declines.
- Informed resource allocation becomes challenging without **clarity on top crime drivers**.
- Missed opportunity for targeted policing in areas like **identity theft**, which is clearly rising.

---

### Recommendations

1. **Launch Focused Intervention Campaigns**
   - Design **community outreach, digital literacy, and neighborhood watch** initiatives around:
     - `Battery - Simple Assault`
     - `Identity Theft`
     - `Vehicle Theft`

2. **Use Historical Top 5 Trends for Predictive Policing**
   - Leverage 2020–2023 trends to build models that predict **likely top crimes in future months**.

3. **Prioritize High-Impact Crimes in Resource Deployment**
   - Law enforcement should **target top severe crimes** (e.g., stolen vehicles, burglary) with **tech-driven tracking and patrol shifts**.
     
---

## Crime Committed by Status (2020–2025)

![alt image](https://github.com/wolethomas78/Crime_Analysis/blob/31608d372ee375836845117115e14a72f29a1d6e/invst.png)

### Chart Referenced
**Matrix Table** displaying the number of crimes by **offender status**:
- **Status Types:** Investigation Continued, Adult Arrest, Adult Other, Juvenile Arrest, Juvenile Other
- **Slicers Used:** 
  - Year (2020–2025)
  - Crime Severity (Not Severe / Severe)

---

### Observation

- **Investigation Continued** status dominates for both severe and not severe crimes, making up **~75%–85%** of records.
- **Adult Arrests** remain relatively stable between **9K–11K** yearly (2020–2023), declining sharply in **2024–2025**.
- **Juvenile involvement** (arrests + other) remains low overall but increases in **2023**.
- **Significant drops in all categories** from **2024 onward**, with **2025 showing near-zero counts**, likely due to reporting issues.

---

### Interpretation

- High "Investigation Continued" figures suggest that a majority of cases **remain open or unresolved**, raising concern about **case closure rates**.
- Stable adult arrest numbers followed by sharp declines indicate a **data transition effect** tied to LAPD’s RMS/NIBRS migration.
- Juvenile crime, while lower in volume, shows **a gradual increase through 2023**, suggesting a trend worth monitoring.

---

### Impact

- **Operational bottlenecks** may exist in investigative workflows due to the large volume of unresolved cases.
- **Drop in 2024–2025 data** may lead to **misleading conclusions** if not flagged in dashboards.
- **Juvenile crime growth** in recent years could impact youth safety and community development if not addressed early.

---

### Recommendations

1. **Flag Transition-Impacted Years**
   - Clearly annotate **2024–2025** as years impacted by **reporting delays or system changes** in all visuals and exports.

2. **Audit Open Investigations**
   - Investigate the **backlog of continued cases**, especially in severe crimes, to evaluate **resource or procedural delays**.

3. **Enhance Arrest Reporting Integration**
   - Ensure arrest data is **fully integrated into new RMS/NIBRS systems** to restore trend continuity post-2023.

4. **Target Juvenile Crime with Early Interventions**
   - Launch **after-school programs, mentorship initiatives, and law enforcement-community partnerships** to reduce youth involvement.

---

## Methodology

- **Data Extraction:** Pulled crime data from the LAPD dataset (2020–2025) and structured it for analysis.
- **Data Cleaning & Transformation:** Used **Python (Pandas)** to clean, preprocess, and categorize crime by severity, victim gender, status, and report lag.
- **Data Aggregation:** Summarized key metrics such as:
  - Crime counts by year and month
  - Crime types (severe vs. not severe)
  - Victim demographics (gender)
  - Offender status
  - Report lag averages
- **Visualization:** Built an interactive dashboard in **Power BI** using slicers for:
  - Year
  - Crime severity
  - Crime category
  - Region and victim gender
- **Exploratory Analysis:** Conducted in-depth EDA to uncover:
  - Gender disparities by crime severity
  - Year-over-year changes in crime volume and reporting behavior
  - Shifts in top crime types
  - Arrest and investigation trends

---

  ## Contact Me
- Feel free to reach out via [LinkedIn](https://www.linkedin.com/in/oluwolefagbemi) or wolethomas78@gmail.com for questions or collaborations!

  ## Why This Project Matters

This dashboard highlights how **data-driven insights** can support **public safety efforts** and **policy-making**. By analyzing crime trends, victim demographics, and reporting behavior over time, it enables better-informed decisions by law enforcement, community leaders, and local governments. 

It also demonstrates technical proficiency in:
- Data preprocessing with Python (Pandas)
- Interactive visualization with Power BI
- Real-world storytelling with complex datasets

These are critical skills for careers in **data analytics**, **public policy**, and **business intelligence**.

