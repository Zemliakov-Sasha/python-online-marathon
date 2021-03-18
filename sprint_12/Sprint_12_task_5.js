function mapCreator(keys, values){
    let map = new Map();
    for (let i = 0; i < keys.length; i++){
        if (typeof values[i] == 'string'){
            map.set(keys[i], values[i])
        }
    }
    return map
}