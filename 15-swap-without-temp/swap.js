function swap(x, y) 
{ 
    x = x + y;
    y = x - y;
    x = x - y;
    return [x, y]
} 

console.log(swap(2,3))