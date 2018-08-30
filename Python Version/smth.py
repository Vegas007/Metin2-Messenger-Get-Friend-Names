def GetFriendNames(self):
	import uiMessenger
	friendNamesList = []

	if self.interface:
		if self.interface.wndMessenger:
			for group in self.interface.wndMessenger.groupList[uiMessenger.FRIEND]:
				memberList = group.GetMemberList()[:]
				if memberList:
					for member in memberList:
						friendNamesList.append(member.GetName())

	return tuple(friendNamesList)