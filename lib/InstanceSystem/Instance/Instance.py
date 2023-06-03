class Instance:
    def __init__(self, InstanceUUID):
        self.MCJVM = None
        self.Information = ""
        self.MCWindowTitle = self.InstanceName
        self.RAMSetting = "AUTO"

        self.RAMLimit = 4096
        self.InstanceAbsolutePath = None
        self.InstanceName = None
        self.InstanceUUID = InstanceUUID

    @property
    def getInstanceUUID(self):
        return self.InstanceUUID

    @property
    def getInstanceName(self):
        return self.InstanceName

    def setInstanceName(self, newInstanceName):
        self.InstanceName = newInstanceName

    @property
    def getInstanceAbsolutePath(self):
        return self.InstanceAbsolutePath

    def setInstanceAbsolutePath(self, InstanceAbsolutePath):
        self.InstanceAbsolutePath = InstanceAbsolutePath

    @property
    def getRAMSetting(self):
        return self.RAMSetting

    def setRAMSetting(self, RAMSetting):
        self.RAMSetting = RAMSetting

    @property
    def getRAMLimit(self):
        if self.RAMSetting == "AUTO":
            return 0
        else:
            return self.RAMLimit

    def setRAMLimit(self, RAMLimit):
        if self.RAMSetting == "AUTO":
            raise TypeError(self.InstanceName + "出现了错误：内存设置为自动但传入内存上限")
        else:
            self.RAMLimit = RAMLimit

    @property
    def getMCWindowTitle(self):
        return self.MCWindowTitle

    def setMCWindowTitle(self, Title):
        self.MCWindowTitle = Title

    @property
    def getMCCustomInformation(self):
        return self.Information

    def setMCCustomInformation(self, Information):
        self.Information = Information

    @property
    def getMCJVM(self):
        return self.MCJVM

    def setMCJVM(self, MCJVM):
        self.MCJVM = MCJVM
