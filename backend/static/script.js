document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData();
    const fileField = document.getElementById('audio-file');

    formData.append('audio-file', fileField.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        if (data.plot) {
            const visualization = document.getElementById('visualization');
            visualization.innerHTML = `<img src="/plot/${data.plot}" alt="Fourier Transform Plot">`;
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
