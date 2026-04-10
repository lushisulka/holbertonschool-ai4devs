function wordCount(text) {
    const words = text.split(" ");
    const counts = {};

    for (let i = 0; i < words.length; i++) {
        const word = words[i];

        if (counts[word]) {
            counts[word]++;
        } else {
            counts[word] = 1;
        }
    }

    return counts;
}

console.log(wordCount("hello world hello"));