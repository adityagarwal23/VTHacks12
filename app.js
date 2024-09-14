function submitForm() {
    const category1 = document.getElementById('category1').value;
    const category2 = document.getElementById('category2').value;
    const rating = document.getElementById('rating').value;

    // Simple validation
    if (category1 === '' || category2 === '' || rating === '') {
        alert('Please fill out all fields.');
        return;
    }

    // Collect existing data
    const existingData = document.getElementById('existingData');
    const currentData = existingData.textContent || '';

    // Append new data
    const newEntry = `Category 1: ${category1}, Category 2: ${category2}, Overall Rating: ${rating}\n`;
    existingData.textContent = currentData + newEntry;

    // Optionally, clear form inputs
    document.getElementById('ratingForm').reset();
}
