function modifyArray(array) {
    let l = array.length
    array[0] = 'Start'
    array[l-1] = 'End'
    return array
}

modifyArray([12, 6, 22, 0, -8])