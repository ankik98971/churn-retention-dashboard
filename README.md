# Churn & Retention Dashboard

**Problem:** A telecom provider is losing 27% of customers annually to churn, with month-to-month contracts driving the majority of attrition. Without visibility into which segments are at risk and what interventions are cost-effective, retention spend is reactive and inefficient.

**Approach:** This interactive dashboard segments customers by contract type and tenure, quantifies revenue at risk, and surfaces three ranked retention actions with estimated ROI — turning raw churn data into a stakeholder-ready action plan.

🔗 **Live Demo:** [https://your-app-name.streamlit.app](https://your-app-name.streamlit.app](https://churn-retention-dashboard-brg6vnuu3verqvj3x8karp.streamlit.app/)) *(update after deploying on Streamlit Community Cloud)*

<img width="1692" height="935" alt="Screenshot 2026-07-24 at 10 33 45 PM" src="https://github.com/user-attachments/assets/f4fd959f-0db2-4076-8d00-6b08bb779d66" />


## Approach

- **Business framing:** Churn is reframed as "revenue at risk" — an estimate of annualized lost revenue from churned customers — to speak the language of finance and customer-success stakeholders.
- **Segmentation:** Customers are filtered by contract type (the strongest churn predictor) and tenure, revealing that month-to-month customers churn at 3–4× the rate of annual-contract customers.
- **Recommendation:** Three retention actions are ranked by estimated ROI, with clear target segments, cost ranges, and revenue-saved estimates — ready for a VP of Customer Success to review and approve.
- **Dashboarding:** Built in a single Python file using Streamlit + Plotly, deployed with one click to Streamlit Community Cloud.

---

## What This Demonstrates

| BA Skill | How It's Shown |
|---|---|
| **Requirements framing** | Translated a raw business problem ("customers are leaving") into measurable metrics (churn rate, revenue at risk) |
| **Segmentation logic** | Identified contract type and tenure as the primary churn drivers through exploratory data patterns |
| **Stakeholder-ready recommendation** | Delivered ranked actions with cost/benefit estimates in a format a non-technical VP can act on in 5 minutes |
| **Dashboarding & data storytelling** | Interactive filters, color-coded risk visuals, and narrative context — not just charts |

---

## Dataset

The dataset used is a **synthetic illustration** (~500 rows) based on the well-known Telco Customer Churn dataset structure. It is designed to show realistic distributions (month-to-month contracts have higher churn, longer tenure reduces churn probability) so the dashboard tells a believable story for portfolio purposes.

---

## Deploy

1. Push this repo to GitHub (public).
2. Go to [share.streamlit.io](https://share.streamlit.io) → "New app" → select this repo, branch `main`, and `app.py` as the entry point.
3. Streamlit builds and gives you a live URL automatically.
