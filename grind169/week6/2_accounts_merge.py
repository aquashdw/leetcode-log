from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.parents = None

    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.parents = [i for i in range(len(accounts))]

        email_owner = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_owner:
                    self.union(i, email_owner[email])
                email_owner[email] = i

        result = defaultdict(list)
        for email, owner in email_owner.items():
            result[self.find(owner)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in result.items()]
