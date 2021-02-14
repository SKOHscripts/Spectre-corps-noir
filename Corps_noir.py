#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@file : Corps_noir - Corentin Michel.py
@brief : Montre l'emittance spectrale du corps noir pour différentes températures.

@author : Corentin MICHEL
'''

import numpy as np
from scipy.constants import *
import matplotlib.pyplot as plt
import matplotlib.pylab as pl

#####################################################
# Liste à changer pour afficher différentes courbes
# Vous povez en mettre autant que vous voulez
# ATENTION: important de les trier par odre croissant
temperatures = [3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000]
#####################################################

#########
# CALCULS
#########

# min et max des longueurs d'onde du visible
min_visible, max_visible = 380, 780

# Constante de Stefan
Stefan = (2 * np.pi**5 * k**4) / (15 * c**2 * h**3)

# Formule de Planck


def Planck(l, T):
    intens = (2 * h * c**2) / ((l**5) *
                               (np.exp((h * c / (l * k * T))) - 1))
    return intens


# On commence à 0.5 mm pour éviter de diviser par zéro
# On va jusqu'à 2.5ym
# tips pour afficher la dernière valeur sur les axes
onde = np.arange(0.5e-9, 2.501e-6, 0.5e-9)

# intnsité
intensity = []
for i in range(len(temperatures)):
    intensity.append(Planck(onde, temperatures[i]))

# determination des pics pour les affichages par la suite
maxx = []
for i in intensity:
    maxx.append(onde[i.argmax()] * 1e9)
maxy = [0]
for i in range(len(temperatures)):
    maxy.append(np.max(intensity[i]))


###############
# PREMIER GRAPH
###############

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(
    20, 10), constrained_layout=True, sharey=True)
ax1 = axs[0]

# couleur des courbes
colors = pl.cm.jet(np.linspace(0, 1, len(temperatures)))

# plot
for i in range(len(temperatures)):
    ax1.plot(onde * 1e9, intensity[i],
             label=temperatures[i], color=colors[i])
    ax1.plot(maxx[i], np.max(intensity[i]), 'ko',
             alpha=0.5)  # plot des max
ax1.plot(maxx[-1], np.max(intensity[-1]), 'ko',
         alpha=0.5, label='$\lambda_{max}$')  # dernier plot des max pour la légende
ax1.legend(loc='best', title='Températures (°K)')  # légende

# lignes pour les zones de longueurs d'ondes
ax1.axvline(min_visible, c='k', ls='--', lw='1')
ax1.axvline(max_visible, c='k', ls='--', lw='1')
# texte pour les zones
bbox = dict(boxstyle="round", fc="0.8", alpha=0.8)
ax1.text(50, maxy[-1], 'Ultraviolet', color='black',
         bbox=bbox, fontsize=10)
ax1.text(500, maxy[-1], 'Visible', color='black',
         bbox=bbox, fontsize=10)
ax1.text(850, maxy[-1], 'Infrarouge', color='black',
         bbox=bbox, fontsize=10)

# axes setup
ax1.set_xlabel("Longueur d'onde $\lambda\ (nm)$")
ax1.set_ylabel('Intensité $(x10^{13}\ W/m^3)$')
fig.suptitle('Emittance spectrale du corps noir',
             fontsize=20, fontweight='bold', fontname='Ubuntu')
ax1.set_title('Tout le spectre', fontsize=12,
              fontweight='bold', fontname='Ubuntu')
ax1.set_xticks([0, 2500], minor=True)
for tick in ax1.xaxis.get_major_ticks():
    tick.label.set_fontsize(10)
    tick.label.set_rotation(45)  # afin d'éviter de supperposer
ax1.set_yticks(maxy)
for tick in ax1.yaxis.get_major_ticks():
    tick.label.set_fontsize(10)

# pas de marges
ax1.margins(0)

# grille
ax1.grid(which='both', alpha=0.5, linestyle='-')


################
# DEUXIEME GRAPH
################

ax2 = axs[1]

# plot
for i in range(len(temperatures)):
    plt.plot(onde * 1e9, intensity[i],
             label=(temperatures[i]), color=colors[i])
    ax2.plot(maxx[i], np.max(intensity[i]), 'ko', alpha=0.5)
    ax2.axvline(maxx[i], color="k", alpha=0.3)


# lignes pour les zones de longueurs d'ondes
ax2.axvline(min_visible, c='k', ls='--', lw='1')
ax2.axvline(max_visible, c='k', ls='--', lw='1')

# axes setup
ax2.set_xlim((maxx[-1] - 50, maxx[0] + 50))
ax2.set_xlabel("Longueur d'onde $\lambda\ (nm)$")
ax2.set_title('Zoom autours des extremums',
              fontsize=12, fontweight='bold', fontname='Ubuntu')
ax2.set_xticks(maxx)
for tick in ax2.xaxis.get_major_ticks():
    tick.label.set_fontsize(10)
    tick.label.set_rotation(45)  # afin d'éviter de supperposer

# grille
ax2.grid(which='both', alpha=0.5, linestyle='-')


###############################
# spectre du Visible
###############################
ax1.axvspan(380, 400, facecolor='#760043', alpha=0.8)
ax1.axvspan(400, 420, facecolor='#FF00C8', alpha=0.8)
ax1.axvspan(420, 440, facecolor='#D200E9', alpha=0.8)
ax1.axvspan(440, 460, facecolor='#6F00F6', alpha=0.8)
ax1.axvspan(460, 480, facecolor='#5100FF', alpha=0.8)
ax1.axvspan(480, 500, facecolor='#00E9FF', alpha=0.8)
ax1.axvspan(500, 520, facecolor='#00E085', alpha=0.8)
ax1.axvspan(520, 540, facecolor='#00C940', alpha=0.8)
ax1.axvspan(540, 560, facecolor='#00DC27', alpha=0.8)
ax1.axvspan(560, 580, facecolor='#B3FF18', alpha=0.8)
ax1.axvspan(580, 600, facecolor='#F8FF0B', alpha=0.8)
ax1.axvspan(600, 620, facecolor='#FF9100', alpha=0.8)
ax1.axvspan(620, 640, facecolor='#FF5200', alpha=0.8)
ax1.axvspan(640, 700, facecolor='#FF0000', alpha=0.8)
ax1.axvspan(700, 780, facecolor='#840000', alpha=0.8)

ax2.axvspan(380, 400, facecolor='#760043', alpha=0.8)
ax2.axvspan(400, 420, facecolor='#FF00C8', alpha=0.8)
ax2.axvspan(420, 440, facecolor='#D200E9', alpha=0.8)
ax2.axvspan(440, 460, facecolor='#6F00F6', alpha=0.8)
ax2.axvspan(460, 480, facecolor='#5100FF', alpha=0.8)
ax2.axvspan(480, 500, facecolor='#00E9FF', alpha=0.8)
ax2.axvspan(500, 520, facecolor='#00E085', alpha=0.8)
ax2.axvspan(520, 540, facecolor='#00C940', alpha=0.8)
ax2.axvspan(540, 560, facecolor='#00DC27', alpha=0.8)
ax2.axvspan(560, 580, facecolor='#B3FF18', alpha=0.8)
ax2.axvspan(580, 600, facecolor='#F8FF0B', alpha=0.8)
ax2.axvspan(600, 620, facecolor='#FF9100', alpha=0.8)
ax2.axvspan(620, 640, facecolor='#FF5200', alpha=0.8)
ax2.axvspan(640, 700, facecolor='#FF0000', alpha=0.8)
ax2.axvspan(700, 780, facecolor='#840000', alpha=0.8)

#######################
# sauvegarder une image
#######################
fig.savefig('Corps_Noir - Corentin MICHEL.png', bbox_inches='tight', dpi=300)

# show the plot
plt.show()
