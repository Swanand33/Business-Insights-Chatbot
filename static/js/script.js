async function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

    // Show a loading indicator while waiting for AI response
    chatBox.innerHTML += `<p><em>AI is thinking...</em></p>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    // Send user input to backend
    let response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput }),
    });

    let result = await response.json();
    document.getElementById("chat-box").innerHTML += `<p><strong>AI:</strong> ${result.response}</p>`;

    document.getElementById("user-input").value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}