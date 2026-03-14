async function checkWallet() {
  const wallet = document.getElementById("wallet").value;

  const response = await fetch("http://localhost:8000/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      wallet: wallet,
    }),
  });

  const data = await response.json();

  document.getElementById("result").innerText =
    "Risk Score: " + data.risk_score;
}
