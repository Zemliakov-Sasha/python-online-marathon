function checkAdult(age){
    try {

        if (0<age){if(age < 18){throw new Error("Access denied - you are too young!")}}
        if (typeof age === "undefined"){throw new Error("Please, enter your age")}
        if (age <= 0){throw new Error("Please, enter positive number")}
        if (age !== parseInt(age)){if(age === parseFloat(age)){throw new Error("Please, enter Integer number")}}
        if (typeof age === "string"){throw new Error("Please, enter number")}
        else {
            console.log("Access allowed")
            console.log("Age verification complete")
        }
    }
    catch (exception){
        console.log(exception.name, exception.message)
        console.log("Age verification complete")
    }
}
checkAdult("2d")