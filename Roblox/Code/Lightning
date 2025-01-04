local strikePart = script.Parent.StormPart
local rnd = Random.new(tick())
local stormSwath = 250
local debris = game:GetService("Debris")
local averageDelay = 10
local beamWdAdj = 100
local startPos = Vector3.new(0,150,-125)

local restrictedAreaMin = Vector3.new(70, 0, -10)
local restrictedAreaMax = Vector3.new(-85, 150, -230)

local function isWithinRestrictedArea(pos)
	return pos.X >= restrictedAreaMin.X and pos.X <= restrictedAreaMax.X and
		pos.Y >= restrictedAreaMin.Y and pos.Y <= restrictedAreaMax.Y and
		pos.Z >= restrictedAreaMin.Z and pos.Z <= restrictedAreaMax.Z
end

local function makeStrike(l_startPos)
	local strikePartClone = strikePart:Clone()
	strikePartClone.Parent = workspace
	strikePartClone.Position = l_startPos
	strikePartClone.StrikeSnd:Play()
	strikePartClone.Beam.Width0 += rnd:NextInteger(0, beamWdAdj)
	strikePartClone.Beam.Width1 += rnd:NextInteger(0, beamWdAdj)
	local stopPos = Vector3.new(l_startPos.X, 10, l_startPos.Z)
	local diff = stopPos - l_startPos
	for i = 1, 5, 1 do
		strikePartClone.Att1.WorldPosition += diff/5
		wait(0)
	end
	wait()
	strikePartClone.Att1.WorldPosition = strikePartClone.Att0.WorldPosition
	debris:AddItem(strikePartClone, strikePartClone.StrikeSnd.TimeLength)
end

while true do
	local xRnd, zRnd
	local newPos

	repeat
		xRnd = rnd:NextInteger(-stormSwath, stormSwath)
		zRnd = rnd:NextInteger(-stormSwath, stormSwath)
		newPos = strikePart.Position + Vector3.new(xRnd, 0, zRnd)
	until not isWithinRestrictedArea(newPos)

	startPos = newPos
	local t = rnd:NextInteger(2, averageDelay)
	wait(t)
	spawn(function()
		makeStrike(startPos)
	end)
end
