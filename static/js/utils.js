
// Obtener CSRF_Token
function getCSRFToken() {
  let cookieValue = null
  const name = 'csrftoken'

  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(';')
    for (let cookie of cookies) {
      const trimCookie = cookie.trim()
      if (trimCookie.startsWith(name + '=')) {
        cookieValue = trimCookie.substring(name.length + 1)
        break;
      }
    }
  }
  return cookieValue
}


const BASEDIR = 'http://127.0.0.1:8000/'

const token = getCSRFToken()
console.log("Token:", token)