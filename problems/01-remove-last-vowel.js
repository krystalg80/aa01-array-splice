/*
Write a function removeLastVowel(word) that takes in a string and returns the
string with its last vowel removed.
Vowels are the letters "a", "e", "i", "o", "u".
*/

// Your code here 
function removeLastVowel(word) {
    let vowels = 'aeiou';
    let wordArr = word.split(''); // make it into a array!

    for (let i = wordArr.length - 1; i >= 0; i--) { // Start from the end of the array
        if (vowels.includes(wordArr[i].toLowerCase())) { // Check if the character is a vowel
            wordArr.splice(i, 1); // use . splice to remove the vowel!
            break; // Exit the loop after removing the first vowel found 
        }
    }

    return wordArr.join(''); // Convert the array back into a string and return it
}

console.log(removeLastVowel('bootcamp')); // 'bootcmp'
console.log(removeLastVowel('better')); // 'bettr'
console.log(removeLastVowel('graph')); // 'grph'
console.log(removeLastVowel('thy')); // 'thy'

/******************** DO NOT MODIFY ANY CODE BELOW THIS LINE *****************/
module.exports = removeLastVowel;
