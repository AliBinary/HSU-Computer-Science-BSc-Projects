function [Y,F] = Example(P,A)
Y = polyval(P,A);

for i=1:size(A,1)
    for j=1:size(A,2)
        F(i,j) = fact(A(i,j));
    end
end

function y = fact(n)
p=1;
for i=2:n
    p = p *i;
end
y = p;
return