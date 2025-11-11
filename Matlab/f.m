function f()
x = 0:.01:5;
y = log(x).*sin(x);
plot(x,y)

hold on
[i,id] = max(y);
sprintf('maximum point is: %f',i)
plot(x(id),y(id),'ro')
