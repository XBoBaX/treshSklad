nowActiv2 = "otp";
buttAdd2 = "otp";
$('.prb, .prn, .otm').hide();
$('#countpallet, #tableSettRz, #stopItem, #tr5, #sendGr, #sendGr2, #otmenaGr, #car_add1, #traffic_dateSet2').hide();
index_item = 1;
countP = 0;
if (window.location.pathname === '/') {
    nowActiv2 = "all1";
    buttAdd2 = "otp1";
}
if (window.location.pathname === "/traffic/unloading/"){
    selected = $("#sklad_tovar").val();
    onSklad(selected)
}
$("#sklad_tovar").change(function() {
    selected = $("#sklad_tovar").val();
    onSklad(selected);
});
indTran = 1;
function changeUploader(number){
    selected = $("#uploader_car" + number).val();
    car = 0;
    t_all = [];
    t_all2 = [];

    t_count = document.getElementById("uploader_car" + number).options.length;
    for (i = 0; i < t_count; i++){
        t_all[i] = document.getElementById("uploader_car" + number).options[i].text;
        t_all2[i] = document.getElementById("uploader_car" + number).options[i].value;
    }
    for (i = 0; i < indTran; i++){
        i+=1;
        var t1 = $('#uploader_car' + i + ">option:selected").index();
        t_all.splice(t1,1);
        t_all2.splice(t1,1);
    }
    idUL = $("#hiddenRT2").val();
    indTran += 1;
    var html_code = '<div class="col-4 divNameT">\n' +
        '<label for="uploader_car'+ indTran +'" class="nameTable">Транспорт для разгрузки '+indTran+'</label></div>\n' +
        '<div class="col-7"><select class="btnTable" id="uploader_car'+ indTran +'" name="uploader_car'+ indTran +'" onchange="changeUploader('+ indTran +')">\n';
    indTran -= 1;

    for (i = 0; i < t_all.length; i++)
    {
        html_code += '<option value="' + t_all2[i] + '">' + t_all[i] + '</option>\n';
    }

    html_code += '</select></div>';
    if (number == indTran){
        $("#uploader1").append(html_code);
        indTran += 1;
    }
}
function razgruzkaTraffic2(indexTrafficU) {
    data = {"UnloadId": indexTrafficU, "count": indTran};
    if (indTran == 1){
        data["t1"] = $("#uploader_car1").val();
    }
    else for (i = 1; i <= indTran; i++)
    {
        data["t" + i] = $("#uploader_car" + i).val();
    }
    $.ajax({
        type: "GET",
        url: "/traffic/setRazgruzkaU/" + indexTrafficU + "/",
        data: data,
        cache: false,
        success: function (data) {
            $('#razgruzkaBtn').hide();
            $('#stopBtn').show();
        }
    });
}

function onSklad(selected) {
    $('#sklad_tovar option').each(function(){
        $('.' + (this.value)).hide();
    });
    if (selected === "Все") {
        $('#sklad_tovar option').each(function(){
            $('.' + (this.value)).show();
        });
    }
    else $('.' + selected).show();
}

function select_active3(index) {
    $('#' + nowActiv2).removeClass('activeFilter');
    nowActiv2 = index;
    $('#' + index).addClass('activeFilter');
    $('.otp1, .prb1, .prn1, .otm1').hide();
    $('#sklad_tovar').hide();
    $('.' + index).show();
    if (index === "all1"){
        $('.otp1, .prb1, .prn1, .otm1').show();
        $('#sklad_tovar').show();
        $('#sklad_tovar').val("Все");

    }
}
dateGet1 = "";
function podtverdit() {
    $('#sendGr2, #traffic_dateSet').hide();
    data["date"] = $('#traffic_dateSet').val();
    data["sklad"] = $('#traffic5').val();
    $.ajax({
        type: "GET",
        url: "/traffic/addNew/1",
        data: data,
        cache: false,
        success: function (data) {
            alert("Дата прибытия: " + data);
            dateGet1 = data;
            $('#traffic_dateSet2').val(data);
            $('#sendGr, #traffic_dateSet2').show();
        }
    });

}
countPallet = 0;
function selProduct(index)
{
    nowItem = $("#" + index + "Tov");
    nowItemC = $("#" + index + "TovC");
    if (nowItem.hasClass("activeTr"))
    {
        nowItem.removeClass("activeTr");
        countPallet -= parseInt(nowItemC.text());
    }
    else {
        nowItem.addClass("activeTr");
        countPallet += parseInt(nowItemC.text());
    }
    $('#razgruzka_count').val(countPallet);
}
$('#btnGetTimeRaz2').hide();
function btnGetTimeRaz(){
    data = {"date": $("#razgruzka_date").val(), "sk": $('#sklad_tovar').val()};
    $.ajax({
        type: "GET",
        url: "/traffic/unloading/getTime/",
        data: data,
        cache: false,
        success: function (data) {
            alert("Дата разгрузки " + data);
            $("#timeRaz").val(data);
            $("#btnGetTimeRaz, #zz1").hide();
            $("#btnGetTimeRaz2, #zz2").show();
        }
    });
}
function btnGetTimeRaz2(){
    data = {"date": $("#razgruzka_date").val(), "sk": $('#sklad_tovar').val(),
        "arr": $("#timeRaz").val()};
    countPal = 0;
    $(".activeTr").each(function (i) {
        data["t" + countPal] = $(this).attr("id");
        countPal++;
    });
    data["countPal"] = countPal;
    $.ajax({
        type: "GET",
        url: "/traffic/unloading/addNew/",
        data: data,
        cache: false,
        success: function (data) {
            window.location = "/traffic/unloading/";
        }
    });
}

