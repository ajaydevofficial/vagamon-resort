function showHide(){
  var button = document.getElementById("submit-button-new");
  var refer = document.getElementById("refer");
  var showhide = document.getElementById("hidden");
  if(button.value = "Show More" &&  refer.value== 0){
    if(showhide.style.display =='none'){
      showhide.style.display ='block';
    }
    button.value = "Show Less";
    refer.value = 1;
  }
  else if(button.value = "Show Less" &&  refer.value== 1){
    if(showhide.style.display =='block'){
      showhide.style.display ='none';
    }
    button.value = "Show More";
    refer.value = 0;
  }
}
