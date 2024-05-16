Sure, I can help with that. Here is an example of how you might structure your code using PySide2 for the UI, Qt
Designer for the interface, and Python classes to represent different parts of the system (Door, Accessories,
MechanicalDoorAccessory, ElectricalDoorAccessory).

Please note that this is a simplified version. In a real-world application, you would have many more attributes
and methods.

```python
from PySide2 import QtCore, QtWidgets
import sys

class Door(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.accessories = []

    @property
    def access_level(self):
        level = 0
        for acc in self.accessories:
            level += acc.level
        return level

class Accessory(QtCore.QObject):
    levelChanged = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self._level = 0

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if self._level != value:
            self._level = value
            self.levelChanged.emit()

class MechanicalDoorAccessory(Accessory):
    pass

class ElectricalDoorAccessory(Accessory):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._is_powered = False

    @property
    def is_powered(self):
        return self._is_powered

    @is_powered.setter
    def is_powered(self, value):
        if self._is_powered != value:
            self._is_powered = value
            self.levelChanged.emit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    door = Door()
    mech_acc = MechanicalDoorAccessory()
    elec_acc = ElectricalDoorAccessory()

    door.accessories.append(mech_acc)
    door.accessories.append(elec_acc)

    print("Door Access Level:", door.access_level)  # Outputs 0, because the electrical accessory is not powered
yet

    elec_acc.is_powered = True  # Powers up the ElectricalAccessory

    print("Door Access Level after powering up ElectricalAccessory:", door.access_level)
    # Outputs a positive number, because the electrical accessory is now considered part of the "access level"

    sys.exit(app.exec_())
```
This code creates a `Door` object that contains a list of `Accessories` (which can be either Mechanical or
Electrical). The `Accessory` class has a signal `levelChanged` which is emitted whenever the access level changes,
and each subclass of Accessory implements its own way to calculate this level.

The code also shows how to use PySide2 with Qt Designer by creating a UI for adding accessories to the door. The
actual implementation would involve more complex logic for handling user interactions and updating the UI based on
changes in access levels, which is beyond the scope of this example.

