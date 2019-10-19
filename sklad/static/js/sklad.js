nowActiv = "sk_all";
buttAdd = "sk_all";

function select_active(index) {
    $('#' + buttAdd).removeClass('activeFilter');
    $('#' + nowActiv).removeClass('activeFilter');

    nowActiv = index;
    $('#' + index).addClass('activeFilter');
    $('.sk_fast, .sk_dry, .sk_dan, .sk_all').hide();
    if (index != "sk_add"){
        document.getElementById('tableSql').style.display = 'block';
        document.getElementById('skladAdd').style.display = 'none';
    }

    if (index == "sk_all"){
        $('.sk_fast, .sk_dry, .sk_dan').show();
    }
    else if (index == "sk_dry"){
        $('.sk_dry').show();
    }
    else if (index == "sk_fast"){
        $('.sk_fast').show();
    }
    else if (index == "sk_dan"){
        $('.sk_dan').show();
    }
}


function skaldAdd() {
    document.getElementById('tableSql').style.display = 'none';
    document.getElementById('skladAdd').style.display = 'block';
    buttAdd = nowActiv;
    nowActiv = "sk_add";
    select_active(nowActiv);
}
function closeAddSklad(){
    document.getElementById('tableSql').style.display = 'block';
    document.getElementById('skladAdd').style.display = 'none';
    select_active(buttAdd);

}
document.getElementById('sklad_visota').onkeydown = function (e) {
    return !(/^[А-Яа-яA-Za-z ]$/.test(e.key));
};
document.getElementById('sklad_ploshad').onkeydown = function (e) {
    return !(/^[А-Яа-яA-Za-z ]$/.test(e.key));
};
document.getElementById('sklad_temp').onkeydown = function (e) {
    return !(/^[А-Яа-яA-Za-z ]$/.test(e.key));
};
document.getElementById('sklad_visota').onkeydown = function (e) {
    return !(/^[А-Яа-яA-Za-z ]$/.test(e.key));
};
document.getElementById('sklad_count_st').onkeydown = function (e) {
    return !(/^[А-Яа-яA-Za-z ]$/.test(e.key));
};

$('#formAddSklad').submit(function (e) {
    e.preventDefault();
    var data = $(this).serialize();
    $.ajax({
        type: "GET",
        url: "/sklad/add/",
        data: data,
        cache: false,
        success: function (data) {
            window.location = '/sklad/'
        }
    });
});