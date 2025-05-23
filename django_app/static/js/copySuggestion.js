function copySuggestion() {
  const suggestionTextDiv = document.getElementById("suggestionText");
  const suggestionText = suggestionTextDiv.innerText;

  navigator.clipboard.writeText(suggestionText).then(function() {
    const copyBtn = document.getElementById("copyButton");
    const original = copyBtn.innerHTML;
    copyBtn.innerHTML = '<i class="fa fa-check me-1"></i> Copiado!';
    copyBtn.classList.remove('btn-outline-primary');
    copyBtn.classList.add('btn-success');

    setTimeout(() => {
      copyBtn.innerHTML = original;
      copyBtn.classList.remove('btn-success');
      copyBtn.classList.add('btn-outline-primary');
    }, 1500);
  }, function() {
    alert("Não foi possível copiar. Tente manualmente.");
  });
}
