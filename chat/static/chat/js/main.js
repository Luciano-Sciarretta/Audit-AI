document.addEventListener('DOMContentLoaded', function () {
  const messageInput = document.getElementById('messageInput');

  messageInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      document.getElementById('chatForm').submit();
    }
  });

});
