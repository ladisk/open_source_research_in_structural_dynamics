import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

def show_modal_data(nat_freq, damping):
    """
    Show modal data in a table-like structure.
    """
    print('   Nat. f.      Damping')
    print(23*'-')
    for i, f in enumerate(nat_freq):
        print(f'{i+1}) {f:6.1f}\t{damping[i]:5.4f}')
        

def plot_mode_shape(shape, axis, style='o-', frequency=None, **kwargs):
    """
    Plot a mode shape in a consistent fashion.
    """
    plot = axis.plot(shape / np.max(np.abs(shape)) * np.sign(shape[0]), 
                     style, **kwargs)
    if frequency is not None:
        axis.set_title(f'Mode shape - {frequency:.0f} Hz')
    axis.set_yticks([])
    plt.tight_layout()


def show_reconstructed(freq, acc, FRF, frf_rec, select_loc=0):
    """
    Split code from visualization to fit the presentation view.
    """
    freq_a = acc.freq

    plt.subplot(211)

    plt.semilogy(freq, np.abs(FRF[select_loc]), label='Experiment')
    plt.semilogy(freq_a, np.abs(frf_rec[select_loc]),'--', label='LSCF')
    plt.xlim(0,freq[-1])
    plt.ylabel(r"abs($\alpha$)")

    plt.legend(loc = 'best')

    plt.subplot(212)
    plt.plot(freq, np.angle(FRF[select_loc],deg = 1), label='Experiment')
    plt.plot(freq_a, np.angle(frf_rec[select_loc],deg = 1),'--',label='LSCF')
    plt.xlim(0,freq[-1])

    plt.ylabel(r"angle($\alpha$)")
    plt.legend(loc = 'best')


def show_lighting(x0, video_light):
    """
    Interactively visualize an example of poorly illuminated video.
    """
    y0 = 9 
    d = 20
    roi = video_light.mraw[0, y0:y0+d, x0:x0+d*2]
    fig, ax = plt.subplots(2)
    ax[0].imshow(video_light.mraw[0], cmap='gray')
    ax[1].hist(roi.flatten(), bins=50);
    # Formating
    ax[0].add_patch(patches.Rectangle((x0, y0), d*2, d, fill=False, color='r', linewidth=2))
    ax[0].grid(False)
    ax[1].set_xlabel('Grayscale value [/]')
    ax[1].set_ylabel('n pixels [/]')
    ax[1].set_xlim([0, 260])
    plt.tight_layout()