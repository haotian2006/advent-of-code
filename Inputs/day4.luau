local inputString = ""--require("file")[1]
local inputTable = inputString:split('\n')
local Utils = require("Libraries/Utils")
local print = Utils.print
local iter = Utils.iter
local create = Utils.create
--[[
    for i,v in inputTable do

    end
]]
local function prompt1()
    local t = create(inputTable, function(i, v:string)
        local cards = v:split(':')
        return cards[2]:split('|')
    end)
    local cards = {

    }
    for index,Values in t do
        local ii = 0
        for i,v in string.gmatch(Values[2],"%d+" ) do
            if string.find(Values[1], ` {i} `) then
                ii+=1
            end
        end
        cards[index] = cards[index] or 0
        cards[index] +=1
        for _=1,cards[index] do
            for b = index +1,index +ii do
                if t[b] ~= nil then
                    cards[b] = cards[b] or 0
                    cards[b] +=1
                end
            end
        end
    end
    print(cards)
    print(Utils.sum(cards))
end

local function prompt2()
    
end
prompt1()
prompt2()