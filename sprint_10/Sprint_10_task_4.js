function factorial(n) {
    let res = 1
    for (let i = 1; i <= n; i++){
        res = res * i
    }
    console.log(res)
    return res
}

function processArray(arr, factorial) {
    let nArr = []
    for (let i of arr){
        nArr.push(factorial(i))
    }
    return nArr
}

console.log(processArray([1, 2, 3, 4, 5, 6], factorial));