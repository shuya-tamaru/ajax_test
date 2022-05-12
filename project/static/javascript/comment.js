

// window.addEventListener('DOMContentLoaded', function(){
//     console.log(1);
//     window.addEventListener('message', function (e) {
//         console.log(2);

//         if (e.origin !== "https://playcanv.as"){ 
//         }else{
//             document.getElementById( "id_cordinate" ).value = e.data.message ;
//         }
//     });
// });
window.addEventListener('DOMContentLoaded', function(){
    window.addEventListener('message', function (e) {
        if (e.origin !== "https://playcanv.as"){ 
        }else{
            document.getElementById( "id_cordinate" ).value = e.data.message ;
        }
    });

    setTimeout(()=>{
        var iframeDocument = document.getElementById("viewer");
        iframeDocument.contentWindow.postMessage({
            message: "hello",
        }, "https://playcanv.as/index/5mhxwmyj");
    },5000);

    const alertBox = document.getElementById('alert-box');
    const form = document.getElementById('p-form');

    const title = document.getElementById('id_title');
    const text = document.getElementById('id_text');
    const cordinate = document.getElementById('id_cordinate');
    const csrf = document.getElementsByName('csrfmiddlewaretoken');
    const url = '';
    const handleAlerts = (type,text) => {
        alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">
                                ${text}
                            </div>`
    }

    form.addEventListener('submit',e=>{
        e.preventDefault()
        const fd = new FormData();
        fd.append('csrfmiddlewaretoken', csrf[0].value);
        fd.append('title', title.value);
        fd.append('text', text.value);
        fd.append('cordinate', cordinate.value);

        $.ajax({
            type: 'POST',
            // url: url,
            enctype: 'multipart/form-data',
            data: fd,
            success: function(response){
                console.log(response);
                const sText = `succeccfully saved ${response.title}`
                handleAlerts('success', sText)
                setTimeout(()=>{
                    alertBox.innerHTML=''
                    title.value = ''
                    text.value = ''
                    cordinate.value = ''
                },2000)
            },
            error: function(error){
                handleAlerts('danger', 'upps..somthing went wrong')
            },
            cache: false,
            contentType: false,
            processData: false,
        })
    });
    console.log(1);
    $.ajax({
        type: 'GET',
        url: '/hello-world/',
        success: function(response){
            console.log('success', response);

        },
        error: function(error){
            console.log('error', error)
        }
    });
})