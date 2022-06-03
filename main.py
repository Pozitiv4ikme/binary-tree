from device import Device
from binary_tree_node import Node


def creation_and_realization_of_a_tree():
    first_devise = Device()
    second_device = Device("ammeter", "VA-1 red", 200, 1000, 2021)
    third_device = Device("digital multimeter", "DT9205A", 746, 2000, 2019)
    fourth_device = Device("digital voltmeter", "VD9032-R", 10, 32, 2022)
    fifth_device = Device("some device", "nEARTH9f-0", 100, 125, 1999)
    sixth_device = Device("another device", "1fGHY56 blue", 1000, 10000, 2045)
    seven_device = Device("new device", "nmscomfc-1.0", 5, 10, 2022)
    eight_device = Device("eight device", "love", 26, 102, 2022)
    nine_device = Device("Number nine", "love", 134, 102, 2022)
    ten_device = Device("TenTaSion", "forever", 20, 21, 2019)

    root = Node(first_devise)

    print("Start adding nodes to the binary tree...")
    root.insert_by_device_brand(second_device)
    root.insert_by_device_brand(third_device)
    root.insert_by_device_brand(fourth_device)
    root.insert_by_device_brand(fifth_device)
    root.insert_by_device_brand(sixth_device)
    root.insert_by_device_brand(seven_device)
    root.insert_by_device_brand(eight_device)
    root.insert_by_device_brand(nine_device)
    root.insert_by_device_brand(ten_device)
    print("Adding nodes to the binary tree is complete!")
    print("")

    print("The binary tree has the form:")
    root.print_tree()
    print("")

    minimum_measurement = 21
    print(f"Output of all nodes with a measurement limit not lower than {minimum_measurement}:")
    root.output_by_minimum_measurement(minimum_measurement)
    print("")

    print("Bypassing the tree 'from top to bottom':")
    print(root.preorder_traversal(root))
    print("")

    root.delete_by_graduation_year(2022)
    print("Removal of all nodes with a given year of issue: ")
    root.print_tree()


if __name__ == '__main__':
    creation_and_realization_of_a_tree()
