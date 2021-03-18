const Checker = require('./Checker.js');

class Movie {
    constructor(n, c, ss) {
        this._n = n
        this._c = c
        this._ss = ss
    }

    get name(){
        return this._n
    }

    get category(){
        return this._c
    }

    get startShow(){
        return this._ss
    }

    watchMovie(){
        return `I watch the movie ${this.name}`
    }
}

const movie1 = new Movie('Titanic', 'drama', 1997)
const movie2 = new Movie('Troya', 'historical', 2004)