function eratosthenes(n){
    const primes = Array(n).fill(true)
    let p = 2;
    while(p*p <= n){
        if(primes[p]){
            for(let i=p*p; i<n+1; i+=p){
                primes[i]=false
            }
        }
        p+=1
    }
    return primes.reduce((agg, curr, idx)=>{
        if(idx<2) return agg 
        if(curr) agg.push(idx)
        return agg
    },[])
}

console.log(eratosthenes(200))