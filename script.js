document.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        let contentDiv = document.getElementById("content");
        let newParagraph = document.createElement("p");
        newParagraph.textContent = "Here's more text!";
        contentDiv.appendChild(newParagraph);
    }
});
