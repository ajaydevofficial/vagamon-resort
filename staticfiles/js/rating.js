var count;
function starmark(item)
{
    count=item.id[0];
    sessionStorage.starRating = count;
    var subid= item.id.substring(1);
    for(var i=0;i<5;i++)
    {
        if(i<count)
        {
            document.getElementById((i+1)+subid).style.color="orange";
        }
        else
        {
            document.getElementById((i+1)+subid).style.color="black";
        }
    }
}
function result()
{
    var URL = "{% url 'Home_Page' %}";
    name =document.getElementById("name").value;
    email = document.getElementById("email").value;
    phone = document.getElementById("phone").value;
    something = document.getElementById("something").value;
    rating = document.getElementById("rating-input");
    if(name && email && phone && something){

        rating.value = count;
        //var data = {"name": name,"email":email,"phone":phone,"something":something,"rating": count};
        //$.post(URL, data, function(response){
        //if(response === 'success'){ alert('Yay!'); }
        //else{ alert('Error! :('); }
        //});
    }
    else{
      alert("All fields in the form must be filled");
    }
}
