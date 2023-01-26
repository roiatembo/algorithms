var romanToInt = function(s) {
    var romanInt = {'I': 1, 'V': 5, 'X': 10, 'L' : 50, 'C': 100, 'D': 500, 'M': 1000};
    var intTotal = 0;
    var prevChar = 2000;
    for (let i=0; i<s.length; i++) {
        if (romanInt[s[i]] > prevChar) {
            intTotal = (intTotal - prevChar) + (romanInt[s[i]] - prevChar);
        } else {
            intTotal += romanInt[s[i]];
        }
        prevChar = romanInt[s[i]];
    }
    return intTotal;
};

console.log(romanToInt("MCMXCIV"))