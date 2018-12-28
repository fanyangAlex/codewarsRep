function sqInRect(lng, wdth) {
  //your code here
  if (lng === wdth) {
    return null;
  } else {
    let big = Math.max(lng, wdth);
    let small = Math.min(lng, wdth);
    let result = [];
    while (big > 0 && small > 0) {
      result.push(small);
      let temp = big - small;
      big = Math.max(temp, small);
      small = Math.min(temp, small);
    }
    return result
  }
}

