function sortArray(array) {
  // Return a sorted array.
  if (array.length === 0) return []
  let oddArr = array.filter((v) => v % 2 === 1).sort((a, b) => a - b)
  let oIndex = 0
  for (let i = 0; i < array.length; i++) {
    let element = array[i]
    if (element % 2 === 1) {
      array[i] = oddArr[oIndex]
      oIndex++
    }
  }

  return array
}

sortArray([1, 11, 2, 8, 3, 4, 5])
