from MechEye import Device


def show_error(status):
    if status.ok():
        return
    print("Error Code : {}".format(status.code()),
          ",Error Description: {}".format(status.description()))


class SetUserSets(object):
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

        print("All user sets : ", end='')
        user_sets = self.device.get_all_user_sets()
        for user_set in user_sets:
            print(user_set, end=' ')

        current_user_set = self.device.get_current_user_set()
        print("\ncurrent_user_set: " + str(current_user_set))

        show_error(self.device.add_user_set("iii"))
        show_error(self.device.delete_user_set('iii'))

        self.device.save_all_settings_to_user_set()

    def main(self):
        self.find_camera_list()
        self.choose_camera()
        self.connect_device_info()


if __name__ == '__main__':
    a = SetUserSets()
    a.main()