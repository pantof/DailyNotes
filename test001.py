class Door:
    def __init__(self, material, size):
        self.material = material
        self.size = size
        self.lock_type = None
        self.accessories = []  # List to store accessory objects

    def set_lock(self, lock_type):
        if lock_type in ['key', 'padlock', 'biometric']:
            self.lock_type = lock_type
        else:
            raise ValueError('Invalid lock type')
        
    def add_accessory(self, accessory):
        # Checking if the given object is an instance of Accessory class
        if not isinstance(accessory, Accessory):
            raise TypeError('The input must be a valid Accessory object.')
        self.accessories.append(accessory)

    def __str__(self):
        return f'Door Material: {self.material}, Door Size: {self.size} sq ft, Lock Type: {self.lock_type}'+' ,Accessories: ' + ', '.join([str(a) for a in self.accessories])

class Accessory:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'Accessory Name: {self.name}, Color: {self.color}'

if __name__ == '__main__':
    # Creating a door instance with accessories
    door1 = Door('Wood', 10)
    door_handle = Accessory('Door Handle', 'Silver')
    door_lock = 'key' #Accessory('Lock', 'Black')

    # Attaching the accessories to the door
    door1.add_accessory(door_handle)
    door1.set_lock(door_lock)

    print(door1)  # Door Material: Wood, Door Size: 10 sq ft, Lock Type: Lock
    print(door_handle)  # Accessory Name: Door Handle, Color: Silver
    print(door_lock)   # Accessory Name: Lock, Color: Black
