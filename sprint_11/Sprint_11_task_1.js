const filterNums = (lst, num=0, par='greater') => {
    let res = []
    for(let n of lst){
        if(par === 'less'){
            if(num > n){
                res.push(n)
            }
        }else {
            if(num<n){
                res.push(n)

            }
        }
    }
    return res
};

console.log(filterNums([-3, 3, 4, 0, 44, -11, 5], 11, 'less'));
console.log(filterNums([-3, 3, 4, 0, 44, -11, 5], 9));
console.log(filterNums([-3, 3, 4, 0, 44, -11, 5]));