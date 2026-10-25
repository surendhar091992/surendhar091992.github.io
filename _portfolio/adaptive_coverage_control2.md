---
title: "Adaptive Coverage Control with obstacle avoidance"
collection: portfolio
project_group: adaptive-coverage
order: 2
permalink: /portfolio/adaptive-coverage-2/
excerpt: "Adaptive coverage control with obstacle avoidance under the relaxed excitations"
header:
  teaser: "RAS_intro.png"
---

## Overview

The key contributions of this work are as follows:

- **Continuous Obstacle Avoidance:** A modified artificial potential-like (AP-like) formulation that employs a continuous control law to prevent undesirable oscillations during obstacle avoidance, providing a novel continuous-time adaptive coverage control framework with obstacle avoidance.

- **Parameter Convergence under Relaxed Excitation Conditions:** A modified parameter estimator designed for obstacle avoidance scenarios, guaranteeing parameter convergence under the relaxed condition of collective initial excitation (C-IE), rather than relying solely on prediction error convergence.

- **Experimental Validation:** The proposed control algorithm is experimentally validated using a network of quadrotor UAVs in a controlled indoor flight facility.

## Simulation Results

The proposed adaptive coverage control algorithm is evaluated through numerical simulations to demonstrate the convergence of the agents toward the desired coverage configuration and the evolution of the corresponding Voronoi partitions.

<figure style="width: 100%; margin: 30px 0;">

  <div style="
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    align-items: center;
    justify-content: center;
  ">

    <!-- Initial positions -->
    <div style="flex: 1 1 220px; min-width: 0;">
      <img
        src="{{ '/images/Figure_2_a.png' | relative_url }}"
        alt="Initial robot positions and Voronoi partition"
        style="width: 100%; height: auto; display: block;"
      >
    </div>

    <!-- Final positions -->
    <div style="flex: 1 1 220px; min-width: 0;">
      <img
        src="{{ '/images/Figure_2_b.png' | relative_url }}"
        alt="Final robot positions and Voronoi partition"
        style="width: 100%; height: auto; display: block;"
      >
    </div>

    <!-- Robot trajectories -->
    <div style="flex: 1 1 220px; min-width: 0;">
      <img
        src="{{ '/images/Figure_2_c.png' | relative_url }}"
        alt="Robot trajectories and final Voronoi partition"
        style="width: 100%; height: auto; display: block;"
      >
    </div>

  </div>

  <!-- Figure caption -->
  <figcaption style="
    text-align: center;
    font-size: 0.85em;
    line-height: 1.6;
    margin-top: 15px;
  ">
    <strong>Figure:</strong>
    Simulation result Plots:  the robots initial and final positions along with their Voronoi cell divisions. The background shading indicates the actual sensory function $\phi(q)$, with Gaussian peaks highlighting regions of high information. The final plot showcases the paths taken by the robots and their corresponding Voronoi partitions, while obstacles are represented by circular shapes.
  </figcaption>

</figure>

## Gazebo simulation

<div style="
  width: 100%;
  aspect-ratio: 16/9;
  margin: 25px 0;
">

  <iframe
    src="https://www.youtube.com/embed/oOGfFYMRsW0"
    title="Experimental Validation of Adaptive Coverage Control"
    style="
      width: 100%;
      height: 100%;
      border: 0;
      border-radius: 8px;
    "
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>

</div>

## Experimental Validation

<div style="
  width: 100%;
  aspect-ratio: 16/9;
  margin: 25px 0;
">

  <iframe
    src="https://www.youtube.com/embed/mVc8sads0qo"
    title="Experimental Validation of Adaptive Coverage Control"
    style="
      width: 100%;
      height: 100%;
      border: 0;
      border-radius: 8px;
    "
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>

</div>

## Related Publication

S. Surendhar, Sayan Basu Roy, and Shubhendu Bhasin, 
"Distributed adaptive coverage control with obstacle avoidance for a drone network based on collective initial excitation,"
*Robotics and Autonomous Systems*, vol. 194, Article 105135, 2025.

[Read Publication](https://doi.org/10.1016/j.robot.2025.105135)

[← Back to Adaptive Coverage Control](/portfolio/adaptive-coverage/)