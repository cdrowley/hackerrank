-- https://www.hackerrank.com/challenges/binary-search-tree-1/
select N,
    case
        when P is null then "Root"
        when n in (
            select p
            from bst
        ) then "Inner"
        else "Leaf"
    end
from bst
order by n;