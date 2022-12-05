const $html = document.querySelector('html')
const $checkbox = document.querySelector('#switch')

$checkbox.addEventListener('change', function() {
    $html.classList.toggle('dark-mode')
})

let corr = 0
let err = 0
let nr = 0
console.log(corr)
console.log(err)
console.log(nr)

const res = document.getElementById("resp").innerHTML;
console.log(res)

const btn1 = document.getElementById("btn_a");
    btn1.addEventListener("click", function(e){

        if (res == " RESPUESTA: A "){
            console.log("certo A")
            e.preventDefault();
            btn1.disabled = true;
            btn1.style.backgroundColor = "#2E8B57"; 
            corr += 1
            console.log(corr)
            }else{
                console.log("errado A")
                e.preventDefault();
                btn1.disabled = true;
                btn1.style.backgroundColor = "#FF69B4";  
                btn1.style.textDecoration = "line-through"
                err += 1
                console.log(err)
        }
    })

    const btn2 = document.getElementById("btn_b");
    btn2.addEventListener("click", function(e){

        if (res == " RESPUESTA: B "){
            console.log("certo B")
            e.preventDefault();
            btn2.disabled = true;
            btn2.style.backgroundColor = "#2E8B57"; 
            corr += 1
            console.log(corr)
            }else{
                console.log("errado B")
                e.preventDefault();
                btn2.disabled = true;
                btn2.style.backgroundColor = "#FF69B4";  
                btn2.style.textDecoration = "line-through"
                err += 1
                console.log(err)
        }
    })

    const btn3 = document.getElementById("btn_c");
    btn3.addEventListener("click", function(e){

        if (res == " RESPUESTA: C "){
            console.log("certo C")
            e.preventDefault();
            btn3.disabled = true;
            btn3.style.backgroundColor = "#2E8B57"; 
            corr += 1
            console.log(corr)
            }else{
                console.log("errado C")
                e.preventDefault();
                btn3.disabled = true;
                btn3.style.backgroundColor = "#FF69B4";  
                btn3.style.textDecoration = "line-through"
                err += 1
                console.log(err)
        }
    })

    const btn4 = document.getElementById("btn_d");
    btn4.addEventListener("click", function(e){

        if (res == " RESPUESTA: D "){
            console.log("certo D")
            e.preventDefault();
            btn4.disabled = true;
            btn4.style.backgroundColor = "#2E8B57"; 
            corr += 1
            console.log(corr)
            }else{
                console.log("errado D")
                e.preventDefault();
                btn4.disabled = true;
                btn4.style.backgroundColor = "#FF69B4";  
                btn4.style.textDecoration = "line-through"
                err += 1
                console.log(err)
        }
    })

    const btn5 = document.getElementById("btn_nr");
    btn5.addEventListener("click", function(e){
        btn5.style.backgroundColor = "#F0E68C";
        nr += 1
        console.log(nr)      
    })

