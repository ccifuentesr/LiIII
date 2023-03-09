#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ccifuentesr
"""

import numpy as np
import pandas as pd
import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.ticker import FormatStrFormatter
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import rc
import scipy.stats as st

plt.rc('font', family='Helvetica')
rc('font', **{'family': 'Helvetica'})
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.rcParams.update({'font.family':'Helvetica'})

# =============================================================================
# DATA
# =============================================================================

data = 'Data/Llo22.v05.csv'
df = pd.read_csv(data, sep=",", header=0)

#
condition1 = (df['sum_Mp'] >= 1) & (df['a_au'] <= 0.2)
condition2 = (df['Porb_d'] <= df['Prot_d']) & (df['a_au'] <= 0.2)
condition3 = (df['Porb_d'] > df['Prot_d']) & (df['a_au'] <= 0.2)
condition4 = (df['logOD'] <= -0.3)

#
Teff_Y = df[df['Pl'] == 'Y']['Teff_K']
eTeff_Y = df[df['Pl'] == 'Y']['eTeff_K']
A_Li_Y = df[df['Pl'] == 'Y']['A(Li)']
vsini_Y = df[df['Pl'] == 'Y']['vsini']
Fe_H_Y = df[df['Pl'] == 'Y']['[Fe/H]']
eFe_H_Y = df[df['Pl'] == 'Y']['e[Fe/H]']
logRHK_Y = df[df['Pl'] == 'Y']['logRHK']
M_Y = df[df['Pl'] == 'Y']['M_Msol']
#
Teff_N = df[df['Pl'] == 'N']['Teff_K']
eTeff_N = df[df['Pl'] == 'N']['eTeff_K']
A_Li_N = df[df['Pl'] == 'N']['A(Li)']
vsini_N = df[df['Pl'] == 'N']['vsini']
Fe_H_N = df[df['Pl'] == 'N']['[Fe/H]']
eFe_H_N = df[df['Pl'] == 'N']['e[Fe/H]']
logRHK_N = df[df['Pl'] == 'N']['logRHK']
M_N = df[df['Pl'] == 'N']['M_Msol']

#
Teff_Y_1 = df[(df['Pl'] == 'Y') & condition1]['Teff_K']
Teff_N_1 = df[(df['Pl'] == 'N') & condition1]['Teff_K']
A_Li_Y_1 = df[(df['Pl'] == 'Y') & condition1]['A(Li)']
A_Li_N_1 = df[(df['Pl'] == 'N') & condition1]['A(Li)']
Fe_H_Y_1 = df[(df['Pl'] == 'Y') & condition1]['[Fe/H]']
Fe_H_N_1 = df[(df['Pl'] == 'N') & condition1]['[Fe/H]']
#
Teff_Y_2 = df[(df['Pl'] == 'Y') & condition2]['Teff_K']
Teff_N_2 = df[(df['Pl'] == 'N') & condition2]['Teff_K']
A_Li_Y_2 = df[(df['Pl'] == 'Y') & condition2]['A(Li)']
A_Li_N_2 = df[(df['Pl'] == 'N') & condition2]['A(Li)']
Fe_H_Y_2 = df[(df['Pl'] == 'Y') & condition2]['[Fe/H]']
Fe_H_N_2 = df[(df['Pl'] == 'N') & condition2]['[Fe/H]']
#
Teff_Y_3 = df[(df['Pl'] == 'Y') & condition3]['Teff_K']
Teff_N_3 = df[(df['Pl'] == 'N') & condition3]['Teff_K']
A_Li_Y_3 = df[(df['Pl'] == 'Y') & condition3]['A(Li)']
A_Li_N_3 = df[(df['Pl'] == 'N') & condition3]['A(Li)']
Fe_H_Y_3 = df[(df['Pl'] == 'Y') & condition3]['[Fe/H]']
Fe_H_N_3 = df[(df['Pl'] == 'N') & condition3]['[Fe/H]']
#
A_Li_Y_4 = df[(df['Pl'] == 'Y') & condition4]['A(Li)']
A_Li_N_4 = df[(df['Pl'] == 'N') & condition4]['A(Li)']
M_Y_1 = df[(df['Pl'] == 'Y') & condition4]['M_Msol']
M_N_1 = df[(df['Pl'] == 'N') & condition4]['M_Msol']
#
N_planets = df[df['Pl'] == 'Y']['N_planets']
sum_Mp_Y = df[df['Pl'] == 'Y']['sum_Mp']
a_au = df['a_au']
Porb_d = df['Porb_d']
logOD = df['logOD']
# Figure 7
vsini_Y_bis = df[(df['logOD'] != 'Nan') & condition2]['vsini']
logOD_bis = df[(df['logOD'] != 'Nan') & condition2]['logOD']


# =============================================================================
# PLOT
# =============================================================================

figure = 8 # Choose figure here
subfigure = 2 # Choose figure here
#
def plot_fig(figure, subfigure):
    figsize = (12, 10)
    pointsize = 32
    linewidth = 3
    elinewidth = 2
    tickssize = 22
    labelsize = 22
    legendsize = 18
    cblabsize = 18
    #
    fig, ax = plt.subplots(figsize=figsize)
    palette = 'coolwarm'
    cmap = plt.get_cmap(palette)
    #
    if figure == 1:
        x = Teff_Y
        y = A_Li_Y
        xlabel = r'$T_{\rm eff}$ (K)'
        ylabel = r'A (Li)'
        colourbar = 'yes'
        #
        if subfigure == 1:
            plotname= 'Teff_ALi_FeH_N'
            zlabel = r'[Fe/H]'
            #
            x = Teff_N
            y = A_Li_N
            z = Fe_H_N
        if subfigure == 2:
            plotname= 'Teff_ALi_FeH_Y'
            zlabel = r'[Fe/H]'
            #
            x = Teff_Y
            y = A_Li_Y
            z = Fe_H_Y
        if subfigure == 3:
            plotname= 'Teff_ALi_vsini_N'
            zlabel = r'$v\sin{i}$ [km s$^{-1}$]'
            #
            x = Teff_N
            y = A_Li_N
            z = vsini_N
        if subfigure == 4:
            plotname= 'Teff_ALi_vsini_Y'
            zlabel = r'$v\sin{i}$ [km s$^{-1}$]'
            #
            x = Teff_Y
            y = A_Li_Y
            z = vsini_Y
        if subfigure == 5:
            plotname= 'Teff_ALi_logR_N'
            zlabel = r'$\log{R}_{HK}$]'
            #
            x = Teff_N
            y = A_Li_N
            z = logRHK_N
        if subfigure == 6:
            plotname= 'Teff_ALi_logR_Y'
            zlabel = r'$\log{R}_{HK}$]'
            #
            x = Teff_Y
            y = A_Li_Y
            z = logRHK_Y
        #
        sc = ax.scatter(x, y, marker='o', c=z, cmap=cmap, s=pointsize)
        #
    if figure == 2:
        if subfigure == 1:
            plotname= 'logR_ALi'
            xlabel = r'$\log{R}_{HK}$'
            ylabel = r'A (Li)'
            colourbar = 'no'
            #
            x1 = logRHK_Y
            x2 = logRHK_N
            y1 = A_Li_Y
            y2 = A_Li_N
            #
            ax.scatter(x1, y1, marker='o', color='red', s=pointsize, zorder=1)
            ax.scatter(x2, y2, marker='o', color='cornflowerblue', s=pointsize, zorder=0)
        if subfigure == 2:
            plotname= 'logR_vsini'
            ylabel = r'$\log{R}_{HK}$'
            xlabel = r'$v\sin{i}$ (km s$^{-1}$)'
            colourbar = 'no'
            #
            y1 = logRHK_Y
            y2 = logRHK_N
            x1 = vsini_Y
            x2 = vsini_N
            #
            ax.scatter(x2, y2, marker='o', color='cornflowerblue', s=pointsize)
            ax.scatter(x1, y1, marker='o', color='red', s=pointsize, zorder=2)
            ax.set_xlim(0, 15)
            plt.axvline(x=5, color='black', linestyle='--', linewidth=2.5, zorder=1)
    if figure == 3:
        if subfigure == 1:
            plotname= 'sumMp_FeH'
            xlabel = r'$\sum{M_p}$ (M$_{\rm Jup}$)'
            ylabel = r'[Fe/H]'
            zlabel = r'Number of planets'
            colourbar = 'no'
            #
            x = sum_Mp_Y
            y = Fe_H_Y
            s = N_planets*35
            #
            sc = ax.scatter(x, y, marker='o', c='r', s=s)
            plt.axvline(x = 1, color='k', linestyle='dashed', linewidth=2.5)
            ax.set_xlim(-0.1, 11.5)
        if subfigure == 2:
            plotname= 'sumMp_ALi'
            xlabel = r'$\sum{M_p}$ (M$_{\rm Jup}$)'
            ylabel = r'A (Li)'
            zlabel = r'Number of planets'
            colourbar = 'no'
            #
            x = sum_Mp_Y
            y = A_Li_Y
            s = N_planets*35
            #
            sc = ax.scatter(x, y, marker='o', c='r', s=s)
            plt.axvline(x = 1, color='k', linestyle='dashed', linewidth=2.5)
        if subfigure == 3:
            plotname= 'sumNp_FeH'
            xlabel = r'Number of planets'
            ylabel = r'[Fe/H]'
            zlabel = r'$\sum{M_p}$ (M$_{\rm Jup}$)'
            colourbar = 'no'
            #
            x = N_planets
            y = Fe_H_Y
            s = sum_Mp*40
            #
            ax.scatter(x, y, marker='o', c='None', edgecolors='b', s=s)
            plt.axvline(x = 1, color='k', linestyle='dashed', linewidth=2.5)
    if figure == 4:
        if subfigure == 1:
            plotname= 'Teff_ALi'
            xlabel = r'$T_{\rm eff}$ (K)'
            ylabel = r'A(Li)'
            colourbar = 'no'
            #
            x1 = Teff_Y
            y1 = A_Li_Y
            x2 = Teff_N
            y2 = A_Li_N
            #
            ax.scatter(x1, y1, marker='o', color='red', s=pointsize*2, zorder=1)
            ax.scatter(x2, y2, marker='o', color='cornflowerblue', s=pointsize*2, zorder=0)
    if figure == 5:
        if subfigure == 1:
            plotname= 'FeH_ALi'
            xlabel = r'[Fe/H]'
            ylabel = r'A(Li)'
            colourbar = 'no'
            #
            x1a = Fe_H_Y_2
            x1b = Fe_H_Y_3
            y1a = A_Li_Y_2
            y1b = A_Li_Y_3
            x2 = Fe_H_N_3
            y2 = A_Li_N_3
            #
            ax.scatter(x1a, y1a, marker='o', color='magenta', s=pointsize*2, zorder=2)
            ax.scatter(x1b, y1b, marker='o', color='orange', s=pointsize*2, zorder=1)
            ax.scatter(x2, y2, marker='o', color='gainsboro', s=pointsize*2, zorder=0)
            plt.axhline(y=1.5, color='grey', linestyle='--', zorder=0)
    if figure == 6:
        if subfigure == 1:
            plotname= 'Teff_ALi_bis'
            xlabel = r'$T_{\rm eff}$ (K)'
            ylabel = r'A(Li)'
            colourbar = 'no'
            x = Teff_Y
            y = A_Li_Y
            #
            x1a = Teff_Y_2
            x1b = Teff_Y_3
            y1a = A_Li_Y_2
            y1b = A_Li_Y_3
            #
            # x2a = Teff_N_3a
            # x2b = Teff_N_3b
            # y2a = A_Li_N_3a
            # y2b = A_Li_N_3b
            #
            ax.scatter(x1a, y1a, marker='o', color='cornflowerblue', s=pointsize*3)
            ax.scatter(x1b, y1b, marker='o', color='red', s=pointsize*3)
            ax.scatter(x, y, marker='o', color='gainsboro', s=pointsize*3, zorder=0)
            # ax.scatter(x2a, y2a, marker='o', edgecolors='magenta', color='None', s=pointsize*3)
            # ax.scatter(x2b, y2b, marker='o', edgecolors='orange', color='None', s=pointsize*3)
            #
    if figure == 7:
        if subfigure == 1:
            plotname= 'vsini_logOD'
            xlabel = r'$v\sin{i}$ (km s$^{-1}$)'
            ylabel = r'$\log{OD}$ (Ga)'
            colourbar = 'no'
            #
            x1 = vsini_Y_bis
            y1 = logOD_bis
            #
            ax.scatter(x1, y1, marker='o', color='red', s=pointsize*2, zorder=1)
            ax.set_xlim(0,8)
    if figure == 8:
        if subfigure == 1:
            plotname= 'M_ALi_bis'
            xlabel = r'$M$ (M$_\odot$)'
            ylabel = r'A(Li)'
            colourbar = 'no'
            #
            x1 = M_Y
            y1 = A_Li_Y
            x2 = M_N
            y2 = A_Li_N
            #
            ax.scatter(x1, y1, marker='o', color='red', s=pointsize*2, zorder=1)
            ax.scatter(x2, y2, marker='o', color='cornflowerblue', s=pointsize*2, zorder=0)
            #
            ax.set_xlim(0.7, 1.6)
        if subfigure == 2:
            plotname= 'M_ALi_bis'
            xlabel = r'$M$ (M$_\odot$)'
            ylabel = r'A(Li)'
            colourbar = 'no'
            #
            x1 = M_Y_1
            y1 = A_Li_Y_4
            x2 = M_N_1
            y2 = A_Li_N_4
            #
            ax.scatter(x1, y1, marker='o', color='red', s=pointsize*4, zorder=1)
            ax.scatter(x2, y2, marker='o', color='cornflowerblue', s=pointsize*4, zorder=0)
            #
            ax.set_xlim(0.7, 1.6)
    if figure == 9:
        if subfigure == 1:
            plotname= 'FeH_PI_bis'
            xlabel = r'[Fe/H]'
            ylabel = r'$\Pi$'
            colourbar = 'no'
            #
            # Make a random dataset:
            height = [3.3, 2.0, 2.3, 1.7, 1.2, 1.0]
            height2 = [0 , 0, 1.0, 1.2, 1.7, 1.6]
            bars = ('[-0.7, -0.5]', '[-0.5, -0.3]', '[-0.3, -0.1]', '[-0.1, 0.1]', '[0.1, 0.3]', '[0.3, 0.5]')
            y_pos = np.arange(len(bars))

            # Create bars
            # ax.bar(y_pos, height, color='maroon')
            ax.bar(y_pos, height2, color='lightcoral')

            # Create names on the x-axis
            plt.xticks(y_pos, bars)

            # Show graphic
            # plt.show()
            #
            # ax.scatter(x1, y1, marker='o', color='red', s=pointsize*2, zorder=1)
            # ax.scatter(x2, y2, marker='o', color='cornflowerblue', s=pointsize*2, zorder=0)
            # #
            # ax.set_xlim(0.77, 1.6)
    ax.tick_params(axis='x', labelsize=tickssize, direction='in',
                    top=True, labeltop=False, which='both')
    ax.tick_params(axis='y', labelsize=tickssize, direction='in',
                    right=True, labelright=False, which='both')
    ax.tick_params('both', length=10, width=1, which='major')
    ax.tick_params('both', length=5, width=1, which='minor')
    ax.xaxis.set_tick_params(which='minor', bottom=True, top=True)
    ax.minorticks_on()
    ax.set_xlabel(xlabel, size=labelsize)
    ax.set_ylabel(ylabel, size=labelsize)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    #
    if colourbar == 'yes':
        # norm = matplotlib.colors.Normalize(vmin=min(z), vmax=max(z), clip=True)
        # mapper = matplotlib.cm.ScalarMappable(norm=norm, cmap=palette)
        # color = np.array([(mapper.to_rgba(v)) for v in z])
        plt.sca(ax)
        divider = make_axes_locatable(plt.gca())
        cax = divider.append_axes("right", "2%", pad="1%")
        cbar = plt.colorbar(sc, cax=cax)  # Colorbar
        cbar.set_label(zlabel, rotation=270, fontsize=labelsize, labelpad=30)
        # sc.set_clim(vmin=min(z), vmax=max(z))
        cbar.ax.tick_params(labelsize=cblabsize)
        cbar.outline.set_visible(False)
    plt.savefig('plot_'+plotname+'.pdf', bbox_inches='tight')
    plt.show()


plot_fig(figure, subfigure)
