const orderForm = document.getElementById("orderForm")

orderForm.addEventListener("submit",async (e)=>{
    e.preventDefault() // not refresh thi page 
        
    /// using fetch
    const room_url = "handle_data" 

    let formData ={
        nom: orderForm.nom.value ,
        prenom: orderForm.prenom.value ,
        tel: orderForm.tel.value  ,
        addr:  orderForm.addr.value  ,
        qt: orderForm.qt.value ,  
        csrf_token : orderForm.csrf_token.value

    }
    console.log(orderForm.csrf_token.value)
    const resp= await fetch("/handle_data", {
        "method": "POST",
        headers:{
            "content-type":"application/json",
            "X-CSRFToken":orderForm.csrf_token.value 
        },
        "body":JSON.stringify(formData),
    });
    const data=await resp.json();
    

    console.log(data)
        

})



