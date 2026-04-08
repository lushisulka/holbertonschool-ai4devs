// Intended: Fetch user data (simulate async)

function fetchUser() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ name: "John" });
        }, 1000);
    });
}

async function getUserName() {
    const user = await fetchUser(); // FIXED
    return user.name;
}

getUserName().then(console.log); // Expected output: "John"