import streamlit as st
from PIL import Image

st.set_page_config(page_title="Srinivas B Portfolio", layout="wide")

# Sidebar with profile
st.sidebar.image("https://avatars.githubusercontent.com/u/your-github-id", width=150)
st.sidebar.title("Srinivas B")
st.sidebar.markdown("""
**Principal Data & BI Architect**  
📍 Bangalore, India  
📧 sbejawa2222@gmail.com  
📞 +91 9611711188  
[LinkedIn](https://linkedin.com) | [GitHub](https://github.com)
""")

# Main Header
st.markdown("""
# 👋 Hello, I'm Srinivas
### Data rchitect | GenAI Builder | ML-Ready Analytics
I'm a seasoned professional with over 15 years of experience in enterprise data platforms, ML/AI, and BI strategy.
""")

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

st.markdown("---")
st.subheader("🚀 Portfolio Projects")

project_data = [
    {
        "title": "Credit Card Fraud Detection",
        "subtitle": "Data Analysis",
        "desc": "Created a ML model to predict whether a transaction is fraudulent on a dataset from Kaggle. Used matplotlib to visualize relationships between target and predictor variables. Compared results from multiple classification models using scikit-learn (Python).",
        "tags": ["Data Analysis", "Data Science", "Machine Learning", "Supervised Learning", "Predictive modeling", "Python"],
        "image_url": "https://images.unsplash.com/photo-1611971262505-b7b45e514d9a",
        "link": "https://example.com/fraud-detection"
    },
    {
        "title": "Twitter Analysis of US Senators",
        "subtitle": "Data Analysis",
        "desc": "Analysed tweets from US senators from 2008–2017 to understand key topics, key members, and relationships. Created multiple hypotheses and tested them using network analysis and NLP techniques.",
        "tags": ["Data Analysis", "Data Science", "Python", "Network analysis", "BeautifulSoup", "JSON", "networkx", "wordcloud"],
        "image_url": "https://cdn-icons-png.flaticon.com/512/733/733579.png",
        "link": "https://example.com/twitter-senators"
    }
]

cols = st.columns(2)
for idx, project in enumerate(project_data):
    with cols[idx % 2]:
        st.image(project["image_url"], use_column_width=True)
        st.caption(project["subtitle"].upper())
        st.markdown(f"### {project['title']}")
        st.write(project['desc'])
        st.markdown(", ".join([f"`{tag}`" for tag in project['tags']]))
        st.markdown(f"[🔗 View Project]({project['link']})")
        st.markdown("---")

st.subheader("💼 Experience")
st.markdown("""
**Senior BI Manager – Regeneron**  
*2023 – Present*  
Led BI strategy across manufacturing, quality, and supply chain. Integrated MES, SAP, and LIMS systems with GxP-ready dashboards.

**Senior BI Manager – Morgan Stanley**  
*2018 – 2023*  
Migrated fund analytics to Power BI. Built executive dashboards. Improved KPI visibility across departments.

**BI Lead – CenturyLink**  
*2010 – 2018*  
Designed and deployed BI frameworks in telecom and retail. Led Power BI adoption across business units.
""")

st.subheader("🎓 Education & Certifications")
st.markdown("""
- MTech in Data Science & ML – PES University (2023)  
- BE in ECE – Anna University (2008)  
- AWS Certified Data Analytics – Specialty  
- Python for Everybody | Applied Data Science with Python (Coursera)
""")

st.markdown("---")
st.caption("© 2025 Srinivas B – Built with ❤️ using Streamlit")
