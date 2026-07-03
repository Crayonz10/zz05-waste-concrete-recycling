%MAIN_PLOT  Generate five publication-ready figures for the biform game.
%
%   Saves PNG files at 300 dpi into ../figures/.
%   Run from simulation/scripts/.

%% ---------- Style constants (Morandi palette) ----------
CLR_BI_M   = [74, 123, 118] / 255;   % Biform M: Soft Teal
CLR_BI_R   = [91, 123, 154] / 255;   % Biform R: Muted Blue
CLR_NC_M   = [181, 108,  96] / 255;  % Non-coop M: Dusty Rose
CLR_NC_R   = [211, 162, 115] / 255;  % Non-coop R: Warm Sand

LATEX      = 'latex';
FONT_SIZE  = 11;

ALPHA_HIGH = 0.55;                   % transparency for surfaces that often sit above others
ALPHA_LOW  = 0.55;                   % lower-layer transparency to keep upper visible

GRID_N     = 40;                     % meshgrid resolution

OUT_DIR    = fullfile('..', 'figures');
if ~exist(OUT_DIR, 'dir'); mkdir(OUT_DIR); end

% Cross-runtime save (Octave-compatible fallback for exportgraphics)
save_fig = @(name) print(gcf, fullfile(OUT_DIR, name), '-dpng', '-r300');

% Legend in top-left, no title, no surrounding box
make_legend = @(labels) legend(labels, ...
    'Interpreter', LATEX, 'Location', 'northwest', ...
    'Box', 'off', 'FontSize', FONT_SIZE, 'Title', '');

% Apply this AFTER each subplot's plot commands to keep 3D box rectangular
setup_3d_box = @() set(gca, 'Box', 'on', 'BoxStyle', 'full', ...
    'Projection', 'perspective', 'TickLabelInterpreter', LATEX, ...
    'FontSize', FONT_SIZE, 'LineWidth', 0.8);

%% ---------- Figure 1: Profit Comparison (3D, 1x3) ----------
alpha = 1.5; beta = 0.134; m = 32; w = 35; s = 87.5; muM = 25; muR = 44;
c = 135000; theta = 137.5; pc = 65; G = 300; e0 = 0.035; gamma = 0.015;

figure('Position', [80, 80, 1700, 520], 'Color', 'w');

% (a) alpha vs beta
[Ax, Bx] = meshgrid(linspace(1.1, 1.8, GRID_N), linspace(0.05, 0.4, GRID_N));
eq = calculate_equilibrium(Ax, Bx, m, w, s, muM, muR, c, theta, pc, G, e0, gamma);
subplot(1,3,1); hold on;
s1 = surf(Ax, Bx, eq.Pi_M_N, 'FaceColor', CLR_NC_M, 'FaceAlpha', ALPHA_LOW, 'EdgeColor', 'none');
s2 = surf(Ax, Bx, eq.Pi_R_N, 'FaceColor', CLR_NC_R, 'FaceAlpha', ALPHA_LOW, 'EdgeColor', 'none');
s3 = surf(Ax, Bx, eq.phi_M,  'FaceColor', CLR_BI_M, 'FaceAlpha', ALPHA_HIGH, 'EdgeColor', 'none');
s4 = surf(Ax, Bx, eq.phi_R,  'FaceColor', CLR_BI_R, 'FaceAlpha', ALPHA_HIGH, 'EdgeColor', 'none');
xlabel('(a) $\alpha$', 'Interpreter', LATEX); ylabel('$\beta$', 'Interpreter', LATEX); zlabel('Profit', 'Interpreter', LATEX);
grid off; box on; axis vis3d;
camlight('headlight'); lighting gouraud; view(-37.5, 28);
make_legend({'$\Pi_M^{N*}$', '$\Pi_R^{N*}$', '$\varphi_M$', '$\varphi_R$'});

