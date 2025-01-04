local ReplicatedStorage = game:GetService("ReplicatedStorage")

local UpdateGuiEvent = ReplicatedStorage.Remotes:WaitForChild("UpdateGui")

local FormatNumber = require(ReplicatedStorage.Libs.FormatNumber:WaitForChild("Simple"))

local player = game.Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")

-- Reference the actual GUI from the player's PlayerGui, not StarterGui
local frame = playerGui:WaitForChild("Currency"):WaitForChild("Frame"):WaitForChild("Frame")
local Upgrades = playerGui:WaitForChild("Upgrades"):WaitForChild("Frame")

local CashAmount = frame:WaitForChild("Cash"):WaitForChild("Amount")
local CookieAmount = frame:WaitForChild("Cookies"):WaitForChild("Amount")
local CookiesPerSec = frame:WaitForChild("CookiesGain"):WaitForChild("Amount")
local CookiesDeliveringPerSec = frame:WaitForChild("CookiesDelivering"):WaitForChild("Amount")

local StorageCost = Upgrades:WaitForChild("Frame"):WaitForChild("Storage"):WaitForChild("Frame"):WaitForChild("Cost")
local DeliveryCost = Upgrades:WaitForChild("Frame"):WaitForChild("Delivery"):WaitForChild("Frame"):WaitForChild("Cost")
local SellCost = Upgrades:WaitForChild("Frame"):WaitForChild("Sell"):WaitForChild("Frame"):WaitForChild("Cost")
local CookieCost = Upgrades:WaitForChild("Frame"):WaitForChild("Cookie"):WaitForChild("Frame"):WaitForChild("Cost")
local ChefCost = Upgrades:WaitForChild("Frame"):WaitForChild("Chef"):WaitForChild("Frame"):WaitForChild("Cost")
local DriverCost = Upgrades:WaitForChild("Frame"):WaitForChild("Drivers"):WaitForChild("Frame"):WaitForChild("Cost")

local player = game.Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")

-- Reference the actual GUI from the player's PlayerGui, not StarterGui
local frame2 = playerGui:WaitForChild("Upgrades"):WaitForChild("Frame")

frame2.Visible = false 

UpdateGuiEvent.OnClientEvent:Connect(function()
	print("Recieved")
	local leaderstats = player:FindFirstChild("leaderstats")
	if leaderstats then
		local cookies = leaderstats:FindFirstChild("cookies")
		local cash = leaderstats:FindFirstChild("cash")
		local backpackSize = player:FindFirstChild("backpackSize")
		local deliveryCapacity = player:FindFirstChild("deliveryCapacity")
		local sellMultiplier = player:FindFirstChild("sellMultiplier")
		local cookieMultiplier = player:FindFirstChild("cookieMultiplier")
		local chefLevel = player:FindFirstChild("chefLevel")
		local driverLevel = player:FindFirstChild("driverLevel")

		if cookies and cash then
			CashAmount.Text = FormatNumber.FormatCompact(cash.Value)
			CookieAmount.Text = FormatNumber.FormatCompact(cookies.Value) .. " / " .. FormatNumber.FormatCompact(backpackSize.Value)
			CookiesPerSec.Text = "Making " .. FormatNumber.FormatCompact(chefLevel.Value) .. " Cookies/S"
			CookiesDeliveringPerSec.Text = "Delivering " .. FormatNumber.FormatCompact(driverLevel.Value) .. " Cookies/S"
			StorageCost.Text = "£" .. FormatNumber.FormatCompact(backpackSize.Value * 3) .. " : " .. FormatNumber.FormatCompact(backpackSize.Value)
			DeliveryCost.Text = "£" .. FormatNumber.FormatCompact(deliveryCapacity.Value * 30) .. " : " .. FormatNumber.FormatCompact(deliveryCapacity.Value)
			SellCost.Text = "£" .. FormatNumber.FormatCompact(sellMultiplier.Value * 250) .. " : " .. FormatNumber.FormatCompact(sellMultiplier.Value)
			CookieCost.Text = "£" .. FormatNumber.FormatCompact(cookieMultiplier.Value * 200) .. " : " .. FormatNumber.FormatCompact(cookieMultiplier.Value)
			ChefCost.Text = "£" .. FormatNumber.FormatCompact((chefLevel.Value + 1) * 1000) .. " : " .. FormatNumber.FormatCompact(chefLevel.Value)
			DriverCost.Text = "£" .. FormatNumber.FormatCompact((driverLevel.Value + 1) * 1000) .. " : " .. FormatNumber.FormatCompact(driverLevel.Value)
		end
	end
end)
