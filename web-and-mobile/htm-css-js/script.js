window.addEventListener("load", function()
{
    // Get click elements.
    let clickButtonElement = document.getElementById("click_button");
    let clickCounterElement = document.getElementById("click_counter");

    // Counter value.
    let counter = 0;
    
    //Button click function.
    let clickButtonFunction = function ()
    {
        //Increment counter.
        counter++;

        //update click counter text.
        clickCounterElement.innerHTML = counter;
    };

    // Attach click function to button.
    clickButtonElement.addEventListener("click", clickButtonFunction);
});