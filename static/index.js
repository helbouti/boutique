const orderForm = document.getElementById("orderForm")

orderForm.addEventListener("submit",(e)=>{
    e.preventDefault() // not refresh thi page 
    
/// using fetch
const room_url = "handle_data" 

let data = new FormData()
data.append("nom",  orderForm.nom.value )
data.append("prenom",  orderForm.prenom.value )
data.append("tel",  orderForm.tel.value  )
data.append("addr",  orderForm.addr.value  )
data.append("qt",  orderForm.qt.value   )

fetch("/", {
    "method": "POST",
    "body": data,
}).then((rep)=>{
    
    rep.json() 
        .then(function(rep) {
            console.log(rep)
        });

})
})


