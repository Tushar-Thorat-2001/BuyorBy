$('#slider1, #slider2, #slider3 , #slider4, #slider5, #slider6, #slider7, #slider8').owlCarousel({
    loop: true,
    margin: 40,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    //console.log(id)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id

        },
        success: function(data){
            eml.innerText = data.quantity
            document.gertElementById("amount").innerText = data.amount
            document.gertElementById("totalmount").innerText = data.totalamount
        }

        
    })
})


$('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    //console.log(id)
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id

        },
        success: function(data){
            eml.innerText = data.quantity
            document.gertElementById("amount").innerText = data.amount
            document.gertElementById("totalmount").innerText = data.totalamount
        }

        
    })
})


$('.remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this
    //console.log(id)
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id
        },
        success: function(data){
            document.gertElementById("amount").innerText = data.amount
            document.gertElementById("totalmount").innerText = data.totalamount
            eml.parentNode.parentNode.parentNode.remove()
        }

        
    })
})