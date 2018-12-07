function isPangram(string) {
  let str = string.trim().toLowerCase()
  if (str.length < 26) return false
  let apha = 'abcdefghijklmnopqrstuvwxyz'
  let arr = '00000000000000000000000000'.split('')
  for (let i = 0; i < str.length; i++) {
    const element = str[i]
    let index = apha.indexOf(element)
    if (index >= 0) {
      arr[index] = '1'
    }
  }

  return arr.indexOf('0') === -1
  //...
}
