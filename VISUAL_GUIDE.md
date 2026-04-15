# Blood Bank UI - Visual Design Guide

## 🎨 Color System

### Primary Palette
```css
--bb-red: #E63946        /* Blood Red - Primary brand */
--bb-blue: #2F80ED       /* Medical Blue - Secondary brand */
--bb-bg: #F5F7FB         /* Background - Light neutral */
--bb-ink: #0B1220        /* Text - Dark ink */
--bb-ink-soft: rgba(11,18,32,0.62)  /* Secondary text */
```

### Glass Morphism
```css
--bb-glass: rgba(255,255,255,0.82)  /* Glass background */
--bb-glass-border: rgba(11,18,32,0.10)  /* Glass border */
```

### Shadows
```css
--bb-shadow: 0 18px 45px rgba(11,18,32,0.10)  /* Strong shadow */
--bb-shadow-soft: 0 12px 30px rgba(11,18,32,0.08)  /* Soft shadow */
```

### Accent Colors
- **Purple**: #A742F5 - Profile, identity, AI features
- **Yellow**: #FFB800 - Awareness, education, warnings
- **Pink**: #FF6B6B - Emergency, urgency
- **Green**: #28a745 - Success, available status
- **Orange**: #ffc107 - Low stock warnings

## 🖼️ Background Themes

### Page Backgrounds Map
| Page Type | Background | Primary Colors | Theme |
|-----------|-----------|----------------|-------|
| Landing | bg-landing-hero.svg | Red, Blue, Purple | Comprehensive medical |
| Dashboard | bg-dashboard.svg | Blue, Red, Purple | Analytics & data |
| Services | bg-services.svg | Blue, Red | Service overview |
| Inventory | bg-inventory.svg | Blue, Red | Stock management |
| Awareness | bg-awareness.svg | Yellow, Red | Education |
| Emergency | bg-emergency.svg | Red, Pink | Urgency |
| Camps | bg-camps.svg | Blue, Red | Community events |
| Profile | bg-profile.svg | Purple, Blue | User identity |
| Login/Register | bg-login.svg | Blue, Red | Security |
| Donor Pages | bg-donor.svg | Red, Blue | Blood donation |
| Find Blood | bg-medical.svg | Red, Blue | Medical search |
| About | bg-about.svg | Blue, Red | Information |

## 🎭 Component Styles

### Cards
```html
<!-- Glass Card -->
<div class="bb-glass bb-card p-4">
  Content here
</div>

<!-- Glass Card with Hover -->
<div class="bb-glass bb-card p-4 h-100">
  Hoverable content
</div>
```

### Buttons
```html
<!-- Primary Gradient Button -->
<button class="btn btn-gradient">
  <i class="bi bi-heart-pulse me-2"></i>Action
</button>

<!-- Outline Glass Button -->
<button class="btn btn-outline-gradient">
  <i class="bi bi-search me-2"></i>Search
</button>
```

### Badges & Pills
```html
<!-- Status Pill -->
<div class="d-inline-flex align-items-center gap-2 px-3 py-2 rounded-pill bb-glass">
  <i class="bi bi-cpu-fill" style="color: var(--bb-blue)"></i>
  <span class="small fw-semibold">AI Powered</span>
</div>

<!-- Blood Badge -->
<div class="blood-badge">A+</div>

<!-- Stock Badge -->
<div class="stock-badge">
  <i class="bi bi-droplet-fill"></i>
</div>
```

### Stock Chips
```html
<div class="stock-chip">
  <div class="stock-badge"><i class="bi bi-droplet-fill"></i></div>
  <div>
    <div class="fw-semibold">Live Availability</div>
    <div class="text-muted small">Real-time updates</div>
  </div>
</div>
```

### Status Indicators
```html
<!-- Available -->
<span class="status-dot available"></span>Available

<!-- Low Stock -->
<span class="status-dot low"></span>Low Stock

<!-- Critical -->
<span class="status-dot critical"></span>Critical
```

## 📐 Layout Patterns

### Hero Section
```html
<section class="hero bb-glass p-4 p-md-5 overflow-hidden">
  <div class="row align-items-center g-4">
    <div class="col-lg-7">
      <!-- Content -->
    </div>
    <div class="col-lg-5">
      <!-- Cards/Stats -->
    </div>
  </div>
  <div class="hero-bg"></div>
</section>
```

### Dashboard Hero
```html
<div class="bb-dashboard-hero">
  <div class="bb-kpi">
    <div>
      <h2 class="bb-hero-title">Dashboard</h2>
      <p class="text-muted">Overview</p>
    </div>
    <div class="bb-hero-controls">
      <!-- Controls -->
    </div>
  </div>
</div>
```

### Service Grid
```html
<div class="row g-3">
  <div class="col-md-6 col-lg-4">
    <div class="bb-glass p-4 h-100">
      <div class="service-icon">
        <i class="bi bi-search-heart"></i>
      </div>
      <div class="fw-bold">Service Title</div>
      <div class="text-muted small">Description</div>
    </div>
  </div>
</div>
```

## 🎬 Animations

### Available Animations
```css
/* Floating */
animation: float 3s ease-in-out infinite;

/* Pulse Glow */
animation: pulse-glow 2s infinite;

/* Slide In */
animation: slide-in 0.6s ease-out;

/* Drop (Blood Drop) */
animation: drop 1.1s ease-in-out infinite;

/* Pulse Scale */
animation: pulse-scale 2s infinite;
```

