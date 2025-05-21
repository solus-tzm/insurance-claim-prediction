document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('prediction-form');
    const resultDiv = document.getElementById('prediction-result');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = {
            age: parseInt(document.getElementById('age').value),
            sex: document.getElementById('sex').value,
            bmi: parseFloat(document.getElementById('bmi').value),
            children: parseInt(document.getElementById('children').value),
            smoker: document.getElementById('smoker').value,
            region: document.getElementById('region').value
        };

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();
            
            resultDiv.innerHTML = `
                <div class="${result.claim ? 'alert-warning' : 'alert-success'}">
                    <h3>Prediction Result:</h3>
                    <p>${result.claim ? 'High likelihood of filing a claim' : 'Low likelihood of filing a claim'}</p>
                </div>
            `;
        } catch (error) {
            resultDiv.innerHTML = `
                <div class="alert-danger">
                    <p>Error: ${error.message}</p>
                </div>
            `;
        }
    });
});