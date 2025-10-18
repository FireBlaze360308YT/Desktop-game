#Imports
import pyautogui
import keyboard
import time
import os

#Main function
def main() -> None:

    #Size of grid cell
    grid_width: int = 112
    grid_height: int = 144

    #Cords of center of cell 0,0 aka starting cell
    x: int = grid_width//2
    y: int = grid_height//2

    #When running script this minimizes all windows
    pyautogui.hotkey("win", "d")

    #Size of the screen
    screen_limits: dict[str, tuple[int, int]] = {"x": (0, 3800), "y": (0, 2000)}

    #Cursor moved to starting cell aka cell 0,0
    pyautogui.moveTo(x, y)

    #Each possibility of direction in 2d plane results in different coordinate changes
    move_deltas: dict[str, tuple[int, int, str]] = {
        "w": (0, -grid_height, "s"),
        "a": (-grid_width, 0, "d"),
        "s": (0, grid_height, "w"),
        "d": (grid_width, 0, "a"),
    }

    # Direction of movement from start
    direction: str = "d"

    #Key press detection
    def on_key_press(event):
        nonlocal direction
        key_local = event.name
        if key_local in move_deltas and move_deltas[key_local][2] != direction:
            direction = key_local

    #Game loop
    while True:

        # Sensor of key to decide the direction
        for key in move_deltas:
            keyboard.on_press_key(key, on_key_press)

        #Q to quit
        if keyboard.is_pressed("q"):
            break

        #Based on the chosen direction, the move_deltas dict gives the change in coordinates
        dx, dy, _ = move_deltas[direction]

        #Calculation of the new x and y based on chosen direction of travel
        x += dx
        y += dy

        #Boundary check
        if not (screen_limits["x"][0] <= x <= screen_limits["x"][1] and
                screen_limits["y"][0] <= y <= screen_limits["y"][1]):
            break

        #Movement in direction
        pyautogui.mouseDown()
        pyautogui.moveTo(x=x, y=y)
        pyautogui.mouseUp()

    #Release keys
    keyboard.unhook_all()

    #Exiting the loop means game finished, the cursor brings the starting file to start position and waits
    pyautogui.mouseDown()
    pyautogui.moveTo(x=grid_width//2, y=grid_height//2)
    pyautogui.mouseUp()

    #The desktop gets cleared from useless files
    desktop: str = "C:/Users/utente/OneDrive/Desktop"
    for file in os.listdir(desktop):
        os.remove(desktop + "/" + file)
    pyautogui.press("F5")

    #Maximizes windows
    pyautogui.hotkey("win", "d")

#Run check
if __name__ == "__main__":
    main()
