// const howMuchSec = (sec=0, min=0,hou=0,day=0,week=0,mon=0,year=0) => {
//     let res = null
//
// }

const howMuchSec = (...args) => {
    let res = null
    let i  = 0
    if(args.length !== 0) {
        while (i<args.length){
            if(args.length-i === 7){res += args[args.length-i-1] * 31104000}
            if(args.length-i === 6){res += args[args.length-i-1] * 2592000}
            if(args.length-i === 5){res += args[args.length-i-1] * 604800}
            if(args.length-i === 4){res += args[args.length-i-1] * 86400}
            if(args.length-i === 3){res += args[args.length-i-1] * 3600}
            if(args.length-i === 2){res += args[args.length-i-1] * 60}
            if(args.length-i === 1){res += args[args.length-i-1] }
            i++
        }
    }else {
        res = 0
    }
    return res
}
console.log(howMuchSec())