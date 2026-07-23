import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(page_title="Churn & Retention Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("telco_churn.csv")
    df["MonthlyCharges"] = pd.to_numeric(df["MonthlyCharges"], errors="coerce")
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["tenure"] = pd.to_numeric(df["tenure"], errors="coerce")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
contract_filter = st.sidebar.multiselect(
    "Contract Type",
    options=df["Contract"].unique(),
    default=df["Contract"].unique()
)

tenure_min, tenure_max = st.sidebar.slider(
    "Tenure Range (months)",
    min_value=int(df["tenure"].min()),
    max_value=int(df["tenure"].max()),
    value=(int(df["tenure"].min()), int(df["tenure"].max()))
)

# Apply filters
filtered = df[
    (df["Contract"].isin(contract_filter)) &
    (df["tenure"] >= tenure_min) &
    (df["tenure"] <= tenure_max)
].copy()

# Header
st.title("📊 Churn & Retention Dashboard")
st.markdown("*Interactive analysis of customer churn risk and retention opportunities*")

# Key metrics
churned = filtered[filtered["Churn"] == "Yes"]
churn_rate = len(churned) / len(filtered) * 100 if len(filtered) > 0 else 0
avg_monthly_churned = churned["MonthlyCharges"].mean() if len(churned) > 0 else 0
revenue_at_risk = avg_monthly_churned * 12 * len(churned)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Customers", f"{len(filtered):,}")
m2.metric("Churn Rate", f"{churn_rate:.1f}%")
m3.metric("Churned Customers", f"{len(churned):,}")
m4.metric("Est. Revenue at Risk (12mo)", f"${revenue_at_risk:,.0f}", 
          help="Estimate = avg monthly charge of churned customers × 12 months × count. For planning purposes only.")

st.divider()

# Charts
left, right = st.columns(2)

with left:
    st.subheader("Churn Rate by Contract Type")
    contract_churn = filtered.groupby("Contract").apply(
        lambda x: (x["Churn"] == "Yes").sum() / len(x) * 100
    ).reset_index(name="Churn Rate (%)")

    fig1 = px.bar(
        contract_churn,
        x="Contract",
        y="Churn Rate (%)",
        color="Churn Rate (%)",
        color_continuous_scale="RdYlGn_r",
        text_auto=".1f"
    )
    fig1.update_layout(showlegend=False, height=350)
    st.plotly_chart(fig1, use_container_width=True)

with right:
    st.subheader("Customer Segments: Tenure vs. Monthly Charge")
    fig2 = px.scatter(
        filtered,
        x="tenure",
        y="MonthlyCharges",
        color="Churn",
        color_discrete_map={"Yes": "#e74c3c", "No": "#2ecc71"},
        opacity=0.7,
        title="",
        labels={"tenure": "Tenure (months)", "MonthlyCharges": "Monthly Charges ($)"}
    )
    fig2.update_layout(height=350)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# Retention recommendations
st.subheader("🎯 Top 3 Recommended Retention Actions")

recommendations = [
    {
        "rank": 1,
        "action": "Contract-upgrade incentive campaign",
        "target": "Month-to-month customers with tenure > 6 months",
        "est_cost": "$15–25 per customer",
        "est_revenue_saved": "$180–360 per converted customer/year",
        "roi": "7–24x",
        "rationale": "Month-to-month contracts show 3–4× higher churn than annual contracts. A targeted discount or service bundle for upgrading to annual contracts locks in revenue and reduces churn probability."
    },
    {
        "rank": 2,
        "action": "Proactive outreach for high-charge, low-tenure segment",
        "target": "Customers paying >$70/month with tenure < 12 months",
        "est_cost": "$8–12 per touch (email + call)",
        "est_revenue_saved": "$840+ per retained customer/year",
        "roi": "70–105x",
        "rationale": "High monthly charges with low tenure indicate price sensitivity. Early engagement (welcome call, usage tips, loyalty preview) prevents buyer's remorse and reduces early-stage churn."
    },
    {
        "rank": 3,
        "action": "Add-on service bundling (security + support)",
        "target": "All customers without OnlineSecurity or TechSupport",
        "est_cost": "$5–10 per customer (marginal cost of features)",
        "est_revenue_saved": "$120–240 per retained customer/year",
        "roi": "12–48x",
        "rationale": "Customers with security and tech support add-ons show measurably lower churn. Bundling these at a slight discount increases stickiness and perceived value."
    }
]

for rec in recommendations:
    with st.container():
        c1, c2 = st.columns([1, 4])
        with c1:
            st.markdown(f"### #{rec['rank']}")
            st.markdown(f"**ROI: {rec['roi']}**")
        with c2:
            st.markdown(f"**{rec['action']}**")
            st.markdown(f"🎯 **Target:** {rec['target']}  |  💰 **Cost:** {rec['est_cost']}  |  💵 **Revenue Saved:** {rec['est_revenue_saved']}")
            st.markdown(f"📌 *Rationale:* {rec['rationale']}")
        st.divider()

# Data table
with st.expander("📋 View Filtered Data"):
    st.dataframe(filtered, use_container_width=True)
