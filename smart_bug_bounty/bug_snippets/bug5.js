// Intended: Fetch user data (simulate async)

function fetchUser() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ name: "John" });
        }, 1000);
    });
}

async function getUserName() {
    const user = fetchUser(); // BUG: missing await
    return user.name;
}

getUserName().then(console.log); // Expected: "John"