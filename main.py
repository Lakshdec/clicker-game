import asyncio
from pyscript import document

score = 0

def handle_click(proxy):
    global score
    score += 1
    document.querySelector("#score-display").innerText = str(score)

async def start_game():
    btn = document.querySelector("#click-btn")
    btn.onclick = handle_click
    document.querySelector("#status").innerText = "Ready!"
    while True:
        await asyncio.sleep(0.1)

# NO asyncio.run() here! 
# We use the built-in PyScript loop
await start_game()