$("#btnSelectTovar2").hide();
function goBackToSettingRz() {
    $("#btnSelectTovar2, #tableSettRz").hide();
    $("#btnSelectTovar").show();
}
function goToSettingRz() {
    $("#btnSelectTovar").hide();
    $("#tableSettRz, #btnSelectTovar2").show();
}
function SendTraffic() {
    countP += parseInt($(id4).val());
    $('#traffic4').val(countP);
    data = {"traffic1": $("#traffic1").val(), "traffic3": $("#traffic3").val(),
        "traffic5": $("#traffic5").val(), "traffic10": $("#traffic10").val(), "count": index_item,
    "date": dateGet1};
    for (i = 0; i <= index_item; i++){
        data["1t" + i] = $("#traffic-1-" + i).val();
        data["2t" + i] = $("#traffic-2-" + i).val();
        data["3t" + i] = $("#traffic-3-" + i).val();
        data["4t" + i] = $("#traffic-4-" + i).val();
    }
    $.ajax({
        type: "GET",
        url: "/traffic/addNew/end",
        data: data,
        cache: false,
        success: function (data) {
           window.location = "/traffic/"
        }
    });
}

function StopAddItem() {
    index_item -= 1;
    flag = false;
    id1 = "#traffic-1-" + index_item;
    id2 = "#traffic-2-" + index_item;
    id3 = "#traffic-3-" + index_item;
    id4 = "#traffic-4-" + index_item;
    if ($(id1).val().length === 0) {
        $(id1).addClass('danger_input');
        flag = true;
    }
    else $(id1).removeClass('danger_input');
    if ($(id2).val().length === 0) {
        $(id2).addClass('danger_input');
        flag = true;
    }
    else $(id2).removeClass('danger_input');
    if ($(id3).val().length === 0) {
        $(id3).addClass('danger_input');
        flag = true;
    }
    else $(id3).removeClass('danger_input');
    if ($(id4).val().length === 0) {
        $(id4).addClass('danger_input');
        flag = true;
    }
    else $(id4).removeClass('danger_input');
    if ($("#traffic1").val().length === 0) {
        $("#traffic1").addClass('danger_input');
        flag = true;
    }
    else $("#traffic1").removeClass('danger_input');
    index_item += 1;
    if (flag === true) return;
    countP += parseInt($(id4).val());
    $('#traffic4').val(countP);
    data = {"traffic1": $("#traffic1").val(), "traffic3": $("#traffic3").val(), "countP": countP,
        "traffic10": $("#traffic10").val()};
    temp = [];
    for (i = 1; i < index_item; i++){
        temp[i-1] = $("#traffic-2-" + i).val();
    }
    data["min"] = Math.min(...temp);
    $.ajax({
        type: "GET",
        url: "/traffic/addNew/",
        data: data,
        cache: false,
        success: function (data) {
            $('#additem, #stopItem').hide();
            $('#tr5, #sendGr2, #otmenaGr').show();

            for (i = 0; i < data["count"];i++){
                var html_code = '<option value="'+data[i]+'">'+data[i]+'</option>';
                $("#traffic5").append(html_code);
            }
            if (data["count"] == 0){
                var html_code = '<option value="0">Нет доступных для размещения</option>';
                $("#traffic5").append(html_code);
            }
        }
    });
}

