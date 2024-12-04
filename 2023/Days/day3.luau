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
local dir ={
    {1,1},{-1,-1},{0,1},{1,0},{-1,0},{0,-1},{1,-1},{-1,1}
}

local function prompt()
    local arry = {{}}
    local function find(r,c)
        local pass = false
        for i,v in dir do
            local lr,lc = r +v[1], c+v[2]
            local e,val = pcall(function(...) return arry[lr][lc] end)
            if not e or not val then continue end 
            if string.match(val, "%p") and val ~= '.' then
                pass = true
                break
            end
        end
        return pass
    end
    for r,row in inputTable do
        for c,col in iter(row) do
            arry[r] =  arry[r]or {}
            arry[r][c] = col
        end
    end
    local sum = 0
    for r,str2 in inputTable do
        local num,p = "",false
        for c,chr in iter(str2) do
            if tonumber(chr) then
                num ..= chr
                if find(r, c) then
                    p = true
                end
            else
                if p then 
                    sum += tonumber(num)
                end
                num = ""
                p = false
            end
        end
    end
    --print(sum)
end

