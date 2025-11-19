function scrollToBottom(container) {
  if (container) {
    container.scrollTop = container.scrollHeight;
  }
}



document.addEventListener("DOMContentLoaded", function () {
  //Variables globales
  const chatForm = document.getElementById("chatForm")
  const chatInput = document.getElementById('chatInput')
  const chatHistory = document.querySelector('.chat__history')
  const fullText = document.querySelector('.chat__title').textContent;
  const userName = fullText.replace('Welcome ', '').replace(' to AuditAI', '');
  const chatContainer = document.querySelector('.chat')

  //Spiner o texto para espera de respuesta de ia
  const spinner = document.createElement('div')
  spinner.classList.add('spinner')
  spinner.style.display = 'none'

  const spinnerText = document.createElement('p')
  spinnerText.textContent = 'AuditAI is working on it…'
  spinnerText.classList.add('spinner-text')
  spinner.appendChild(spinnerText)
  //scroll para mostrar los últimos mensajes
  chatHistory.style.opacity = '0';
  scrollToBottom(chatContainer)
  setTimeout(() => {
    chatHistory.style.opacity = '1';
    chatHistory.style.transition = 'opacity 0.2s ease'; // Suavizar
  }, 10);

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


      //div para diferenciar mensajes del cliente
      const chatClient = document.createElement('div')
      chatClient.classList.add('client-chat')
      messageParagraph.classList.add('client-paragraph')
      chatClient.appendChild(clientParagraph)
      chatClient.appendChild(messageParagraph)
      chatMessages.appendChild(chatClient)

      //scroll del chat para que se vea el client input sin la rueda
      scrollToBottom(chatContainer)

      //Spinner mientras se espera la respuesta del servidor
      chatHistory.appendChild(spinner)
      spinner.style.display = 'block'
      scrollToBottom(chatContainer)


      const response = await responsePromise
      //Respuesta del servidor
      const data = await response.json()
      
        auditNameParagraph.innerHTML = `<strong>AuditAI:</strong>`
        spinner.style.display = 'none'
        auditResponse.textContent = data.ai_response

        chatMessages.appendChild(auditNameParagraph)
        chatMessages.appendChild(auditResponse)
        scrollToBottom(chatContainer)
      
      
    }
    else {
      console.log("Mensaje vacío boludo")
    }
  })
})

//scroll abajo al cargar la página

