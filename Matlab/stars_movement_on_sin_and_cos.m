% حرکت ستاره ها روی نمودار سینوس و کسینوس
clc
clear all
close all

x = 0:.1:2*pi;
for j=1:2
    for R = 1:length(x)
        plot(x,sin(x),x,cos(x))
        hold on
        plot(x(R),sin(x(R)),'r*', x(R),cos(x(R)),'b*')
        pause(0.1)
        hold off
    end
    x = fliplr(x);
end

