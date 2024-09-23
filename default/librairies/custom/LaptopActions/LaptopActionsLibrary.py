import pyautogui

class LaptopActionsLibrary:

    def press_key(self, key):
        """
        Press a single key.
        :param key: The key to be pressed (e.g., 'a', 'b', 'enter', 'tab').
        """
        pyautogui.press(key)
    
    def type_text(self, text):
        """
        Type a string of text letter by letter.
        :param text: The string to be typed.
        """
        pyautogui.typewrite(text)
    
    def press_multiple_keys(self, *keys):
        """
        Press multiple keys in sequence.
        :param keys: A sequence of keys to be pressed.
        """
        for key in keys:
            pyautogui.press(key)
    
    def hold_and_press_key(self, modifier, key):
        """
        Hold down a modifier key (like 'ctrl', 'shift') and press another key.
        :param modifier: The modifier key (e.g., 'ctrl', 'shift').
        :param key: The key to press while holding the modifier.
        """
        pyautogui.hotkey(modifier, key)

    def take_screenshot(self):
        imagevar = pyautogui.screenshot()
        imagevar.save('screenshot.png')

# # # Example usage:
# actions = LaptopActionsLibrary()
# actions.take_screenshot()

# # Press a single key (e.g., 'a')
# # actions.press_key('a')

# # Type a full text (e.g., 'hello')
# actions.type_text('user')
# actions.press_key('tab')
# actions.type_text('password')
# actions.press_key('enter')



# # Press multiple keys in sequence (e.g., 'h', 'e', 'l', 'l', 'o')
# # actions.press_multiple_keys('h', 'e', 'l', 'l', 'o')

# # Hold down 'ctrl' and press 's' (for saving a file, for example)
# # actions.hold_and_press_key('ctrl', 's')

