#Imports
import pyautogui
import keyboard


#Main function
def main() -> None:

    #Size of grid cell
    grid_width: int = 112
    grid_height: int = 144

    locations: list[list[int]] = [[0, 0], [1, 0], [2, 0]] #Snake

    #When running script this minimizes all windows
    pyautogui.hotkey("win", "d")

    #Size of the screen
    screen_limits: dict[str, tuple[int, int]] = {"x": (0, 3800), "y": (0, 2000)}

    #Cursor moved to starting cell aka cell 0,0
    pyautogui.moveTo(x=grid_width//2, y=grid_height//2)

    # Direction of movement from start
    direction: str = "d"

    keys: list[str] = ["w", "a", "s", "d"]

    #Game loop
    while True:

        # Q to quit
        if keyboard.is_pressed("q"):
            break

        if direction == "d":
            pyautogui.moveTo(locations[0][0]*112+56, locations[0][1]*144+72)
            pyautogui.mouseDown()
            pyautogui.moveTo(locations[-1][0]*112+112, locations[-1][1]*144+72)
            pyautogui.mouseUp()
            for i in range(len(locations) - 1):
                locations[i][0] = locations[i + 1][0]
            for i in range(len(locations) - 1):
                locations[i][1] = locations[i + 1][1]
            locations[2][0] += 1

        if direction == "a":
            pyautogui.moveTo(locations[0][0]*112+56, locations[0][1]*144+72)
            pyautogui.mouseDown()
            pyautogui.moveTo(locations[-1][0]*112-112, locations[-1][1]*144+72)
            pyautogui.mouseUp()
            for i in range(len(locations) - 1):
                locations[i][0] = locations[i + 1][0]
            for i in range(len(locations) - 1):
                locations[i][1] = locations[i + 1][1]
            locations[2][0] -= 1

        if direction == "w":
            pyautogui.moveTo(locations[0][0]*112+56, locations[0][1]*144+72)
            pyautogui.mouseDown()
            pyautogui.moveTo(locations[-1][0]*112, locations[-1][1]*144-144)
            pyautogui.mouseUp()
            for i in range(len(locations) - 1):
                locations[i][0] = locations[i + 1][0]
            for i in range(len(locations) - 1):
                locations[i][1] = locations[i + 1][1]
            locations[2][1] -= 1

        if direction == "s":
            if locations[-1][1]*144+144 > screen_limits["y"][1]:
                locations[-1][1] = locations[-1][1] * 144 - 72
                continue
            pyautogui.moveTo(locations[0][0]*112+56, locations[0][1]*144+72)
            pyautogui.mouseDown()
            pyautogui.moveTo(locations[-1][0]*112, locations[-1][1]*144+144)
            pyautogui.mouseUp()

            for i in range(len(locations)-1):
                locations[i][0] = locations[i+1][0]
            for i in range(len(locations)-1):
                locations[i][1] = locations[i+1][1]
            locations[2][1] += 1

        for key in keys:
            if keyboard.is_pressed(key):
                direction = key
                break

    #Exiting the loop means game finished, the cursor brings the starting file to start position and waits
    pyautogui.mouseDown()
    pyautogui.moveTo(x=grid_width//2, y=grid_height//2)
    pyautogui.mouseUp()

    #Maximizes windows
    pyautogui.hotkey("win", "d")

#Run check
if __name__ == "__main__":
    main()
