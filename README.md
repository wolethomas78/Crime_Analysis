
![alt image](https://github.com/wolethomas78/Crime_Analysis/blob/e0bce7d834702f4fcebf542df408e815d076dc51/LAPDcrime.png)

# Crime Data Dashboard & Public Safety Insights  
**Data Source**: LAPD Crime Data (2020–Present)  
**Metadata Updated**: July 12, 2025

This project features a dynamic and interactive dashboard that analyzes crime trends across Los Angeles from 2020 to the present. Using official LAPD crime report data, the dashboard empowers public safety professionals, policymakers, and community members with clear, data-driven insights.

---

## Project Overview

### Goal  
Build a user-friendly, interactive dashboard to:

- Track and compare crime trends over time  
- Visualize crime types, frequencies, and locations  
- Identify hotspots and regional safety patterns  
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
## KPI Analysis: YTD vs PYTD Crime & Reporting Lag (2020–2025)

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

### Summary Recommendations

1. **Enhance Real-Time Reporting**  
   → Expand mobile/digital tools to maintain low report lag times.

2. **Audit 2024–2025 Data Drops**  
   → Validate if declines are due to system change or real reductions.

3. **Create Monitoring Thresholds**  
   → Set automated alerts for major changes in crime count or lag time.



---

## Gender-Based Crime Victim Analysis (2020–2025)

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







---

---


