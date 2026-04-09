import numpy as np
import matplotlib.subplots as sub
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Joukowski map constants
c = 1.0
xc, yc = -0.1, 0.15 
zc = xc + 1j * yc
r_cyl = np.sqrt((c - xc)**2 + yc**2)

def zeta_to_z(zeta):
    z_sq = zeta**2 - 4 * c**2
    root = np.sqrt(z_sq + 0j)
    
    z1 = (zeta + root) / 2
    z2 = (zeta - root) / 2
    
    return np.where(np.abs(z1) > np.abs(z2), z1, z2)

def get_vel(X, Y, u_inf, gamma, aoa):
    alpha = np.radians(aoa)
    zeta = X + 1j * Y
    z = zeta_to_z(zeta)
    Z = z - zc 
    
    # check if point inside body
    inside = np.abs(Z) < (r_cyl * 0.98)
    Z_safe = np.where(inside, r_cyl + 1j*1e-6, Z)
    
    # complex potential velocity map
    dwdZ = (u_inf * np.exp(-1j * alpha) 
            - u_inf * (r_cyl**2 * np.exp(1j * alpha)) / Z_safe**2 
            + 1j * gamma / (2 * np.pi * Z_safe))
             
    z_safe_div = np.where(np.abs(z) < 1e-6, 1e-6 + 0j, z)
    dzeta_dz = 1 - (c**2) / z_safe_div**2
    dzeta_dz = np.where(np.abs(dzeta_dz) < 0.05, 0.05, dzeta_dz)
    
    dw_dzeta = dwdZ / dzeta_dz
    u = np.real(dw_dzeta)
    v = -np.imag(dw_dzeta)
    
    u[inside] = 0
    v[inside] = 0
    return u, v

def get_stags(u_inf, gamma, aoa):
    alpha = np.radians(aoa)
    
    a = u_inf * np.exp(-1j * alpha)
    b = 1j * gamma / (2 * np.pi)
    cc = -u_inf * r_cyl**2 * np.exp(1j * alpha)
    
    disc = np.sqrt(b**2 - 4 * a * cc + 0j)
    
    Z1 = (-b + disc) / (2 * a)
    Z2 = (-b - disc) / (2 * a)
    
    # remap stagnation to global coordinate structure
    z1 = Z1 + zc
    z2 = Z2 + zc
    zeta1 = z1 + c**2 / z1
    zeta2 = z2 + c**2 / z2
    
    return [zeta1, zeta2]

def main():
    u_inf = 1.0       
    view_l = 3.5 
    
    x_grid = np.linspace(-view_l, view_l, 200)
    y_grid = np.linspace(-view_l, view_l, 200)
    X, Y = np.meshgrid(x_grid, y_grid)
    
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.subplots_adjust(bottom=0.25)
    
    # cache drawn shape
    angles = np.linspace(0, 2*np.pi, 250)
    circle = zc + r_cyl * np.exp(1j * angles)
    foil_shape = circle + (c**2) / circle
    
    def redraw(gamma, aoa):
        ax.clear()
        ax.set_aspect('equal')
        ax.set_xlim(-view_l, view_l)
        ax.set_ylim(-view_l, view_l)
        ax.axis('off')

        u, v = get_vel(X, Y, u_inf, gamma, aoa)
        speed = np.sqrt(u**2 + v**2)
        
        ax.streamplot(X, Y, u, v, color=speed, cmap='cool', 
                      density=1.6, linewidth=1.2, arrowsize=1.5)
        
        ax.fill(np.real(foil_shape), np.imag(foil_shape), 
                color='#1e293b', ec='#0ea5e9', lw=2, zorder=5)
        
        sp = get_stags(u_inf, gamma, aoa)
        ax.scatter([np.real(sp[0]), np.real(sp[1])], 
                   [np.imag(sp[0]), np.imag(sp[1])], 
                   color='#f43f5e', s=100, zorder=10, 
                   edgecolor='white', label='Stag')
        
        ax.legend(loc='upper right', facecolor='#0f172a', edgecolor='none')

    redraw(0.0, 0.0)
    
    ax_gamma = plt.axes([0.15, 0.12, 0.65, 0.03], facecolor='#334155')
    ax_aoa = plt.axes([0.15, 0.06, 0.65, 0.03], facecolor='#334155')
    
    sl_gamma = Slider(ax_gamma, 'Circ', -10.0, 10.0, valinit=0.0)
    sl_aoa = Slider(ax_aoa, 'AoA', 0.0, 360.0, valinit=0.0)

    def update(val):
        redraw(sl_gamma.val, sl_aoa.val)
        fig.canvas.draw_idle()

    sl_gamma.on_changed(update)
    sl_aoa.on_changed(update)
    plt.show()

if __name__ == "__main__":
    main()
