function consecutive(arr){
    var numbers = new Set(arr);
    for(let i=0; i<arr.length; i++){
        numbers.add(arr[i]);
    }
    let maxConsec = 0
    for(let i=0; i<arr.length; i++){
        if (numbers.has(arr[i])){
            let j = arr[i];
            while(numbers.has(j)){
                j += 1
            }
            if (j - arr[i] == 3){
                return true
            }
        }
    }
    return false
}

console.log(consecutive([76,12,56,77,23,75,78])); // Output: True (75,76,77,78)
console.log(consecutive([45,12,67,90,13])); // Output: False (12,13,???)
console.log(consecutive([14,12,67,90,13])); // Output: True (12,13,14)