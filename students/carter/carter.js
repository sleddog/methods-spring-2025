// Event listener for button click
window.addEventListener("DOMContentLoaded", () => {
    // Create button
    const button = document.createElement("button");
    button.textContent = "Click me!";
    button.style.padding = "10px 20px";
    button.style.marginTop = "2rem";
    button.style.fontSize = "1rem";
    button.style.cursor = "pointer";

    document.body.appendChild(button);

    // Upon click, pop open welcome modal
    button.addEventListener("click", () => {
        alert("Welcome to my personal page!");
    });
});