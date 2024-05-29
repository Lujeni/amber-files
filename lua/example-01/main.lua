-- Basic Syntax and Functions
function greeting(name)
    if name then
        return "Hello, " .. name .. "!"
    else
        return "Hello, World!"
    end
end

-- Tables (Lua's data structure)
function table_example()
    local fruits = {"apple", "banana", "cherry"}
    table.insert(fruits, "date")
    for i, fruit in ipairs(fruits) do
        print(i, fruit)
    end
end

-- Loops and Conditionals
function loop_example()
    for i = 1, 5 do
        if i % 2 == 0 then
            print(i .. " is even")
        else
            print(i .. " is odd")
        end
    end
end

-- Metatables
function metatable_example()
    local mt = {
        __add = function(t1, t2)
            return t1.value + t2.value
        end
    }

    local t1 = {value = 10}
    local t2 = {value = 20}
    setmetatable(t1, mt)
    setmetatable(t2, mt)

    local sum = t1 + t2
    print("Sum of t1 and t2: " .. sum)
end

-- Coroutines
function coroutine_example()
    local co = coroutine.create(function()
        for i = 1, 5 do
            print("Coroutine: " .. i)
            coroutine.yield()
        end
    end)

    for i = 1, 5 do
        print("Main: " .. i)
        coroutine.resume(co)
    end
end
