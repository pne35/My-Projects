local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local introStart = ReplicatedStorage:WaitForChild("IntroStart")
local campfireDetection = ReplicatedStorage:WaitForChild("CampfireEnterDetection")
local ruinDetection = ReplicatedStorage:WaitForChild("RuinFound")

local player = Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")
local dialogueGui = playerGui:WaitForChild("IntroGui")
local frame = dialogueGui:WaitForChild("Frame")
--local imageLabel = frame:WaitForChild("ImageLabel")
local textLabel = frame:WaitForChild("TextBox")

--local function getPlayerThumbnail(userId)
--	local thumbType = Enum.ThumbnailType.HeadShot
--	local thumbSize = Enum.ThumbnailSize.Size420x420
--	local content, isReady = Players:GetUserThumbnailAsync(userId, thumbType, thumbSize)
--	return content
--end

local dialogues1 = {
	{userId = player.UserId, text = "This island has been haunted for years."},
	{userId = player.UserId, text = "It's your job to find out what is on the island."}
}

local dialogues2 = {
	{userId = player.UserId, text = "What... Was that"},
	{userId = player.UserId, text = "I must just be seeing things."}
}

local dialogues3 = {
	{userId = player.UserId, text = "This.."},
	{userId = player.UserId, text = "This ruin's magical."}
}

-- Separate variables to track the current dialogue index for each sequence
local currentDialogueIndex1 = 1
local currentDialogueIndex2 = 0
local currentDialogueIndex3 = 0

local function showDialogue(dialogue, index)
	local currentDialogueData = dialogue[index]
	local text = currentDialogueData.text
	--imageLabel.Image = getPlayerThumbnail(currentDialogueData.userId)
	dialogueGui.Enabled = true

	for i = 1, #text do
		textLabel.Text = string.sub(text, 1, i)
		wait(0.05)
	end
end

local function hideDialogue()
	dialogueGui.Enabled = false
end

local function nextDialogue(dialogue, indexVar)
	if indexVar == "currentDialogueIndex1" then
		currentDialogueIndex1 = currentDialogueIndex1 + 1
		if currentDialogueIndex1 <= #dialogue then
			textLabel.TextColor3 = Color3.new(0.517647, 0.105882, 0.113725)
			showDialogue(dialogue, currentDialogueIndex1)
		else
			hideDialogue()
		end
	elseif indexVar == "currentDialogueIndex2" then
		currentDialogueIndex2 = currentDialogueIndex2 + 1
		if currentDialogueIndex2 <= #dialogue then
			textLabel.TextColor3 = Color3.new(0, 0, 0)
			showDialogue(dialogue, currentDialogueIndex2)
		else
			hideDialogue()
		end
	elseif indexVar == "currentDialogueIndex3" then
		currentDialogueIndex3 = currentDialogueIndex3 + 1
		if currentDialogueIndex3 <= #dialogue then
			textLabel.TextColor3 = Color3.new(1, 1, 1)
			showDialogue(dialogue, currentDialogueIndex3)
		else
			hideDialogue()
		end
	end
end

-- Listen for the introStart event to start the dialogue
introStart.OnClientEvent:Connect(function()
	currentDialogueIndex1 = 1
	showDialogue(dialogues1, currentDialogueIndex1)
	wait(7)
	nextDialogue(dialogues1, "currentDialogueIndex1")
	wait(3)
	hideDialogue()
end)

campfireDetection.OnClientEvent:Connect(function()
	wait(5)
	nextDialogue(dialogues2, "currentDialogueIndex2")
	wait(2)
	nextDialogue(dialogues2, "currentDialogueIndex2")
	wait(2)
	hideDialogue()
end)

ruinDetection.OnClientEvent:Connect(function()
	nextDialogue(dialogues3, "currentDialogueIndex3")
	wait(2)
	nextDialogue(dialogues3, "currentDialogueIndex3")
	wait(2)
	hideDialogue()
end)
