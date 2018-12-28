
function display()
{
    var oneDay = 24*60*60*1000; // hours*minutes*seconds*milliseconds
    var fd = document.getElementById("search-input-in").value;
    var sd = document.getElementById("search-input-out").value;
    var firstDate = new Date(fd)
    var secondDate = new Date(sd)
    var diffDays = Math.round(Math.abs((firstDate.getTime() - secondDate.getTime())/(oneDay)));
    var ind = document.getElementById("search-input-min").value;
    var base =  document.getElementById("search-input").value;
    var button = document.getElementById("search-button");

    if(base == "cottage-only")
    {
      base = 2000;
    }
    if(base == "other")
    {
      base = 1500;
    }
    if(diffDays == 0)
    {
      diffDays=1;
    }

    num = base*ind*diffDays;
    str1 = "Pay Rs.";
    str2 = num.toString();
    res = str1.concat(str2);
    if(isNaN(num))
    {
      button.value = "Pay Rs.0";
    }
    else
    {
      button.value = res;
      return num;
    }


}
