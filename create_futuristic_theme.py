#!/usr/bin/env python3
"""
Transform Blood Bank into Futuristic AI-Enhanced Blue Theme
"""

import os
import re

CSS_FILE = "static/css/styles.css"
BACKUP_FILE = "static/css/styles.css.backup.original"

def backup_css():
    """Create backup"""
    if not os.path.exists(BACKUP_FILE):
        with open(CSS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(BACKUP_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created backup: {BACKUP_FILE}")
    else:
        print(f"✓ Backup exists: {BACKUP_FILE}")

def generate_futuristic_css():
    """Generate futuristic AI-themed CSS with blue color scheme"""
    
    css = """
/* ============================================================
   FUTURISTIC AI-ENHANCED BLUE THEME
   ============================================================ */

:root {
  /* AI Blue Theme Colors */
  --ai-primary: #0066FF;
  --ai-secondary: #00D4FF;
  --ai-accent: #7B2FFF;
  --ai-dark: #0A1628;
  --ai-darker: #050B14;
  --ai-light: #E6F2FF;
  --ai-glow: rgba(0, 102, 255, 0.5);
  --ai-glow-bright: rgba(0, 212, 255, 0.8);
  
  /* Glass & Effects */
  --glass-bg: rgba(10, 22, 40, 0.75);
  --glass-border: rgba(0, 212, 255, 0.2);
  --neon-shadow: 0 0 20px rgba(0, 102, 255, 0.5);
  --neon-shadow-bright: 0 0 40px rgba(0, 212, 255, 0.8);
}

/* Remove old backgrounds */
html {
  background-color: var(--ai-darker) !important;
  background-image: none !important;
}

body {
  background: var(--ai-darker) !important;
  color: var(--ai-light) !important;
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
  position: relative;
  overflow-x: hidden;
}

/* Animated gradient background */
body::before {
  content: "";
  position: fixed;
  inset: 0;
  background: 
    radial-gradient(circle at 20% 30%, rgba(0, 102, 255, 0.15) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(0, 212, 255, 0.15) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(123, 47, 255, 0.1) 0%, transparent 50%),
    linear-gradient(135deg, #0A1628 0%, #050B14 100%);
  animation: gradientShift 15s ease infinite;
  z-index: 0;
  pointer-events: none;
}

@keyframes gradientShift {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.8; }
}

/* Grid overlay for tech feel */
body::after {
  content: "";
  position: fixed;
  inset: 0;
  background-image: 
    linear-gradient(rgba(0, 212, 255, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 212, 255, 0.03) 1px, transparent 1px);
  background-size: 50px 50px;
  z-index: 0;
  pointer-events: none;
  animation: gridMove 20s linear infinite;
}

@keyframes gridMove {
  0% { transform: translate(0, 0); }
  100% { transform: translate(50px, 50px); }
}

/* Content above background */
body > * {
  position: relative;
  z-index: 10;
}

/* Futuristic Navbar */
.bb-nav {
  background: var(--glass-bg) !important;
  border-bottom: 1px solid var(--glass-border) !important;
  backdrop-filter: blur(20px) !important;
  box-shadow: 0 4px 30px rgba(0, 102, 255, 0.1) !important;
}

.navbar-brand {
  color: var(--ai-secondary) !important;
  font-weight: 700;
  text-shadow: 0 0 10px var(--ai-glow);
  transition: all 0.3s ease;
}

.navbar-brand:hover {
  color: var(--ai-primary) !important;
  text-shadow: 0 0 20px var(--ai-glow-bright);
  transform: scale(1.05);
}

.nav-link {
  color: var(--ai-light) !important;
  position: relative;
  transition: all 0.3s ease;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--ai-primary), var(--ai-secondary));
  transition: all 0.3s ease;
  transform: translateX(-50%);
}

.nav-link:hover {
  color: var(--ai-secondary) !important;
}

.nav-link:hover::after {
  width: 80%;
}

/* Futuristic Glass Cards */
.bb-glass,
.card {
  background: var(--glass-bg) !important;
  border: 1px solid var(--glass-border) !important;
  backdrop-filter: blur(20px) !important;
  box-shadow: 
    0 8px 32px rgba(0, 0, 0, 0.3),
    inset 0 1px 0 rgba(0, 212, 255, 0.1) !important;
  border-radius: 16px !important;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.bb-glass::before,
.card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(0, 212, 255, 0.1),
    transparent
  );
  transition: left 0.5s ease;
}

.bb-glass:hover::before,
.card:hover::before {
  left: 100%;
}

.bb-glass:hover,
.card:hover {
  border-color: var(--ai-secondary) !important;
  box-shadow: 
    0 12px 48px rgba(0, 102, 255, 0.3),
    inset 0 1px 0 rgba(0, 212, 255, 0.2) !important;
  transform: translateY(-4px);
}

/* Neon Buttons */
.btn-gradient {
  background: linear-gradient(135deg, var(--ai-primary), var(--ai-secondary)) !important;
  border: none !important;
  color: white !important;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  box-shadow: var(--neon-shadow) !important;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.btn-gradient::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  transform: translate(-50%, -50%);
  transition: width 0.6s ease, height 0.6s ease;
}

.btn-gradient:hover::before {
  width: 300px;
  height: 300px;
}

.btn-gradient:hover {
  box-shadow: var(--neon-shadow-bright) !important;
  transform: translateY(-2px);
}

.btn-outline-gradient {
  background: transparent !important;
  border: 2px solid var(--ai-primary) !important;
  color: var(--ai-secondary) !important;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-outline-gradient:hover {
  background: var(--ai-primary) !important;
  color: white !important;
  box-shadow: var(--neon-shadow) !important;
  transform: translateY(-2px);
}

/* AI Glow Effects */
.ai-glow {
  animation: aiPulse 3s ease-in-out infinite;
}

@keyframes aiPulse {
  0%, 100% {
    box-shadow: 0 0 20px rgba(0, 102, 255, 0.5);
  }
  50% {
    box-shadow: 0 0 40px rgba(0, 212, 255, 0.8);
  }
}

/* Stat Cards with Neon */
.stat-card {
  background: var(--glass-bg) !important;
  border: 1px solid var(--glass-border) !important;
  border-radius: 12px;
  padding: 20px;
  transition: all 0.3s ease;
}

.stat-card:hover {
  border-color: var(--ai-secondary);
  box-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
  transform: scale(1.05);
}

.stat-icon {
  background: linear-gradient(135deg, var(--ai-primary), var(--ai-secondary));
  box-shadow: 0 0 20px var(--ai-glow);
}

/* Blood Badge - Futuristic */
.blood-badge,
.stock-badge {
  background: linear-gradient(135deg, var(--ai-primary), var(--ai-accent)) !important;
  box-shadow: 0 0 20px var(--ai-glow) !important;
  border: 2px solid var(--ai-secondary);
  animation: badgePulse 2s ease-in-out infinite;
}

@keyframes badgePulse {
  0%, 100% {
    box-shadow: 0 0 20px var(--ai-glow);
  }
  50% {
    box-shadow: 0 0 40px var(--ai-glow-bright);
  }
}

/* Tables */
.table {
  color: var(--ai-light) !important;
}

.table thead th {
  background: var(--glass-bg) !important;
  color: var(--ai-secondary) !important;
  border-color: var(--glass-border) !important;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.85rem;
}

.table tbody tr {
  border-color: var(--glass-border) !important;
  transition: all 0.3s ease;
}

.table tbody tr:hover {
  background: rgba(0, 102, 255, 0.1) !important;
  box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
}

/* Forms */
.form-control,
.form-select {
  background: rgba(10, 22, 40, 0.6) !important;
  border: 1px solid var(--glass-border) !important;
  color: var(--ai-light) !important;
  transition: all 0.3s ease;
}

.form-control:focus,
.form-select:focus {
  background: rgba(10, 22, 40, 0.8) !important;
  border-color: var(--ai-secondary) !important;
  box-shadow: 0 0 20px var(--ai-glow) !important;
  color: white !important;
}

.form-control::placeholder {
  color: rgba(230, 242, 255, 0.5) !important;
}

/* Footer */
footer.footer {
  background: var(--glass-bg) !important;
  border-top: 1px solid var(--glass-border) !important;
  backdrop-filter: blur(20px) !important;
  color: var(--ai-light) !important;
}

/* Text Colors */
.text-muted {
  color: rgba(230, 242, 255, 0.6) !important;
}

h1, h2, h3, h4, h5, h6 {
  color: var(--ai-light) !important;
  font-weight: 700;
}

/* Alerts */
.alert {
  background: var(--glass-bg) !important;
  border: 1px solid var(--glass-border) !important;
  color: var(--ai-light) !important;
  backdrop-filter: blur(20px);
}

.alert-success {
  border-left: 4px solid #00FF88 !important;
}

.alert-danger {
  border-left: 4px solid #FF0055 !important;
}

.alert-warning {
  border-left: 4px solid #FFB800 !important;
}

.alert-info {
  border-left: 4px solid var(--ai-secondary) !important;
}

/* Badges */
.badge {
  background: linear-gradient(135deg, var(--ai-primary), var(--ai-secondary)) !important;
  box-shadow: 0 0 10px var(--ai-glow);
  font-weight: 600;
  padding: 6px 12px;
}

/* Progress Bars */
.progress {
  background: rgba(10, 22, 40, 0.6) !important;
  border: 1px solid var(--glass-border);
  box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.3);
}

.progress-bar {
  background: linear-gradient(90deg, var(--ai-primary), var(--ai-secondary)) !important;
  box-shadow: 0 0 20px var(--ai-glow);
  animation: progressGlow 2s ease-in-out infinite;
}

@keyframes progressGlow {
  0%, 100% {
    box-shadow: 0 0 20px var(--ai-glow);
  }
  50% {
    box-shadow: 0 0 40px var(--ai-glow-bright);
  }
}

/* Chatbot - Futuristic */
.chatbot-button {
  background: linear-gradient(135deg, var(--ai-primary), var(--ai-accent)) !important;
  box-shadow: 0 0 30px var(--ai-glow) !important;
  border: 2px solid var(--ai-secondary);
  animation: chatbotPulse 3s ease-in-out infinite;
}

@keyframes chatbotPulse {
  0%, 100% {
    box-shadow: 0 0 30px var(--ai-glow);
    transform: scale(1);
  }
  50% {
    box-shadow: 0 0 50px var(--ai-glow-bright);
    transform: scale(1.05);
  }
}

.chatbot-window {
  background: var(--glass-bg) !important;
  border: 1px solid var(--glass-border) !important;
  backdrop-filter: blur(20px) !important;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5) !important;
}

.chatbot-header {
  background: linear-gradient(135deg, var(--ai-primary), var(--ai-secondary)) !important;
  box-shadow: 0 0 20px var(--ai-glow);
}

.chatbot-messages {
  background: rgba(5, 11, 20, 0.5) !important;
}

.bot-message {
  background: rgba(0, 102, 255, 0.2) !important;
  border-left: 3px solid var(--ai-secondary);
}

.user-message {
  background: linear-gradient(135deg, var(--ai-primary), var(--ai-accent)) !important;
  box-shadow: 0 0 10px var(--ai-glow);
}

/* Scrollbar */
::-webkit-scrollbar {
  width: 12px;
  height: 12px;
}

::-webkit-scrollbar-track {
  background: var(--ai-darker);
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, var(--ai-primary), var(--ai-secondary));
  border-radius: 10px;
  border: 2px solid var(--ai-darker);
}

::-webkit-scrollbar-thumb:hover {
  box-shadow: 0 0 10px var(--ai-glow);
}

/* Selection */
::selection {
  background: var(--ai-primary);
  color: white;
}

/* Loading Animation */
.blood-drop {
  background: linear-gradient(135deg, var(--ai-primary), var(--ai-secondary)) !important;
  box-shadow: 0 0 30px var(--ai-glow) !important;
  animation: dropGlow 1.1s ease-in-out infinite;
}

@keyframes dropGlow {
  0%, 100% {
    box-shadow: 0 0 30px var(--ai-glow);
  }
  50% {
    box-shadow: 0 0 50px var(--ai-glow-bright);
  }
}

/* Hero Section */
.hero {
  background: var(--glass-bg) !important;
  border: 1px solid var(--glass-border) !important;
  backdrop-filter: blur(20px) !important;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3) !important;
  position: relative;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(0, 212, 255, 0.1) 0%, transparent 70%);
  animation: heroRotate 20s linear infinite;
}

@keyframes heroRotate {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Stock Chips */
.stock-chip {
  background: var(--glass-bg) !important;
  border: 1px solid var(--glass-border) !important;
  backdrop-filter: blur(20px);
  transition: all 0.3s ease;
}

.stock-chip:hover {
  border-color: var(--ai-secondary);
  box-shadow: 0 0 20px var(--ai-glow);
  transform: translateY(-3px);
}

/* Dropdown */
.dropdown-menu {
  background: var(--glass-bg) !important;
  border: 1px solid var(--glass-border) !important;
  backdrop-filter: blur(20px) !important;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5) !important;
}

.dropdown-item {
  color: var(--ai-light) !important;
  transition: all 0.3s ease;
}

.dropdown-item:hover {
  background: rgba(0, 102, 255, 0.2) !important;
  color: var(--ai-secondary) !important;
}

/* Page-specific backgrounds with different images */
body.page-landing::before {
  background: 
    url('../img/1.avif'),
    radial-gradient(circle at 20% 30%, rgba(0, 102, 255, 0.2) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(0, 212, 255, 0.2) 0%, transparent 50%),
    linear-gradient(135deg, #0A1628 0%, #050B14 100%);
  background-size: cover, auto, auto, auto;
  background-position: center, center, center, center;
  background-blend-mode: overlay, normal, normal, normal;
  opacity: 0.3;
}

body.page-dashboard::before {
  background: 
    url('../img/3.jpg'),
    radial-gradient(circle at 50% 50%, rgba(0, 102, 255, 0.2) 0%, transparent 50%),
    linear-gradient(135deg, #0A1628 0%, #050B14 100%);
  background-size: cover, auto, auto;
  background-position: center, center, center;
  background-blend-mode: overlay, normal, normal;
  opacity: 0.3;
}

body.page-services::before,
body.page-emergency_request::before {
  background: 
    url('../img/4.webp'),
    radial-gradient(circle at 30% 70%, rgba(0, 212, 255, 0.2) 0%, transparent 50%),
    linear-gradient(135deg, #0A1628 0%, #050B14 100%);
  background-size: cover, auto, auto;
  background-position: center, center, center;
  background-blend-mode: overlay, normal, normal;
  opacity: 0.3;
}

/* Responsive */
@media (max-width: 768px) {
  .bb-glass,
  .card {
    border-radius: 12px !important;
  }
  
  .hero::before {
    animation: heroRotate 30s linear infinite;
  }
}

/* Accessibility */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
"""
    return css

def update_css():
    """Replace CSS with futuristic theme"""
    
    if not os.path.exists(CSS_FILE):
        print(f"✗ CSS file not found: {CSS_FILE}")
        return False
    
    # Generate new CSS
    new_css = generate_futuristic_css()
    
    # Write completely new CSS
    with open(CSS_FILE, 'w', encoding='utf-8') as f:
        f.write(new_css)
    
    print(f"✓ Created futuristic AI theme CSS")
    return True

def main():
    """Main function"""
    print("=" * 60)
    print("Creating Futuristic AI-Enhanced Blue Theme")
    print("=" * 60)
    print()
    
    # Backup
    backup_css()
    print()
    
    # Update CSS
    print("Generating futuristic theme...")
    if update_css():
        print()
        print("=" * 60)
        print("✓ Futuristic AI Theme Created!")
        print("=" * 60)
        print()
        print("New Features:")
        print("  ✓ Blue AI color scheme")
        print("  ✓ Neon glow effects")
        print("  ✓ Animated gradients")
        print("  ✓ Tech grid overlay")
        print("  ✓ Glass morphism cards")
        print("  ✓ Futuristic buttons")
        print("  ✓ AI pulse animations")
        print("  ✓ Different images per page")
        print()
        print("Next steps:")
        print("1. Clear browser cache (Ctrl+Shift+R)")
        print("2. Restart Django server")
        print("3. Experience the futuristic AI theme!")
        print()
        return 0
    else:
        print("\n✗ Failed to create theme")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
