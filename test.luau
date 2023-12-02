local data = require("file")[1]:split('\n')
local Utils = require("Libraries/Utils")
local print = Utils.print
local iter = Utils.iter

print(Utils.create("1t2d3aa3", function(i,v)
    return tonumber(v)
end))

for i,v in iter({1,2,3,4}) do
    print(i,v)
end
