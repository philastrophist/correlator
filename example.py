import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
from statsmodels.stats.moment_helpers import corr2cov

from correlator.estimation import find_mode

N = 1000

#### assume there is a slight correlation between x and redshift
corr = np.zeros((3, 3))
labels = ['z', 'x', 'mass']
# correlation coefficients
corr[0, 1] = 0.5  # redshift, x
corr[0, 2] = 0.3  # redshift, mass
corr[1, 2] = 0.5  # x, mass

corr = corr + corr.T + np.eye(3)

std = [0.2, 0.01, 2]  # stds for redshift, x
cov = corr2cov(corr, std)  # covariance

mu = [1., 0., 10.]  # centre for correlation gaussian (not much meaning here unless you convert to a line)

data = np.random.multivariate_normal(mu, cov, size=1000) # sample it
data_covariances = None

#### No controlling
from correlator.correlation import CorrelationModel

correlation = CorrelationModel('correlation', labels, data)
correlation.sample(50)
correlation.traceplot()

from chainconsumer import ChainConsumer
fig = ChainConsumer()
fig.add_chain(data, labels, 'data')
samples = np.random.multivariate_normal(correlation.best_fit['mu'], correlation.best_fit['Sigma'], size=1000)
fig.add_chain(samples, labels, 'bestfit')
fig.plotter.plot()
plt.suptitle("Total correlation - no controlling")
print("Best Fit correlation coefficients:")
print(["{:.2f} (+{:.2f}/-{:.2f})".format(v, *abs(v-hpd)) for v, hpd in zip(correlation.best_fit['corr_coeffs'], correlation.best_fit_hpd['corr_coeffs'].T)])

### Control for mass

from correlator.linear import LinearRelation

with pm.Model() as global_model:
    x_mass = LinearRelation('x_mass', ['x', 'mass'], data[:, 1:])
    z_mass = LinearRelation('z_mass', ['z', 'mass'], data[:, [0, 2]])
    correlation = CorrelationModel('correlation', labels, data, controlling_relations=[x_mass, z_mass])
    trace = pm.sample(100, cores=2)  # unfortunately have to revert to pymc3 syntax here, working on a patch

pm.traceplot(trace, ['correlation_corr_coeffs'])
# correlation coefficients should be reduced for x-mass, and z-mass
# However, since we generated this from a multivariate gaussian with no other things happening, z-x should remain roughly the same

hpd = find_mode(trace)  # dictionary of [best fit, highest-posterior-density region]

best_fits, regions = hpd['correlation_corr_coeffs']
