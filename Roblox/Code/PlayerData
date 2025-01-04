-- Services
local DataStoreService = game:GetService("DataStoreService")
local playerDataStore = DataStoreService:GetDataStore("PlayerData_2")

-- Function to create leaderstats and player stats
local function createPlayerStats(player)
	-- Create leaderstats folder for Cash and Cookies
	local leaderstats = Instance.new("Folder")
	leaderstats.Name = "leaderstats"
	leaderstats.Parent = player

	-- Create a 'Cash' stat under leaderstats
	local cash = Instance.new("IntValue")
	cash.Name = "cash"
	cash.Value = 100 -- Default value for new players
	cash.Parent = leaderstats

	-- Create a 'Cookies' stat under leaderstats
	local cookies = Instance.new("IntValue")
	cookies.Name = "cookies"
	cookies.Value = 10 -- Default value for new players
	cookies.Parent = leaderstats

	-- Create other stats directly under the player
	local backpackSize = Instance.new("IntValue")
	backpackSize.Name = "backpackSize"
	backpackSize.Value = 25 -- Default value
	backpackSize.Parent = player

	local sellMultiplier = Instance.new("IntValue")
	sellMultiplier.Name = "sellMultiplier"
	sellMultiplier.Value = 2 -- Default value
	sellMultiplier.Parent = player

	local cookieMultiplier = Instance.new("IntValue")
	cookieMultiplier.Name = "cookieMultiplier"
	cookieMultiplier.Value = 1 -- Default value
	cookieMultiplier.Parent = player

	local deliveryCapacity = Instance.new("IntValue")
	deliveryCapacity.Name = "deliveryCapacity"
	deliveryCapacity.Value = 5 -- Default value
	deliveryCapacity.Parent = player

	local chefLevel = Instance.new("IntValue")
	chefLevel.Name = "chefLevel"
	chefLevel.Value = 1 -- Default value
	chefLevel.Parent = player

	local driverLevel = Instance.new("IntValue")
	driverLevel.Name = "driverLevel"
	driverLevel.Value = 1 -- Default value
	driverLevel.Parent = player

	-- Load player data
	local success, data = pcall(function()
		return playerDataStore:GetAsync(player.UserId)
	end)

	if success and data then
		cash.Value = data.cash or 100
		cookies.Value = data.cookies or 10 
		backpackSize.Value = data.backpackSize or 25
		sellMultiplier.Value = data.sellMultiplier or 1
		cookieMultiplier.Value = data.cookieMultiplier or 1
		deliveryCapacity.Value = data.deliveryCapacity or 5
		chefLevel.Value = data.chefLevel or 0
		driverLevel.Value = data.driverLevel or 0
	else
		warn("Error loading data for player: " .. player.Name)
	end
end

-- Function to save player data
local function savePlayerData(player)
	local leaderstats = player:FindFirstChild("leaderstats")
	if leaderstats then
		local cash = leaderstats:FindFirstChild("cash")
		local cookies = leaderstats:FindFirstChild("cookies")
		local backpackSize = player:FindFirstChild("backpackSize")
		local sellMultiplier = player:FindFirstChild("sellMultiplier")
		local cookieMultiplier = player:FindFirstChild("cookieMultiplier")
		local deliveryCapacity = player:FindFirstChild("deliveryCapacity")
		local chefLevel = player:FindFirstChild("chefLevel")
		local driverLevel = player:FindFirstChild("driverLevel")

		if cash and cookies and backpackSize and sellMultiplier and cookieMultiplier and deliveryCapacity and chefLevel and driverLevel then
			local data = {
				cash = cash.Value,
				cookies = cookies.Value,
				backpackSize = backpackSize.Value,
				sellMultiplier = sellMultiplier.Value,
				cookieMultiplier = cookieMultiplier.Value,
				deliveryCapacity = deliveryCapacity.Value,
				chefLevel = chefLevel.Value,
				driverLevel = driverLevel.Value
			}
			local success, err = pcall(function()
				playerDataStore:SetAsync(player.UserId, data)
			end)

			if not success then
				warn("Error saving data for player: " .. player.Name .. " - " .. err)
			end
		end
	end
end

-- Player Added Event
game.Players.PlayerAdded:Connect(function(player)
	createPlayerStats(player)
end)

-- Player Removing Event (for saving data when player leaves)
game.Players.PlayerRemoving:Connect(function(player)
	savePlayerData(player)
end)

-- If the server shuts down, save player data
game:BindToClose(function()
	for _, player in pairs(game.Players:GetPlayers()) do
		savePlayerData(player)
	end
end)
