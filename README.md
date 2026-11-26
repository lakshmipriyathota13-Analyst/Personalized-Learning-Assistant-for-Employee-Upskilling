  # 🎓 AI-Powered Personalized Learning Assistant for Employee Upskilling
  
  ## Project Overview
  
  The AI-Powered Personalized Learning Assistant is a Streamlit-based application that delivers personalized learning recommendations for employees based on their department, role level, learning profile, and learning history.
  
  The project demonstrates how employee learning data can be transformed into actionable recommendations through rule-based personalization and explainable AI-style interactions.
  
  The application helps employees discover relevant learning opportunities while avoiding modules they have already completed.
  
  ---
  ## 🚀 Live Demo

Try the deployed application:

https://personalized-learning-assistant-for-employee-upskilling-h9vngx.streamlit.app
  
  ## Business Problem
  
  Traditional learning platforms often provide the same learning content to all employees regardless of their job role, department, previous learning activity, or individual preferences.
  
  This can lead to:
  
  - Reduced learner engagement
  - Repeated learning assignments
  - Irrelevant recommendations
  - Lower learning effectiveness
  
  This project addresses these challenges by providing personalized recommendations based on employee characteristics and completed learning activities.
  
  ---
  
  ## Key Features
  
  ### 👤 Employee Profile Dashboard
  
  The application automatically displays:
  
  - Employee ID
  - Department
  - Role Level
  - Preferred Learning Style
  
  ---
  
  ### 📊 Learning Insights
  
  The dashboard provides a quick overview of employee learning activity:
  
  - Completed Modules
  - In Progress Modules
  - Dropped Modules
  - Average Learning Score
  
  ---
  
  ### 🎯 Personalized Learning Recommendations
  
  Recommendations are generated using:
  
  - Department Matching
  - Role-Level Matching
  - Learning History Filtering
  - Module Catalog Personalization
  
  Previously completed modules are automatically excluded from recommendations.
  
  ---
  
  ### 🤖 AI Learning Assistant
  
  The interactive assistant provides additional support through:
  
  #### Ask Why
  
  Explains why a module was recommended based on:
  
  - Department
  - Role Level
  - Learning Style
  - Learning History
  
  #### Summary
  
  Displays a concise AI-style summary of the recommended module.
  
  #### Quick View
  
  Provides a short explanation of the recommendation.
  
  ---
  
  ## Recommendation Logic
  
  The recommendation engine follows a rule-based personalization approach.
  
  A module is recommended when:
  
  1. The module matches the employee's department or is available for all departments.
  2. The module matches the employee's role level or is available for all role levels.
  3. The employee has not already completed the module.
  
  The system then presents the most relevant learning opportunities from the training catalog.
  
  ---
  
  ## Application Workflow
  
  1. Employee selects their profile.
  2. Employee information is loaded.
  3. Learning history is analyzed.
  4. Completed modules are identified.
  5. Eligible modules are retrieved from the catalog.
  6. Personalized recommendations are generated.
  7. AI Assistant provides explanations and learning summaries.
  
  ---
  
  ## Technology Stack
  
  ### Frontend
  
  - Streamlit
  
  ### Data Processing
  
  - Python
  - Pandas
  
  ### Data Sources
  
  - Employee Learning Dataset
  - Module Catalog Dataset
  
  ---
  
  ## Files Included
  
  - `app.py`
  - `employee_learning_data.csv`
  - `module_catalog.csv`
  - `README.md`
  
  ---
  
  ## Future Improvements
  
  Potential enhancements include:
  
  - Recommendation scoring engine
  - Skill-gap analysis
  - Personalized learning paths
  - Manager dashboard
  - GPT/Azure OpenAI integration
  - Advanced recommendation models
  - Real-time learning analytics
  
  ---
  
  ## Author
  
  **Lakshmi Priya Thota**
  
  AI-Powered Personalized Learning Assistant for Employee Upskilling
