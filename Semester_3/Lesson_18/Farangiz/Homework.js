function accum(s) {
    let result = [];
    for (let i = 0; i < s.length; i++) {
        let output = "";
        if (s[i].match(/[0-9]/g) !== null) {
            return "This string contains number";
        }

        for (let j = 0; j < i + 1; j++) {
            output += j === 0 ? s[i].toUpperCase() : s[i].toLowerCase();
        }
        result.push(output);
    }
    return result.join("-");
}
console.log(accum("gnn"));