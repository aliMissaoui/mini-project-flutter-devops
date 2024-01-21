import os

PATH= '~/Project/_EDU_/DevOps'
TAG= 'flutter-foile'



def build_image():
    os.system('docker build ~/Project/_EDU_/DevOps --tag %s'%TAG)


def launch_flutter():
    os.system("mkdir -p /home/$USER/Project/_EDU_/DevOps/workspace && chmod 777 /home/$USER/Project/_EDU_/DevOps/workspace")
    ch= 'docker run --privileged --name flutter-foile -itd --rm  -v /home/$USER/Project/_EDU_/DevOps/workspace:/home/developer/workspace --mount type=bind,source=/dev/bus/usb,target=/dev/bus/usb %s '%str(TAG)
    print(ch)
    os.system(ch)





build_image()
launch_flutter()

