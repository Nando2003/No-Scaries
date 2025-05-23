document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('emailUploadForm');
  const overlay = document.getElementById('loadingOverlay');

  if (form && overlay) {
    form.addEventListener('submit', function () {
      overlay.style.display = 'flex';
      overlay.style.alignItems = 'center';
      overlay.style.justifyContent = 'center';
    });
  }
});