function waitForMs(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}


async function typeSentence(sentence, eleRef, delay=100) {
  const letters = sentence.split("");
  let i = 0;
  while(i < letters.length) {
    await waitForMs(delay);
    $(eleRef).append(letters[i]);
    i++
  }
  return;
}
