import subprocess

name = input("What name would you like to assign to the USB drive after formatting it? : ")
usb_disk = input('Please enter the USB location : ')
# usb_disk = "/dev/disk5"  # Replace with the actual disk identifier of your USB drive

try:

    # Unmount the USB drive first
    subprocess.run(["diskutil", "unmountDisk", usb_disk], check=True)

    # Erase the USB drive (replace "MyVolumeName" with your desired volume name)
    subprocess.run(["diskutil", "eraseDisk", "MS-DOS", name, usb_disk], check=True)

    print(f"USB drive {usb_disk} has been erased successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")