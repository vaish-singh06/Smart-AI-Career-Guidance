import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { loginUser } from "../services/api";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    const data = await loginUser(email, password);

    if (data.access_token) {
      localStorage.setItem("token", data.access_token);
      localStorage.setItem("user_id", data.user_id);
      navigate("/profile");
    } else {
      alert("Login failed");
    }
  };

  return (
    <div className="container">
      <h2>Student Login</h2>

      <form onSubmit={handleLogin}>
        <input type="email" required onChange={(e) => setEmail(e.target.value)} />
        <input type="password" required onChange={(e) => setPassword(e.target.value)} />
        <button type="submit">Login</button>
      </form>

      <p><Link to="/forgot-password">Forgot Password?</Link></p>
      <p>New user? <Link to="/register">Register</Link></p>
    </div>
  );
}

export default Login;
