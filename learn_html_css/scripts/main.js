var myHeading = document.querySelector("h1");
var myButton = document.querySelector("button");

function setUsername(){
    var myname = prompt("please enter your name.");
    localStorage.setItem('name', myname);
    myHeading.textContent = 'Javascript is so cool!' + myname;
}

if(!localStorage.getItem('name')){
    setUsername();
}else{
    var name = localStorage.getItem('name');
    myHeading.textContent = 'Javascript is so cool!' + name;
    
}