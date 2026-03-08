import asyncio
from pyscript import document

score = 0

def handle_click(event):
    global score
    score += 1
    document.querySelector("#score-display").innerText = str(score)

async def main():
    # Setup the button
    btn = document.querySelector("#click-btn")
    btn.onclick = handle_click
    
    # Change status when ready
    document.querySelector("#status").innerText = "Ready to play!"
    
    # Keep the game running
    while True:
        await asyncio.sleep(0.1)

# FIXED: Just call the function with 'await' 
# instead of using asyncio.run()
await main()
