document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('prediction-form');
    const resultDiv = document.getElementById('prediction-result');

    // Add error checking for form elements
    if (!form) {
        console.error('Could not find form with id "prediction-form"');
        return;
    }

    if (!resultDiv) {
        console.error('Could not find div with id "prediction-result"');
        return;
    }

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Add error checking for form fields
        const elements = {
            age: document.getElementById('age'),
            sex: document.getElementById('sex'),
            bmi: document.getElementById('bmi'),
            children: document.getElementById('children'),
            smoker: document.getElementById('smoker'),
            region: document.getElementById('region')
        };

        // Check if all elements exist
        for (const [key, element] of Object.entries(elements)) {
            if (!element) {
                console.error(`Could not find element with id "${key}"`);
                resultDiv.innerHTML = `
                    <div class="alert-danger">
                        <p>Error: Form field "${key}" not found</p>
                    </div>
                `;
                return;
            }
        }
        
        const formData = {
            age: parseInt(elements.age.value),
            sex: elements.sex.value,
            bmi: parseFloat(elements.bmi.value),
            children: parseInt(elements.children.value),
            smoker: elements.smoker.value,
            region: elements.region.value
        };

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            
            if (result === null || result === undefined) {
                throw new Error('Received null or undefined response');
            }
            
            resultDiv.innerHTML = `
                <div class="${result.claim ? 'alert-warning' : 'alert-success'}">
                    <h3>Prediction Result:</h3>
                    <p>${result.claim ? 'High likelihood of filing a claim' : 'Low likelihood of filing a claim'}</p>
                </div>
            `;
        } catch (error) {
            console.error('Error:', error);
            resultDiv.innerHTML = `
                <div class="alert-danger">
                    <p>Error: ${error.message}</p>
                </div>
            `;
        }
    });
});