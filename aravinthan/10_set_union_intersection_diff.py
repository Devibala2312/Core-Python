def findUnionIntersectionDiff(input1, input2):
    return {
        'union': input1 | input2,
        'intersection': input1 & input2,
        'diff(AB)': input1 - input2,
        'diff(BA)': input2 - input1
    }
    
print(findUnionIntersectionDiff({1,3,4},{3,5,6,7}))