function addNewItem() {
    $('#stopItem').show();
    if (index_item !== 1){
        index_item -= 1;
        flag = false;
        id1 = "#traffic-1-" + index_item;
        id2 = "#traffic-2-" + index_item;
        id3 = "#traffic-3-" + index_item;
        id4 = "#traffic-4-" + index_item;
        if ($(id1).val().length === 0) {
            $(id1).addClass('danger_input');
            flag = true;
        }
        else $(id1).removeClass('danger_input');
        if ($(id2).val().length === 0) {
            $(id2).addClass('danger_input');
            flag = true;
        }
        else $(id2).removeClass('danger_input');
        if ($(id3).val().length === 0) {
            $(id3).addClass('danger_input');
            flag = true;
        }
        else $(id3).removeClass('danger_input');
        if ($(id4).val().length === 0) {
            $(id4).addClass('danger_input');
            flag = true;
        }
        else $(id4).removeClass('danger_input');
        index_item += 1;
        if (flag === true) return;
        $('#countpallet').show();
        countP += parseInt($(id4).val());
        $('#traffic4').val(countP);
    }
    id1 = "traffic-1-" + index_item;
    id2 = "traffic-2-" + index_item;
    id3 = "traffic-3-" + index_item;
    id4 = "traffic-4-" + index_item;
    var html_code = '<div class="col-3 h36 pad15TB">\n' +
        '                                <div class="center"><input id="'+ id1 +'" type="text" name="'+ id1 +'" placeholder="Продукт"></div>\n' +
        '                            </div>\n' +
        '                            <div class="col-3">\n' +
        '                                <div class="center"><input id="'+ id2 + '" type="number" name="'+ id2 +'" placeholder="Оптим. температура"></div>\n' +
        '                            </div>\n' +
        '                            <div class="col-3">\n' +
        '                                <div class="center"><input id="'+ id3 +'" type="date" name="'+ id3 +'" placeholder="Срок годности до"></div>\n' +
        '                            </div>\n' +
        '                            <div class="col-3">\n' +
        '                                <div class="center"><input id="'+ id4 +'" type="number" name="'+ id4 + '" placeholder="Количество паллет"></div>\n' +
        '                            </div>';
    $("#item_selector").append(html_code);

    index_item += 1;
}
$('.zag, .z').hide();
if (window.location.pathname === "/traffic/"){
    $('.tableSql').hide();
    $('#tableSql').show();

}
function select_active2(index) {
    $('#' + buttAdd2).removeClass('activeFilter');
    $('#' + nowActiv2).removeClass('activeFilter');

    nowActiv2 = index;
    $('#' + index).addClass('activeFilter');
    $('.otp, .prb, .prn, .otm, .zag').hide();
    if (index == "tr_add"){
        $('#tableSql2').show();
    }
    else $('#tableSql').hide();

    if (index != "tr_add"){
        document.getElementById('tableSql').style.display = 'block';
        document.getElementById('trafficAdd').style.display = 'none';
    }
    $(".nezag").show();
    if (index == "otp"){
        $('.otp').show();
    }
    else if (index == "zag"){
        $('.zag').show();
        $('#tableSql').show();

        $('.nezag').hide();
    }
    else if (index == "prb"){
        $('.prb').show();
    }
    else if (index == "prn"){
        $('.prn').show();
    }
    else if (index == "otm"){
        $('.otm').show();
    }
}

function trafficAdd() {
    document.getElementById('tableSql').style.display = 'none';
    document.getElementById('trafficAdd').style.display = 'block';
    buttAdd2 = nowActiv2;
    nowActiv2 = "tr_add";
    select_active2(nowActiv2);
}


function closeAddTraffic(){
    document.getElementById('tableSql').style.display = 'block';
    document.getElementById('trafficAdd').style.display = 'none';
    select_active2(buttAdd2);
}

function selTraffic(index) {
     $('#tov' + index + ", #tov_" + index + ", #tov-" + index).show();
}

function closeTraffic(index) {
    window.event.stopPropagation();
    $("#tov" + index + ", #tov_" + index + ", #tov-" + index).hide();
}

function editTraffic(index) {
    window.location = "/traffic/edit/" + index + "/";
}

function editTraffic2(index) {
    window.location = "/traffic/editU/" + index + "/";
}
$("#unload_start").hide();
function startUnload(index) {
    $.ajax({
        type: "GET",
        url: "/traffic/startUnload/" + index + "/",
        data: {},
        cache: false,
        success: function (data) {
            $('#pribilBtn').hide();
            $('#unload_start, #uploader1, #razgruzkaBtn, #stopBtn').show();
            $('#unload_dateUpl').val(data);
        }
    });
}

