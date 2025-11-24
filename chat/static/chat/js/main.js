
document.addEventListener("DOMContentLoaded", function () {

  const chatForm = document.getElementById("chatForm")
  const chatInput = document.getElementById('chatInput')
  const chatHistory = document.querySelector('.chat__history')
  const fullText = document.querySelector('.chat__title').textContent;
  const userName = fullText.replace('Welcome ', '').replace(' to AuditAI', '');
  // Lógica para envío de formulario con el enter

  chatInput.addEventListener('keydown', function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      chatForm.dispatchEvent(new Event('submit'))
    }
  });

  chatForm.addEventListener("submit", async function (e) {
    e.preventDefault()
    const message = chatInput.value.trim();
    const formData = new FormData(chatForm)

    if (message) {
      const responsePromise = fetch('/chat/client_input/', {
        method: 'POST',
        body: formData,
      })
      // limpio el text area
      chatInput.value = ""
      // Creo un div para insertar los p con  el input del cliente y la respuesta de la ia
      const chatMessages = document.createElement('div')
      chatMessages.classList.add('chat__messages')
      chatHistory.appendChild(chatMessages)
      //Creo el p con el mensaje del cliente
      const clientParagraph = document.createElement('p')
      const messageParagraph = document.createElement('p')
      const auditNameParagraph = document.createElement('p')
      const auditResponse = document.createElement('p')

      clientParagraph.innerHTML = `<strong>${userName}:</strong>`
      messageParagraph.textContent = message

      chatMessages.appendChild(clientParagraph)
      chatMessages.appendChild(messageParagraph)
      //scroll del chat para que se vea el client input sin la rueda
      const chatContainer = document.querySelector('.chat')
      chatContainer.scrollTop = chatContainer.scrollHeight
     

      const response = await responsePromise
      //Respuesta del servidor
      const data = await response.json()
      
      auditNameParagraph.innerHTML = `<strong>AuditAI:</strong>`
      auditResponse.textContent = data.ai_response

      chatMessages.appendChild(auditNameParagraph)
      chatMessages.appendChild(auditResponse)

      chatContainer.scrollTop = chatContainer.scrollHeight
    }
    else {
      console.log("Mensaje vacío boludo")
    }


  })
})