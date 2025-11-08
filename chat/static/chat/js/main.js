document.addEventListener('DOMContentLoaded', function () {
  const messageInput = document.getElementById('messageInput');
  
  messageInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      document.getElementById('chatForm').submit();
    }
  });

  // Lógica para envío de mensajes sin recargar la página
  const chatForm = document.getElementById('chatForm')
  const chatButton = document.getElementById('chatButton')
  
  chatForm.addEventListener('submit', function(e) {
    e.preventDefault()
    console.log("Formulario interceptado")
  })
});


