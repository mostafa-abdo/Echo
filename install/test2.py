import os
import shutil
import zipfile
import winreg
import sys
import ctypes


def create_desktop_shortcut(program_name):
    desktop_path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
    shortcut_path = os.path.join(desktop_path, f"{program_name}.lnk")
    target_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "install.py")

    shell = ctypes.windll.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    shortcut.IconLocation = target_path
    shortcut.save()

def install_program(program_name, program_folder, program_executable):
    # Get the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Create a temporary directory to store the packaged program
    temp_dir = os.path.join(script_dir, "install_package")
    os.makedirs(temp_dir, exist_ok=True)

    # Copy the program files to the temporary directory
    temp_program_folder = os.path.join(temp_dir, program_name)
    shutil.copytree(program_folder, temp_program_folder)

    # Create a zip archive of the program files and installation script
    zip_file = os.path.join(script_dir, f"{program_name}_install_package.zip")
    with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                archive_path = os.path.relpath(file_path, temp_dir)
                zf.write(file_path, archive_path)

    print("Installation package created:", zip_file)
    print("Transfer the package to the target device and run the 'install.py' script.")

# Example usage
install_program("Test", "C:\Program Files (x86)\Betternet\\6.3.2.527", "Betternet.exe")
