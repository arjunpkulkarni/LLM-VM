document.addEventListener('DOMContentLoaded', function () {
    // Selecting the button element
    var runButton = document.querySelector('.button-container .button');

    // Selecting the input box
    var inputBox = document.querySelector('.input-container .input-box');

    // Function to be called when the button is clicked
    function onRunButtonClick() {
        // Get the value from the input box
        var inputValue = inputBox.value;

        // Simple action: Display an alert with the input value
        alert("Creating a SoundCloud set for: " + inputValue);
    }

    // Add an event listener to the button
    runButton.addEventListener('click', onRunButtonClick);
});
