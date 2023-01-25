function isomorphic_strings(s, t) {
    if (s.length != t.length) {
        return false;
    }

    var s_hash = {};
    var t_hash = {};

    for (let i=0; i<s.length; i++) {
        char_s = s[i]
        char_t = t[i]
        if(!(char_s in s_hash)) {
            s_hash[char_s] = char_t
        }
        if(!(char_t in t_hash)) {
            t_hash[char_t] = char_s
        }
        if (s_hash[char_s] != char_t || t_hash[char_t] != char_s) {
            return false
        }

    }
    return true
}

console.log(isomorphic_strings('aacad','bbdbe'))