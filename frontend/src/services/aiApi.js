const API_URL = "http://127.0.0.1:8000";

export async function getCareerGuidance(profile) {
  const res = await fetch(`${API_URL}/ai/full-career-guidance`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(profile)
  });

  return res.json();
}
