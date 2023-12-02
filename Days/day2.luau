local inputString = require("Inputs/day2_Input")[1]
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
    local target = {
        red = 12,
        green = 13,
        blue = 14
    }
    local sum = 0
    for i,str in inputTable do
        local colors = {
            red = 0,
            green = 0,
            blue = 0
        }
        local possible = true
        local split1 = str:split(':')
        local gamenum = split1[1]:split(' ')[2]
        local split2 = split1[2]:split(';')
        for _,section in split2 do
            local colorT = section:split(',')
            for _,color in colorT do
                local _,count,c = unpack(color:split(" "))
                colors[c] += tonumber(count)
                if tonumber(count) > target[c] then
                    possible = false
                    break
                end
            end
        end
        if not possible then continue end 
        sum += tonumber(gamenum)
    end
    print(sum)
end

local function prompt2()
    local target = {
        red = 12,
        green = 13,
        blue = 14
    }
    local sum = 0
    for i,str in inputTable do
        local colors = {
            red = 0,
            green = 0,
            blue = 0
        }
        local possible = true
        local split1 = str:split(':')
        local gamenum = split1[1]:split(' ')[2]
        local split2 = split1[2]:split(';')
        for _,section in split2 do
            local colorT = section:split(',')
            for _,color in colorT do
                local _,count,c = unpack(color:split(" "))
                if colors[c] < tonumber(count) then
                    colors[c] = tonumber(count)
                end
            end
        end
        mul = 1;
        for i,v in colors do
            mul*=v
        end
        sum+= mul
    end
    print(sum)
end
--prompt1()
prompt2()