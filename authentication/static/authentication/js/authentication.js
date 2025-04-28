document.addEventListener('DOMContentLoaded', function () {
  const uploadButton = document.getElementById('upload-btn');
  const fileInput = document.getElementById('id_documents');
  const fileNameDisplay = document.getElementById('file-name');

  console.log('Elementos encontrados:', {
    uploadButton: uploadButton !== null,
    fileInput: fileInput !== null,
    fileNameDisplay: fileNameDisplay !== null
  });

  if (uploadButton && fileInput && fileNameDisplay) {
    uploadButton.addEventListener('click', function (e) {
      e.preventDefault();
      fileInput.click();  //Simulo un click en el input hidden para acceder a buscar los archivos
    });

    fileInput.addEventListener('change', function () {
      const fileName = this.files.length > 0 ? this.files[0].name : 'No file selected';
      fileNameDisplay.textContent = fileName;
    });
  } else {
    console.error('Elementos faltantes:', {
      uploadButton: uploadButton === null,
      fileInput: fileInput === null,
      fileNameDisplay: fileNameDisplay === null
    });
  }


  //Validación de email

  const email1Input = document.getElementById('id_email1');
  const email2Input = document.getElementById('id_email2');
  const errorElement = document.getElementById('email-error');
  const form = document.querySelector('form');
  const submitButton = form ? form.querySelector('button[type="submit"]') : null;

  function validateEmail(isSubmit = false) {
    const email1 = email1Input.value.trim();
    const email2 = email2Input.value.trim();

    // Si ambos están vacíos
    if (email1 === '' && email2 === '') {
      if (isSubmit === true) {
        errorElement.textContent = 'Emails cannot be empty.';
        errorElement.style.display = 'block';
       
      } else {
        errorElement.style.display = 'none';
      }
      
      return false;
    }

    else if (email1 !== email2) {
      errorElement.textContent = 'All emails should be exactly the same in content and formatting.';
      errorElement.style.display = 'block';
      if (submitButton) submitButton.disabled = true;
      return false;
    }
    // Si coinciden y no están vacíos
    else {
      errorElement.style.display = 'none';
      if (submitButton) submitButton.disabled = false;
      return true;
    }
  }

  // Validación inicial 
  if (email1Input && email2Input) {

    validateEmail(); // Estado inicial (no es submit)
    email1Input.addEventListener('input', () => validateEmail());
    email2Input.addEventListener('input', () => validateEmail());
  }

  if (form) {
    form.addEventListener('submit', function (e) {
      const isValid = validateEmail(true)
      if (!isValid) { 
        e.preventDefault();
      } 
    });
    
  }
  
});

