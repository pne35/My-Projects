local module = {}

local ServerScriptService = game:GetService("ServerScriptService")
local SellModule = require(ServerScriptService.Modules:WaitForChild("ModifyCash")) -- Adjust the path if needed

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local UpdateGuiEvent = ReplicatedStorage.Remotes:WaitForChild("UpdateGui")

function module.sell(player)
	local leaderstats = player:FindFirstChild("leaderstats")
	if leaderstats then
		local cookies = leaderstats:FindFirstChild("cookies")

		-- Access sellMultiplier directly from the player
		local sellMultiplier = player:FindFirstChild("sellMultiplier")
		local deliveryCapacity = player:FindFirstChild("deliveryCapacity")

		if cookies and sellMultiplier then
			if cookies.Value >= deliveryCapacity.Value then
				-- Use the module function to modify cash
				SellModule.modifyCash(player, deliveryCapacity.Value * sellMultiplier.Value)
				-- Set cookies to 0 after the transaction
				cookies.Value = cookies.Value - deliveryCapacity.Value
			else
				-- Handle the case when cookies is greater than deliveryCapacity
				SellModule.modifyCash(player, cookies.Value * sellMultiplier.Value)
				-- Set cookies to 0 after the transaction
				cookies.Value = 0
			end
			
			UpdateGuiEvent:FireClient(player) -- Fire the RemoteEvent to the player
		end
	end
end

return module
