import asyncio
from pyscript import document

# Global score variable
score = 0

def handle_click(event):
    global score
    score += 1
    # Update the text on the webpage
    document.querySelector("#score-display").innerText = f"Score: {score}"

async def main():
    # Hide the loading message once Python starts
    document.querySelector("#loading-msg").style.display = "none"
    
    # Find the button and tell it what to do when clicked
    btn = document.querySelector("#click-btn")
    btn.onclick = handle_click
    
    # The "Game Loop" - this keeps the script alive
    while True:
        # await asyncio.sleep(0) allows the browser to process clicks
        await asyncio.sleep(0.1)

# This line starts the game loop
asyncio.run(main())
