from MechEye import Device


def show_error(status):
    if status.ok():
        return
    print("Error Code : {}".format(status.code()),
          ",Error Description: {}".format(status.description()))


class SetFrameRange(object):
    def __init__(self):
        self.device = Device()

    def find_camera_list(self):
        self.device_list = self.device.get_device_list()
        if len(self.device_list) == 0:
            print("No Mech-Eye device found.")
            return
        for i, info in enumerate(self.device_list):
            print_device_info(i, info)

    def choose_camera(self):
        while True:
            self.user_input = input(
                "Please enter the device index you want to connect: ")
            if self.user_input.isdigit() and len(self.device_list) > int(self.user_input):
                break
            print("Input invalid! Please enter the device index you want to connect: ")

    def connect_device_info(self):
        status = self.device.connect(self.device_list[int(self.user_input)])
        if not status.ok():
            show_error(status)
            return -1
        print("Connect Mech-Eye Success.")

        # Parameter of laser camera, please comment out when connecting non-laser camera.
        laser_settings = self.device.get_laser_settings()
        print("\n partition_count:{}".format(laser_settings.get_count()))

        show_error(self.device.set_laser_settings(laser_settings.get_mode(
        ), 51, 90, laser_settings.get_count(), laser_settings.get_level()))

        laser_settings = self.device.get_laser_settings()
        print("\n partition_count:{}".format(laser_settings.get_count()))

    def main(self):
        self.find_camera_list()
        self.choose_camera()
        self.connect_device_info()


if __name__ == '__main__':
    a = SetFrameRange()
    a.main()