const maxInterv = (...args) => {
    let i = 0
    let res = []
    if (args.length === 1){return 0}
    while (i < args.length-1){
        if (args[i+1] - args[i]<0) {
            res.push((args[i+1] - args[i])*-1)
        }else
            res.push(args[i+1] - args[i])
        i++
    }
    return Math.max(...res)
}
console.log(maxInterv (3, 5, 2, 7, 11, 0, -2))