% (b) w vs s
[Wx, Sx] = meshgrid(linspace(20, 60, GRID_N), linspace(50, 120, GRID_N));
eq = calculate_equilibrium(alpha, beta, m, Wx, Sx, muM, muR, c, theta, pc, G, e0, gamma);
subplot(1,3,2); hold on;
surf(Wx, Sx, eq.Pi_M_N, 'FaceColor', CLR_NC_M, 'FaceAlpha', ALPHA_LOW, 'EdgeColor', 'none');
surf(Wx, Sx, eq.Pi_R_N, 'FaceColor', CLR_NC_R, 'FaceAlpha', ALPHA_LOW, 'EdgeColor', 'none');
surf(Wx, Sx, eq.phi_M,  'FaceColor', CLR_BI_M, 'FaceAlpha', ALPHA_HIGH, 'EdgeColor', 'none');
surf(Wx, Sx, eq.phi_R,  'FaceColor', CLR_BI_R, 'FaceAlpha', ALPHA_HIGH, 'EdgeColor', 'none');
xlabel('(b) $w$', 'Interpreter', LATEX); ylabel('$s$', 'Interpreter', LATEX); zlabel('Profit', 'Interpreter', LATEX);
grid off; box on; axis vis3d;
camlight('headlight'); lighting gouraud; view(-37.5, 28);
make_legend({'$\Pi_M^{N*}$', '$\Pi_R^{N*}$', '$\varphi_M$', '$\varphi_R$'});

% (c) theta vs delta_mu
[Tx, DMx] = meshgrid(linspace(100, 200, GRID_N), linspace(5, 40, GRID_N));
eq = calculate_equilibrium(alpha, beta, m, w, s, muM, muM + DMx, c, Tx, pc, G, e0, gamma);
subplot(1,3,3); hold on;
surf(Tx, DMx, eq.Pi_M_N, 'FaceColor', CLR_NC_M, 'FaceAlpha', ALPHA_LOW, 'EdgeColor', 'none');
surf(Tx, DMx, eq.Pi_R_N, 'FaceColor', CLR_NC_R, 'FaceAlpha', ALPHA_LOW, 'EdgeColor', 'none');
surf(Tx, DMx, eq.phi_M,  'FaceColor', CLR_BI_M, 'FaceAlpha', ALPHA_HIGH, 'EdgeColor', 'none');
surf(Tx, DMx, eq.phi_R,  'FaceColor', CLR_BI_R, 'FaceAlpha', ALPHA_HIGH, 'EdgeColor', 'none');
xlabel('(c) $\theta$', 'Interpreter', LATEX); ylabel('$\Delta\mu$', 'Interpreter', LATEX); zlabel('Profit', 'Interpreter', LATEX);
grid off; box on; axis vis3d;
camlight('headlight'); lighting gouraud; view(-37.5, 28);
make_legend({'$\Pi_M^{N*}$', '$\Pi_R^{N*}$', '$\varphi_M$', '$\varphi_R$'});

save_fig('Figure_1.png');

%% ---------- Figure 2: Conversion Rate k (3D, 1x2) ----------
figure('Position', [80, 80, 1200, 540], 'Color', 'w');

% (a) theta vs gamma
[Tx, Gx] = meshgrid(linspace(100, 200, GRID_N), linspace(0, 0.05, GRID_N));
eq = calculate_equilibrium(alpha, beta, m, w, s, muM, muR, c, Tx, pc, G, e0, Gx);
subplot(1,2,1); hold on;
surf(Tx, Gx, eq.k_N, 'FaceColor', CLR_NC_R, 'FaceAlpha', 0.45, 'EdgeColor', 'none');
surf(Tx, Gx, eq.k_C, 'FaceColor', CLR_BI_M, 'FaceAlpha', 0.55, 'EdgeColor', 'none');
xlabel('(a) $\theta$', 'Interpreter', LATEX); ylabel('$\gamma$', 'Interpreter', LATEX); zlabel('$k$', 'Interpreter', LATEX);
grid off; box on; axis vis3d;
camlight('headlight'); lighting gouraud; view(-37.5, 28);
make_legend({'$k^{N*}$', '$k^{C*}$'});

