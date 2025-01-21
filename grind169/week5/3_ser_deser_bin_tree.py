# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(
            self,
            x,
            left: Optional['TreeNode'] = None,
            right: Optional['TreeNode'] = None,
    ):
        self.val = x
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "_"

        return self.preorder_serial(root, 0)

    def preorder_serial(self, node: Optional[TreeNode], idx: int):
        if node is None:
            return "_"

        return f"({node.val},{idx},{idx}l{self.preorder_serial(node.left, idx * 2 + 1)},{idx}r{self.preorder_serial(node.right, idx * 2 + 2)})"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "_":
            return None

        return self.preorder_deserial(data)

    def preorder_deserial(self, data: str):
        if data == "_":
            return None

        data = data[1:-1]
        first_com = data.find(",")
        second_com = data.find(",", first_com + 1)
        val = int(data[:first_com])
        idx = data[first_com + 1:second_com]
        left_sep = f",{idx}l"
        left_start = data.find(left_sep)
        right_sep = f",{idx}r"
        right_start = data.find(right_sep)

        node = TreeNode(val)
        node.left = self.preorder_deserial(data[left_start + len(left_sep):right_start])
        node.right = self.preorder_deserial(data[right_start + len(right_sep):])
        return node


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
if __name__ == '__main__':
    ser = Codec()
    deser = Codec()
    # ans = deser.deserialize(ser.serialize(TreeNode(
    #     1,
    #     left=TreeNode(2),
    #     right=TreeNode(3, TreeNode(4), TreeNode(5))
    # )))
    # print(ans.right.val)

    serialized = ser.serialize(TreeNode(
        1,
        left=TreeNode(2),
        right=TreeNode(
            3,
            right=TreeNode(5),
            left=TreeNode(
                4,
                left=TreeNode(6),
                right=TreeNode(7)
            ),
        )
    ))
    print(serialized)
    ans = deser.deserialize(serialized)
    print(ans.right.left.right.val)

    print(ser.serialize(None))
    # ans = deser.deserialize(serialized)
    # print(ans.right.left.right.val)

    serialized = ser.serialize(TreeNode(
        1,
        left=TreeNode(
            10,
            left=TreeNode(9, right=TreeNode(8, left=TreeNode(7, right=TreeNode(6, left=TreeNode(5, right=TreeNode(4,
                                                                                                                  left=TreeNode(
                                                                                                                      3,
                                                                                                                      right=TreeNode(
                                                                                                                          2,
                                                                                                                          left=TreeNode(
                                                                                                                              1))))))))),
            right=TreeNode(11, left=(TreeNode(12, right=TreeNode(13, left=TreeNode(14, right=TreeNode(15,
                                                                                                      left=TreeNode(16,
                                                                                                                    right=TreeNode(
                                                                                                                        17,
                                                                                                                        left=TreeNode(
                                                                                                                            18,
                                                                                                                            right=TreeNode(
                                                                                                                                19))))))))))
        )
    ))
    print(serialized)
