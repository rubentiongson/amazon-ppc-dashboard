 codex/create-amazon-ppc-dashboard-web-app-dvy9h2

import pandas as pd
 main
import streamlit as st

st.set_page_config(page_title="PPC Insights Dashboard", layout="wide")

CUSTOM_CSS = """
<style>
 codex/create-amazon-ppc-dashboard-web-app-dvy9h2
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
:root{--bg:#f8fafa;--surface:#fff;--line:#dbc2ad;--text:#191c1d;--muted:#554434;--primary:#8a5100;--side:#f2f4f4;--tertiary:#00687a;}
html,body,[class*="css"]{font-family:Inter,sans-serif;}
.stApp{background:var(--bg);color:var(--text)}
header[data-testid="stHeader"]{background:transparent}
section.main > div{max-width:1440px;padding-top:.2rem}
[data-testid="stSidebar"]{background:var(--side);border-right:1px solid var(--line)}
.brand{font-size:28px;font-weight:700;color:var(--primary);margin:10px 0 0}
.subbrand{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#887361;margin:0 0 10px}
.topbar{height:64px;background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin:0 -1rem 12px;padding:0 2rem;display:flex;justify-content:space-between;align-items:center}
.top-title{font-size:46px;line-height:1;color:#1f2a44;font-weight:700}
.chip{display:inline-block;border:1px solid var(--line);background:#f2f4f4;border-radius:999px;padding:7px 14px;font-size:11px;font-weight:700}
.kpi{border:1px solid var(--line);background:#fff;border-radius:8px;padding:14px}
.k-label{font-size:10px;letter-spacing:.09em;font-weight:700;color:var(--muted)}
.k-val{font-size:40px;color:var(--primary);font-weight:700;line-height:1.05}
.badge{font-size:10px;font-weight:700;border-radius:6px;padding:2px 8px}.up{background:#e8f5e9;color:#2e7d32}.down{background:#ffdad6;color:#ba1a1a}
.section-title{font-size:30px;font-weight:700;margin:0 0 8px}
.alert{padding:12px 14px;border-radius:8px;margin-bottom:10px}.a1{background:#d4e1f566;border-left:4px solid #535f70}.a2{background:#ffdcbd44;border-left:4px solid #8a5100}.a3{background:#adecff44}
.table-shell{margin-top:10px;border:1px solid var(--line);border-radius:8px;background:#fff;overflow:hidden}
.table-head{display:flex;justify-content:space-between;align-items:center;padding:14px 18px;border-bottom:1px solid var(--line)}
.table-head .v{font-size:11px;font-weight:700;color:var(--primary)}
.tbl{width:100%;border-collapse:collapse;font-size:14px}
.tbl th{font-size:11px;letter-spacing:.05em;color:var(--muted);background:#f2f4f4;text-align:left;padding:10px 14px;border-bottom:1px solid var(--line)}
.tbl td{padding:11px 14px;border-bottom:1px solid #efe2d5}
.tbl tr:nth-child(even){background:#fafbfb}
.right{text-align:right}.center{text-align:center}
.pill{font-size:10px;font-weight:700;border-radius:999px;padding:2px 8px;display:inline-block}
.active{background:#e8f5e9;color:#2e7d32;border:1px solid #c8e6c9}.paused{background:#d4e1f5;color:#576474;border:1px solid #b9c8df}.oob{background:#ffdad6;color:#ba1a1a;border:1px solid #f0b8b2}
</style>
"""

@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap");

:root {
  --bg:#f8fafa; --text:#191c1d; --muted:#554434; --line:#dbc2ad;
  --side:#f2f4f4; --primary:#8a5100; --tertiary:#00687a;
}
html, body, [class*="css"] { font-family: Inter, sans-serif; }
.stApp { background: var(--bg); color: var(--text); }
header[data-testid="stHeader"] { background: transparent; }
section.main > div { padding-top: 0.25rem; max-width: 1440px; }

