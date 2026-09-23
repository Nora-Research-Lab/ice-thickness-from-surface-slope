import math

def compute_thickness(theta_deg, tau_b, rho, g):
    """
    Compute ice thickness using the shallow-ice approximation.

    Parameters
    ----------
    theta_deg : float
        Surface slope in degrees (0.1–30).
    tau_b : float
        Basal shear stress in kPa (20–200).
    rho : float
        Ice density in kg/m³ (typically 917).
    g : float
        Gravitational acceleration in m/s² (typically 9.81).

    Returns
    -------
    float
        Ice thickness in meters.
    """
    theta_rad = math.radians(theta_deg)
    sin_theta = math.sin(theta_rad)
    if sin_theta <= 0:
        return 0.0  # degenerate case, thickness infinite actually but return 0
    # tau_b is in kPa -> convert to Pa = kPa * 1000
    tau_b_pa = tau_b * 1000.0
    h = tau_b_pa / (rho * g * sin_theta)
    return h
