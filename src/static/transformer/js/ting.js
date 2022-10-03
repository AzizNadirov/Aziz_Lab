const BASE_URL = "http://127.0.0.1:8000/";


function get_cookie(name){
    let cookie_name = null;
    if(document.cookie && document.cookie !== '' ){
        let cookies = document.cookie.split(';');
        for(let i = 0; i < cookies.length; i++){
            let cookie = cookies[i].trim();
            if(cookie.substring(0, name.length + 1) === (name + '=')){
                cookie_value = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookie_value
}


function _drawTable_and_statTable(success_json){
    let dfs = document.getElementsByClassName("dataframe")
    for (let df of dfs) {
        df.className = df.className + " table"
    }
    let table = document.getElementById("table")
    table.innerHTML = success_json.table
    document.getElementById("table_pre_stats").innerHTML = success_json.stats.stat_table;
    let tables = document.getElementsByTagName("table")
    for (table of tables) {
        table.className = table.className + " " + "table"
    }
}

function load_hdf(btn){
    function listener(e){
    e.preventDefault();
    fetch(BASE_URL + "apps/transformer/",
        {method: "GET"}
        ).then(
            response => response.json()
        ).then(
            success => {
                let table = document.getElementById("table")
                table.innerHTML = success.table
                document.getElementById("table_pre_stats").innerHTML = success.stats.stat_table;
            }
        ).catch(
          error => {console.log(error);
          }
        );
  }
    btn.addEventListener('click', listener)
}


function _collect_tools_todo(e){
    let std = document.getElementById('slct_std');
    let mm = document.getElementById('slct_mm');
    let rb = document.getElementById('slct_rb');
    let lb = document.getElementById('slct_lb');
    let oh = document.getElementById('slct_oh');
    let rm = document.getElementById('slct_rm');

    let todo = {'std':[], 'mm':[], 'rb':[], 'lb':[], 'oh':[], 'rm':[]};

    for (let select of [std, mm, rb, lb, oh, rm]) {
        for (let op of select) {
            if (op.selected){
                todo[select.name].push(op.value)
            }
        }
    }
    _post_to_transforming(todo)
}

function collect_tools_apply(){
    let btn_apply = document.getElementById('btn_apply');
    btn_apply.addEventListener('click', _collect_tools_todo);
}


function _post_to_transforming(data){
    data = {'todo' : data}
    data = JSON.stringify(data)
    let csrtoken = get_cookie('csrftoken');
    fetch(BASE_URL + "apps/transformer/ting/",
        {method: "POST",
            body: data,
            headers: {"X-CSRFToken" : csrtoken, "Content-Type": "application/json"}
        }
        ).then(
            response => response.json()
        ).then(
            success => {
                _drawTable_and_statTable(success)
                document.getElementById('tr-tools').remove()
                document.getElementsByClassName("result_table"[0]).className = "col-md-12 col-lg-12"
            }
        ).catch(
          error => {console.log(error);
          }
        );
}
collect_tools_apply()

let dfs = document.getElementsByClassName("dataframe")
for (let df of dfs) {
        df.className = df.className + " table mh-25"
    }