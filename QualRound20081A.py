import sys
def bestEngine(QueryArray, startIndex, EngineSet):
    engineSetCopy = set(EngineSet)  # Copy the search Engine Set to allow changes without loss of data
    while startIndex < len(QueryArray) and len(engineSetCopy) > 0:  # Iterate through all queries processed or 0 engines
        if QueryArray[startIndex] in engineSetCopy:
            engineSetCopy.remove(QueryArray[startIndex])  # Remove search engines from the EngineSet until 1 remains
        startIndex += 1
    if startIndex == len(QueryArray):  # We have iterated through the entire QueryArray without further changes.
        if len(engineSetCopy) == 0:  # Covers the case where we had to transition on last element
            return 1
        return 0
    return 1 + bestEngine(QueryArray, startIndex-1, EngineSet)  # Otherwise increment the transitions call recursively


sys.setrecursionlimit(3000)
t = int(input())
outfile = open("1Aout", 'w')
for i in range(1, t+1):
    Engines = set({})
    for j in range(1, int(input())+1):
        Engines.add(str(input()))
    Queries = []
    for k in range(1, int(input())+1):
        Queries.append(str(input()))
    transitions = bestEngine(Queries, 0, Engines)
    outfile.write("Case #%d: %d\n" % (i, transitions))
outfile.close()
