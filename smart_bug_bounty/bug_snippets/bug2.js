// Intended: Count occurrences of each word in a string

function wordCount(text) {
    const words = text.split(" ");
    const counts = {};

    for (let i = 0; i <= words.length; i++) { // BUG: should be < not <=
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