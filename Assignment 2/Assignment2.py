games_played = [13, 14, 14, 16, 16, 16, 16, 9, 16, 16, 16, 16, 12]

rushing_attempts = [196,311,339,333,369,317,339,148,314,381,324,321,146]

rushing_yards = [679,1390,1852,1395,1610,1460,1222,596,1421,1684,1551,1333,533]

receiving_attempts = [33,15,27,50,31,46,41,32,53,45,49,37,33]

receiving_yards = [213,149,269,480,313,367,379,311,607,368,483,328,217]

touches = [229,326,366,383,400,363,380,180,367,426,373,358,179]

yard_from_scrimmage = [892,1539,2121,1875,1923,1827,1601,907,2028,2052,2034,1661,750]

for ra, ry in zip(rushing_attempts, rushing_yards):
    print(ry/ra)

for ra, ry in zip(receiving_attempts, receiving_yards):
    print(ry/ra)

large = max(touches)
touches.remove(large)

large2 = max(touches)
touches.remove(large2)

large3 = max(touches)
print(large3, large2, large)

h = sum(receiving_yards)
y = sum(yard_from_scrimmage)
print(h / y * 100)

count = 0
for n in receiving_yards:
    if n <= 300:
        count = count + 1
        print(count)