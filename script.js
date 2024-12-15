function showContent2(div_id){
    var divs = document.getElementsByClassName('content')
    for (var i = 0; i < divs.length; i++){
        divs[i].classList.remove('active')
    }

    var select_div = document.getElementById(div_id)
    select_div.classList.add('active')

}