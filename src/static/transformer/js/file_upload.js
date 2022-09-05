function load_table(form){
  const BASE_URL = "http://127.0.0.1:8000/"
  const upload_btn = document.getElementById('btn-upload')
  upload_btn.addEventListener('click',
    function (e) {
        e.preventDefault();
        $.ajax({
          type: 'POST',
          url: "http://127.0.0.1:8000/" + "transformer/",
          data: {file : new FormData(form),
                  csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
          processData: false,
          contentType: false
          })
          .done(function (json) {
            console.log("ok !!")
            console.log(json)
            })
          .fail(function (json) {
            console.log("upps !!")
            console.log(json)
            })
    }
    )
  }
const form = document.getElementById("table-upload-form")
load_table(form)