import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Sample data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Bills & Utilities": [62.14, 62.14, 130.41, 62.14, 62.14],
    "Education": [59, 59, 59, 0, 0],
    "Entertainment": [332.21, 264.7, 0, 295.57, 27],
    "Food & Drink": [1749.34, 1423.3, 1739.79, 1753.01, 303.75],
    "Gifts & Donations": [362.32, 921.32, 364.49, 362.32, 271.16],
    "Groceries": [837.65, 530.54, 800.86, 833.88, 252.1],
    "Health & Wellnes": [201.42, 35.79, 231.04, 74.28, 22.89],
    "Personal": [683.93, 99.52, 293.17, 103.44, 19.77],
    "Professional Services": [0, 0, 37.99, 16.32, 0],
    "Shopping": [782.6, 122.69, 455.26, 515.38, 21.89],
    "Travel": [470.6, 486.23, 393.3, 1906.07, 37.41],

}

# Convert to DataFrame
df = pd.DataFrame(data)
df.set_index("Month", inplace=True)

# Calculate total spendings
df["Total Spendings"] = df.sum(axis=1)

# 1. Stacked Bar Chart of Category-wise Monthly Spending
fig_bar = go.Figure()
for category in df.columns[:-1]:  # Exclude Total Spendings
    fig_bar.add_trace(go.Bar(
        x=df.index,
        y=df[category],
        name=category
    ))

fig_bar.update_layout(
    barmode='stack',
    title="Monthly Spending by Category",
    xaxis_title="Month",
    yaxis_title="Amount ($)",
    legend_title="Category",
    hovermode="x unified"
)

# 2. Line Chart for Total Spendings
fig_line = px.line(
    df,
    x=df.index,
    y="Total Spendings",
    title="Total Monthly Spendings",
    markers=True
)
fig_line.update_layout(
    yaxis_title="Amount ($)",
    xaxis_title="Month",
    hovermode="x"
)

# Show figures
fig_bar.show()
fig_line.show()
