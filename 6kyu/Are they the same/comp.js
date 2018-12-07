function comp(array1, array2) {
  if (array1 && array2) {
    if (array1.length === 0 && array2.length === 0) {
      return true
    } else if (array1.length === 0 || array2.length === 0) {
      return false
    } else {
      array1 = array1.sort((a, b) => a - b)
      array2 = array2.sort((a, b) => a - b)
      for (let i = 0; i < array1.length; i++) {
        if (array2[i] !== array1[i] * array1[i]) {
          return false
        }
      }

      return true
    }
  }
  return false
}
