import pywinusb.hid as hid
import pywinusb.usb as usb

def save_usb_info_to_file(file_path, usb_info):
    with open(file_path, 'a') as file:
        file.write("------------------------------\n")
        file.write("Device ID: {}\n".format(usb_info['device_id']))
        file.write("Manufacturer: {}\n".format(usb_info['manufacturer']))
        file.write("Product: {}\n".format(usb_info['product']))
        file.write("Serial Number: {}\n".format(usb_info['serial_number']))
        file.write("Protected: {}\n".format(usb_info['protected']))
        file.write("------------------------------\n")

def main():
    # Definišite putanju do tekstualnog dokumenta
    file_path = 'usb_info.txt'

    # Pronađi sve USB uređaje
    all_devices = usb.core.find(find_all=True)

    # Set za praćenje već prikazanih uređaja
    shown_devices = set()

    for device in all_devices:
        device_id = device.idProduct

        # Proveri da li je uređaj već prikazan
        if device_id in shown_devices:
            continue

        # Dodaj uređaj u set prikazanih uređaja
        shown_devices.add(device_id)

        # Prikupi informacije o uređaju
        manufacturer = usb.util.get_string(device, device.iManufacturer)
        product = usb.util.get_string(device, device.iProduct)
        serial_number = usb.util.get_string(device, device.iSerialNumber)
        is_protected = device.is_kernel_driver_active(0)

        # Sačuvaj informacije o USB uređaju u tekstualni dokument
        usb_info = {
            'device_id': device_id,
            'manufacturer': manufacturer,
            'product': product,
            'serial_number': serial_number,
            'protected': is_protected
        }
        save_usb_info_to_file(file_path, usb_info)

if __name__ == '__main__':
    main()