### Usage Examples
```html
<!-- Floating Illustration -->
<img class="bb-illus" src="..." alt="...">

<!-- Emergency Indicator -->
<div class="emergency-indicator">
  <i class="bi bi-exclamation-triangle"></i>
</div>

<!-- Loading Blood Drop -->
<div class="blood-drop"></div>
```

## 🎯 Icon Usage

### Bootstrap Icons
```html
<!-- Medical -->
<i class="bi bi-heart-pulse"></i>
<i class="bi bi-droplet-fill"></i>
<i class="bi bi-hospital"></i>

<!-- Actions -->
<i class="bi bi-search"></i>
<i class="bi bi-person-plus"></i>
<i class="bi bi-calendar-event"></i>

<!-- Status -->
<i class="bi bi-check-circle-fill"></i>
<i class="bi bi-exclamation-triangle"></i>
<i class="bi bi-info-circle"></i>

<!-- Navigation -->
<i class="bi bi-house"></i>
<i class="bi bi-grid"></i>
<i class="bi bi-box-seam"></i>
```

### Icon Colors
```html
<!-- Red (Blood/Emergency) -->
<i class="bi bi-droplet" style="color: var(--bb-red)"></i>

<!-- Blue (Medical/Info) -->
<i class="bi bi-hospital" style="color: var(--bb-blue)"></i>

<!-- Purple (AI/Profile) -->
<i class="bi bi-cpu-fill" style="color: #A742F5"></i>
```

## 📱 Responsive Classes

### Bootstrap Grid
```html
<!-- Mobile First -->
<div class="col-12 col-md-6 col-lg-4">
  <!-- Stacks on mobile, 2 cols on tablet, 3 cols on desktop -->
</div>

<!-- Responsive Padding -->
<div class="p-2 p-md-4 p-lg-5">
  <!-- Increases padding on larger screens -->
</div>
```

### Display Utilities
```html
<!-- Hide on Mobile -->
<div class="d-none d-md-block">Desktop only</div>

<!-- Show on Mobile Only -->
<div class="d-block d-md-none">Mobile only</div>
```

## 🎨 Gradient Text
```html
<h1 class="gradient-text">AI Powered System</h1>
```

```css
.gradient-text {
  background: linear-gradient(135deg, var(--bb-red), var(--bb-blue));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

## 📊 Data Visualization

### Progress Bars
```html
<div class="progress">
  <div class="progress-bar" style="width: 75%">75%</div>
</div>
```

### Stat Cards
```html
<div class="stat-card">
  <div class="stat-icon" style="background: rgba(230,57,70,0.12); color: var(--bb-red)">
    <i class="bi bi-droplet-fill"></i>
  </div>
  <div>
    <div class="value">1,234</div>
    <div class="text-muted small">Total Units</div>
  </div>
</div>
```

## 🔔 Notifications

### Alerts
```html
<!-- Success -->
<div class="alert alert-success">
  <i class="bi bi-check-circle-fill me-2"></i>
  Operation successful!
</div>

<!-- Danger -->
<div class="alert alert-danger">
  <i class="bi bi-exclamation-triangle me-2"></i>
  Critical stock level!
</div>

<!-- Warning -->
<div class="alert alert-warning">
  <i class="bi bi-exclamation-circle me-2"></i>
  Low stock warning
</div>
```

### Toast Notifications
```html
<div class="toast show">
  <div class="toast-header">
    <i class="bi bi-bell-fill me-2"></i>
    <strong class="me-auto">Notification</strong>
    <small>Just now</small>
  </div>
  <div class="toast-body">
    New blood request received
  </div>
</div>
```

## 🎯 Best Practices

### Do's ✅
- Use `.bb-glass` for card backgrounds
- Apply `.bb-card` for hover effects
- Use semantic color variables
- Include icons with text for clarity
- Maintain consistent spacing (gap-2, gap-3, gap-4)
- Use Bootstrap grid for layouts
- Add loading states to forms
- Respect reduced motion preferences

### Don'ts ❌
- Don't use pure white backgrounds
- Avoid mixing gradient styles
- Don't override Bootstrap core classes
- Avoid excessive animations
- Don't use colors without semantic meaning
- Avoid fixed pixel widths
- Don't skip accessibility attributes

## 🚀 Quick Start Template

```html
{% extends 'base.html' %}
{% load static %}

{% block title %}Page Title | Blood Bank{% endblock %}

{% block content %}
<div class="bb-glass bb-card p-4">
  <div class="d-flex justify-content-between align-items-center mb-3">
    <div>
      <h3 class="fw-bold mb-1">Page Title</h3>
      <div class="text-muted">Page description</div>
    </div>
    <a class="btn btn-gradient" href="#">
      <i class="bi bi-plus-lg me-2"></i>Action
    </a>
  </div>
  
  <div class="row g-3">
    <div class="col-md-6 col-lg-4">
      <div class="bb-glass p-4 h-100">
        <!-- Card content -->
      </div>
    </div>
  </div>
</div>
{% endblock %}
```

## 📚 Resources

- Bootstrap 5 Docs: https://getbootstrap.com/docs/5.3/
- Bootstrap Icons: https://icons.getbootstrap.com/
- CSS Variables: https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties
- Accessibility: https://www.w3.org/WAI/WCAG21/quickref/

---

**Design System Version**: 1.0
**Last Updated**: 2026
**Theme**: Blood Bank Medical Interface
