function countOfOneBits(value){
    let n=0;
    while(value){
        value = value & value-1
        n+=1
    }
    return n
}

console.log(11, countOfOneBits(11))
console.log(16, countOfOneBits(16));