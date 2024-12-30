document.getElementById('prediction-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const parameters = document.getElementById('parameters').value.split(',').map(Number);
    console.log(parameters)
    const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ parameters })
    });
    console.log(await response.text());  // Ispisuje cijeli odgovor kao tekst

    const result = await response.json();
    document.getElementById('result').textContent = `Diagnosis: ${response.text}`;
});
