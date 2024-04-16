//Events

//node.event = () => {
//handle here 
// }

let divs = document.querySelectorAll(".box");

let divo = divs[0];

var m = ['a','b','c','d'];

let i = 0;

divo.onclick = () => { //Give argument in this to define the event variable. Like evt, functions: evt.type, evt.target, evt.clientX,evt.clientY

    let newtext = divo.innerText;
    newtext = newtext.substring(0,3) + i;
    console.log(newtext);
    i++;
    divo.innerText = newtext;    
}

divo.addEventListener("dblclick", (e) => { //We can handle multiple events through this unlike something else.
    console.log(e.type);
    console.log(e.clientX,e.clientY);
    console.log("1");
})

divo.addEventListener("dblclick", (e) => { //We can handle multiple events through this unlike something else.
    console.log(e.type);
    console.log("2");
    console.log(e.clientX,e.clientY);
})

//Similarily we have removeEventListener  but reference should be same.
