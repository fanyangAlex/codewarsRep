function findEvenIndex(arr) {
  if (arr.length === 1) return 0
  let sum = 0
  for (let i = 0; i < arr.length; i++) {
    const element = arr[i]
    sum += element
  }
  let left = 0
  let right = sum
  for (let i = 0; i < arr.length; i++) {
    if (i > 0) {
      left += arr[i - 1]
    }
    right -= arr[i]
    if (left === right) {
      return i
    }
  }

  return -1
  //Code goes here!
}
console.log(findEvenIndex([1, 2, 3, 4, 3, 2, 1]))
