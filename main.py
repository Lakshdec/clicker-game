import asyncio
from pyscript import document

# This keeps track of your clicks
score = 0

def handle_click(event):
    global score
    score += 1
    # This changes the number on the screen
    document.querySelector("#score-display").innerText = str(score)

async def main():
    # This finds the button in the HTML
    button = document.querySelector("#click-btn")
    
    # This tells the button to run 'handle_click' when you press it
    button.onclick = handle_click
    
    # This hides the loading message when the game is ready
    document.querySelector("#loading-text").innerText = "Game Ready! Click away!"
    
    # This loop keeps the game 'alive' in your browser
    while True:
        await asyncio.sleep(0.1)

# Start the game!
asyncio.run(main())
