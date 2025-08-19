import { getCSRFToken } from '/static/js/utils.js';
import { BASEDIR } from '/static/js/utils.js';

document.addEventListener('DOMContentLoaded', () => {

  const csrfToken = getCSRFToken()
  const thumbUp = document.querySelector('.profile__thumb-up')
  const thumbDown = document.querySelector('.profile__thumb-down')


  if (thumbUp) {
    thumbUp.addEventListener('click', () => {
  
      const auditorId = thumbUp.getAttribute('data-auditor')
      const vote = 'up'

      fetch(`${BASEDIR}clients/client-review/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
          auditor_id : auditorId,
          vote : vote
        })
      })
      .then(response => response.json())
      .then(data => {
        console.log("Data:", data)
        if (!data.error) {
          const counter = document.querySelector('#thumb-up-count')
          console.log("Review_count:", data.review_count)
          counter.textContent = data.review_count;
        }
      })

    })
  }
})


