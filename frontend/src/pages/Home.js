import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="container">
      <h1>Smart AI Career Guidance System</h1>
      <p>Your personalized career assistant</p>

      <Link to="/login">
        <button>Login</button>
      </Link>

      <Link to="/register">
        <button style={{ marginTop: "10px" }}>Register</button>
      </Link>
    </div>
  );
}

export default Home;
