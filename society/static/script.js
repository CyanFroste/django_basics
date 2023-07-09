function getCookie(name) {
  if (!document.cookie) return
  for (let cookie of document.cookie.split(';')) {
    if (cookie.trim().startsWith(name)) {
      return decodeURIComponent(cookie.slice(name.length + 1))
    }
  }
}

const createPostModal = document.querySelector('.create-post-modal')

document.querySelectorAll('.create-post-modal-toggle').forEach(it =>
  it.addEventListener('click', () => {
    createPostModal?.classList.toggle('open')
  })
)

document.querySelectorAll('.post-like-toggle').forEach(it => {
  it.addEventListener('click', () => {
    const method = it.dataset.method
    const url = it.dataset.url
    fetch(url, {
      method,
      credentials: 'same-origin',
      headers: { 'X-CSRFToken': getCookie('csrftoken') },
    })
      .then(res => (res.ok ? res.json() : Promise.reject(res.statusText)))
      .then(data => {
        it.classList.toggle('button-outline')
        if (method === 'POST') {
          // after unlike
          it.dataset.method = 'DELETE'
          it.dataset.url = `${url}/${data.id}`
          const [c] = it.nextElementSibling.textContent.split(' ')
          it.nextElementSibling.textContent = `${+c + 1} likes`
        } else {
          // after unlike
          it.dataset.method = 'POST'
          it.dataset.url = url.slice(0, url.lastIndexOf('/'))
          const [c] = it.nextElementSibling.textContent.split(' ')
          it.nextElementSibling.textContent = `${+c - 1} likes`
        }
      })
      .catch(() => {})
  })
})
