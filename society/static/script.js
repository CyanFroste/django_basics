const createPostModal = document.querySelector('.create-post-modal')

document.querySelectorAll('.create-post-modal-toggle').forEach(it =>
  it.addEventListener('click', () => {
    createPostModal?.classList.toggle('open')
  })
)
