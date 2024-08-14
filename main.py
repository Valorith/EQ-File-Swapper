import os
import urllib.request
import shutil
import configparser

#To Compile: pyinstaller main.py -F --uac-admin -i Old_eq_icon.ico

# Define default settings
default_settings = {
    'Settings': {
        'test_server_ip': '000.000.000.000:0000',
        'live_server_ip': '000.000.000.000:0000'
    }
}

# Check if exporter.ini exists
ini_file = 'swapper.ini'
if not os.path.exists(ini_file):
    # Create exporter.ini with default settings
    config = configparser.ConfigParser()
    config.read_dict(default_settings)
    with open(ini_file, 'w') as configfile:
        config.write(configfile)
    print(f"{ini_file} created with default settings.")


# Load settings from exporter.ini
config = configparser.ConfigParser()
config.read('swapper.ini')

# Load settings from ini files
print(f"Loading app settings from {ini_file}.")

# Load test server IP
fallback_test_server_ip = '000.000.000.000:0000' # Default test server IP. Overwritten if loaded from ini file.
loaded_test_server_ip = config.get('Settings', 'test_server_ip', fallback=fallback_test_server_ip)
test_server_ip = '000.000.000.000:0000'
if loaded_test_server_ip == '000.000.000.000:0000':
    test_server_ip = fallback_test_server_ip
    print("Test server ip reverted to default ip.")
else:
    test_server_ip = loaded_test_server_ip
    print(f"Test server ip loaded: {loaded_test_server_ip}")

# Load live server IP
fallback_live_server_ip = '000.000.000.000:0000' # Default test server IP. Overwritten if loaded from ini file.
loaded_live_server_ip = config.get('Settings', 'live_server_ip', fallback=fallback_live_server_ip)
if loaded_live_server_ip == '000.000.000.000:0000':
    live_server_ip = fallback_live_server_ip
    print("Live server ip reverted to default ip.")
else:
    live_server_ip = loaded_live_server_ip
    print(f"Live server ip loaded: {loaded_live_server_ip}")


def create_directories(base_path):
    test_server_path = os.path.join(base_path, "Test_Server")
    live_server_path = os.path.join(base_path, "Live_Server")
    os.makedirs(test_server_path, exist_ok=True)
    os.makedirs(live_server_path, exist_ok=True)
    return test_server_path, live_server_path

def download_files(urls, destination_folder):

    # Mapping of URL endings to filenames
    filename_mapping = {
        "spells": "spells_us.txt",
        "dbstring": "dbstr_us.txt",
        "skills": "SkillCaps.txt",
        "basedata": "BaseData.txt"
    }

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    for url in urls:
        file_key = url.split('/')[-1]  # Extract the file key from the URL
        file_name = filename_mapping.get(file_key, file_key)  # Get the mapped filename or default to the key
        file_path = os.path.join(destination_folder, file_name)
        print(f"Downloading {file_name} to {file_path}...")
        urllib.request.urlretrieve(url, file_path)
        print(f"Success!")


def copy_files_to_base(server, base_path):
    source_folder = os.path.join(base_path, f"{server}_Server")
    root_directory = os.getcwd()  # Get the root directory where the application is running

    if not os.listdir(source_folder):
        print(f"No files found in {source_folder}...")
        return

    for file_name in os.listdir(source_folder):
        print(f"Copying {file_name} from {source_folder} to {root_directory}...")
        source_file = os.path.join(source_folder, file_name)
        destination_file = os.path.join(root_directory, file_name)  # Copy to the root directory
        shutil.copy2(source_file, destination_file)
        print(f"Success!")

def main():
    base_path = os.path.join(os.getcwd(), "Version_Files")

    type = input("Do you want to connect to the `Test` or `Live` server? ")

    if type.lower() not in ["test", "live"]:
        print("Invalid server type (must be `Live` or `Test`). Exiting the application.")
        return
    
    if not os.path.exists(base_path):
        print("Creating 'Version_Files' directory and subdirectories...")
        test_server_path, live_server_path = create_directories(base_path)
    
    test_server_path = os.path.join(base_path, "Test_Server")
    live_server_path = os.path.join(base_path, "Live_Server")

    # List of files to download for use with the test server
    test_server_urls = [
        f"http://{test_server_ip}/api/v1/eqemuserver/export-client-file/spells",
        f"http://{test_server_ip}/api/v1/eqemuserver/export-client-file/dbstring"
    ]
    #Skills and BaseData files can be added to the above list if needed
    #f"http://{test_server_ip}/api/v1/eqemuserver/export-client-file/skills",
    #f"http://{test_server_ip}/api/v1/eqemuserver/export-client-file/basedata"

    # List of files to download for use with the live server
    live_server_urls = [
        f"http://{live_server_ip}/api/v1/eqemuserver/export-client-file/spells",
        f"http://{live_server_ip}/api/v1/eqemuserver/export-client-file/dbstring",
        f"http://{live_server_ip}/api/v1/eqemuserver/export-client-file/skills",
        f"http://{live_server_ip}/api/v1/eqemuserver/export-client-file/basedata"
    ]
    
    if type.lower() == "test":
        download_files(test_server_urls, test_server_path)
        copy_files_to_base("Test", base_path)
    elif type.lower() == "live":
        download_files(live_server_urls, live_server_path)
        copy_files_to_base("Live", base_path)

    input("Press any key to close...")

if __name__ == "__main__":
    main()