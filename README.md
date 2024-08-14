
[How to Run]

- Download the most current release binary (exe) file.
- ![image](https://github.com/user-attachments/assets/04173bf7-81a3-4e9f-83c4-3e38a92c65b6)
- Place the exe file in your EQ client directory.
- ![image](https://github.com/user-attachments/assets/ec9ceda7-005c-49e9-b5c3-8dea1c1e0f80)
- Run the app.
- When asked, select which server you want to download the files for: `Test` or `Live`.
- ![image](https://github.com/user-attachments/assets/d92634a3-18b6-487b-b2a7-6de9c76f1537)
- Be patient and allow time for the downloading to complete. This can take a couple minutes, depending on your internet speed.
- ![image](https://github.com/user-attachments/assets/48ecf1b6-5277-4914-abcb-366ba8e0ccc2)
- The default server IP addresses for `Live` and `Test` server files are for the `Clumsy's World: Resurgence` EQ Emulator servers. This can be changed via the `swapper.ini` settings file (gets created on first run if not present).
- ![image](https://github.com/user-attachments/assets/d1fa0050-21fc-44c0-8cf3-6142a6af27f9)
- Simply repeat this process any time you want to swap your local files to match a specific server's files.
- Thats it!

[Compile]

- THIS IS NOT REQUIRED! You only need to compile your own binaries if you want to change the application.
- If you just want to USE the default app, you can simply use the Release binaries.
- I use a package called `pyinstaller` to compile this python script into a binary file. You can alternatively just run the script in place without compiling (will need Python installed: https://www.python.org/downloads/).
- Once you have installed `pyinstaller` (https://pyinstaller.org), you can run the following command to compile binaries: `pyinstaller main.py -F --uac-admin -i Old_eq_icon.ico`
 - Your exe will be saved in `<project_folder/dist/main.exe`