% (b) alpha vs beta
[Ax, Bx] = meshgrid(linspace(1.1, 1.8, GRID_N), linspace(0.05, 0.4, GRID_N));
eq = calculate_equilibrium(Ax, Bx, m, w, s, muM, muR, c, theta, pc, G, e0, gamma);
subplot(1,2,2); hold on;
surf(Ax, Bx, eq.k_N, 'FaceColor', CLR_NC_R, 'FaceAlpha', 0.45, 'EdgeColor', 'none');
surf(Ax, Bx, eq.k_C, 'FaceColor', CLR_BI_M, 'FaceAlpha', 0.55, 'EdgeColor', 'none');
xlabel('(b) $\alpha$', 'Interpreter', LATEX); ylabel('$\beta$', 'Interpreter', LATEX); zlabel('$k$', 'Interpreter', LATEX);
grid off; box on; axis vis3d;
camlight('headlight'); lighting gouraud; view(-37.5, 28);
make_legend({'$k^{N*}$', '$k^{C*}$'});

save_fig('Figure_2.png');

%% ---------- Figure 3: Cap-and-Trade Impact on Profit (3D, 1x2) ----------
figure('Position', [80, 80, 1200, 540], 'Color', 'w');

[Px, E0x] = meshgrid(linspace(0, 120, GRID_N), linspace(0.01, 0.1, GRID_N));
eq = calculate_equilibrium(alpha, beta, m, w, s, muM, muR, c, theta, Px, G, E0x, gamma);

% (a) M's profit
subplot(1,2,1); hold on;
surf(Px, E0x, eq.Pi_M_N, 'FaceColor', CLR_NC_M, 'FaceAlpha', 0.45, 'EdgeColor', 'none');
surf(Px, E0x, eq.phi_M,  'FaceColor', CLR_BI_M, 'FaceAlpha', 0.55, 'EdgeColor', 'none');
xlabel('(a) $p_c$', 'Interpreter', LATEX); ylabel('$e_0$', 'Interpreter', LATEX); zlabel('$\Pi_M$', 'Interpreter', LATEX);
grid off; box on; axis vis3d;
camlight('headlight'); lighting gouraud; view(-37.5, 28);
make_legend({'$\Pi_M^{N*}$', '$\varphi_M$'});

% (b) R's profit
subplot(1,2,2); hold on;
surf(Px, E0x, eq.Pi_R_N, 'FaceColor', CLR_NC_R, 'FaceAlpha', 0.45, 'EdgeColor', 'none');
surf(Px, E0x, eq.phi_R,  'FaceColor', CLR_BI_R, 'FaceAlpha', 0.55, 'EdgeColor', 'none');
xlabel('(b) $p_c$', 'Interpreter', LATEX); ylabel('$e_0$', 'Interpreter', LATEX); zlabel('$\Pi_R$', 'Interpreter', LATEX);
grid off; box on; axis vis3d;
camlight('headlight'); lighting gouraud; view(-37.5, 28);
make_legend({'$\Pi_R^{N*}$', '$\varphi_R$'});

save_fig('Figure_3.png');

%% ---------- Figure 4: Biform Sensitivity to Carbon Price (2D, 1x3) ----------
figure('Position', [80, 80, 1700, 520], 'Color', 'w');

pc_vec = linspace(0, 150, 200);
eq = calculate_equilibrium(alpha, beta, m, w, s, muM, muR, c, theta, pc_vec, G, e0, gamma);

% (a) prices
subplot(1,3,1); hold on; box on; grid off;
plot(pc_vec, eq.pM_C, 'Color', CLR_BI_M, 'LineWidth', 2);
plot(pc_vec, eq.pR_C, 'Color', CLR_BI_R, 'LineWidth', 2);
set(gca, 'TickLabelInterpreter', LATEX, 'FontSize', FONT_SIZE);
xlabel('(a) $p_c$', 'Interpreter', LATEX); ylabel('Price', 'Interpreter', LATEX);
make_legend({'$p_M^{C*}$', '$p_R^{C*}$'});

% (b) quantities
subplot(1,3,2); hold on; box on; grid off;
plot(pc_vec, eq.qM_C,           'Color', CLR_BI_M, 'LineWidth', 2);
plot(pc_vec, eq.qR_C,           'Color', CLR_BI_R, 'LineWidth', 2);
plot(pc_vec, eq.qM_C + eq.qR_C, 'Color', CLR_NC_R, 'LineWidth', 2, 'LineStyle', '--');
set(gca, 'TickLabelInterpreter', LATEX, 'FontSize', FONT_SIZE);
xlabel('(b) $p_c$', 'Interpreter', LATEX); ylabel('Quantity', 'Interpreter', LATEX);
make_legend({'$q_M^{C*}$', '$q_R^{C*}$', '$q_{total}$'});

