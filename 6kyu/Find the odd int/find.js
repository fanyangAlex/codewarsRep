function findOdd(A) {
  //happy coding!
  let obj = {};

  A.map(v => {
    if (obj[v]) {
      obj[v]++;
    } else {
      obj[v] = 1;
    }
  });
  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      const element = obj[key];
      if (element % 2 === 1) {
        return parseInt(key);
      }
    }
  }

  return 0;
}
