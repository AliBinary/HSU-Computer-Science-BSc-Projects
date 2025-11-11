function [y,t] = S(a)
y = sum(diag(a));

temp = a(1,:);
a(1,:) = a(size(a,1),:);
a(size(a,1),:) = temp;

temp = a(:,1);
a(:, 1) = a(:, size(a,2));
a(:, size(a,2)) = temp;

t = a;