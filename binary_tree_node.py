from device import Device


class Node:
    def __init__(self, data: Device):
        self.left = None
        self.right = None
        self.data = data

    def insert_by_device_brand(self, data: Device):
        if self.data:

            if data.brand_of_the_device < self.data.brand_of_the_device:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_by_device_brand(data)

            elif data.brand_of_the_device > self.data.brand_of_the_device:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_by_device_brand(data)

            else:
                self.data = data

    def output_by_minimum_measurement(self, measurement_minimum):
        if self.left:
            self.left.output_by_minimum_measurement(measurement_minimum)
        if self.right:
            self.right.output_by_minimum_measurement(measurement_minimum)
        if self.data.measurement_limit_minimum >= measurement_minimum:
            print(self.data)

    def min_value(self):
        current = self
        pre_current = None
        while current and current.left:
            pre_current = current
            current = current.left

        return current, pre_current

    def delete_by_graduation_year(self, graduation_year):
        if self.left:
            self.left = self.left.delete_by_graduation_year(graduation_year)
        if self.right:
            self.right = self.right.delete_by_graduation_year(graduation_year)
        if self.data.graduation_year == graduation_year:

            if not self.left and not self.right:  # no child
                return None
            elif not self.left:  # only right child
                return self.right
            elif not self.right:  # only left child
                return self.left

            # has 2 child
            temp, recurrent = self.right.minValue()
            if recurrent:
                if temp.right:
                    recurrent.left = temp.right
                else:
                    recurrent.left = None
            else:
                self.right = temp.right
            self.data = temp.data

        return self

    def print_tree(self):
        print(" - ", self.data.type_of_device)
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

    def preorder_traversal(self, root):
        result = []
        if root:
            result.append(root.data.type_of_device)
            result = result + self.preorder_traversal(root.left)
            result = result + self.preorder_traversal(root.right)
        return result

    def __str__(self):
        return "None"
