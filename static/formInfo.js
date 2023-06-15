formWords = document.querySelector('form#words')

formWords.addEventListener('submit', function(e) {
    e.preventDefault()
    const formData = new FormData(this);
    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(result => {
        document.querySelector('#result').textContent = result;
    })
    .catch(error => console.error(error))
})