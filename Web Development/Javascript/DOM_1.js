// It represents the browser's window. All global JavaScript objects, functions, and variables automatically become members of the window object. Global variables are properties of the window object. Global functions are methods of the window object.

//Used for Dynamic changes in webpage


console.log(window.document);
console.log(window);

console.log(document.body.childNodes[0]);

document.body.style.background = "lime";
//Changes background color

document.body.childNodes[1].innerText = "back-with-it";
//changes inner text properties of the div

//Selecting their ID, class or tag

let heading = document.getElementById("header1"); //h1

console.log(heading);

//similar with document.getElementsByClassName() and documentgetElementsByTagName()

//Query Selector selects the first element of the name be it id/class/tag
//Use # and . for id and class

let para = document.querySelector("p"); //returns 1st element
let parag = document.querySelectorAll("p"); //returns all elements with the tag

//DOM Manipulation

let tago = heading.tagName; //returns name of the tag
console.log(tago);

//parent,child,sibling . firstChild / lastChild property

console.log(heading.innerText); //text inside tag
console.log(heading.innerHTML); //html of tag

//these properties can be altered similarily as well

console.log(`heading = ${heading}`);
console.log(heading);

//This is manual implementation
let divs = document.querySelectorAll(".box");
// divs[0].innerText += " = 1";
// divs[1].innerText += " = 2";
// divs[2].innerText += " = 3";

let ind = 1;

//loop implementation

for(div of divs){
    div.innerText += ` = ${ind}`;
    ind++;
}
