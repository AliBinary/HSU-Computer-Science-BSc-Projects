clc
clear all;
close all;

input = linspace(0, 4*pi, 100);
target = sin(input);

figure (1)
plot(input, target, 'o');

[targetMinMax, mapping] = mapminmax(target, 0, 1);

net = newff(input, targetMinMax, 6, {'tansig' 'tansig'});
net = init(net);

net.trainparam.epochs = 200;
net = train(net, input, targetMinMax);

output = sim(net, input);

figure (2)
plot(input, mapminmax('reverse', output, mapping)), hold on
plot(input, sin(input), 'r')

p = linspace(4*pi, 6*pi, 50);
a = sim(net, p);
figure (3)
plot(p, mapminmax('reverse', a, mapping)), hold on
plot(p, sin(p), 'r')