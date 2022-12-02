const fs = require('fs');


const decrementChar = (char, delta) => {
    return parseInt(String.fromCharCode(char.charCodeAt(0) - delta))
};

const parseGame = (data) => {
    const hasWon = (elf, self) => {
        const win_table = [1, 2, 3]
        while (self != win_table[1]) {
            win_table.unshift(win_table.pop())
        }
        return win_table[0] == elf ? 6 : win_table[1] == elf ? 3 : 0
    }
    console.log(
        data.split("\n").filter((row) => row.length == 3).map(s =>
            [decrementChar(s[0], 16), decrementChar(s[2], 39)]
        ).map(game => {
            return game[1] + hasWon(game[0], game[1])
        }).reduce((a, b) => a+b)
    )
}

const part1 = () => {
    fs.readFile("./day2/day2.txt", 'utf8', (err, data) => {
            parseGame(data);
    });
};

const part2 = () => {
    const whatWins = (elf, tgt) => {
        const win_table = [1, 2, 3]
        while (elf != win_table[1]) {
            win_table.unshift(win_table.pop())
        }
        return win_table[tgt-1]
    }
    fs.readFile("./day2/day2.txt", 'utf8', (err, data) => {
        parseGame(
            data.split("\n").filter((row) => row.length == 3).map(s =>
                [decrementChar(s[0], 16), decrementChar(s[2], 39)]
            ).map(game => `${String.fromCharCode(game[0] + 48 + 16)} ${String.fromCharCode(whatWins(game[0], game[1]) + 48 + 39)}`).join("\n")
        )
    })
};
part1()
part2()