function load_table2(ting_url, aing_url){
  const BASE_URL = "http://127.0.0.1:8000/";
  const btn_load = document.getElementById('btn_load');
  const file_input = document.getElementById("file_input");
  const csrf_token = document.querySelector('input[name="csrfmiddleware{'todo': 'ok'}token"]');

  function listener(e){
    console.log("click!")
    e.preventDefault();
    var data = new FormData();
    data.append("file", file_input.files[0]);
    data.append("csrfmiddlewaretoken", csrf_token.value);
    data.append("delimeter",  document.getElementById("delimeter").value)

    fetch(BASE_URL + "transformer/",
        {method: "POST", body: data}
        ).then(
            response => response.json()
        ).then(
            success => {
                console.log(success)
                document.getElementById('preload_file').remove()
                var table = document.getElementById("table")
                table.innerHTML = success.table
                document.getElementById("table_pre_stats").innerHTML =
                    success.stats.stat_table + "<br>" + success.stats.row_col;
                insert_buttons(ting_url, aing_url)
            }
        ).catch(
          error => {console.log(error);
                    console.log(ting_url, aing_url)
          }// Handle the error response object
        );
  }
  btn_load.addEventListener('click', listener)
}

function insert_buttons(url_ting, url_aing){
    const tranform_or_analysis =
    `<button class="btn-success btn-block" id="btn_transform">
        <a href=${url_ting}>GoTo <b>Transform</b></a>
     </button>
     <button class="btn-success btn-block" id="btn_analisis">
        <a href=${url_aing}>GoTo <b>Analising</b></a>
     </button>`

    document.getElementById('tranform_or_analysis').innerHTML = tranform_or_analysis
}




