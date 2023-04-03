def function(k,n):
    if n == k:
        return
    else:
        function(k+1, n)

function(0,2)