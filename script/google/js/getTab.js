var s3 = document.getElementsByTagName("table")[0];

for (var i = 0; i < s3.rows.length; i++) {
    for (var j = 0; j < s3.rows[i].cells.length; j++) {
        alert(s3.rows[i].cells[j].innerHTML);
    }
}