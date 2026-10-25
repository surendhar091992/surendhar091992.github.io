---
title: "Initial Excitation-Based Adaptive Coverage Control"
collection: portfolio
project_group: adaptive-coverage
order: 1
permalink: /portfolio/adaptive-coverage-1/
excerpt: "Distributed adaptive coverage control under relaxed excitation conditions for a network of drones."
header:
  teaser: "lcss.png"
---

## Overview

This work develops a gradient-based control law and a collective initial excitation (C-IE)-based composite adaptation law for fast adaptive coverage control in multi-agent robotic systems.

The proposed composite adaptive law compensates for an unknown tracking error term while relaxing the excitation requirements through information exchange among agents. Unlike conventional approaches, which require each agent to individually satisfy the initial excitation (IE) condition, the proposed framework requires the agents to satisfy the excitation condition collectively (C-IE).

The control law incorporates a tracking error correction term, ensuring exponential convergence of a combined measure of the coverage cost and parameter estimation error to zero.

Consequently, the proposed approach offers two key advantages over existing adaptive coverage control schemes:

- **Exponential convergence of parameter estimation error**, improving upon the asymptotic convergence guarantees of previous approaches.

- **Exponential convergence of the combined cost**, enabling faster convergence toward the desired coverage configuration.

These properties make the proposed algorithm particularly suitable for time-critical applications. Furthermore, the approach eliminates the need for computationally complex switching mechanisms.

To the best of our knowledge, this is the first work to introduce the concept of collective excitation in adaptive coverage control.

The proposed theoretical results are validated through real-time experiments using a network of quadrotor UAVs in a controlled indoor flight facility.

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
        src="{{ '/images/ini_voro_loose_with_ui.png' | relative_url }}"
        alt="Initial robot positions and Voronoi partition"
        style="width: 100%; height: auto; display: block;"
      >
    </div>

    <!-- Final positions -->
    <div style="flex: 1 1 220px; min-width: 0;">
      <img
        src="{{ '/images/final_voro_loose_with_ui.png' | relative_url }}"
        alt="Final robot positions and Voronoi partition"
        style="width: 100%; height: auto; display: block;"
      >
    </div>

    <!-- Robot trajectories -->
    <div style="flex: 1 1 220px; min-width: 0;">
      <img
        src="{{ '/images/tracj_plot_loose_with_ui.png' | relative_url }}"
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
    Simulation results illustrating the initial and final robot
    positions with their corresponding Voronoi partitions.
    The background shading represents the true sensory function
    φ(q), with high-information regions corresponding to Gaussian
    peaks. The rightmost plot illustrates the robot trajectories
    and final Voronoi partition.
  </figcaption>

</figure>

## Experimental Validation

<div style="
  width: 100%;
  aspect-ratio: 16/9;
  margin: 25px 0;
">

  <iframe
    src="https://www.youtube.com/embed/DMF7IB-3xfs"
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

S. Surendhar, Sayan Basu Roy, and Shubhendu Bhasin, "Collective Initial Excitation-Based Distributed Composite Adaptive Coverage Control With Application to a Network of Drones," *IEEE Control Systems Letters*, vol. 8, pp. 309–314, 2024.

[Read Publication](https://doi.org/10.1109/LCSYS.2023.3335957)

[← Back to Adaptive Coverage Control](/portfolio/adaptive-coverage/)