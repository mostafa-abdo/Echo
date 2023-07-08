import winreg
import pickle


class ProgramData:
    def __init__(self, data):
        self.data = data

def get_installed_programs():
    installed_programs = []

    try:
        # Open the 64-bit 'Uninstall' key
        uninstall_key_64bit = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ)

        # Iterate through subkeys to retrieve installed 64-bit programs
        for i in range(winreg.QueryInfoKey(uninstall_key_64bit)[0]):
            subkey_name = winreg.EnumKey(uninstall_key_64bit, i)
            subkey_path = fr"Software\Microsoft\Windows\CurrentVersion\Uninstall\{subkey_name}"
            subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path, 0, winreg.KEY_READ)
            
            try:
                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                installed_programs.append((display_name, subkey_path))
            except OSError:
                # Some subkeys might not have a 'DisplayName' value
                pass

        # Open the 32-bit 'Uninstall' key
        uninstall_key_32bit = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ)

        # Iterate through subkeys to retrieve installed 32-bit programs
        for i in range(winreg.QueryInfoKey(uninstall_key_32bit)[0]):
            subkey_name = winreg.EnumKey(uninstall_key_32bit, i)
            subkey_path = fr"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\{subkey_name}"
            subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path, 0, winreg.KEY_READ)
            
            try:
                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                installed_programs.append((display_name, subkey_path))
            except OSError:
                # Some subkeys might not have a 'DisplayName' value
                pass

        return installed_programs

    except FileNotFoundError:
        print("Uninstall key not found.")
        return None
    except PermissionError:
        print("Access denied when trying to read registry keys.")
        return None
    finally:
        # Close the uninstall keys
        winreg.CloseKey(uninstall_key_64bit)
        winreg.CloseKey(uninstall_key_32bit)



def copy_registry_entry(source_key_path, destination_key_path):
    try:
        # Open the source registry key for reading
        source_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, source_key_path, 0, winreg.KEY_READ)

        # Retrieve the values from the source key
        values = []
        for i in range(winreg.QueryInfoKey(source_key)[1]):
            value_name, value_data, value_type = winreg.EnumValue(source_key, i)
            values.append((value_name, value_data, value_type))
        
        # Create the destination registry key
        destination_key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, destination_key_path)

        # Set the values in the destination key
        for value_name, value_data, value_type in values:
            winreg.SetValueEx(destination_key, value_name, 0, value_type, value_data)

        print("Registry entry copied successfully.")

    except FileNotFoundError:
        print(f"Source registry key '{source_key_path}' not found.")
    except PermissionError:
        print(f"Access denied when trying to access registry keys.")
    finally:
        # Close the registry keys
        winreg.CloseKey(source_key)
        winreg.CloseKey(destination_key)


# # Usage example
# installed_programs = get_installed_programs()

# i = 1

# if installed_programs:
#     print("List of installed programs:")
#     for program in installed_programs:
#         print(f"{i}- Program: {program[0]}")
#         # print(f"Registry Key: {program[1]}")
#         print()
#         i += 1
#     c = int(input("Choose a program: "))

subkey_path = r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\{2E77104D-96E1-4A9C-86F2-C7CFACA05BA9}"
subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path, 0, winreg.KEY_READ)

num_values = winreg.QueryInfoKey(subkey)[1]

regdata = []
for i in range(num_values):
    regdata.append(winreg.EnumValue(subkey, i))
    print(winreg.EnumValue(subkey, i))

data = ProgramData(regdata)

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)


    # print(f"Registry Key: {installed_programs[c-1][1]}")
    # source_key_path = installed_programs[c-1][1]
    # destination_key_path = r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Testo"
    # print(installed_programs[c-1])
    # copy_registry_entry(source_key_path, destination_key_path)