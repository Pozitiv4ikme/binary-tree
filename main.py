from device import Device
from binary_tree_node import Node


def creation_and_realization_of_a_tree():
    print("Start adding nodes to the binary tree...")
    list_of_device = [
        Device(),
        Device("ammeter", "VA-1 red", 200, 1000, 2021),
        Device("digital multimeter", "DT9205A", 746, 2000, 2019),
        Device("digital voltmeter", "VD9032-R", 10, 32, 2022),
        Device("some device", "nEARTH9f-0", 100, 125, 1999),
        Device("another device", "1fGHY56 blue", 1000, 10000, 2045),
        Device("new device", "nmscomfc-1.0", 5, 10, 2022),
        Device("eight device", "love", 26, 102, 2022),
        Device("Number nine", "love", 134, 102, 2022),
        Device("TenTaSion", "forever", 20, 21, 2019)
    ]

    root = Node(list_of_device[0])
    for i in range(1, len(list_of_device)):
        root.insert_by_device_brand(list_of_device[i])

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
