import streamlit as st
from PIL import Image

st.set_page_config(page_title="Srinivas B Portfolio", layout="wide")

# Sidebar with basic info
st.sidebar.image("https://avatars.githubusercontent.com/u/your-github-id", width=150)
st.sidebar.title("Srinivas B")
st.sidebar.markdown("""
**Principal Data & BI Architect**  
📍 Bangalore, India  
📧 sbejawa2222@gmail.com  
📞 +91 9611711188  
[LinkedIn](https://linkedin.com) | [GitHub](https://github.com)  
""")

# Header
st.markdown("""
# 👋 Hello, I'm Srinivas
### Data & BI Architect | GenAI Builder | ML-Ready Analytics
""")

st.markdown("""
I'm a seasoned professional with over 15 years of experience in building enterprise-scale data platforms, integrating ML/AI solutions, and enabling BI strategies that power business decisions. With a passion for clean architecture and cutting-edge AI, I help organizations unlock the full value of their data.
""")

# Skills section
st.markdown("---")
st.subheader("🧠 Skills & Tech Stack")
cols = st.columns(3)
cols[0].markdown("""
- ETL & Data Engineering  
- dbt, Airflow, Spark  
- SQL, Python, Pandas
""")
cols[1].markdown("""
- Power BI, Tableau, Qlik  
- ML & MLOps  
- LangChain, LlamaIndex
""")
cols[2].markdown("""
- AWS (Glue, Redshift, S3)  
- Streamlit, Flask, Dash  
- Pinecone, Weaviate, GPT-4
""")

# Projects
st.markdown("---")
st.subheader("🚀 Featured Projects")
st.markdown("""
### 🧾 Enterprise BI Chatbot (RAG + LLM)
Built a Streamlit-based assistant that answers natural language queries over dashboards using GPT-4 + Pinecone + Power BI API.

### 🔍 Data Quality Copilot
Auto-detect and explain pipeline issues with LLMs. Integrated Great Expectations with prompt-driven diagnostics.

### 📊 KPI Insight Generator
Summarizes quarterly metrics from Power BI into executive-ready insights using OpenAI + Pandas profiling.
""")

# Experience
st.markdown("---")
st.subheader("💼 Work Experience")
st.markdown("""
**Senior BI Manager – Regeneron**  
*2023 – Present*  
- Led BI strategy across manufacturing, quality, and supply chain.  
- Unified data sources (MES, SAP, LIMS) with GxP-compliant dashboards.

**Senior BI Manager – Morgan Stanley**  
*2018 – 2023*  
- Migrated legacy systems to Power BI. Built self-service analytics platform.  
- Designed complex data models across fund services and finance ops.

**BI Lead – CenturyLink**  
*2010 – 2018*  
- Created scalable BI solutions in telecom retail.  
- Led transition from QlikView to Power BI.
""")

# Education
st.markdown("---")
st.subheader("🎓 Education & Certifications")
st.markdown("""
- MTech in Data Science & ML – PES University (2023)  
- BE in ECE – Anna University (2008)  
- AWS Data Analytics – Specialty  
- Python for Everybody | Applied DS with Python (Coursera)
""")

# Footer
st.markdown("---")
st.caption("© 2025 Srinivas B – Built with ❤️ using Streamlit")
