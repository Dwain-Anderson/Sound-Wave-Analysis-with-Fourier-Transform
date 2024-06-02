import React from 'react';

function AudioForm() {
    return (
        <div className='audio-form'>
            <h2>Upload Audio File</h2>
            <form id="upload-form" action="/upload" method="post" encType="multipart/form-data">
                <input type="file" id="audio-file" name="audio-file" required />
                <select id="filter-type" name="filter-type" required>
                    <option value="low-pass">Low Pass Filter</option>
                    <option value="high-pass">High Pass Filter</option>
                    <option value="band-pass">Band Pass Filter</option>
                </select>
                <input type="number" id="cutoff-frequency" name="cutoff-frequency" placeholder="Cutoff Frequency (Hz)" />
                <input type="number" id="lowcut" name="lowcut" placeholder="Low Cut Frequency (Hz)" />
                <input type="number" id="highcut" name="highcut" placeholder="High Cut Frequency (Hz)" />
                <input type="submit" value="Upload" />
            </form>
        </div>
    );
}

export default AudioForm;
