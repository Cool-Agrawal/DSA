class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        a = 0
        if len(v1) > len(v2):
            a = len(v1) - len(v2)
            for i in range(a):
                v2.append(0)
        else:
            a = len(v2) - len(v1)
            for i in range(a):
                v1.append(0)

        flag = 0

        for i in range(len(v1)):
            if int(v1[i]) < int(v2[i]):
                flag =  -1
                return -1
            elif int(v1[i]) > int(v2[i]):
                flag = 1
                return 1
            else:
                flag = 0
                print(0)

        return flag