import { useNavigate } from "react-router-dom";
import { getCareerGuidance } from "../services/aiApi";

function Dashboard() {
  const navigate = useNavigate();

  const handleCareerGuidance = async () => {
    const profile = JSON.parse(localStorage.getItem("profile"));

    if (!profile) {
      alert("Profile not found. Please fill profile again.");
      navigate("/profile");
      return;
    }

    const result = await getCareerGuidance(profile);
    localStorage.setItem("career_report", JSON.stringify(result));
    navigate("/report");
  };

  return (
    <div className="container">
      <h2>Career Guidance Dashboard</h2>
      <button onClick={handleCareerGuidance}>
        Get AI Career Guidance
      </button>
    </div>
  );
}

export default Dashboard;
