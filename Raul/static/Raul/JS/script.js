
 var mybutton = document.getElementById("scrollTop");

 window.onscroll = function() {scrollFunction(),navbarFunction()};

 function scrollFunction() {
     if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
         mybutton.style.display = "block";
     } else {
         mybutton.style.display = "none";
     }
 }

 function topFunction() {
     document.body.scrollTop = 0;
     document.documentElement.scrollTop = 0;
 }

 
 function navbarFunction() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        document.getElementById("hideOnScroll").style.color = "white";
        document.getElementById("hideOnScroll").style.opacity = "1";
        document.getElementById("headerOnScroll").style.height = "7.5em";
        document.getElementById("headerOnScroll").style.background = "#6d6d6d";
        document.getElementById("headerOnScroll").style.boxShadow = "0px 0px 5px 1px rgba(0,0,0,0.5)";
        
    } else {
        document.getElementById("hideOnScroll").style.background = "transparent";
        document.getElementById("hideOnScroll").style.opacity = "0";
        document.getElementById("hideOnScroll").style.color = "transparent";

        document.getElementById("headerOnScroll").style.background = "transparent";
        document.getElementById("headerOnScroll").style.height = "7.5em";
        document.getElementById("headerOnScroll").style.boxShadow = "0px 0px 0px 0px";
    }
}

function openCity(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();

// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

var modal2 = document.getElementById('id02');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal2) {
        modal2.style.display = "none";
    }
}



function openNav() {
     document.getElementById("contentHam").style.height = "100%";
}

function closeNav() {
    document.getElementById("contentHam").style.height = "0%";
}

function openStore(){
    document.getElementById("store").style.height = "100%";
}

function closeStore(){
    document.getElementById("store").style.height = "0%";
}

