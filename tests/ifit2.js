function createPackage(small, big, goal) {
    // Calculate number of bigs
    var b = Math.floor(goal / 5);

    // Check if there is enough
    if (b > big) {
        // It is not - use all there is
        b = big;
    }

    // Calculate number of smalls
    var s = goal - 5 * b;

    // Check if there is enough
    if (s > small) {
        // It is not - cannot do it
       s = -1
    }

    return s;
}

console.log(createPackage(4, 1, 9)); // Output: 4
console.log(createPackage(4, 1, 10)); // Output: -1
console.log(createPackage(7, 3, 22)); // Output: 7