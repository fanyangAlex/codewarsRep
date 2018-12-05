const binaryArrayToNumber = (arr) => {
  const l = arr.length
  let result = 0
  let time = 1
  for (let i = l - 1; i >= 0; i++) {
    result += time * (arr[i] === '1' ? 1 : 0)
    time *= 2
  }
  return result
  // your code
}
