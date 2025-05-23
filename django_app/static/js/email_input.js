document.addEventListener('DOMContentLoaded', function() {
  const fileInput = document.getElementById('id_uploaded_file');
  const textInput = document.getElementById('id_manual_text');

  if (fileInput && textInput) {
    // Quando o arquivo muda
    fileInput.addEventListener('change', function() {
      if (fileInput.value) {
        textInput.value = '';
        textInput.disabled = true;
      } else {
        textInput.disabled = false;
      }
    });

    // Quando o texto é digitado
    textInput.addEventListener('input', function() {
      if (textInput.value.length > 0) {
        fileInput.value = '';
        fileInput.disabled = true;
      } else {
        fileInput.disabled = false;
      }
    });
  }
});

