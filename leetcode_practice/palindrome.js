var isPalindrome = function (x) {
    stringX = x.toString()
    var reverseString = stringX.split("").reverse().join("");
    if (reverseString == x) {
        return true;
    } else{
        return false;
    }
}

console.log(isPalindrome(121));