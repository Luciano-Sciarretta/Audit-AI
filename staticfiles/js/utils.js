
// Obtener CSRF_Token
  export function getCSRFToken() {
    let cookieValue = null
    const name = 'csrftoken'

    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(';')
      for (let cookie of cookies) {
        if (cookie.startsWith(name + '=')) {
          cookieValue = cookie.substring(name.length + 1)
          
          break;
        }
      }
    }
    return cookieValue
  }

  export const BASEDIR = 'http://127.0.0.1:8000/'

