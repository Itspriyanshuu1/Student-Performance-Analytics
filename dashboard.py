import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Analytics Pro",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. PROFESSIONAL DESIGN AND ANIMATIONS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at top left,
            #172554 0%,
            #080d1b 55%,
            #0f172a 100%
        );
    color: #f8fafc;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, h4, p, label {
    color: #f1f5f9;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #111827,
        #172554
    );
    border-right: 1px solid #334155;
}

section[data-testid="stSidebar"] * {
    color: #f8fafc;
}

.hero {
    background: linear-gradient(
        -45deg,
        #312e81,
        #1d4ed8,
        #6d28d9,
        #0e7490
    );
    background-size: 300% 300%;
    animation: gradientMove 10s ease infinite;
    padding: 35px;
    border-radius: 24px;
    border: 1px solid #818cf8;
    margin-bottom: 25px;
    box-shadow: 0 10px 40px rgba(59, 130, 246, 0.18);
}

.hero h1 {
    color: white;
    font-size: 36px;
    font-weight: 800;
    animation: fadeIn 1.2s ease-out;
}

.hero p {
    color: #dbeafe;
    font-size: 16px;
}

@keyframes gradientMove {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.metric-card {
    background: linear-gradient(
        145deg,
        rgba(30, 41, 90, 0.95),
        rgba(15, 23, 42, 0.95)
    );
    padding: 23px;
    border-radius: 18px;
    border: 1px solid #3730a3;
    margin-bottom: 12px;
    min-height: 120px;
    box-shadow: 0 5px 18px rgba(0, 0, 0, 0.18);
    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease,
        border-color 0.3s ease;
    animation: fadeIn 0.8s ease-out;
}

.metric-card:hover {
    transform: translateY(-6px);
    border-color: #38bdf8;
    box-shadow: 0 10px 30px rgba(56, 189, 248, 0.18);
}

.metric-label {
    color: #a5b4fc;
    font-size: 14px;
    margin-bottom: 12px;
}

.metric-value {
    color: #ffffff;
    font-size: 30px;
    font-weight: 800;
}

.panel {
    background: rgba(23, 37, 84, 0.65);
    border: 1px solid #334155;
    padding: 20px;
    border-radius: 18px;
    margin: 10px 0;
}

div[data-testid="stFileUploader"] {
    background: rgba(23, 37, 84, 0.75);
    padding: 15px;
    border-radius: 15px;
    border: 1px dashed #818cf8;
}

.stButton button,
.stDownloadButton button {
    border-radius: 10px;
    font-weight: 700;
    border: 1px solid #6366f1;
    transition: all 0.25s ease;
}

.stButton button:hover,
.stDownloadButton button:hover {
    transform: translateY(-2px);
    border-color: #38bdf8;
    box-shadow: 0 5px 18px rgba(56, 189, 248, 0.2);
}

div[data-testid="stDataFrame"] {
    border: 1px solid #334155;
    border-radius: 12px;
}

hr {
    border-color: #334155;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# 3. HEADER
# =========================================================

st.markdown("""
<div class="hero">
    <h1>🎓 Student Performance Analytics</h1>
    <p>
        Intelligent academic insights • Student rankings •
        Performance monitoring • Data-driven decisions
    </p>
</div>
""", unsafe_allow_html=True)

st.caption("STUDENT ANALYTICS PRO  |  DATA-DRIVEN ACADEMIC INSIGHTS")

# =========================================================
# 4. SIDEBAR
# =========================================================

st.sidebar.markdown("# 🎓 Analytics Pro")
st.sidebar.caption("Student performance management")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "🏠 Overview",
        "👨‍🎓 Students",
        "📊 Subject Analytics",
        "🏆 Rankings",
        "🧠 Smart Insights",
        "📥 Reports"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📂 Student Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV or Excel",
    type=["csv", "xlsx"],
    key="student_file"
)

st.sidebar.caption(
    "Required format: Name column followed by subject marks."
)

# =========================================================
# 5. LOAD DATA
# =========================================================

if uploaded_file is None:

    st.info(
        "👋 Welcome! Upload your student CSV or Excel file "
        "using the sidebar to explore your dashboard."
    )

    st.markdown("## ✨ What this dashboard can do")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">📊 ANALYTICS</div>
            <div class="metric-value">Insights</div>
            <p>Analyze class averages and subject performance.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">🏆 RANKINGS</div>
            <div class="metric-value">Results</div>
            <p>Find top performers and identify students needing support.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">📥 REPORTS</div>
            <div class="metric-value">Exports</div>
            <p>Download analyzed student results.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🚀 Getting started")
    st.write("1. Prepare a CSV or Excel file.")
    st.write("2. Include a column named `Name`.")
    st.write("3. Add subject columns with marks from 0 to 100.")
    st.write("4. Upload your file using the sidebar.")

    st.stop()

try:
    if uploaded_file.name.lower().endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

except Exception as error:
    st.error(f"Unable to read your file: {error}")
    st.stop()

# =========================================================
# 6. VALIDATE DATA
# =========================================================

df.columns = df.columns.astype(str).str.strip()

if df.empty:
    st.error("Your uploaded file is empty.")
    st.stop()

if "Name" not in df.columns:
    st.error("Your file must contain a column named Name.")
    st.stop()

df["Name"] = df["Name"].astype("string").str.strip()

if df["Name"].isna().any() or df["Name"].eq("").any():
    st.error("Every student must have a name.")
    st.stop()

subjects = [column for column in df.columns if column != "Name"]

if not subjects:
    st.error("No subject columns were found.")
    st.stop()

for subject in subjects:
    df[subject] = pd.to_numeric(df[subject], errors="coerce")

if df[subjects].isna().any().any():
    st.error(
        "Subject marks must contain valid numbers. "
        "Please check your CSV or Excel file for missing or invalid marks."
    )
    st.stop()

if ((df[subjects] < 0) | (df[subjects] > 100)).any().any():
    st.error("Marks must be between 0 and 100.")
    st.stop()

# =========================================================
# 7. PERFORMANCE CALCULATIONS
# =========================================================

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

def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    return "F"

df["Grade"] = df["Percentage"].apply(assign_grade)

# =========================================================
# 8. COMMON METRICS
# =========================================================

total_students = len(df)
class_average = df["Percentage"].mean()
highest_score = df["Percentage"].max()
lowest_score = df["Percentage"].min()

pass_count = int(df["Result"].eq("Pass").sum())
fail_count = int(df["Result"].eq("Fail").sum())

pass_rate = (pass_count / total_students) * 100

topper = df.loc[df["Percentage"].idxmax()]
weakest_subject = df[subjects].mean().idxmin()
strongest_subject = df[subjects].mean().idxmax()

# =========================================================
# 9. REUSABLE METRIC CARDS
# =========================================================

def metric_card(label, value):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# 10. CHART HELPER
# =========================================================

def style_axis(ax, fig):
    fig.patch.set_facecolor("#111827")
    ax.set_facecolor("#111827")

    ax.tick_params(colors="#e2e8f0")
    ax.xaxis.label.set_color("#e2e8f0")
    ax.yaxis.label.set_color("#e2e8f0")
    ax.title.set_color("#f8fafc")

    ax.spines["bottom"].set_color("#475569")
    ax.spines["left"].set_color("#475569")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.18
    )

    ax.set_axisbelow(True)

