function compare()
{
    var startDt = document.getElementById("startDate").value;
    var endDt = document.getElementById("endDate").value;

    if( (new Date(startDt).getTime() > new Date(endDt).getTime()))
    {
        alert("Select a date before End-date");
        window.location.replace("/book")
    }
}
