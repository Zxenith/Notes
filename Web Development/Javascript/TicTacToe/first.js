//Events

//node.event = () => {
//handle here 
// }

let divs = document.querySelectorAll(".box");
let res = document.querySelector("#reset");
let bod = document.querySelector("body");

const check = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [3, 4, 5],
    [6, 7, 8]
];

let chalo = true;
let yet = true;

const checkwinner = () => {
    for (pattern of check) {
        let pos0 = divs[pattern[0]].innerText;
        let pos1 = divs[pattern[1]].innerText;
        let pos2 = divs[pattern[2]].innerText;

        if (pos0 !== "" && pos0 === pos1 && pos1 === pos2) {
            let newbtn = document.createElement("h3");
            newbtn.innerText = `Winner: ${pos0}`;
            bod.prepend(newbtn);
            return true; // Return true if there's a winner
        }
    }
    return false; // Return false if no winner found
};

divs.forEach((box) => {
    box.addEventListener("click",() => {
        
        if(chalo){
            box.innerText = "X";
            chalo = false;
        }
        else{
            box.innerText = "O";
            chalo = true;
        }
        // box.disabled = true;
        let here = checkwinner();
        if(here === true){
            yet = false;
        }
        
        if(yet === false){
            divs.forEach((div) => { 
                div.style.pointerEvents = 'none'; // Disable pointer events 
                div.style.opacity = '0.5'; // Reduce opacity to visually disable the content 
                div.setAttribute('disabled', true); // Set disabled attribute 
              });
        }

    }, {once: true});
});

// {once: true}
