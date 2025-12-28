import { useState } from "react";
import { saveProfile } from "../services/api";
import { useNavigate } from "react-router-dom";

function ProfileForm() {
  const [profile, setProfile] = useState({
    name: "",
    degree: "",
    year: "",
    skills: "",
    interests: ""
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setProfile({ ...profile, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const user_id = localStorage.getItem("user_id");
localStorage.setItem(
  "profile",
  JSON.stringify({ ...profile })
);

    if (!user_id) {
      alert("User not logged in. Please login again.");
      navigate("/login");
      return;
    }

    try {
      await saveProfile({ ...profile, user_id });
      alert("Profile saved successfully");
      navigate("/dashboard");
    } catch (err) {
      alert("Error saving profile");
      console.error(err);
    }
  };

  return (
    <div className="container">
      <h2>Student Profile</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Full Name"
          value={profile.name}
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="degree"
          placeholder="Degree (e.g. BTech AIML)"
          value={profile.degree}
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="year"
          placeholder="Year (e.g. 3rd Year)"
          value={profile.year}
          onChange={handleChange}
          required
        />

        <textarea
          name="skills"
          placeholder="Skills (e.g. Python, ML, SQL)"
          value={profile.skills}
          onChange={handleChange}
          rows="3"
        />

        <textarea
          name="interests"
          placeholder="Interests (e.g. AI, Data Science)"
          value={profile.interests}
          onChange={handleChange}
          rows="3"
        />

        <button type="submit">Save Profile</button>
      </form>
    </div>
  );
}

export default ProfileForm;
