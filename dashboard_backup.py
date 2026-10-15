import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page settings
st.set_page_config(
    page_title="Student Analytics",
    page_icon="🎓",
    layout="wide"
)

# Custom dashboard design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #172554);
    color: white;
}

.block-container {
    padding-top: 2rem;
    max-width: 1400px;
}

h1, h2, h3, p, label {
    color: #f1f5f9;
}

.hero {
    background: linear-gradient(120deg, #312e81, #1e40af);
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 25px;
    border: 1px solid #6366f1;
}

.hero h1 {
    font-size: 34px;
    color: white;
}

.hero p {
    color: #dbeafe;
    font-size: 17px;
}

.metric-card {
    background: #172554;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #3730a3;
    margin-bottom: 15px;
}

.metric-label {
    color: #a5b4fc;
    font-size: 14px;
}

.metric-value {
    color: white;
    font-size: 28px;
    font-weight: bold;
}

div[data-testid="stFileUploader"] {
    background: #172554;
    padding: 15px;
    border-radius: 15px;
    border: 1px dashed #818cf8;
}

.stButton button,
.stDownloadButton button {
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Dashboard heading
st.markdown("""
<div class="hero">
    <h1>🎓 Student Performance Analytics</h1>
    <p>Smart insights into student marks, rankings and academic performance.</p>
</div>
""", unsafe_allow_html=True)

# File upload
st.subheader("📂 Upload Student Data")

uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is None:
    st.info("👋 Upload your student data to explore the dashboard.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📊 Analytics</h3>
            <p>Calculate averages and percentages.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🏆 Rankings</h3>
            <p>Identify toppers and rank students.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>📈 Visual Reports</h3>
            <p>Compare student and subject performance.</p>
        </div>
        """, unsafe_allow_html=True)

    st.stop()

# Read uploaded file
try:
    if uploaded_file.name.lower().endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

except Exception as error:
    st.error(f"Unable to read the file: {error}")
    st.stop()

# Validate uploaded data
df.columns = df.columns.astype(str).str.strip()

if df.empty:
    st.error("The uploaded file is empty.")
    st.stop()

if "Name" not in df.columns:
    st.error("Your file must contain a column named Name.")
    st.stop()

df["Name"] = df["Name"].astype("string").str.strip()

if df["Name"].isna().any() or df["Name"].eq("").any():
    st.error("Please provide a name for every student.")
    st.stop()

subjects = [col for col in df.columns if col != "Name"]

if not subjects:
    st.error("No subject columns were found.")
    st.stop()

for subject in subjects:
    df[subject] = pd.to_numeric(df[subject], errors="coerce")

if df[subjects].isna().any().any():
    st.error("Subject marks must be numeric and cannot be empty.")
    st.stop()

if ((df[subjects] < 0) | (df[subjects] > 100)).any().any():
    st.error("Marks must be between 0 and 100.")
    st.stop()

# Calculate performance
df["Total"] = df[subjects].sum(axis=1)
df["Percentage"] = df[subjects].mean(axis=1)

df["Rank"] = (
    df["Total"]
    .rank(method="min", ascending=False)
    .astype(int)
)

df["Result"] = df[subjects].ge(40).all(axis=1).map({
    True: "Pass",
    False: "Fail"
})

# Performance overview
st.subheader("📊 Performance Overview")

col1, col2, col3, col4 = st.columns(4)

metrics = [
    (col1, "👥 Total Students", str(len(df))),
    (col2, "📈 Class Average", f"{df['Percentage'].mean():.2f}%"),
    (col3, "🏆 Highest Score", f"{df['Percentage'].max():.2f}%"),
    (col4, "✅ Pass Rate", f"{(df['Result'].eq('Pass').mean() * 100):.1f}%")
]

for col, label, value in metrics:
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

topper = df.loc[df["Total"].idxmax()]

st.success(
    f"🏆 Top Performer: {topper['Name']} — "
    f"{topper['Percentage']:.2f}%"
)

# Display uploaded records
with st.expander("📋 View Uploaded Student Data"):
    st.dataframe(df, use_container_width=True, hide_index=True)

# Charts
st.subheader("📈 Academic Insights")

left, right = st.columns(2)

with left:
    st.markdown("#### Subject-wise Average Marks")

    fig, ax = plt.subplots(figsize=(7, 4))
    fig.patch.set_facecolor("#172554")
    ax.set_facecolor("#172554")

    df[subjects].mean().plot(kind="bar", ax=ax)

    ax.set_ylim(0, 100)
    ax.set_ylabel("Average Marks", color="white")
    ax.tick_params(axis="x", colors="white", rotation=30)
    ax.tick_params(axis="y", colors="white")
    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    st.pyplot(fig)
    plt.close(fig)

with right:
    st.markdown("#### Student Performance")

    chart_df = df.nlargest(15, "Percentage")

    fig, ax = plt.subplots(figsize=(7, 4))
    fig.patch.set_facecolor("#172554")
    ax.set_facecolor("#172554")

    ax.bar(chart_df["Name"], chart_df["Percentage"])

    ax.set_ylim(0, 100)
    ax.set_ylabel("Percentage", color="white")
    ax.tick_params(axis="x", colors="white", rotation=45)
    ax.tick_params(axis="y", colors="white")
    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    st.pyplot(fig)
    plt.close(fig)

# Search and rankings
st.subheader("🔎 Student Rankings")

search = st.text_input("Search for a student by name")

filtered_df = df[
    df["Name"].str.contains(search, case=False, na=False)
]

ranked_df = filtered_df.sort_values(["Rank", "Name"])

st.dataframe(
    ranked_df,
    use_container_width=True,
    hide_index=True
)

# Download results
st.subheader("📥 Download Your Report")

csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇️ Download Analyzed Results",
    data=csv_data,
    file_name="student_analysis_results.csv",
    mime="text/csv"
)

st.caption(
    "Pass criteria: at least 40 marks in every subject. "
    "Adjust this rule to match your institution's policy."
)