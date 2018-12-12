function chooseBestSum(t, k, ls) {
  if (ls.length < k) return null
  if (k === 1) {
    let vaidArray = ls.filter((v) => v <= t)
    return vaidArray.length ? vaidArray.sort((a, b) => b - a)[0] : null
  }
  let sum = 0
  for (let index = 0; index < ls.length; index++) {
    const element = ls[index]
    let tempSum = chooseBestSum(t - element, k - 1, ls.slice(index + 1))
    if (tempSum !== null) {
      sum = Math.max(sum, element + tempSum)
    }
  }

  return sum === 0 ? null : sum
}
