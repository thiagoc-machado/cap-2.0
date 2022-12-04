const $html = document.querySelector('html')
const $checkbox = document.querySelector('#switch')

$checkbox.addEventListener('change', function() {
    $html.classList.toggle('dark-mode')
})

const res = document.querySelector("#btn_a");

res.addEventListener("click",function(e){
    e.preventDefault();
    const name = document.querySelector("res");
    const value = name.value;
    console.log(value)
});


