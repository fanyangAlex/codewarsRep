function duplicateEncode(word) {
  let dic = {}
  let newWord = word.toLowerCase().split('')
  for (let i = 0; i < newWord.length; i++) {
    let element = newWord[i]
    if (dic[element] !== undefined) {
      newWord[i] = ')'
      newWord[dic[element]] = ')'
    } else {
      dic[element] = i
      newWord[i] = '('
    }
  }

  return newWord.join('')
  // ...
}

console.log(duplicateEncode('dIn'))
