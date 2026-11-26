import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🎓",
    layout="wide"
)

# Read CSV
df = pd.read_csv("employee_learning_data.csv")
catalog = pd.read_csv("module_catalog.csv")


# Employee list
employee_list = sorted(df["employee_id"].unique())

st.title("🎓 AI-Powered Personalized Learning Assistant")

st.caption(
    "Personalized learning recommendations based on role, department, learning history and learning style."
)
st.subheader("👤 Select Employee")
col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    employee = st.selectbox(
        "Employee",
        employee_list
    )
emp_data = df[df["employee_id"] == employee]
role_level = emp_data["role_level"].iloc[0]
department = emp_data["department"].iloc[0]

st.markdown(
    f"""
    ### 👋 Welcome {department} {role_level}

    The assistant has prepared personalized learning recommendations
    based on your role, department, learning history, and preferred learning style.
    """
)

learning_style = emp_data["preferred_learning_style"].iloc[0]


emp_data = df[df["employee_id"] == employee]

st.subheader("👤 Employee Profile")

department = emp_data["department"].iloc[0]
role_level = emp_data["role_level"].iloc[0]
learning_style = emp_data["preferred_learning_style"].iloc[0]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("**Employee ID**")
    st.write(employee)

with col2:
    st.write("**Department**")
    st.write(department)

with col3:
    st.write("**Role Level**")
    st.write(role_level)

with col4:
    st.write("**Learning Style**")
    st.write(learning_style)

style_module_map = {
"Visual": ["Video"],
"Auditory": ["Webinar", "Video"],
"Reading/Writing": ["Article"],
"Kinesthetic": ["Quiz"]
}
preferred_types = style_module_map.get(
learning_style,
 ["Article", "Video", "Quiz", "Webinar"]
)
completed = emp_data[
    emp_data["completion_status"] == "Completed"
]

incomplete = emp_data[
    emp_data["completion_status"] == "Incomplete"
]
dropped = emp_data[
emp_data["completion_status"] == "Dropped"
]


st.subheader("📊 Learning Insights")


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("✅ Completed")
    st.write(len(completed))

with col2:
    st.write("📖 In Progress")
    st.write(len(incomplete))

with col3:
    st.write("⚠️ Dropped")
    st.write(len(dropped))

with col4:
    avg_score = emp_data["score"].mean()
    st.write("🎯 Avg Score")
    st.write(round(avg_score, 2))




st.subheader("🎯 Personalized Learning Recommendations")
left_col, right_col = st.columns([3,1])

with left_col:

    st.subheader("📚 Top Recommended Learning Modules")
completed_modules = emp_data[
emp_data["completion_status"] == "Completed"
]["module_name"].tolist()
department = emp_data["department"].iloc[0]

role_level = emp_data["role_level"].iloc[0]

recommended = catalog[
(
    (catalog["Department"] == department)
    |
    (catalog["Department"] == "All")
)
&
(
    (catalog["Role-level"] == role_level)
    |
    (catalog["Role-level"] == "All")
)
&
(~catalog["Module_name"].isin(completed_modules))
].copy()



st.caption(
    f"Recommendations are based on your {department} department, {role_level} role level, learning style, and completion history."
)


top_recommendations = recommended.head(3)

for _, row in top_recommendations.iterrows():

    with st.container():

      

     st.markdown(
        f"""
        #### 📚 {row['Module_title']}

        📘 Module ID: {row['Module_name']}

        🎯 What you'll learn:
        {row['Module_summary']}
        """
    )

    st.info(
    f"Recommended because it aligns with your {department} responsibilities and {role_level} role level."
)

    st.divider()
    
activity_df = emp_data[
    [
        "module_name",
        "completion_status",
        "score"
    ]
].head(5)

activity_df.columns = [
    "Module",
    "Status",
    "Score"
]

st.dataframe(
    activity_df,
    height=150
)

left_col, right_col = st.columns([3, 2])

with right_col:
    st.subheader("🤖 AI Learning Assistant")      


    col1, col2, col3 = st.columns(3)

    with col1:
     why_btn = st.button("💬 Ask Why")

    with col2:
     summary_btn = st.button("📋 Summary")

    with col3:
     short_btn = st.button("⚡ Quick View")
response_area = st.container()
if why_btn:

    with response_area:

        emp_data = df[df["employee_id"] == employee]

        department = emp_data["department"].iloc[0]

        role_level = emp_data["role_level"].iloc[0]

        learning_style = emp_data["preferred_learning_style"].iloc[0]

        st.info(
            f"""
            🤖 AI Explanation

            This module was recommended because you work in the
            {department} department and your role level is {role_level}.

            Your preferred learning style is {learning_style},
            therefore the assistant prioritizes content that can support
            your learning preferences and professional development.

            The recommendation also excludes modules that you have
            already completed, helping you focus on new learning opportunities.
            """
        )

if summary_btn:

    with response_area:

     emp_data = df[df["employee_id"] == employee]

    completed_modules = emp_data[
    emp_data["completion_status"] == "Completed"
    ]["module_name"].tolist()

    department = emp_data["department"].iloc[0]
    role_level = emp_data["role_level"].iloc[0]

    recommended = catalog[
    (
        (catalog["Department"] == department)
        |
        (catalog["Department"] == "All")
    )
    &
    (
        (catalog["Role-level"] == role_level)
        |
        (catalog["Role-level"] == "All")
    )
    &
    (~catalog["Module_name"].isin(completed_modules))
    ].copy()
    first_module = recommended.iloc[0]

    st.success(
    f"""
    📋 Module Summary

    {first_module['Module_title']}

    {first_module['Module_summary']}

    This module was selected as one of your recommended learning
    opportunities based on your profile and learning needs.
    """
    )


if short_btn:

    with response_area:
     st.warning(
    """
    ⚡ Short Version

    Recommended because it matches your profile,
    learning history, and workplace learning needs.
    """
)