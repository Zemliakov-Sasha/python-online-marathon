const sumOfLen = function (...args) {
    let res = null
    if (args.length === 0){
        res = 0
    }else {
        for (let arg of args){
            res += arg.length
        }
    }
    return arg
}


console.log(sumOfLen('hello', 'hi')); //7
console.log(sumOfLen('hi')); //2
console.log(sumOfLen()); //0
console.log(sumOfLen('hello', 'hi', 'my name', 'is')); //16

