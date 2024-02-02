-- float point precision up to 13 digits
-- you cannot use shorthand notations with += 1 and ++ and whatever
-- check which operations you can use, they come from the math library

-- Generate random numbers
math.randomseed(os.time())
io.write('math.random() : ', math.random(), '\n')
io.write('math.random(10) : ', math.random(10), '\n')
io.write('math.random(5,100) : ', math.random(5,100), '\n')

print(string.format('Pi = %.10f', math.pi))


-- Conditional statements
-- Relational operators: > < ... == ~=
-- Locical operators: and or not
-- there are not switches

age = 13
if age < 16 then
	io.write('you can go to schol\n')
	local localVar = 10
elseif (age <= 16) and (age < 18) then
	io.write('you can trige\n')
else
	io.write('you can drive\n')
end

-- Some casting 
print(string.format('not true = %s', tostring(not true)))

-- There is not ternary operator! But we can knock it of like this
canvote = age > 16 and true or false

local someString = 'a;isudfasdfasdf iu safd iu asdf ladsf asdf haliusdhf '
io.write('Quote lenght ', #someString ,'\n')
io.write('Replace sud with asdf:', string.gsub(someString, 'sud', 'asdf'), '\n')
io.write('index of password: ', string.find(someString, 'asdf'), '\n')
io.write('String upper: ', string.upper(someString), '\n')
io.write('String lower: ', string.lower(someString), '\n')


-- LOOPING: THERE IS NOT CONTINUE STATEMENT??
local i = 1
while (i<10) do
	io.write(i)
	i = i + 1
	if i == 8 then
		io.write('\n')
		break
	end
end

io.write('Guess the number (its 15)\n')
repeat
	break
	io.write('Enter your guess: ')
	guess = io.read()
until tonumber(guess) == 15


-- TABLE INDEXING STARTS AT ONE????
local someTable = {}
for i=1, 10, 1 do
	someTable[i] = i
end
for key, value in pairs(someTable) do
	io.write(key, ' ', value, '\n')
end

print('First item:', someTable[1])
print('Number of items:', #someTable)
table.insert(someTable, 1, 0)
print('First item:', someTable[1])
print(table.concat(someTable, ',')) -- this is so cool, btw it makes it printable!
table.remove(someTable, 1) -- removed the index, not the element
print(table.concat(someTable, ' '))


local multiTable = {}
for i=0, 9 do
	multiTable[i] = {}
	for j=0, 0 do
		multiTable[i][j] = tostring(i) .. tostring(j) -- WHAT IS THIS?
	end
end

print('Multi Table[0][0]: ', multiTable[0][0])


-- functions, ayyyyyy
function someFun(n, m)
	return n + m
end

function splitStr(str)
	local stringTable = {}
	local i = 1
	for s in string.gmatch(str, '[^%s]+') do-- this is regex matching study this
		stringTable[i] = s
		i = i + 1
	end
	return stringTable, i
end

local splitStrTable, numOfStr = splitStr('ciao sono una stringa molto stupida etc')

for j=1, numOfStr - 1 do -- notice the little -1
	print(string.format('%d : %s', j, splitStrTable[j]))
end

function getSumMore(...) -- variadic function!
	local sum = 0
	for k, v in pairs{...} do -- notice pairs is unpacking, and { } is casting
		sum = sum + v
	end
	return sum
end

print('Sum ', getSumMore(1,2,3,4))

-- A function is an object so you can assign it to a variable
doubleit = function(x) return x * 2 end
print(doubleit(4))

-- CLOSURES (spicy): a function that can access local variables of an enclosing function
function Outer()
	local i = 0
	return function()
		i = i + 1
		return i
	end
end

getI = Outer()
print(getI()) -- notice that the value of i increments and this gets remembered
print(getI()) -- kinda has the feel of a generator? I have to read more about this for now

-- COROUTINES: they are like threads but they cannot run in parrallel (lol)
co = coroutine.create(function()
	for i=1, 10, 1 do
		print(i)
		print(coroutine.status(co))
		if i == 5 then coroutine.yield() end
	end
end)

print(coroutine.status(co))
coroutine.resume(co)
print(coroutine.status(co))

co2 = coroutine.create(function()
	for i = 101, 110, 1 do print(i) end
end)

coroutine.resume(co2)
coroutine.resume(co)
print(coroutine.status(co))


-- File io!! yay - this looks all the fkn same man
-- r: read only
-- w: overwrite or create a new file
-- a: append or create new
-- r+ read & write existin file
-- w+: oeverwrite read or create a file
-- a+: append read or create

local file = io.open('test.txt', 'w+')
file:write('Random string of text\n')
file:write('Some more text i guess\n')
file:seek('set', 0) -- this command i did not really understand

print(file:read('*a'))
file:close()

file = io.open('text.txt', 'a+')
file:write('even more text\n')
file:seek('set', 0)
print(file:read('*a'))
file:close()


-- FINALLY: MODULES 
local convertModule = require('convert')
print(string.format('%.3f cm', convertModule.ftToCm(12)))

-- Meta-tables (wow wtf)
local atable = {}
for x = 1, 10 do
	atable[x] = x
end

local mt = {
	__add = function(table1, table2) 
		local sumtable = {}
		for y=1, #table1 do
			if (table1[y] ~= nil) and (table2[y] ~= nil) then
				sumtable[y] = table1[y] + table2[y]
			else
				sumTable[y] = 0
			end
		end
		return sumtable
	end,
	__eq = function(table1, table2)
		return table1.value == table2.value
	end
}

setmetatable(atable, mt)
print(atable == atable)
local addtable = atable + atable
print(table.concat(addtable, ' '))


-- Classes knockoff
local animal = {height = 0, weight = 0}
function animal:new(height, weight)
	setmetatable({}, animal)
	self.height = height
	self.weight = weight
	return self
end
function animal:toString()
	animalStr = string.format('weight: %s, height: %s', self.weight, self.height)
	return animalStr
end

spot = animal:new(10, 15)
print(spot:toString())

-- inheritance knockoff, looks a bit like js prototypes or smt like that 
cat = animal:new()
function cat:new(height, weight, food)
	setmetatable({}, cat)
	self.food = food
	self.height = height
	self.weight = weight
	return self
end

fluffy = cat:new(10,10,'ciao')


