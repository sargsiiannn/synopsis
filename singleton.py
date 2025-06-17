# Ensures only one instance of SettingsManager is created
# Shared object for app-wide config

class SettingsManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.theme = "dark"
        return cls._instance

# Usage
s1 = SettingsManager()
s2 = SettingsManager()
print(s1 is s2)  # True
print(s2.theme)  # dark
