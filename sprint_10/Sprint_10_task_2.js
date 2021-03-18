function combArray(arr1, arr2) {
    let nArr = []
    for (let i of arr1){
        if (i === Number(i)){ nArr.push(i)}
    }
    for (let i of arr2){
        if (i === Number(i)){ nArr.push(i)}
    }
    return nArr
}

console.log(combArray ([12, "User01", 22, true, -8], ["Index", 6, null, 15]))