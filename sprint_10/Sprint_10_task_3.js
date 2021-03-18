function longestLogin(loginList) {
    let maxL = 0
    let maxV = null
    for (let i of loginList){
        if (i.length >= maxL)
            maxV = i
            maxL = i.length
    }
    return maxV
}

console.log(longestLogin(["user1", "user2", "333", "user4", "aa"]))