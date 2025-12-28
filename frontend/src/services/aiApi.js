const API_URL = "https://smart-ai-career-guidance.onrender.com";

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
