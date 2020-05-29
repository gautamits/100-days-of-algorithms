function hanoi(height, left='left', right='right', middle='middle'){ // height, from, to, using
    if(height){
        hanoi(height - 1, left, middle, right)
        console.log(left,'=>', right)
        hanoi(height-1, middle, right, left)
    }
}

hanoi(3)