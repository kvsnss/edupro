import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
page_title="EduPro Student Segmentation",
page_icon="🎓",
layout="wide"
)

# Load Data

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

users = pd.read_csv(DATA_DIR / "EduPro Online Platform.xlsx - Users.csv")
courses = pd.read_csv(DATA_DIR / "EduPro Online Platform.xlsx - Courses.csv")
transactions = pd.read_csv(DATA_DIR / "EduPro Online Platform.xlsx - Transactions.csv")
segments = pd.read_csv(DATA_DIR / "student_segments.csv")
# Sidebar

st.sidebar.title("EduPro Dashboard")

selected_user = st.sidebar.selectbox(
"Select Learner",
sorted(segments["UserID"].astype(str).unique())
)

# Get Selected Learner

student_df = segments[
    segments["UserID"].astype(str) == str(selected_user)
]

if student_df.empty:
    st.error("Learner not found")
    st.stop()

student = student_df.iloc[0]

# Learner Profile Explorer

st.title(
"Student Segmentation & Personalized Course Recommendation"
)

student = segments[
segments["UserID"] == selected_user
]


st.header("Learner Profile Explorer")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if "Cluster" in segments.columns:
        st.metric(
            "Segment",
            int(student["Cluster"])
        )

with col2:
    if "TotalCourses" in segments.columns:
        st.metric(
            "Total Courses",
            int(student["TotalCourses"])
        )

with col3:
    if "AvgRating" in segments.columns:
        st.metric(
            "Average Rating",
            round(float(student["AvgRating"]), 2)
        )

with col4:
    if "AvgSpending" in segments.columns:
        st.metric(
            "Average Spending",
            round(float(student["AvgSpending"]), 2)
        )

#Student Details

st.subheader("Student Profile")

profile_data = {
    "UserID": student["UserID"]
}

if "Age" in student.index:
    profile_data["Age"] = student["Age"]

if "Gender" in student.index:
    profile_data["Gender"] = student["Gender"]

if "CourseCategory" in student.index:
    profile_data["Preferred Category"] = student["CourseCategory"]

if "CourseLevel" in student.index:
    profile_data["Preferred Level"] = student["CourseLevel"]

if "LearningDepthIndex" in student.index:
    profile_data["Learning Depth Index"] = round(
        float(student["LearningDepthIndex"]), 2
    )

st.json(profile_data)

# Cluster Visualization

st.header("Cluster Visualization Dashboard")

if "Cluster" in segments.columns:

    cluster_count = (
        segments["Cluster"]
        .value_counts()
        .reset_index()
    )

    cluster_count.columns = [
        "Cluster",
        "Learners"
    ]

    fig = px.bar(
        cluster_count,
        x="Cluster",
        y="Learners",
        title="Learners per Segment"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# Segment Comparison

st.header("Segment Comparison Panel")

numeric_cols = [
    c for c in [
        "TotalCourses",
        "AvgSpending",
        "EnrollmentFrequency",
        "DiversityScore",
        "AvgRating",
        "LearningDepthIndex"
    ]
    if c in segments.columns
]

if "Cluster" in segments.columns:

    cluster_summary = (
        segments
        .groupby("Cluster")[numeric_cols]
        .mean()
        .reset_index()
    )

    st.dataframe(cluster_summary)

# Personalized Course Recommendations

st.header("🎯 Personalized Course Recommendations")

# Make sure selected learner exists

student_df = segments[
    segments["UserID"].astype(str) == str(selected_user)
]

if student_df.empty:
    st.warning("Selected learner not found.")
    st.stop()

# Get cluster value (IMPORTANT)

user_cluster = int(
    student_df["Cluster"].iloc[0]
)

st.write(f"Current Learner Cluster: {user_cluster}")

# Find all learners in same cluster
cluster_users = segments.loc[
    segments["Cluster"] == user_cluster,
    "UserID"
]

# Transactions of learners in same cluster
cluster_transactions = transactions[
    transactions["UserID"].isin(cluster_users)
]

# Courses already enrolled by selected learner
enrolled_courses = transactions.loc[
    transactions["UserID"] == selected_user,
    "CourseID"
]

# Most popular courses within cluster
popular_courses = (
    cluster_transactions
    .groupby("CourseID")
    .size()
    .reset_index(name="Enrollments")
    .sort_values(
        by="Enrollments",
        ascending=False
    )
)

# Remove already enrolled courses
popular_courses = popular_courses[
    ~popular_courses["CourseID"].isin(
        enrolled_courses
    )
]

# Merge with course details
recommended_courses = popular_courses.merge(
    courses,
    on="CourseID",
    how="left"
)

# Filters

if "CourseLevel" in courses.columns:

    level_filter = st.selectbox(
        "Course Level",
        ["All"] +
        sorted(
            courses["CourseLevel"]
            .dropna()
            .unique()
            .tolist()
        )
    )

    if level_filter != "All":

        recommended_courses = (
            recommended_courses[
                recommended_courses[
                    "CourseLevel"
                ] == level_filter
            ]
        )

if "CourseCategory" in courses.columns:

    category_filter = st.selectbox(
        "Course Category",
        ["All"] +
        sorted(
            courses["CourseCategory"]
            .dropna()
            .unique()
            .tolist()
        )
    )

    if category_filter != "All":

        recommended_courses = (
            recommended_courses[
                recommended_courses[
                    "CourseCategory"
                ] == category_filter
            ]
        )

# Display Recommendations

if len(recommended_courses) > 0:

    st.success(
        f"{len(recommended_courses)} recommendations found"
    )

    st.dataframe(
        recommended_courses.head(10),
        use_container_width=True
    )

else:

    st.warning(
        "No recommendations available for this learner."
    )
