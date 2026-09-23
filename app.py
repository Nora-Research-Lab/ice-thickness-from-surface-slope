import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import gradio as gr
from ice_thickness_from_surface_slope import compute_thickness

def compute_h(theta_deg, tau_b, rho, g):
    if rho is None or rho <= 0:
        rho = 917.0
    if g is None or g <= 0:
        g = 9.81
    if theta_deg <= 0 or theta_deg > 30:
        return "Slope must be between 0.1° and 30°."
    if tau_b <= 0:
        return "Basal shear stress must be positive."
    h = compute_thickness(theta_deg, tau_b, rho, g)
    return f"{h:.1f} m"

def make_plot(theta_deg, tau_b, rho, g):
    if rho is None or rho <= 0:
        rho = 917.0
    if g is None or g <= 0:
        g = 9.81
    if tau_b <= 0:
        tau_b = 100.0
    slopes = np.linspace(0.1, 30, 300)
    thicknesses = [compute_thickness(s, tau_b, rho, g) for s in slopes]
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(slopes, thicknesses, 'b-', linewidth=2)
    ax.set_xlabel('Surface slope (degrees)')
    ax.set_ylabel('Ice thickness (m)')
    ax.set_title(f'Sensitivity curve at τ_b = {tau_b:.1f} kPa')
    ax.grid(True)
    plt.tight_layout()
    return fig

with gr.Blocks(title="Ice Thickness from Surface Slope") as demo:
    gr.Markdown("# Ice Thickness from Surface Slope")
    gr.Markdown("Uses the shallow-ice approximation: $H = \\tau_b / (\\rho g \\sin\\theta)$")
    with gr.Row():
        theta_slider = gr.Slider(minimum=0.1, maximum=30, step=0.1, value=5.0, label="Surface slope θ (°)")
        tau_slider = gr.Slider(minimum=20, maximum=200, step=1, value=100, label="Basal shear stress τ_b (kPa)")
    with gr.Row():
        rho_input = gr.Number(value=917.0, minimum=825.3, maximum=1008.7, step=0.1, label="Ice density ρ (kg/m³)")
        g_input = gr.Number(value=9.81, minimum=0.1, maximum=20.0, step=0.01, label="Gravitational acceleration g (m/s²)")
    output_text = gr.Label(label="Ice Thickness H = ?", value="1000.0 m")
    with gr.Row():
        plot = gr.Plot(label="Thickness vs. Slope for current parameters")
    
    # Update output and plot when any input changes
    inputs = [theta_slider, tau_slider, rho_input, g_input]
    outputs = [output_text, plot]
    demo.load(fn=lambda *args: (compute_h(*args), make_plot(*args)), inputs=inputs, outputs=outputs)
    for comp in [theta_slider, tau_slider, rho_input, g_input]:
        comp.change(fn=lambda *args: (compute_h(*args), make_plot(*args)), inputs=inputs, outputs=outputs)

demo.launch(server_name="0.0.0.0", server_port=7860)
