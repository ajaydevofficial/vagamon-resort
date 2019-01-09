tag="";
a = document.getElementsByClassName("star");
//var tag[a.length]
//for(i=0;i<a.length;i++){
 //tag[i]="";
//}
for(j=0;j<3;j++){
  tag+="<span id='1one' class='fa fa-star checked'></span>";
}
for(i=0;i<a.length;i++){
 a[i].innerHTML = tag;
}
