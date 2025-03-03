document.addEventListener('DOMContentLoaded', function() {
    // Preview uploaded files
    const fileInput = document.querySelector('input[type="file"]');
    const previewContainer = document.getElementById('preview-container');

    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            previewContainer.innerHTML = '';
            const file = e.target.files[0];
            
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const preview = document.createElement(file.type.startsWith('image/') ? 'img' : 'video');
                    preview.src = e.target.result;
                    preview.className = 'img-fluid mt-2';
                    if (preview.tagName === 'VIDEO') {
                        preview.controls = true;
                    }
                    previewContainer.appendChild(preview);
                }
                reader.readAsDataURL(file);
            }
        });
    }

    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});
