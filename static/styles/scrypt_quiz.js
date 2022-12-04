const $html = document.querySelector('html')
const $checkbox = document.querySelector('#switch')

$checkbox.addEventListener('change', function() {
    $html.classList.toggle('dark-mode')
})


const res = document.getElementById("resp").innerHTML;
console.log(res)

if (res == " RESPUESTA: A "){
    console.log("certo")
    }else{
        console.log("errado")
    }
