local Utils = {}
local wordNums = {
    ["zero"] = "0",
    ["one"] = "1",
    ["two"] = "2",
    ["three"] = "3",
    ["four"] = "4",
    ["five"] = "5",
    ["six"] = "6",
    ["seven"] = "7",
    ["eight"] = "8",
    ["nine"] = "9",
}

Utils.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
--//Tables
function Utils.create(iterable,func:(i:any,v:any)->boolean)
    local t = {}
    for i,v in Utils.iter(iterable) do
        if func then
            local value = func(i,v)
            if not value then continue end 
            table.insert(t,value)
        elseif not func then
            table.insert(t,v)
        end
    end
    return t
end

function Utils.reverse(tbl)
    local reversed = {}
    local n = #tbl
    for i = n, 1, -1 do
        table.insert(reversed, tbl[i])
    end
    return reversed
end

function Utils.slice(tbl,starti,endi)
    local sliced = {}
    starti = starti or 1
    endi = endi or #tbl
    if starti < 0 then
        starti = #tbl + starti + 1
    end
    if endi < 0 then
        endi = #tbl + endi + 1
    end
    starti = math.max(1, starti)
    endi = math.min(#tbl, endi)
    table.move(tbl, starti, endi, 1, sliced)
    return sliced
end

function Utils.map(t:{},f:(x:any)->(any))
    for i,v in t do
        t[i] = f(v)
    end
    return t 
end
function Utils.sum(t:{[number]:number})
    local sum = 0
    for i,v in t do
        sum += v
    end
    return sum
end
function Utils.min(t:{[number]:number})
    return math.min(table.unpack(t))
end
function Utils.max(t:{[number]:number})
    return  math.max(table.unpack(t))
end
function Utils.combine(...:{[number]:any})
    local new = {}
    for i,v in {...} do
        table.insert(new,v)
    end
    return new
end

function Utils.print(...)
    local function printFormattedTable(tbl, indent)
        indent = indent or 0
        local output = "{\n"
        for k, v in tbl do
            local keyStr = tostring(k)
            local valueStr = ""
            local valueType = type(v)
    
            if valueType == "table" then
                valueStr = printFormattedTable(v, indent + 1)
            elseif valueType == "string" then
                valueStr = '"' .. tostring(v) .. '"'
            else
                valueStr = tostring(v)
            end
            output = output .. string.rep("    ", indent) .. keyStr .. " = " .. valueStr .. ",\n"
        end
        output = output .. string.rep("    ", indent - 1) .. "}"
        return output
    end
    local str = ""
    for i,v in {...} do
        if type(v) == "table" then
            str = printFormattedTable(v,1) .. '\n'
        else
            str ..= tostring(v)..' '
        end
    end
    print(str)
end
--//Other
function iterHelper (a, i)
    i = i + 1
    local v = a[i]
    if v ~= nil then
        return i, v
    end
    return 
end

function Utils.iter(x)
    if type(x) =="table" then 
        if x[1] then
            return iterHelper,x,0
        else
            return next,x 
        end
    elseif type(x) =="string" then
        return iterHelper,x:split(""),0
    end   
    error("Given Type cannot be iterable")
end
local function helperAllIter(x)
    return type(x) == "string" or type(x) =="table"
end
function Utils.allIterable(x)
    for i,v in x do
        if not helperAllIter(v) then return false end 
    end
    return true 
end

function Utils.round(x,to)
    to = to or 0
    return math.round(x*10^to)/10^to
end

function Utils.eval(str)
    local fx = loadstring(`return {str}`)
    return  fx and fx()
end

--//Strings
function Utils.ord(char)
    return string.byte(char)
end

function Utils.chr(byte)
    return string.char(byte)
end

function Utils.replaceWordNums(str)
    for word, num in pairs(wordNums) do
        str = str:gsub(word, num)
    end
    return str
end


--//Math
function Utils.gcd(a, b)
    while b ~= 0 do
        a, b = b, a % b
    end
    return a
end

function Utils.lcm(a, b)
    return (a * b) / Utils.gcd(a, b)
end

function Utils.factorial(n)
    if n == 0 then
        return 1
    else
        return n * Utils.factorial(n - 1)
    end
end

function Utils.is_prime(n)
    if n <= 1 then return false end
    for i = 2, math.sqrt(n) do
        if n % i == 0 then
            return false
        end
    end
    return true
end

function Utils.combinations(n, r)
    if r == 0 or n == r then
        return 1
    else
        return Utils.factorial(n) / (Utils.factorial(r) * Utils.factorial(n - r))
    end
end
return table.freeze(Utils)