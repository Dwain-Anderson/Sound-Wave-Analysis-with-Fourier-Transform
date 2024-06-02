document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData();
    const fileField = document.getElementById('audio-file');
    formData.append('audio-file', fileField.files[0]);
    formData.append('filter-type', document.getElementById('filter-type').value);
    formData.append('cutoff-frequency', document.getElementById('cutoff-frequency').value);
    formData.append('lowcut', document.getElementById('lowcut').value);
    formData.append('highcut', document.getElementById('highcut').value);

    fetch('/upload', {method: 'POST', body: formData})
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.blob();
    })
    .then(blob => {
        const url = URL.createObjectURL(blob);
        const visualization = document.getElementById('visualization');
        visualization.innerHTML = `<audio controls><source src="${url}" type="audio/wav"></audio>`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
