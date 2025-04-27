const button = document.getElementById('button');
const colors = ['red','orange','yellow','green','blue','rebeccapurple','violet', 'lemon', 'grey', 'black'];
function change() {
document.body.style.background = colors[Math.floor(10*Math.random())];
}
button.addEventListener('click', change);

let question = '"Do you want to learn JavaScript? "Yes!"'
console.log(question)

let language = "JavaScript";
let message = `Let's learn ${language}`;
console.log(message);

const name = prompt('Please enter your name.');
alert(name);

const permission = confirm('Do you give consent for us to steal all of your personal data?');

// ask the user for their name
// say hello
alert('Hello');
// then personalize it!
alert('Hello ' + name + '. The first letter of your name is ' + name[0] + ' he last letter is ' + name[name.length -1]);

// ask the user for some words....
const animal = prompt('Please enter an animal.');
const color = prompt('Please enter a color.');
const verb = prompt('Please enter a verb.');
const job = prompt('Please enter a job.')
// create the Mad Lib
const madlib = `The ${animal} wanted to be a ${job}, but turned a funny shade of ${color} after trying to ${verb}!`

// Show the Mad Lib
alert(madlib);

// age converter
const ageInYears = prompt('How old are you (in years)?')
const ageInSeconds = ageInYears * 365.25 * 24 * 60 * 60;
alert(`That means you have been alive for at least ${ageInSeconds} seconds!!`);

//dice gme
const sides = prompt('How many sides does the dice have?');
alert('Press Enter or click close to roll the dice...');
const number = Math.ceil(sides*Math.random())
alert(`The dice landed on the number ${number}`);


let arr = [0, 1, 2];
console.log(typeof arr)

let dog = { dogName: "puppi ",
            weight: 2.4,
            color: "brown",
            breed: "bruwn", 
            age:     3,
            burglarBiter: true
};
        let activity = 0
        switch(activity){
            case "Get up" : 
            console.log("it is 6:30am");
            break;
            case "breakfast" : 
            console.log("it is 7:00am");
            break;
            case "Drive to work " : 
            console.log("it is 8:00am");
            break;
            case "Lunch" : 
            console.log("it is 12:00pm");
            break;
            case "Drive Home " : 
            console.log("it is 5:00pm");
            break;
            case "Dinner" : 
            console.log("it is 6:00pm");
            break;
        }

       let sch = 9
       if (sch < 15) {
        console.log('I m bck home ')
       }
       function myFunction() {
      var x = document.getElementById("myTopnav");
      if (x.className === "topnav") {
        x.className += " responsive";
      } else {
        x.className = "topnav";
      }
    }
    document.getElementById('year').textContent = new Date().getFullYear();
