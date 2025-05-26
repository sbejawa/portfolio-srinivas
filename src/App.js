import logo from './logo.svg';
import './App.css';

function Portfolio() {
  return (
    <main className="min-h-screen bg-gray-50 text-gray-800 p-6">
      <section className="max-w-5xl mx-auto">
        <header className="mb-10">
          <h1 className="text-4xl font-bold text-blue-700">Srinivas B</h1>
          <p className="text-lg mt-2">Principal Data & BI Architect | Data Engineering | ML-Ready Analytics | Visualization Expert</p>
          <p className="mt-1 text-sm text-gray-600">Bangalore, India | sbejawa2222@gmail.com | +91 9611711188</p>
        </header>

        <section className="mb-12">
          <h2 className="text-2xl font-semibold text-blue-600 mb-4">About Me</h2>
          <p className="text-gray-700">
            I’m a Data & BI Architect with over 15 years of experience in building data platforms, cloud-native pipelines, and AI-integrated reporting systems. Skilled in AWS, Power BI, Tableau, Spark, and dbt, I specialize in delivering scalable analytics solutions across Pharma, Finance, and Telecom sectors. I’m passionate about transforming raw data into actionable insights and enabling real-time business decisions through intelligent dashboards and ML-ready architectures.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-2xl font-semibold text-blue-600 mb-4">Skills</h2>
          <ul className="grid grid-cols-2 gap-2 text-gray-700">
            <li>ETL / Data Pipelines</li>
            <li>Data Modeling (Star/Snowflake)</li>
            <li>Power BI / Tableau / Qlik</li>
            <li>Python / SQL / Spark</li>
            <li>AWS (S3, Redshift, Glue)</li>
            <li>Data Governance (Collibra)</li>
            <li>ML Readiness / AI Enablement</li>
            <li>Agile & Stakeholder Management</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-2xl font-semibold text-blue-600 mb-4">Projects</h2>
          <div className="space-y-6">
            <div>
              <h3 className="text-xl font-bold">Enterprise BI Platform – Regeneron</h3>
              <p>Designed a centralized BI platform integrating MES, LIMS, SAP, and QMS data, enhancing manufacturing decision-making and enabling GxP compliance.</p>
            </div>
            <div>
              <h3 className="text-xl font-bold">Fund Services Analytics – Morgan Stanley</h3>
              <p>Led BI modernization and dashboard strategy, improving KPI visibility and system performance by 50% through optimized data models and governance.</p>
            </div>
            <div>
              <h3 className="text-xl font-bold">Retail BI Migration – CenturyLink</h3>
              <p>Migrated legacy QlikView reports to Power BI for a Fortune 500 client, streamlining reporting processes and improving user adoption by 40%.</p>
            </div>
          </div>
        </section>

        <section className="mb-12">
          <h2 className="text-2xl font-semibold text-blue-600 mb-4">Certifications & Education</h2>
          <ul className="list-disc ml-5 text-gray-700">
            <li>MTech in Data Science and Machine Learning – PES University (Pursuing, 2023)</li>
            <li>BE in Electronics & Communication – Anna University (2008)</li>
            <li>AWS Certified Data Analytics – Specialty</li>
            <li>Cognos BI Author | Applied Data Science with Python | Python for Everybody</li>
          </ul>
        </section>

        <footer className="text-center text-sm text-gray-500 mt-10">
          &copy; 2025 Srinivas B. All rights reserved.
        </footer>
      </section>
    </main>
  );
}


export default Portfolio;
