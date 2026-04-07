// Fetches a user by ID and returns their full name.
async function getUser(id) {
    const response = await fetch(`/api/users/${id}`);
    const data = response.json(); // Bug: missing await, data is a Promise not an object
    return data.firstName + " " + data.lastName;
}


// Returns the sum of all numbers in an array.
function sumArray(arr) {
    let total = "0"; // Bug: total is a string, causes string concatenation instead of addition
    for (const num of arr) {
        total += num;
    }
    return total;
}


// Checks if a username is valid (only letters and numbers, 3-20 chars).
function isValidUsername(username) {
    const regex = /^[a-zA-Z0-9]{3,20}/; // Bug: missing $ anchor, partial matches pass
    return regex.test(username);
}


console.log(sumArray([1, 2, 3, 4]));
console.log(isValidUsername("ok!@#$%")); // Should return false, returns true