import asyncio
from pyscript import document

# Start score at 0
score = 0

# This runs when you click the button
def handle_click(event):
    global score
    score += 1
    # Update the number on the screen
    document.querySelector("#score-display").innerText = str(score)

async def main():
    # Find the button in HTML
    btn = document.querySelector("#click-btn")
    
    # Tell the button to run our function when clicked
    btn.onclick = handle_click
    
    # Change status text when ready
    document.querySelector("#status").innerText = "Ready to Play!"
    
    # The "Game Loop" - keeps the script running in the browser
    while True:
        await asyncio.sleep(0.1)

# Start the game loop
asyncio.run(main())
