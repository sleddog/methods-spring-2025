document.addEventListener("DOMContentLoaded", () => {
    const toggleButton = document.getElementById("toggleButton");
    const linkList = document.getElementById("linkList");

    toggleButton.addEventListener("click", () => {
        linkList.style.display = linkList.style.display === "none" ? "block" : "none";
    });
});

