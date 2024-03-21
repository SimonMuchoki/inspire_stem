const randomNumber=Math.floor(Math.random()*100) +1

let attempt = 0

function checkGuess(){
    const guess = parseInt(document.getElementById("guessfield").value)
    attempt++

    if(isNaN(guess) || guess < 1 || guess > 100){
        setMessage("Please Enter a valid number between 1 and 100")
        return
    }

    if(guess === randomNumber){
        setMessage("Damn! You Passed")
    }else if(guess < randomNumber){
        setMessage("The Number is below requirements")
    }else if(guess > randomNumber) {
        setMessage("The Number is above requirement")
    }
    console.log(randomNumber)
}
function setMessage(message){
    document.getElementById("message").textContent = message
}