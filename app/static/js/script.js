// document.getElementById('prediction-form').addEventListener('submit', async function(event) {
//     event.preventDefault();
//     const parameters = document.getElementById('parameters').value.split(',').map(Number);
//     console.log(parameters)
//     const response = await fetch('/predict', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ parameters })
//     });
//     console.log(await response.text());  // Ispisuje cijeli odgovor kao tekst

//     const result = await response.json();
//     document.getElementById('result').textContent = `Diagnosis: ${response.text}`;
// });

document.getElementById('prediction-form').addEventListener('submit', function (e) {
    e.preventDefault(); // Sprječava default ponašanje forme

    // Prikupljanje svih vrijednosti
    const data = {};
    document.querySelectorAll('#prediction-form input').forEach(input => {
        data[input.name] = parseFloat(input.value); // Konvertuje vrijednosti u brojeve
    });

    // Slanje podataka kao JSON objekt
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(result => {
            // Prikaz rezultata
            document.getElementById('result').innerHTML = `Prediction: ${result.prediction} <br>`;

            document.getElementById('prediction-result').innerHTML =` ${result.prediction == 'Malignant' ? 
                "<p><b>Malignant breast cancer</b> refers to cancerous growths in the breast tissue that have the potential to invade nearby tissues and spread (metastasize) to other parts of the body. It is a serious and life-threatening condition that can be classified into various types based on the cells involved. Malignant breast cancer often requires aggressive treatments, including surgery, chemotherapy, radiation therapy, and targeted therapies, depending on the type and stage of cancer.</p>"
                : 
                "<p><b>Benign breast tumors</b> are non-cancerous growths that do not spread to other parts of the body. These tumors are typically not life-threatening and can often be removed or monitored without the need for extensive treatment. Common types of benign breast conditions include fibroadenomas, cysts, and benign hyperplasia. While they are not cancerous, benign tumors can cause discomfort or concern and may require medical attention for proper diagnosis and management.</p>"
            }`
            
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
