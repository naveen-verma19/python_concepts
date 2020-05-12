s={1,2,3,4,5}
s2={1,3,5}

union=s.union(s2) #or s|s2

intersect=s.intersection(s2) # or s&s2

xor=s^s2 #elements either in s or in s2 but not in both

(s|s2) - (s&s2)==s^s2  #True

s>=s2 #True  s2 is subset of s