[data-testid="stSidebar"] { background: var(--side); border-right: 1px solid var(--line); }
[data-testid="stSidebar"] .stRadio label { padding: 4px 0; }
.brand { font-size: 1.75rem; font-weight:700; color:var(--primary); margin:12px 0 0 0; }
.subbrand { font-size:11px; text-transform:uppercase; letter-spacing:.12em; color:#887361; margin:0 0 10px 0; }

.topbar {
  height:62px; background:#fff; border-top:1px solid var(--line); border-bottom:1px solid var(--line);
  margin:0 -1rem 14px -1rem; display:flex; align-items:center; justify-content:space-between; padding:0 2rem;
}
.top-title { font-size:2.1rem; color:#1f2a44; font-weight:700; }
.chip { border:1px solid var(--line); background:#f2f4f4; padding:7px 14px; border-radius:999px; font-size:11px; font-weight:700; }

.metric-card { border:1px solid var(--line); background:#fff; border-radius:8px; padding:14px; min-height:88px; }
.metric-label { font-size:10px; font-weight:700; letter-spacing:.09em; color:var(--muted); }
.metric-value { font-size:2.5rem; font-weight:700; color:var(--primary); line-height:1.1; }
.badge-red,.badge-green { font-size:10px; font-weight:700; padding:2px 8px; border-radius:6px; }
.badge-red { background:#ffdad6; color:#ba1a1a; }
.badge-green { background:#e8f5e9; color:#2e7d32; }

.section-title { font-size:1.9rem; font-weight:700; margin:0 0 8px 0; }
.alert { border-radius:8px; padding:12px 14px; margin-bottom:10px; font-size:0.95rem; }
.a1 { background:#d4e1f566; border-left:4px solid #535f70; }
.a2 { background:#ffdcbd44; border-left:4px solid #8a5100; }
.a3 { background:#adecff44; }

.table-wrap { border:1px solid var(--line); border-radius:8px; overflow:hidden; background:#fff; margin-top:10px; }
.table-head { display:flex; justify-content:space-between; align-items:center; padding:14px 18px; border-bottom:1px solid var(--line); }
.small-btn { font-size:11px; font-weight:700; color:var(--primary); }
[data-testid="stDataFrame"] { border:1px solid var(--line); border-radius:0 0 8px 8px; overflow:hidden; }
[data-testid="stDataFrame"] table tbody tr:nth-child(even){background:#f8fafa}
</style>
"""

 main
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<div class='brand'>Ads Console</div><div class='subbrand'>Seller Central API</div>", unsafe_allow_html=True)
 codex/create-amazon-ppc-dashboard-web-app-dvy9h2
    st.radio("", ["Dashboard", "Campaigns", "Products", "Match Type", "Keywords", "Search Terms", "ASIN Targets", "ASIN from STR", "Auto Campaigns", "Category Targets", "Wasted Ad Spend"], index=0)
=======
    st.radio(
        "",
        [
            "Dashboard", "Campaigns", "Products", "Match Type", "Keywords",
            "Search Terms", "ASIN Targets", "ASIN from STR", "Auto Campaigns",
            "Category Targets", "Wasted Ad Spend"
        ],
        index=0,
    )
 main
    st.button("⚡ Sync Data", use_container_width=True)
    st.divider()
    st.button("Help Center", use_container_width=True)
    st.button("Log Out", use_container_width=True)

 codex/create-amazon-ppc-dashboard-web-app-dvy9h2
st.markdown("<div class='topbar'><div class='top-title'>PPC Insights</div><div class='chip'>🏦 ACCOUNT SELECTION ▾</div></div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([6, 1, 2])
c1.markdown("<div class='chip'>📅 Date Range: Last 30 Days</div>", unsafe_allow_html=True)
c2.markdown("<div style='padding-top:8px'>🔔</div>", unsafe_allow_html=True)
c3.markdown("<div style='padding-top:8px'>❔ &nbsp; 👤</div>", unsafe_allow_html=True)

cards = [("TOTAL SPEND", "$12,450.00", "+5%", "down"), ("TOTAL SALES", "$84,200.00", "+12%", "up"), ("ACoS", "14.78%", "-2%", "up"), ("ROAS", "6.76x", "+8%", "up")]
for col, (label, val, delta, trend) in zip(st.columns(4), cards):
    cls = "up" if trend == "up" else "down"
    col.markdown(f"<div class='kpi'><div class='k-label'>{label}</div><div style='display:flex;justify-content:space-between;align-items:end'><div class='k-val'>{val}</div><span class='badge {cls}'>{delta}</span></div></div>", unsafe_allow_html=True)

main, side = st.columns([3, 1])
with main:
    st.markdown("<div class='section-title'>Performance Trends</div>", unsafe_allow_html=True)
    st.line_chart({"Spend":[40,42,45,49,51,54,56,60,63,64,64,62,59,56,54,53,55,59,65,72,77,80,79,75,68,63,61,62,66,72],"Sales":[50,54,58,64,71,78,86,94,102,108,112,113,111,106,100,96,95,98,105,116,128,138,143,142,135,126,120,118,121,131]}, color=["#8a5100", "#00687a"], height=360)

st.markdown(
    "<div class='topbar'><div class='top-title'>PPC Insights</div><div class='chip'>🏦 ACCOUNT SELECTION ▾</div></div>",
    unsafe_allow_html=True,
)

a, b, c = st.columns([6, 1, 2])
a.markdown("<div class='chip'>📅 Date Range: Last 30 Days</div>", unsafe_allow_html=True)
b.markdown("<div style='padding-top:9px'>🔔</div>", unsafe_allow_html=True)
c.markdown("<div style='padding-top:9px'>❔ &nbsp;&nbsp; 👤</div>", unsafe_allow_html=True)

kcols = st.columns(4)
for col, (label, value, delta, is_good) in zip(
    kcols,
    [
        ("TOTAL SPEND", "$12,450.00", "+5%", False),
        ("TOTAL SALES", "$84,200.00", "+12%", True),
        ("ACoS", "14.78%", "-2%", True),
        ("ROAS", "6.76x", "+8%", True),
    ],
):
    badge = "badge-green" if is_good else "badge-red"
    col.markdown(
        f"<div class='metric-card'><div class='metric-label'>{label}</div>"
        f"<div style='display:flex;justify-content:space-between;align-items:end;'>"
        f"<div class='metric-value'>{value}</div><div class='{badge}'>{delta}</div></div></div>",
        unsafe_allow_html=True,
    )

main, side = st.columns([3, 1])

with main:
    st.markdown("<div class='section-title'>Performance Trends</div>", unsafe_allow_html=True)
    chart_df = pd.DataFrame(
        {
            "Spend": [40,42,45,49,51,54,56,60,63,64,64,62,59,56,54,53,55,59,65,72,77,80,79,75,68,63,61,62,66,72],
            "Sales": [50,54,58,64,71,78,86,94,102,108,112,113,111,106,100,96,95,98,105,116,128,138,143,142,135,126,120,118,121,131],
        }
    )
    st.line_chart(chart_df, height=360, color=["#8a5100", "#00687a"])

 main
with side:
    st.markdown("<div class='section-title'>Insights & Alerts</div>", unsafe_allow_html=True)
    st.markdown("<div class='alert a1'><b>Budget Alert</b><br><br>3 campaigns are nearing daily budget limit.</div>", unsafe_allow_html=True)
    st.markdown("<div class='alert a2'><b>Optimization Tip</b><br><br>Lowering bids on \"keyword_x\" could save $45/day.</div>", unsafe_allow_html=True)
    st.markdown("<div class='alert a3'><b>Unlock AI Insights</b><br><br>Get predictive keyword scaling advice.</div>", unsafe_allow_html=True)
    st.button("UPGRADE PRO", use_container_width=True)

codex/create-amazon-ppc-dashboard-web-app-dvy9h2
st.markdown("""
<div class='table-shell'>
  <div class='table-head'><div class='section-title' style='font-size:20px;margin:0'>Top Performing Campaigns</div><div class='v'>VIEW ALL REPORTS</div></div>
  <table class='tbl'>
    <thead><tr><th>CAMPAIGN NAME</th><th class='center'>STATUS</th><th class='right'>SPEND</th><th class='right'>SALES</th><th class='right'>ACoS</th><th class='center'>ACTION</th></tr></thead>
    <tbody>
      <tr><td>Summer_Collection_Manual_2023</td><td class='center'><span class='pill active'>ACTIVE</span></td><td class='right'>$1,420.50</td><td class='right'>$12,500.00</td><td class='right'>11.36%</td><td class='center'>⋯</td></tr>
      <tr><td>Prime_Day_Headphones_Auto</td><td class='center'><span class='pill active'>ACTIVE</span></td><td class='right'>$2,105.00</td><td class='right'>$18,450.00</td><td class='right'>11.41%</td><td class='center'>⋯</td></tr>
      <tr><td>Competitor_Targeting_Bags</td><td class='center'><span class='pill paused'>PAUSED</span></td><td class='right'>$850.40</td><td class='right'>$6,120.00</td><td class='right'>13.89%</td><td class='center'>⋯</td></tr>
      <tr><td>Brand_Defense_Keywords</td><td class='center'><span class='pill active'>ACTIVE</span></td><td class='right'>$3,200.00</td><td class='right'>$24,800.00</td><td class='right'>12.90%</td><td class='center'>⋯</td></tr>
      <tr><td>Home_Office_Desk_Lamp_Manual</td><td class='center'><span class='pill oob'>OUT OF BUDGET</span></td><td class='right'>$680.00</td><td class='right'>$3,450.00</td><td class='right'>19.71%</td><td class='center'>⋯</td></tr>
    </tbody>
  </table>
</div>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='table-wrap'><div class='table-head'>"
    "<div class='section-title' style='font-size:1.25rem;margin:0;'>Top Performing Campaigns</div>"
    "<div class='small-btn'>VIEW ALL REPORTS</div></div></div>",
    unsafe_allow_html=True,
)

df = pd.DataFrame(
    [
        ["Summer_Collection_Manual_2023", "ACTIVE", "$1,420.50", "$12,500.00", "11.36%", "⋯"],
        ["Prime_Day_Headphones_Auto", "ACTIVE", "$2,105.00", "$18,450.00", "11.41%", "⋯"],
        ["Competitor_Targeting_Bags", "PAUSED", "$850.40", "$6,120.00", "13.89%", "⋯"],
        ["Brand_Defense_Keywords", "ACTIVE", "$3,200.00", "$24,800.00", "12.90%", "⋯"],
        ["Home_Office_Desk_Lamp_Manual", "OUT OF BUDGET", "$680.00", "$3,450.00", "19.71%", "⋯"],
    ],
    columns=["CAMPAIGN NAME", "STATUS", "SPEND", "SALES", "ACoS", "ACTION"],
)

st.dataframe(df, use_container_width=True, hide_index=True)
main