% (c) n_C and k_C (plotyy for cross-runtime compatibility)
subplot(1,3,3); box on; grid off;
[ax4c, h1c, h2c] = plotyy(pc_vec, eq.n_C, pc_vec, eq.k_C, @plot, @plot);
set(h1c, 'Color', CLR_BI_M, 'LineWidth', 2);
set(h2c, 'Color', CLR_BI_R, 'LineWidth', 2);
set(ax4c(1), 'YColor', CLR_BI_M, 'FontSize', FONT_SIZE, 'TickLabelInterpreter', LATEX);
set(ax4c(2), 'YColor', CLR_BI_R, 'FontSize', FONT_SIZE, 'TickLabelInterpreter', LATEX);
set(ax4c(1), 'XColor', 'k', 'TickLabelInterpreter', LATEX);
xlabel('(c) $p_c$', 'Interpreter', LATEX);
ylabel(ax4c(1), '$n^{C*}$', 'Interpreter', LATEX);
ylabel(ax4c(2), '$k^{C*}$', 'Interpreter', LATEX);
make_legend({'$n^{C*}$', '$k^{C*}$'});

save_fig('Figure_4.png');

%% ---------- Figure 5: Biform Sensitivity to Initial Carbon Emission (2D, 1x3) ----------
figure('Position', [80, 80, 1700, 520], 'Color', 'w');

e0_vec = linspace(0.01, 0.1, 200);
eq = calculate_equilibrium(alpha, beta, m, w, s, muM, muR, c, theta, pc, G, e0_vec, gamma);

% (a) prices
subplot(1,3,1); hold on; box on; grid off;
plot(e0_vec, eq.pM_C, 'Color', CLR_BI_M, 'LineWidth', 2);
plot(e0_vec, eq.pR_C, 'Color', CLR_BI_R, 'LineWidth', 2);
set(gca, 'TickLabelInterpreter', LATEX, 'FontSize', FONT_SIZE);
xlabel('(a) $e_0$', 'Interpreter', LATEX); ylabel('Price', 'Interpreter', LATEX);
make_legend({'$p_M^{C*}$', '$p_R^{C*}$'});

% (b) quantities
subplot(1,3,2); hold on; box on; grid off;
plot(e0_vec, eq.qM_C,           'Color', CLR_BI_M, 'LineWidth', 2);
plot(e0_vec, eq.qR_C,           'Color', CLR_BI_R, 'LineWidth', 2);
plot(e0_vec, eq.qM_C + eq.qR_C, 'Color', CLR_NC_R, 'LineWidth', 2, 'LineStyle', '--');
set(gca, 'TickLabelInterpreter', LATEX, 'FontSize', FONT_SIZE);
xlabel('(b) $e_0$', 'Interpreter', LATEX); ylabel('Quantity', 'Interpreter', LATEX);
make_legend({'$q_M^{C*}$', '$q_R^{C*}$', '$q_{total}$'});

% (c) n_C and k_C (plotyy for cross-runtime compatibility)
subplot(1,3,3); box on; grid off;
[ax5c, h1c, h2c] = plotyy(e0_vec, eq.n_C, e0_vec, eq.k_C, @plot, @plot);
set(h1c, 'Color', CLR_BI_M, 'LineWidth', 2);
set(h2c, 'Color', CLR_BI_R, 'LineWidth', 2);
set(ax5c(1), 'YColor', CLR_BI_M, 'FontSize', FONT_SIZE, 'TickLabelInterpreter', LATEX);
set(ax5c(2), 'YColor', CLR_BI_R, 'FontSize', FONT_SIZE, 'TickLabelInterpreter', LATEX);
set(ax5c(1), 'XColor', 'k', 'TickLabelInterpreter', LATEX);
xlabel('(c) $e_0$', 'Interpreter', LATEX);
ylabel(ax5c(1), '$n^{C*}$', 'Interpreter', LATEX);
ylabel(ax5c(2), '$k^{C*}$', 'Interpreter', LATEX);
make_legend({'$n^{C*}$', '$k^{C*}$'});

save_fig('Figure_5.png');

fprintf('All figures saved to %s\n', OUT_DIR);
