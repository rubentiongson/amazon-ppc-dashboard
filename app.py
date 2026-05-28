import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📊 Amazon PPC Dashboard")
st.markdown("Upload your raw Amazon Sponsored Ads report files (.csv or .xlsx) below.")

# 1. File Uploader Component
uploaded_files = st.file_uploader("Choose Amazon PPC Report Files", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    all_dfs = []
    
    # 2. Comprehensive Column Name Mapping
    column_mapping = {
        'Start Date': 'Date',
        'Cost': 'Spend',
        '7-Day Total Sales': 'Sales',
        '14-Day Total Sales': 'Sales',
        '7-Day Total Orders': 'Orders',
        'Total Orders': 'Orders',
        '7-Day Total Units': 'Units',
        'Total Units': 'Units'
    }
    
    for file in uploaded_files:
        try:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)
                
            df.rename(columns=column_mapping, inplace=True)
            all_dfs.append(df)
        except Exception as e:
            st.error(f"Error reading {file.name}: {e}")
            
    if all_dfs:
        df = pd.concat(all_dfs, ignore_index=True)
        
        # Ensure critical raw numeric columns exist with default 0 if missing
        required_columns = ['Impressions', 'Clicks', 'Spend', 'Sales', 'Orders', 'Units']
        for col in required_columns:
            if col not in df.columns:
                df[col] = 0
            else:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        
        # 3. Aggregate Data Safely
        total_impressions = int(df['Impressions'].sum())
        total_clicks = int(df['Clicks'].sum())
        total_spend = float(df['Spend'].sum())
        total_sales = float(df['Sales'].sum())
        total_orders = int(df['Orders'].sum())
        total_units = int(df['Units'].sum())
        
        # 4. Dynamically Calculate Percentage Metrics
        overall_ctr = (total_clicks / total_impressions) if total_impressions > 0 else 0.0
        overall_cvr = (total_orders / total_clicks) if total_clicks > 0 else 0.0
        overall_acos = (total_spend / total_sales) if total_sales > 0 else 0.0
        
        # 5. Display 9 Metrics Top Bar (3x3 Grid Layout)
        st.markdown("### 📈 Performance Overview")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Impressions", f"{total_impressions:,}")
            st.metric("Spend", f"${total_spend:,.2f}")
            st.metric("Orders", f"{total_orders:,}")
        with col2:
            st.metric("Clicks", f"{total_clicks:,}")
            st.metric("Sales", f"${total_sales:,.2f}")
            st.metric("Units", f"{total_units:,}")
        with col3:
            st.metric("CTR", f"{overall_ctr:.2%}")
            st.metric("ACoS", f"{overall_acos:.2%}")
            st.metric("CVR", f"{overall_cvr:.2%}")
            
        # 6. Data Table Preview by Campaign
        st.markdown("---")
        if 'Campaign Name' in df.columns:
            st.markdown("### 📋 Performance Breakdown by Campaign")
            campaign_summary = df.groupby('Campaign Name')[required_columns].sum().reset_index()
            
            # Recalculate rates per campaign row
            campaign_summary['CTR'] = (campaign_summary['Clicks'] / campaign_summary['Impressions']).fillna(0)
            campaign_summary['CVR'] = (campaign_summary['Orders'] / campaign_summary['Clicks']).fillna(0)
            campaign_summary['ACoS'] = (campaign_summary['Spend'] / campaign_summary['Sales']).fillna(0)
            
            # Format display
            campaign_summary['Spend'] = campaign_summary['Spend'].map('${:,.2f}'.format)
            campaign_summary['Sales'] = campaign_summary['Sales'].map('${:,.2f}'.format)
            campaign_summary['CTR'] = campaign_summary['CTR'].map('{:.2%}'.format)
            campaign_summary['CVR'] = campaign_summary['CVR'].map('{:.2%}'.format)
            campaign_summary['ACoS'] = campaign_summary['ACoS'].map('{:.2%}'.format)
            
            st.dataframe(campaign_summary, use_container_width=True)
        else:
            st.markdown("### 📋 Raw Combined Data Preview")
            st.dataframe(df.head(100), use_container_width=True)
