import { getCSRFToken } from '/static/js/utils.js';
import { BASEDIR } from '/static/js/utils.js';

document.addEventListener('DOMContentLoaded', () => {

  const csrfToken = getCSRFToken()
  const thumbUp = document.querySelector('.profile__thumb-up')
  const thumbDown = document.querySelector('.profile__thumb-down')

  function manageVoteCount(auditorId, voteType) {
    fetch(`${BASEDIR}clients/client-review/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify({
        auditor_id: auditorId,
        vote: voteType
      })
    })
      .then(response => response.json())
      .then(data => {
        // console.log("Data:", data)
        if (!data.error) {
          const counterUp = document.querySelector('#thumb-up-count')
          const counterDown = document.querySelector('#thumb-down-count')
          counterUp.textContent = data.review_up_count;
          counterDown.textContent = data.review_down_count;
        }
      })
      .catch(error => console.error("Fetch error:", error))
  }

  if (thumbUp) {
    thumbUp.addEventListener('click', () => {
      const auditorId = thumbUp.dataset.auditor
      manageVoteCount(auditorId, 'up')
    })
  }

  if (thumbDown) {
    thumbDown.addEventListener('click', () => {
      const auditorId = thumbDown.dataset.auditor
      manageVoteCount(auditorId, 'down')
    })
  }
})