# =========================================================
# 11. OVERVIEW PAGE
# =========================================================

if page == "🏠 Overview":

    st.subheader("📊 Performance Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("👥 TOTAL STUDENTS", f"{total_students:,}")

    with c2:
        metric_card("📈 CLASS AVERAGE", f"{class_average:.2f}%")

    with c3:
        metric_card("🏆 HIGHEST SCORE", f"{highest_score:.2f}%")

    with c4:
        metric_card("✅ PASS RATE", f"{pass_rate:.1f}%")

    st.success(
        f"🏆 Top Performer: {topper['Name']} — "
        f"{topper['Percentage']:.2f}%"
    )

    st.markdown("---")
    st.subheader("📈 Academic Performance")

    left, right = st.columns(2)

    with left:
        st.markdown("#### Subject-wise Average")

        subject_averages = df[subjects].mean().sort_values()

        fig, ax = plt.subplots(figsize=(8, 4))

        subject_averages.plot(
            kind="barh",
            ax=ax
        )

        ax.set_xlim(0, 100)
        ax.set_xlabel("Average Marks (%)")

        style_axis(ax, fig)
        fig.tight_layout()

        st.pyplot(fig)
        plt.close(fig)

    with right:
        st.markdown("#### Student Performance")

        chart_df = df.nlargest(10, "Percentage").sort_values(
            "Percentage"
        )

        fig, ax = plt.subplots(figsize=(8, 4))

        ax.barh(
            chart_df["Name"],
            chart_df["Percentage"]
        )

        ax.set_xlim(0, 100)
        ax.set_xlabel("Percentage (%)")

        style_axis(ax, fig)
        fig.tight_layout()

        st.pyplot(fig)
        plt.close(fig)

    st.markdown("---")
    st.subheader("📋 Student Data Preview")

    st.dataframe(
        df.sort_values("Rank"),
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# 12. STUDENTS PAGE
# =========================================================

elif page == "👨‍🎓 Students":

    st.subheader("👨‍🎓 Student Explorer")

    search = st.text_input(
        "🔍 Search by student name"
    )

    result_filter = st.selectbox(
        "Filter by result",
        ["All", "Pass", "Fail"]
    )

    grade_filter = st.selectbox(
        "Filter by grade",
        ["All"] + sorted(df["Grade"].unique().tolist())
    )

    filtered = df.copy()

    if search:
        filtered = filtered[
            filtered["Name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    if result_filter != "All":
        filtered = filtered[
            filtered["Result"] == result_filter
        ]

    if grade_filter != "All":
        filtered = filtered[
            filtered["Grade"] == grade_filter
        ]

    st.write(f"Students found: **{len(filtered)}**")

    st.dataframe(
        filtered.sort_values("Rank"),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")
    st.subheader("🪪 Individual Student Profile")

    selected_name = st.selectbox(
        "Select a student",
        sorted(df["Name"].unique().tolist())
    )

    student = df[df["Name"] == selected_name].iloc[0]

    a, b, c, d = st.columns(4)

    with a:
        metric_card("🎯 PERCENTAGE", f"{student['Percentage']:.2f}%")

    with b:
        metric_card("🏆 RANK", str(student["Rank"]))

    with c:
        metric_card("📚 GRADE", student["Grade"])

    with d:
        metric_card("📝 RESULT", student["Result"])

    st.markdown("#### Subject-wise Marks")

    profile_data = pd.DataFrame({
        "Subject": subjects,
        "Marks": [student[subject] for subject in subjects]
    })

    fig, ax = plt.subplots(figsize=(9, 4))

    profile_data.plot(
        x="Subject",
        y="Marks",
        kind="bar",
        legend=False,
        ax=ax
    )

    ax.set_ylim(0, 100)
    ax.set_ylabel("Marks")

    style_axis(ax, fig)
    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)

    student_subjects = pd.Series(
        {subject: student[subject] for subject in subjects}
    )

    best_subject = student_subjects.idxmax()
    weakest_student_subject = student_subjects.idxmin()

    st.info(
        f"Strongest subject: **{best_subject}** "
        f"({student_subjects.max():.1f} marks)"
    )

    if student["Result"] == "Fail":
        st.warning(
            f"This student needs additional support. "
            f"Weakest subject: {weakest_student_subject}."
        )
    else:
        st.success(
            f"The student passed all subjects under the "
            f"current 40-mark passing rule."
        )

# =========================================================
# 13. SUBJECT ANALYTICS PAGE
# =========================================================

elif page == "📊 Subject Analytics":

    st.subheader("📊 Subject Analytics")

    subject = st.selectbox(
        "Choose a subject",
        subjects
    )

    marks = df[subject]

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("📈 SUBJECT AVERAGE", f"{marks.mean():.2f}")

    with c2:
        metric_card("🏆 HIGHEST MARK", f"{marks.max():.2f}")

    with c3:
        metric_card("📉 LOWEST MARK", f"{marks.min():.2f}")

    with c4:
        metric_card(
            "✅ PASS RATE",
            f"{(marks.ge(40).mean() * 100):.1f}%"
        )

    left, right = st.columns(2)

    with left:
        st.markdown("#### Student Marks")

        subject_df = df.sort_values(
            subject,
            ascending=False
        )

        fig, ax = plt.subplots(figsize=(8, 4))

        ax.bar(
            subject_df["Name"],
            subject_df[subject]
        )

        ax.set_ylim(0, 100)
        ax.set_ylabel("Marks")
        ax.tick_params(axis="x", rotation=45)

        style_axis(ax, fig)
        fig.tight_layout()

        st.pyplot(fig)
        plt.close(fig)

    with right:
        st.markdown("#### Marks Distribution")

        fig, ax = plt.subplots(figsize=(8, 4))

        ax.hist(
            marks,
            bins=[0, 40, 50, 60, 70, 80, 90, 100],
            edgecolor="white"
        )

        ax.set_xlabel("Marks")
        ax.set_ylabel("Number of Students")

        style_axis(ax, fig)
        fig.tight_layout()

        st.pyplot(fig)
        plt.close(fig)

    st.markdown("#### Subject Ranking")

    subject_ranking = df[["Name", subject]].sort_values(
        subject,
        ascending=False
    )

    st.dataframe(
        subject_ranking,
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# 14. RANKINGS PAGE
# =========================================================

elif page == "🏆 Rankings":

    st.subheader("🏆 Student Leaderboard")

    ranking = df.sort_values(
        ["Rank", "Name"]
    ).reset_index(drop=True)

    ranking.insert(
        0,
        "Position",
        range(1, len(ranking) + 1)
    )

    top_three = ranking.head(3)

    if len(top_three) >= 1:
        st.markdown("### 🌟 Top Performers")

        cols = st.columns(min(len(top_three), 3))

        medals = ["🥇", "🥈", "🥉"]

        for i, (_, row) in enumerate(top_three.iterrows()):
            with cols[i]:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-label">
                            {medals[i]} POSITION {i + 1}
                        </div>
                        <div class="metric-value">
                            {row['Name']}
                        </div>
                        <p>{row['Percentage']:.2f}%</p>
                        <p>Grade: {row['Grade']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.markdown("### 📋 Complete Ranking")

    st.dataframe(
        ranking,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 📉 Students Requiring Support")

    support_df = df[
        (df["Result"] == "Fail")
        | (df["Percentage"] < 50)
    ].sort_values("Percentage")

    if support_df.empty:
        st.success(
            "No students fall below the current support criteria."
        )
    else:
        st.warning(
            f"{len(support_df)} student(s) meet the current "
            f"criteria for additional academic support."
        )

        st.dataframe(
            support_df,
            use_container_width=True,
            hide_index=True
        )

# =========================================================
# 15. SMART INSIGHTS PAGE
# =========================================================

elif page == "🧠 Smart Insights":

    st.subheader("🧠 Automatic Academic Insights")

    st.markdown("### 📈 Class Summary")

    st.write(f"👥 Total students analyzed: **{total_students}**")
    st.write(f"📊 Overall class average: **{class_average:.2f}%**")
    st.write(f"🏆 Highest individual percentage: **{highest_score:.2f}%**")
    st.write(f"📉 Lowest individual percentage: **{lowest_score:.2f}%**")
    st.write(f"✅ Students passing all subjects: **{pass_count}**")
    st.write(f"❌ Students failing one or more subjects: **{fail_count}**")

    st.markdown("---")
    st.markdown("### 📚 Subject Insights")

    subject_averages = df[subjects].mean()

    st.success(
        f"Strongest class subject by average: "
        f"**{strongest_subject}** "
        f"({subject_averages[strongest_subject]:.2f}/100)"
    )

    st.warning(
        f"Lowest class subject average: "
        f"**{weakest_subject}** "
        f"({subject_averages[weakest_subject]:.2f}/100)"
    )

    above_80 = int(df["Percentage"].ge(80).sum())
    below_50 = int(df["Percentage"].lt(50).sum())

    st.info(
        f"🌟 Students scoring 80% or higher: **{above_80}**"
    )

    st.info(
        f"📌 Students scoring below 50% overall: **{below_50}**"
    )

    st.markdown("---")
    st.markdown("### 📊 Grade Distribution")

    grade_counts = df["Grade"].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(9, 4))

    grade_counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("Grade")
    ax.set_ylabel("Number of Students")

    style_axis(ax, fig)
    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)

    st.caption(
        "Insights are based on the uploaded dataset. "
        "Grade boundaries are illustrative and can be customized."
    )

# =========================================================
# 16. REPORTS PAGE
# =========================================================

elif page == "📥 Reports":

    st.subheader("📥 Download Your Reports")

    st.write(
        "Download the analyzed dataset for use in Excel "
        "or other data analysis tools."
    )

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV Report",
        data=csv_data,
        file_name="student_analysis_results.csv",
        mime="text/csv",
        use_container_width=True
    )

    excel_buffer = BytesIO()

    with pd.ExcelWriter(
        excel_buffer,
        engine="openpyxl"
    ) as writer:
        df.to_excel(
            writer,
            index=False,
            sheet_name="Student Results"
        )

        df[subjects].mean().rename(
            "Average Marks"
        ).to_frame().to_excel(
            writer,
            sheet_name="Subject Summary"
        )

    st.download_button(
        label="📊 Download Excel Report",
        data=excel_buffer.getvalue(),
        file_name="student_analysis_results.xlsx",
        mime=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
        use_container_width=True
    )

    st.markdown("---")
    st.markdown("### 📋 Report Summary")

    st.write(f"Students: **{total_students}**")
    st.write(f"Subjects: **{len(subjects)}**")
    st.write(f"Class average: **{class_average:.2f}%**")
    st.write(f"Pass rate: **{pass_rate:.1f}%**")

    st.caption(
        "PDF report generation can be added in a later upgrade."
    )

# =========================================================
# 17. FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; padding:15px;">
        <p style="color:#94a3b8;">
            🎓 Student Performance Analytics Pro
        </p>
        <p style="color:#64748b; font-size:12px;">
            Built with Python, Streamlit, Pandas and Matplotlib
        </p>
    </div>
    """,
    unsafe_allow_html=True
)