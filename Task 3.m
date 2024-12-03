% MATLAB Code for Pi/4-QPSK Modulation, Demodulation with AWGN, and Analytical BER
% Parameters
numSymbols = 1000; % Number of symbols
M = 4; % Modulation order for QPSK
EbNo_dB = 0:2:20; % SNR values in dB
% Generate random bit stream
data = randi([0 3], numSymbols, 1); % 2 bits per symbol for QPSK
% Define modulation and demodulation objects
hMod = comm.PSKModulator('ModulationOrder', M, 'PhaseOffset', pi/4, 'SymbolMapping', 'Gray');
hDemod = comm.PSKDemodulator('ModulationOrder', M, 'PhaseOffset', pi/4, 'SymbolMapping', 'Gray');
% BER calculation
BER_simulated = zeros(length(EbNo_dB), 1);
BER_theoretical = zeros(length(EbNo_dB), 1);
% Loop over different Eb/No values
for i = 1:length(EbNo_dB)
   % Modulate the data
   txSignal = step(hMod, data);
   % Pass through AWGN channel
   rxSignal = awgn(txSignal, EbNo_dB(i), 'measured');
   % Demodulate the received signal
   rxData = step(hDemod, rxSignal);
   % Calculate simulated BER
   [~, BER_simulated(i)] = biterr(data, rxData);
   % Calculate theoretical BER for pi/4-QPSK
   EbNo_linear = 10^(EbNo_dB(i)/10); % Convert Eb/No from dB to linear
   BER_theoretical(i) = 2 * qfunc(sqrt(2 * EbNo_linear)) / log2(M); % Theoretical BER for QPSK
end
% Plot constellation for received signal at a specific SNR
scatterplot(rxSignal);
title(['Received Constellation at SNR = ' num2str(10) ' dB']);
grid on;
% Eye Diagram
eyediagram(real(rxSignal), 2);
title('Eye Diagram of Received Signal');
% Plot BER vs. Eb/No
figure;
semilogy(EbNo_dB, BER_simulated, '-o', 'DisplayName', 'Simulated BER');
hold on;
semilogy(EbNo_dB, BER_theoretical, '-x', 'DisplayName', 'Theoretical BER');
xlabel('Eb/No (dB)');
ylabel('Bit Error Rate (BER)');
title('BER vs. Eb/No for \pi/4-QPSK');
legend('Location', 'southwest');
grid on;
hold off;
