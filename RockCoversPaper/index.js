const rockButton = document.querySelector('#r');
const paperButton = document.querySelector('#p');
const scissorsButton = document.querySelector('#s');
const restartButton = document.querySelector('#restartB');
let uesrReslt = document.querySelector('#userReslt');
let compReslt = document.querySelector('#compReslt');
let statuss = document.querySelector('#showStatus');
restartButton.addEventListener('click' , restart)
scissorsButton.addEventListener('click', function(){game('s');});
rockButton.addEventListener("click",function(){game('r');});
paperButton.addEventListener('click',function(){game('p');});

function restart()
{
    uesrReslt.innerHTML = 0;
    compReslt.innerHTML = 0;
    statuss.innerHTML = "OK ! Let's get started !";
    
}

    

function choiceWord(a)
    {
        switch (a) {
            case 'r':
             return "Rock";
            case 'p':
                return 'Paper';
            case 's' :
                return "Scissors";
        }
    }
   
    
function game(userChoice)
    {
        console.log("pressed");
            let choices = ['r','p','s'];
           let  compChoice =  choices[(Math.floor(Math.random() * 3)) ];
        
           const result = userChoice + compChoice;
            console.log(result);
          switch (result) {
          case "rr" :
          case "pp":
          case "ss" :     
               draw(userChoice);
               break;
          case "rs":
          case "sp":
          case "pr":
              statuss.innerHTML = "Woah ! That was a win!"
                win(userChoice,compChoice);
                break;
    
           default:   
           lost(userChoice,compChoice);
          }
    
    }


function win(u,c){
        
        statuss.innerHTML = `Woah! That was a WIN ! \n You chose ${choiceWord(u)} and Computer chose ${choiceWord(c)}`
        uesrReslt.innerHTML = `${parseInt(uesrReslt.innerHTML)+ 1}` ;
        document.getElementById(u).classList.add('win-glow');
        document.getElementById('gameboard').classList.add('win-glow');
        setTimeout(function(){ document.getElementById(u).classList.remove('win-glow');document.getElementById('gameboard').classList.remove('win-glow');}, 1000);
      

    }

    function lost(u,c){
        
        statuss.innerHTML = `Opps! That was a loss ! \n You chose ${choiceWord(u)} and Computer chose ${choiceWord(c)}`
        compReslt.innerHTML = `${parseInt(compReslt.innerHTML)+ 1}` ;
        document.getElementById(u).classList.add('lost-glow');
        document.getElementById('gameboard').classList.add('lost-glow');
        setTimeout(function(){ document.getElementById(u).classList.remove('lost-glow');document.getElementById('gameboard').classList.remove('lost-glow');}, 1000);

    }


    function draw(u){
        
        statuss.innerHTML = `Oh! This is a draw ! \n Both you and the computer chose ${choiceWord(u)}  `;
        document.getElementById(u).classList.add('draw-glow');
        document.getElementById('gameboard').classList.add('draw-glow');
        setTimeout(function(){ document.getElementById(u).classList.remove('draw-glow');document.getElementById('gameboard').classList.remove('draw-glow');}, 1000);
    }
