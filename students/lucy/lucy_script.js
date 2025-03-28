// FizzBuzz 
function fizzbuzz(n) {
     let output = [];    // initialize an empty array to store output
     for (let i = 1; i <= n; i++) {
         if (i % 3 === 0 && i % 5 === 0) {    // check if number is multiple of 3 and 5
             output.push(">> BobCat");
         } else if (i % 3 === 0) {            // check if number is multiple of 3
             output.push(">> Bob");   
         } else if (i % 5 === 0) {            // check if number is multiple of 5
             output.push(">> Cat");
         } else {
             output.push(">> "+ i);
         }
     }
     return output;    // return the output as an array of strings
 }






 document.querySelectorAll(".play-button").forEach(button => {          // select all play buttons by selecting all elements with class "play-button"
     button.addEventListener("click", function() {                      // add a click event listener to each play button 

         let new_fizzbuzz_form = document.createElement("form");         // create a form element for user to enter input for fizzbuzz 
         new_fizzbuzz_form.innerHTML = '<input type="text" placeholder="Enter a number"> <button type="submit"><p>Submit</p></button>';
         this.parentNode.parentNode.appendChild(new_fizzbuzz_form);      // add the new form to grandparent element of play button (list item)        

         this.outerHTML = '<a class="play-button"><img src="images/done-check.svg" height="30px"></a>';     // swap the play button with a check mark button to indicate that FizzBuzz is running




         // get the FizzBuzz form, input, and submit button elements
         const fizzbuzz_form = document.querySelector("form");
         const fizzbuzz_form_input = fizzbuzz_form.querySelector("input");
         const submit_button = fizzbuzz_form.querySelector("button");

         fizzbuzz_form.addEventListener("submit", function(event) {      // add a submit event listener to the FizzBuzz form 
             event.preventDefault();                                     // prevent reloading the page when the form is submitted 

             submit_button.disabled = true;                              // disable submit button once form is submitted
             submit_button.style.backgroundColor = "#619dd0";


             const input_value = fizzbuzz_form_input.value;             // get and store the value entered as input for the Fizzbuzz form
             let form_feedback = document.createElement("p");           // create a paragraph element to display user's input 
             form_feedback.innerHTML = `Your input:  ${input_value}.`;
             this.parentNode.appendChild(form_feedback);                // add the new paragraph to parent element of FizzBuzz form (list item)
             
             let fizzbuzz_output = fizzbuzz(input_value);               // run FizzBuzz with user's input 
             fizzbuzz_output = fizzbuzz_output.join("<br>");            // join strings in output array into a single string, separating each element with a line break
             let output_div = document.createElement("div");            // create a new div to contain the output of FizzBuzz
             output_div.innerHTML = `<p> <strong>FizzBuzz Output:</strong> <br> <em>${fizzbuzz_output}</em> </p>`
             this.parentNode.appendChild(output_div);                   // add the new div to parent element of FizzBuzz form (list item)
         });
     });
 });
