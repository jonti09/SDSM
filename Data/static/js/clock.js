function clock() {
    var today = new Date();

    var h = today.getHours();
    var m = today.getMinutes();

    var meridian = "AM";
    if(h >= 12) {
        if (h >= 12)
            meridian = "PM"
        if(h > 12)
            h -= 12;
    }

    m = checkTime(m);
    document.getElementById('time').innerHTML = h + ":" + m + " " + meridian;
    var t = setTimeout(clock, 500);
}

function checkTime(i) {
    if (i < 10) {i = "0" + i}  // add zero in front of numbers < 10
    return i;
}
