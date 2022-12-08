const $html = document.querySelector('html')
const $checkbox = document.querySelector('#switch')
dark = 0
$checkbox.addEventListener('change', function() {
    $html.classList.toggle('dark-mode')
    $html.classList.toggle('dark')
    })
nodupl = 0
corr = 0
err = 0
nr = 0

corr = getCookie("corr")
err = getCookie("err")
nr = getCookie("nr")

console.log("correto " + corr);
console.log("errado " + err);
console.log("n resp " + nr);
console.log("Tema " + dark)


const res = document.getElementById("resp").innerHTML;
console.log(res)
//*****************************************BTN RESP A************************************ */
const btn1 = document.getElementById("btn_a");
btn1.addEventListener("click", function(e){
    if (res == "RESPUESTA: A\n"){
        console.log("certo A")
        e.preventDefault();
        btn1.disabled = true;
        btn1.style.backgroundColor = "#2E8B57"; 
        if (nodupl == 0){
            corr ++
            nodupl ++
        }
        console.log(corr)
        }else{
            console.log("errado A")
            e.preventDefault();
            btn1.disabled = true;
            btn1.style.backgroundColor = "#FF69B4";
            btn1.style.textDecoration = "line-through"
            if (nodupl == 0){
                err ++
                nodupl ++
            }
            console.log(err)
            console.log(nodupl)
        }
    })
//*****************************************BTN RESP B************************************ */
    const btn2 = document.getElementById("btn_b");
    btn2.addEventListener("click", function(e){
    if (res == "RESPUESTA: B\n"){
        console.log("certo B")
        e.preventDefault();
        btn2.disabled = true;
        btn2.style.backgroundColor = "#2E8B57"; 
        if (nodupl == 0){
            corr ++
            nodupl ++
        }
        console.log(corr)
        }else{
            console.log("errado B")
            e.preventDefault();
            btn2.disabled = true;
            btn2.style.backgroundColor = "#FF69B4";  
            btn2.style.textDecoration = "line-through"
            if (nodupl == 0){
                err ++
                nodupl ++
            }
            console.log(err)
        }
    })
//*****************************************BTN RESP C************************************ */
    const btn3 = document.getElementById("btn_c");
    btn3.addEventListener("click", function(e){
        if (res == "RESPUESTA: C\n"){
            console.log("certo C")
            e.preventDefault();
            btn3.disabled = true;
            btn3.style.backgroundColor = "#2E8B57"; 
            if (nodupl == 0){
                corr ++
                nodupl ++
            }
            console.log(corr)
            }else{
                console.log("errado C")
                e.preventDefault();
                btn3.disabled = true;
                btn3.style.backgroundColor = "#FF69B4";  
                btn3.style.textDecoration = "line-through"
                if (nodupl == 0){
                    err ++
                    nodupl ++
                }
                console.log(err)
        }
    })
//*****************************************BTN RESP C************************************ */
    const btn4 = document.getElementById("btn_d");
    btn4.addEventListener("click", function(e){
        if (res == "RESPUESTA: D\n"){
            console.log("certo D")
            e.preventDefault();
            btn4.disabled = true;
            btn4.style.backgroundColor = "#2E8B57"; 
            if (nodupl == 0){
                corr ++
                nodupl ++
            }
            console.log(corr)
            }else{
                console.log("errado D")
                e.preventDefault();
                btn4.disabled = true;
                btn4.style.backgroundColor = "#FF69B4";  
                btn4.style.textDecoration = "line-through"
                if (nodupl == 0){
                    err ++
                    nodupl ++
                }
                console.log(err)
        }
    })
//*****************************************BTN NO RESP*********************************** */
    const btn5 = document.getElementById("btn_nr");
    btn5.addEventListener("click", function(e){
        btn5.style.backgroundColor = "#F0E68C";
        if (nodupl == 0){
            nr ++
            nodupl ++
            setCookie("nr", nr, 365)
        }else{
            e.preventDefault();
        }
        console.log(nr)      
    })
//*****************************************BTN PROX************************************** */
    const btn6 = document.getElementById("btn_p");
    btn6.addEventListener("click", function(e){
        btn6.style.backgroundColor = "#2E8B57";
        //e.preventDefault();
        setCookie("corr", corr, 365)
        setCookie("err", err, 365)
        setCookie("nr", nr, 365)
        setCookie("dark", dark, 365)
    })
//*****************************************RES COUNT************************************* */

document.getElementById("corr").innerHTML = "Corectas " + corr;
document.getElementById("err").innerHTML = "Erroneas " + err;
document.getElementById("nr").innerHTML = "No resp. " + nr;
tot = corr + err + nr
document.getElementById("tot").innerHTML = "Total.   " + tot;
if (dark == 0){
    document.getElementById("switch").checked = false;
}else{
    document.getElementById("switch").checked = true;
}


//*****************************************SET COOKIES*********************************** */
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}
    
function getCookie(cname) {
    let name = cname + "=";
    let ca = document.cookie.split(";");
    for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") {
        c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
    }
    }
    return "";
}
    
    function eraseCookie(nome) {   
        document.cookie = nome +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    }


