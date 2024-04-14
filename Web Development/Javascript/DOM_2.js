//Getting the attributes of the HTML of a particular element.

let ho = document.querySelector("h1");
console.log(ho);

let classo = ho.getAttribute("id");
console.log(classo);

//Sets the attribute element with this syntax.
ho.setAttribute("class","mainheader");

let o = ho.getAttribute("class");
console.log(o);

//Giving inline style.
let divo = document.querySelector(".box");
console.log(divo.style);

//Changing CSS of the elements
divo.style.backgroundColor = "green";
divo.style.fontSize += 5;

//Similarily we can change other properties of the styles of elements as well.

let newbtn = document.createElement("button");
newbtn.innerText = "Click Whatever";

divo.before(newbtn);

// node.append(el); (inside)
// node.prepend(el); (inside)
// node.before(el); (outside)
// node.after(el); (outside)

//node.remove() removing the node

let sec = document.createElement("button");
sec.innerText = "Click me";

sec.style.backgroundColor = "red";
sec.style.color = "white";

let bod = document.querySelector("body");
bod.prepend(sec);

//See classlist for various class manipulation.

