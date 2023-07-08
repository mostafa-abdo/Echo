import winreg
import pickle
import socket


class SendReg():
    def __init__(self, search_query):
        # Example usage: search for keys and send the registry information
        search_query = search_query
        found_keys = self.search_registry_keys(search_query)

        if found_keys:
            print(f"Found registry keys matching '{search_query}':")
            for key in found_keys:
                registry_info = self.get_registry_info(r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\\" + key)
                
                # TCP client to send the serialized data
                host = '192.168.2.7'  # Replace with the target IP address
                port = 12345  # Replace with the desired port

                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((host, port))
                client_socket.send(registry_info)

                client_socket.close()
        else:
            print(f"No registry keys found matching '{search_query}'.")

        

    def search_registry_keys(self, search_query):
        keys = []
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

        for i in range(winreg.QueryInfoKey(registry_key)[0]):
            subkey_name = winreg.EnumKey(registry_key, i)
            subkey = winreg.OpenKey(registry_key, subkey_name)
            
            try:
                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                if search_query.lower() in display_name.lower():
                    keys.append(subkey_name)
            except FileNotFoundError:
                pass
        
        return keys

    def get_registry_info(self, registry_key_path):
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_key_path)

        values = {}
        try:
            i = 0
            while True:
                value_name, value_data, value_type = winreg.EnumValue(registry_key, i)
                values[value_name] = {
                    "type": value_type,
                    "value": value_data
                }
                i += 1
        except OSError:
            pass

        serialized_data = pickle.dumps({"key_path": registry_key_path, "key_values": values})
        return serialized_data
