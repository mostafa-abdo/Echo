import os
import shutil
import zipfile

# Get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create a temporary directory to store the packaged program
temp_dir = os.path.join(script_dir, "install_package")
os.makedirs(temp_dir, exist_ok=True)

# Copy the program files to the temporary directory
temp_program_folder = os.path.join(temp_dir, "Testo")
shutil.copytree("C:\Program Files\Audacity", temp_program_folder)

# Create a zip archive of the program files and installation script
zip_file = os.path.join(script_dir, f"Testo_install_package.zip")
with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            archive_path = os.path.relpath(file_path, temp_dir)
            zf.write(file_path, archive_path)

print("Installation package created:", zip_file)
