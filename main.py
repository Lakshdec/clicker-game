from pyscript import document

score = 0

def handle_click(event):
    global score
    score += 1
    document.querySelector("#score-display").innerText = str(score)

# This tells the button what to do without needing a "loop"
btn = document.querySelector("#click-btn")
btn.onclick = handle_click

# Tell the user we are ready
document.querySelector("#status").innerText = "Ready to click!"
