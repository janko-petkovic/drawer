local lfs = require 'lfs'


local plugins = {}


for file in lfs.dir('.') do
  if
    file ~= 'init.lua' and
    file ~= '.' and
    file ~= '..' then
      local filename = string.gsub(file, '.lua', '')
      local mod = require(filename)
      table.insert(plugins, mod)
    end
end

for k,v in pairs(plugins) do
  print(k, v)
end
