![alt text](https://github.com/sourceryltd/miniCNC/blob/main/MakerMade-CNC-Logo.png)

# MKS-DLC32-FIRMWARE
The source code of MKS DLC32.

unzip libraries.zip into the current directory 
rename vscode  directory as  .vscode 

## Environment construction:

- vscode

- platformIO

PlatformIOc needs to be installed on vscode.

Open Firmware with vscode, and platformIO will be started, In the platform.ini file，

`default_envs = mks_dlc32_v2_1` 

Note:We will make a pin suitable for V1.0，Settings corresponding to the selection of coreXY.

Then compile and download.

