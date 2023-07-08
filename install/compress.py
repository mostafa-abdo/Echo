import os
import shutil
import zipfile

class Compress():
    def __init__(self, name, path):
        # Get the current script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))

        if not os.path.exists('install_package'):
            # Create a temporary directory to store the packaged program
            temp_dir = os.path.join(script_dir, "install_package")
            os.makedirs(temp_dir, exist_ok=True)

            # Copy the program files to the temporary directory
            temp_program_folder = os.path.join(temp_dir, name)
            if not os.path.exists(temp_program_folder):
                shutil.copytree(path, temp_program_folder)

            # Create a zip archive of the program files and installation script
            self.zip_file = os.path.join(script_dir, f"{name}_install_package.zip")
            with zipfile.ZipFile(self.zip_file, "w", zipfile.ZIP_DEFLATED) as zf:
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        archive_path = os.path.relpath(file_path, temp_dir)
                        zf.write(file_path, archive_path)

            print("Installation package created:", self.zip_file)
        else:
            self.zip_file = os.path.join(script_dir, f"{name}_install_package.zip")
    def getfile(self):
        return self.zip_file