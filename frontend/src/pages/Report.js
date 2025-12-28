function Report() {
  const report = JSON.parse(localStorage.getItem("career_report"));

  if (!report) {
    return (
      <div className="container">
        <p>No report available. Please run career guidance.</p>
      </div>
    );
  }

  return (
    <div className="container">
      <h2>Your AI Career Guidance Report</h2>

      <h3>🔹 Skill Analysis</h3>
      <p>{report.skill_analysis}</p>

      <h3>🔹 Skill Gaps</h3>
      <ul>
        {report.skill_gaps.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>

      <h3>🔹 Recommended Courses</h3>
      <p>{report.courses}</p>

      <h3>🔹 Job & Internship Suggestions</h3>
      <p>{report.jobs}</p>
    </div>
  );
}

export default Report;