function pribilTraffic(index) {
    $.ajax({
        type: "GET",
        url: "/traffic/setPribil/" + index + "/",
        data: {},
        cache: false,
        success: function (data) {
            $('#pribilBtn').hide();
            $('#pribil1, #pribil2, #razgruzkaBtn').show();
            $('#traffic_dateUpload').val(data);
        }
    });
}
function razgruzkaTraffic(index) {
    car = $('#traffic_car').val();
    $.ajax({
        type: "GET",
        url: "/traffic/setRazgruzka/" + index + "/" + car + "/",
        data: {},
        cache: false,
        success: function (data) {
            $('#razgruzkaBtn').hide();
            $('.btnTable').show();
        }
    });
}

function stopTraffic3(index) {
    car = $('#traffic_car').val();
    $.ajax({
        type: "GET",
        url: "/traffic/stopTraffic3/" + index + "/",
        data: {},
        cache: false,
        success: function (data) {
            window.location = "/traffic/"
        }
    });
}

function stopTraffic2(index, status) {
    car = $('#traffic_car').val();
    $.ajax({
        type: "GET",
        url: "/traffic/stopTraffic2/" + index + "/" + status + "/",
        data: {},
        cache: false,
        success: function (data) {
            window.location = "/traffic/"
        }
    });
}

function stopTraffic(index, status) {
    car = $('#traffic_car').val();
    $.ajax({
        type: "GET",
        url: "/traffic/stopTraffic/" + index + "/" + status + "/",
        data: {},
        cache: false,
        success: function (data) {
            window.location = "/traffic/"
        }
    });
}

$('.d2').hide();
$('#car_type_Boolean').change(function() {
    if ($('#car_type_Boolean').val() === "Разгрузка/Загрузка"){
        $("#palletTruck").hide();
    }
    else {
        $("#palletTruck").show();
    }
});

function car_activ(index) {
    v1 = '#car_sty';
    v2 = '#car_use';
    v3 = ".d1";
    v4 = ".d2";
    $(v1 + ',' + v2).removeClass('active_btnTable2');
    $('#' + index).addClass('active_btnTable2');
    if (index === "car_use")
    {
        $(v3).hide();
        $(v4).show();
    }
    else {
        $(v4).hide();
        $(v3).show();
    }

}

function addCar() {
    data = {"name": $('#car_name').val(), "normal_Den": $('#car_normal_Den').val(),
        "normal": $('#car_normal').val(), "type": $("#car_type").val(),
        "truck": $('#car_type_Boolean').val(), "count": $('#car_pallet').val()};
    $.ajax({
        type: "GET",
        url: "/car/add/",
        data: data,
        cache: false,
        success: function (data) {
            window.location = '/car/'
        }
    });
}

function stelag_activ(index) {
    $('#st_show, #st_add').removeClass('active_btnTable2');
    $('#' + index).addClass('active_btnTable2');
    if (index == "st_add"){
        document.getElementById('tableSql').style.display = 'none';
        document.getElementById('stelagAdd').style.display = 'block';
    }
    else{
        document.getElementById('tableSql').style.display = 'block';
        document.getElementById('stelagAdd').style.display = 'none';
    }
}
function closeAddStelag(){
    document.getElementById('tableSql').style.display = 'block';
    document.getElementById('stelagAdd').style.display = 'none';
    stelag_activ("st_show");
}
document.getElementById('stelag_height').onkeydown = function (e) {
    return !(/^[А-Яа-яA-Za-z ]$/.test(e.key));
};
document.getElementById('stelag_dlina').onkeydown = function (e) {
    return !(/^[А-Яа-яA-Za-z ]$/.test(e.key));
};
document.getElementById('stelag_shirina').onkeydown = function (e) {
    return !(/^[А-Яа-яA-Za-z ]$/.test(e.key));
};
document.getElementById('stelag_count').onkeydown = function (e) {
    return !(/^[А-Яа-яA-Za-z ]$/.test(e.key));
};
document.getElementById('stelag_kg').onkeydown = function (e) {
    return !(/^[А-Яа-яA-Za-z ]$/.test(e.key));
};

$('#formAddStelag').submit(function (e) {
    e.preventDefault();
    var data = $(this).serialize();
    $.ajax({
        type: "GET",
        url: "/shelving/add/",
        data: data,
        cache: false,
        success: function (data) {
            window.location = '/shelving/'
        }
    });
});