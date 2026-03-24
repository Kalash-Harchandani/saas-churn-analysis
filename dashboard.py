import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

st.set_page_config(page_title="SaaS Churn Dashboard", layout="wide")

st.title("SaaS Churn Analytics Dashboard")
st.markdown("Interactive dashboard displaying key drivers of customer attrition.")

@st.cache_data
def load_data():
    accounts = pd.read_csv("data/ravenstack_accounts.csv")
    subscriptions = pd.read_csv("data/ravenstack_subscriptions.csv")
    feature_usage = pd.read_csv("data/ravenstack_feature_usage.csv")
    support_tickets = pd.read_csv("data/ravenstack_support_tickets.csv")
    churn_events = pd.read_csv("data/ravenstack_churn_events.csv")
    
    accounts['signup_date'] = pd.to_datetime(accounts['signup_date'])
    subscriptions['start_date'] = pd.to_datetime(subscriptions['start_date'])
    subscriptions['end_date'] = pd.to_datetime(subscriptions['end_date'])
    feature_usage['usage_date'] = pd.to_datetime(feature_usage['usage_date'])
    support_tickets['submitted_at'] = pd.to_datetime(support_tickets['submitted_at'])
    support_tickets['closed_at'] = pd.to_datetime(support_tickets['closed_at'])
    churn_events['churn_date'] = pd.to_datetime(churn_events['churn_date'])
    
    # 2. Aggregations on Unique Accounts
    usage_acc = feature_usage.merge(subscriptions[['subscription_id', 'account_id']], on='subscription_id', how='inner')
    usage_agg = usage_acc.groupby('account_id')['usage_count'].sum().reset_index()
    tickets_agg = support_tickets.groupby('account_id').size().reset_index(name='ticket_count')
    churn_events['is_churned'] = 1
    churn_agg = churn_events[['account_id', 'is_churned', 'churn_date', 'reason_code']]
    
    # 3. Merging cleanly to Base Accounts
    master_df = accounts.copy()
    master_df = master_df.merge(usage_agg, on='account_id', how='left')
    master_df['usage_count'] = master_df['usage_count'].fillna(0)
    master_df = master_df.merge(tickets_agg, on='account_id', how='left')
    master_df['ticket_count'] = master_df['ticket_count'].fillna(0)
    master_df = master_df.merge(churn_agg, on='account_id', how='left')
    master_df['is_churned'] = master_df['is_churned'].fillna(0).astype('int')
    
    today = pd.to_datetime("today")
    master_df['tenure_days'] = (master_df['churn_date'].fillna(today) - master_df['signup_date']).dt.days
    
    return master_df

with st.spinner("Loading and processing data..."):
    data = load_data()

st.markdown("---")

st.header("Key Performance Metrics")
col1, col2, col3 = st.columns(3)
total_users = len(data)
churned_users = data['is_churned'].sum()
churn_rate = churned_users / total_users

col1.metric("Total Unique Accounts", f"{total_users:,}")
col2.metric("Churned Accounts", f"{churned_users:,}")
col3.metric("Overall Account Churn Rate", f"{churn_rate:.2%}")

st.markdown("---")

st.header("Churn Analysis Visualizations")
sns.set_theme(style="whitegrid", palette="deep")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Churn Rate by Plan Tier")
    plan_churn = data.groupby('plan_tier')['is_churned'].mean().reset_index()
    plan_churn.sort_values(by='is_churned', ascending=False, inplace=True)
    
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=plan_churn, x='plan_tier', y='is_churned', color='steelblue', ax=ax)
    ax.set_ylabel("Churn Rate (%)")
    ax.set_xlabel("Plan Tier")
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    sns.despine()
    st.pyplot(fig)

with col2:
    st.subheader("Tenure vs Churn")
    tenure_churn = data.groupby('is_churned')['tenure_days'].mean().reset_index()
    tenure_churn['Status'] = tenure_churn['is_churned'].map({0: 'Retained', 1: 'Churned'})
    
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=tenure_churn, x='Status', y='tenure_days', hue='Status', legend=False, palette=['#2ecc71', '#e74c3c'], ax=ax)
    ax.set_ylabel("Average Tenure (Days)")
    ax.set_xlabel("")
    sns.despine()
    st.pyplot(fig)

col3, col4 = st.columns(2)

with col3:
    st.subheader("Support Tickets vs Churn")
    ticket_churn = data.groupby('is_churned')['ticket_count'].mean().reset_index()
    ticket_churn['Status'] = ticket_churn['is_churned'].map({0: 'Retained', 1: 'Churned'})
    
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=ticket_churn, x='Status', y='ticket_count', hue='Status', legend=False, palette=['#2ecc71', '#e74c3c'], ax=ax)
    ax.set_ylabel("Average Tickets per Account")
    ax.set_xlabel("")
    sns.despine()
    st.pyplot(fig)

with col4:
    st.subheader("Feature Usage vs Churn")
    usage_churn = data.groupby('is_churned')['usage_count'].mean().reset_index()
    usage_churn['Status'] = usage_churn['is_churned'].map({0: 'Retained', 1: 'Churned'})
    
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=usage_churn, x='Status', y='usage_count', hue='Status', legend=False, palette=['#2ecc71', '#e74c3c'], ax=ax)
    ax.set_ylabel("Average Total Usage per Account")
    ax.set_xlabel("")
    sns.despine()
    st.pyplot(fig)

st.markdown("---")
st.markdown("**Insight Summary**")
st.info("""
- **Product Engagement**: Feature usage between retained and churned accounts is nearly identical.
- **Support Friction**: Customers who churn raise significantly more support tickets than retained customers.
- **Retention Peak**: Customers who stay longer than 3-4 months are significantly less likely to churn.
""")
