% calculates choose n from m
function y = Choose(n,m)
if n>= m
    y = Fact(n)/ (Fact(m) * Fact(n-m));
end
return