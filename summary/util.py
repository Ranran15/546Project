# --  LICENSE file in the root directory of this source tree. An additional grant
# --  of patent rights can be found in the PATENTS file in the same directory.
# --
# --  Author: Alexander M Rush <srush@seas.harvard.edu>
# --          Sumit Chopra <spchopra@fb.com>
# --          Jason Weston <jase@fb.com>

# -- The utility tool box
import random
util = {}

def string_shortfloat(t):
    return '%2.4g'.format(t)


# function util.string_shortfloat(t)
#     return string.format('%2.4g', t)
# end

def shuffleTable(t):
    rand = random.random()
    iterations = len(t)
    for i in range(iterations-1,1,-1):
        j = random.randint(0,i)
        t[i],t[j] = t[j], t[i]

# function util.shuffleTable(t)
#     local rand = math.random
#     local iterations = #t
#     local j
#     for i = iterations, 2, -1 do
#        j = rand(i)
#        t[i], t[j] = t[j], t[i]
#     end
# end

def string_split(s, c=None):
    if not c:
        c=' '
    temp = s.split(c)
    return [x for x in temp if x]
#print(string_split("helloworld",'l'))
# function util.string_split(s, c)
#    if c==nil then c=' ' end
#    local t={}
#    while true do
#        local f=s:find(c)
#        if f==nil then
#            if s:len()>0 then
#                table.insert(t, s)
#            end
#            break
#        end
#        if f > 1 then
#           table.insert(t, s:sub(1,f-1))
#        end
#        s=s:sub(f+1,s:len())
#    end
#    return t
# end

def add(t,key):
    cur = t
    for i in range(len(key)):
        if key[i] not in new_cur:
            cur[key[i]]={}
            new_cur = cur[key[i]]
        cur = new_cur
    cur[key[len(key)-1]]=True

# function util.add(tab, key)
#    local cur = tab

#    for i = 1, #key-1 do
#       local new_cur = cur[key[i]]
#       if new_cur == nil then
#          cur[key[i]] = {}
#          new_cur = cur[key[i]]
#       end
#       cur = new_cur
#    end
#    cur[key[#key]] = true
# end

def has(t,key):
    cur = t
    for i in range(len(key)):
        if not (key[i] in cur):
            return False
    return True

# print(has({1:1,2:2,3:3},[2,3]))
# print(has({1:1,2:2,3:3},[2,4]))
# function util.has(tab, key)
#    local cur = tab
#    for i = 1, #key do
#       cur = cur[key[i]]
#       if cur == nil then
#          return false
#       end
#    end
#    return true
# end

def isnan(x):
    return x!=x
# function util.isnan(x)
#     return x ~= x
# end

# return util
