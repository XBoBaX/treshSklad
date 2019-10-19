var ctx = document.getElementById('chart1').getContext('2d');
var trN1 = 0, trN2, trN3, trN4;
var trW1 = 0, trW2, trW3, trW4;
var unN1 = 0, unN2, unN3, unN4;
var unload_now;
getValue();

$('#sel_mnt').change(function() {
    getValue();
});
$('#sel_skl_stats').change(function() {
    getValue();
});

function getValue() {
    $.ajax({
        type: "GET",
        url: "/stats/get/",
        data: {"date": $("#sel_mnt").val(), "sk": $("#sel_skl_stats").val()},
        cache: false,
        success: function (data) {
            trN1 = data["trN1"];
            trN2 = data["trN2"];
            trN3 = data["trN3"];
            trN4 = data["trN4"];
            trW1 = data["trW1"];
            trW2 = data["trW2"];
            trW3 = data["trW3"];
            trW4 = data["trW4"];
            unN2 = data["unN1"];
            unN2 = data["unN2"];
            unN3 = data["unN3"];
            unN4 = data["unN4"];
            setChart();
        }
});
}

function setChart()
{
    var chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['1 неделя', '2 неделя ', '3 неделя', '4 неделя'],
        datasets: [
            {
            label: 'Принято',
            backgroundColor: '#f47c28',
            borderColor: 'rgb(255, 99, 132)',
            data: [trN1, trN2, trN3, trN4]
        },
        {
            label: 'Скоро прибудет',
            backgroundColor: '#adb0bb',
            borderColor: 'red',
            data: [trW1, trW2, trW3, trW4]
        },

        {
            label: 'Разгруженно',
            backgroundColor: 'white',
            borderColor: 'green',
            data: [unN1, unN2, unN3, unN4]
        },
        ]
    },

    options: {}
    });
}

document.getElementById('pdf_btn').addEventListener("click", downloadPDF);

function downloadPDF() {
    var canvas1 = document.querySelector('#chart1');
	var canvasImg = canvas1.toDataURL("image/jpeg", 1.0);
	var doc = new jsPDF('landscape');
	doc.setFontSize(20);
	doc.text(15, 15, "Cool Chart");
	doc.addImage(canvasImg, 'JPEG', 10, 10, 280, 150 );
	doc.save('stat.pdf');
}
