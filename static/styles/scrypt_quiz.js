const $html = document.querySelector('html')
const $checkbox = document.querySelector('#switch')

$checkbox.addEventListener('change', function() {
    $html.classList.toggle('dark-mode')
})

res = document.querySelector('#resp')
console.log(res)
