document.getElementById('salaryForm').addEventListener('submit', async function (e) {
    e.preventDefault();


    const experienceInput = document.getElementById('experience');
    const roleSelect = document.getElementById('role');
    const educationSelect = document.getElementById('education');
    const locationSelect = document.getElementById('location');
    const companyTypeSelect = document.getElementById('company_type');

    const resultOverlay = document.getElementById('resultOverlay');
    const salaryAmount = document.getElementById('salaryAmount');
    const submitBtn = this.querySelector('button[type="submit"]');


    const requestData = {
        "Experience": parseFloat(experienceInput.value),
        "Role": roleSelect.value,
        "Education": educationSelect.value,
        "Location": locationSelect.value,
        "Company_Type": companyTypeSelect.value
    };

    const originalBtnText = submitBtn.innerText;
    let dotCount = 0;
    submitBtn.innerText = "Calculating";
    const loadingInterval = setInterval(() => {
        dotCount = (dotCount + 1) % 4;
        submitBtn.innerText = "Calculating" + ".".repeat(dotCount);
    }, 400);
    submitBtn.disabled = true;
    submitBtn.classList.add('opacity-75', 'cursor-not-allowed');

    try {
        const response = await fetch('https://salary-predictor-gr9o.onrender.com/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestData)
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        const finalSalary = data.salary || data.prediction || 0;
        const formattedSalary = new Intl.NumberFormat('en-IN', {
            style: 'currency',
            currency: 'INR',
            maximumFractionDigits: 0
        }).format(finalSalary);

        salaryAmount.innerText = formattedSalary;
        resultOverlay.classList.remove('hidden');
        setTimeout(() => {
            resultOverlay.classList.remove('opacity-0', 'translate-y-4');
        }, 10);

    } catch (error) {
        salaryAmount.innerText = "Error";
        alert("Failed to get prediction.");
    } finally {
        clearInterval(loadingInterval)
        submitBtn.innerText = originalBtnText;
        submitBtn.disabled = false;
        submitBtn.classList.remove('opacity-75', 'cursor-not-allowed');
    }
});