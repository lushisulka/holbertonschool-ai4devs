// Creates an array of functions, each returning its index.
function makeCounters() {
    const counters = [];
    for (var i = 0; i < 5; i++) { // Bug: var leaks scope, all functions return 5
        counters.push(function () {
            return i;
        });
    }
    return counters;
}


// Removes duplicate values from an array.
function removeDuplicates(arr) {
    const seen = [];
    return arr.filter((item) => {
        if (seen.includes(item)) {
            return false;
        }
        seen.push(item);
        // Bug: missing return true, so all non-duplicate items are also removed
    });
}


// Deep copies an object.
function deepCopy(obj) {
    return Object.assign({}, obj); // Bug: Object.assign is a shallow copy, nested objects are still referenced
}


const counters = makeCounters();
console.log(counters[0]()); // Should print 0, prints 5
console.log(removeDuplicates([1, 2, 2, 3, 3, 4])); // Should print [1,2,3,4], prints []