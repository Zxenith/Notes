let marks = [10, 50, 80, 15, 93, 65, 91, 92];

let topo = marks.filter((mark => {
    return mark > 90;
}));

console.log(topo);

console.log(marks);

let sum = 0;

marks.forEach((val) => {
    sum += val;
})

console.log(sum);

let done = ((mark) => {
    let sumo = 0;
    for(i = 0; i < mark.length; i++){
        sumo += mark[i];
    }
    console.log(sum);
    return sum;
})

console.log(done(marks));

let val = prompt();

let arr = [];

for(let i = 0; i < val; i++){
    arr[i] = i + 1;
}

console.log(arr);

let res = arr.reduce((prev, curr) => {
    return prev + curr;
});

console.log(res);

let fact = arr.reduce((prev, curr) => {
    return prev * curr;
});

console.log(fact);
