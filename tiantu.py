from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
from astropy import units as u
import numpy as np


def dot(ra, dec, color='k', markersize=2):
	plt.gca()
	c = SkyCoord(ra, dec, frame='icrs')
	plt.plot(c.ra.wrap_at(180*u.deg).radian, c.dec.radian, linestyle='none', 
			 marker='+', markersize=markersize, color=color)


def area(ra, dec, ra_error, dec_error, color='blue'):
	ax = plt.gca()
	c = SkyCoord(ra, dec, frame='icrs')
	c_error = SkyCoord(ra_error, dec_error, frame='icrs')
	ell = Ellipse(xy=(c.ra.wrap_at(180*u.deg).radian, c.dec.radian), width=c_error.ra.radian * 2, height=c_error.dec.radian * 2, angle=0.0, facecolor=color, alpha=0.3)
	ax.add_patch(ell)


def circle(ra, dec, ra_error, dec_error, color='r'):
	theta = np.arange(0, 2*np.pi, np.pi/50)
	c = SkyCoord(ra, dec, frame='icrs')
	c_error = SkyCoord(ra_error, dec_error, frame='icrs')
	x0 = c.ra.wrap_at(180*u.deg).radian
	y0 = c.dec.radian
	a = c_error.ra.radian
	b = c_error.dec.radian
	x = x0 + a * np.cos(theta)
	y = y0 + b * np.sin(theta)
	plt.plot(x, y, linestyle='none', 
			 marker='.', markersize=0.05, color=color)