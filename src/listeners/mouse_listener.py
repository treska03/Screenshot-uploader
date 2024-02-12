from pynput import mouse

class Mouse_listener:

    def __init__(self):
        self._start_coordinates = ()
        self._end_coordinates = ()

    def _on_click(self, x, y, button, pressed):
        if button == mouse.Button.left and pressed:
            self._start_coordinates = x, y
        elif button == mouse.Button.left and not pressed and self._start_coordinates:
            self._end_coordinates = x, y
            return False

    def select_area(self):
    
        with mouse.Listener(
            on_click=self._on_click) as listener:
            listener.join()

        return self._start_coordinates[0], self._start_coordinates[1], self._end_coordinates[0], self._end_coordinates[1]
