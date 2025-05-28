import streamlit as st

st.set_page_config(page_title="Srinivas B - Resume", layout="wide")

# Title and Header
st.title("📄 Srinivas B")
st.subheader("Principal Data & BI Architect | AI-Enabled Analytics | Streamlit Resume")

# Sidebar
st.sidebar.title("Contact Info")
st.sidebar.markdown("""
📍 Bangalore, India  
📧 sbejawa2222@gmail.com  
📞 +91 9611711188  
🔗 [LinkedIn](https://linkedin.com)  
🔗 [GitHub](https://github.com)  
""")

# Summary
st.header("🔹 Summary")
st.write("""
Experienced Data & BI Architect with 15+ years of delivering enterprise data platforms and AI-powered insights. 
Specialized in data engineering, visualization (Power BI, Tableau), and ML/AI integrations across Pharma, BFSI, and Telecom.
""")

# Skills
st.header("🛠️ Skills & Tools")
cols = st.columns(3)
cols[0].markdown("- Data Engineering\n- ETL, Airflow, dbt")
cols[1].markdown("- Power BI, Tableau, Qlik\n- SQL, Python, Spark")
cols[2].markdown("- AWS (S3, Redshift, Glue)\n- ML: scikit-learn, MLflow")

# Experience
st.header("💼 Work Experience")

st.subheader("Senior BI Manager – Regeneron Pharma")
st.caption("June 2023 – Present")
st.write("""
- Led enterprise BI strategy across manufacturing, quality, and supply chain  
- Integrated MES, SAP, LIMS data and improved ETL by 40%  
- Established GxP-ready dashboards and governance with Collibra
""")

st.subheader("Senior BI Manager – Morgan Stanley")
st.caption("Jun 2018 – Jun 2023")
st.write("""
- Modernized fund services analytics stack  
- Built advanced dashboards and led migration to Power BI  
- Developed self-service frameworks and optimized KPIs
""")

st.subheader("BI Lead – CenturyLink")
st.caption("Apr 2010 – May 2018")
st.write("""
- Migrated QlikView to Power BI for Fortune 500 retail client  
- Streamlined data modeling and dashboard delivery  
- Trained business users and implemented BI governance
""")

# Projects
st.header("🚀 Projects")
st.markdown("""
- **GenAI Assistant for BI** – Chatbot over dashboards using LangChain + GPT-4  
- **Data Quality Copilot** – Auto-detect + explain pipeline issues using LLMs  
- **Power BI Insight Generator** – NLP + chart summarizer from live BI reports  
""")

# Education & Certs
st.header("🎓 Education & Certifications")
st.markdown("""
- MTech in Data Science and ML – PES University (2023)  
- BE in ECE – Anna University (2008)  
- AWS Certified Data Analytics – Specialty  
- Python for Everybody, Applied Data Science (Coursera)  
""")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
