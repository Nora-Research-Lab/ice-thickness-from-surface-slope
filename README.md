![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Ice Thickness from Surface Slope
 
*For glaciologists and field researchers: enter surface slope and basal shear stress to instantly compute glacier ice thickness using the shallow-ice approximation.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Glaciology / Cryosphere
 
This tool computes the approximate thickness of a glacier or ice sheet using the shallow-ice approximation, which assumes that the driving stress is balanced by basal shear stress. The user provides four inputs: (1) surface slope in degrees (θ, range 0.1–30°), (2) basal shear stress in kilopascals (τ_b, range 20–200 kPa), (3) ice density in kg/m³ (ρ, default 917, adjustable ±10%), and (4) gravitational acceleration in m/s² (g, default 9.81, adjustable for planetary applications). The core calculation converts θ to radians, then uses H = τ_b / (ρ × g × sin(θ_rad)). All inputs are given via sliders (θ and τ_b) and numeric text boxes (ρ and g). The single numeric output is ice thickness H in meters, displayed with one decimal place. A small inset plot shows H as a function of slope for a fixed τ_b (using the user's current τ_b value) to visualise sensitivity. The UI layout: two sliders side by side at top (slope left, basal shear right), two numeric inputs below them, a large output number in the middle, and the sensitivity curve beneath. No AI/ML component is used; the tool relies on a standard glaciological formula.
 
## Run it
 
```bash
docker build -t ice-thickness-from-surface-slope .
docker run -p 7860:7860 ice-thickness-from-surface-slope
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-23.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
