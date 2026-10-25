---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

<a href="{{ '/files/suren_cv.pdf' | relative_url }}" class="btn btn--primary" download>
  Download Résumé (PDF)
</a>

## Research Profile

I am a Ph.D. candidate in Control and Automation at the Indian Institute of Technology Delhi (IIT Delhi). My research focuses on adaptive control, distributed estimation, and multi-agent robotic systems, combining theoretical analysis with experimental validation using networks of quadrotor UAVs.

## Education

- **Ph.D., Indian Institute of Technology Delhi (IIT Delhi)** | 2020–Present  
  **Thesis:** *Distributed Adaptive Coverage Control for Mobile Sensor Networks: Application to a Network of Drones*  
  **CGPA:** 9.16

- **M.E. in Instrumentation Engineering, Madras Institute of Technology, Anna University** | 2015–2017  
  **Thesis:** *PI-PD Controller Using Extended MPC for a Binary Distillation Column*  
  **CGPA:** 7.85

- **B.E. in Electronics and Instrumentation Engineering, Anna University** | 2010–2014  
  **CGPA:** 7.89

## Employment History

- **Research Assistant (Ph.D.)**, Department of Electrical Engineering, IIT Delhi | 2022–2025
- **Assistant Professor**, Thiagarajar College of Engineering (TCE), Anna University | 2017–2020
- **Assistant System Engineer**, Tata Consultancy Services (TCS) | 2014–2015

## Research Interests

- Adaptive Control and Learning-Based Control
- Distributed Estimation and Optimization
- Multi-Agent Systems and Autonomous Systems
- Robotics and Online Decision-Making

## Technical Skills

- **Programming:** Python, C++, MATLAB, ROS/ROS 2, SQL, C#, LaTeX
- **Simulation and Development Tools:** Gazebo, PX4 SITL, Docker, Git, Linux (Ubuntu), Visual Studio Code
- **Experimental Platforms:** Crazyflie UAVs, OptiTrack motion capture system, ROS-based multi-robot systems
- **Languages:** English (fluent), Tamil (native)

## Academic and Teaching Experience

- **2020–2022:** Teaching Assistant for postgraduate courses in Adaptive Control and Probability; the undergraduate course Basic Electrical Engineering; and the NPTEL course on Adaptive Control.
- **2017–2020:** Teaching experience in Industrial Automation, Signal Processing and Instrumentation, and Project Management.

## Industrial Experience

- Performance and load testing using HP LoadRunner and SQL; training in C#.

## Funded Projects

### Distributed Adaptive Coverage Control of a Network of Drones — Theory to Practice (2022–2025)

**Role:** Research Assistant  
**Funding:** Technology Innovation Hub (TIH) for Cobotics, IIT Delhi

Developed distributed coverage-control algorithms to guide multiple UAVs toward optimal sensing locations while estimating spatially distributed quantities relevant to precision agriculture, including the Normalized Difference Vegetation Index (NDVI) and soil moisture. The project involved multispectral and thermal imagery and collaboration with Vecros Pvt. Ltd.

### Development of Advanced Control Schemes for a Binary Distillation Column (2015–2016)

**Funding:** Student Innovation Project, Centre for Technology Development and Transfer (CTDT), Anna University

Developed adaptive tuning schemes for conventional controllers, including PID and fractional-order PID controllers, for an ethanol–water binary distillation column.


## Research Publications

{% assign journals = site.publications | where: "category", "manuscripts" | sort: "date" | reverse %}
{% if journals.size > 0 %}
### Journal Articles and Manuscripts

<ul>
{% for post in journals %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>.
    {% if post.venue %}<em>{{ post.venue }}</em>, {% endif %}
    {{ post.date | date: "%Y" }}.
    {% if post.paperurl %}<a href="{{ post.paperurl }}" target="_blank" rel="noopener noreferrer">Read paper</a>.{% endif %}
  </li>
{% endfor %}
</ul>
{% endif %}

{% assign conferences = site.publications | where: "category", "conferences" | sort: "date" | reverse %}
{% if conferences.size > 0 %}
### Conference Papers and Presentations

<ul>
{% for post in conferences %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>.
    {% if post.venue %}<em>{{ post.venue }}</em>, {% endif %}
    {{ post.date | date: "%Y" }}.
    {% if post.paperurl %}<a href="{{ post.paperurl }}" target="_blank" rel="noopener noreferrer">Read paper</a>.{% endif %}
  </li>
{% endfor %}
</ul>
{% endif %}

For more details, see my [Publications]({{ '/publications/' | relative_url }}) page.