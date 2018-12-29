function sumDigPow(a, b) {
    let result=[]
    for (let index = a; index <= b; index++) {
        if(isSum(index)){
            result.push(index)
        }
    }
    return result
}

function isSum(num) {
  let m = 2;
  return (
    num
      .toString()
      .split("")
      .map(v=>parseInt(v))
      .reduce((a, b) => {
        let result = a + Math.pow(b, m);
        m++;
        return result;
      }) === num
  );
}

isSum(135)