import os

# Read common header and footer components
with open('index.html', 'r') as f:
    idx = f.read()

header_part = '<header class="site-header"' + idx.split('<header class="site-header"')[1].split('</aside>')[0] + '</aside>'
footer_part = '<footer class="clear-footer"' + idx.split('<footer class="clear-footer"')[1]

# -------------------------------------------------------------
# 1. STREAMLINED INDEX.HTML (Home page jangan kepanjangan)
# -------------------------------------------------------------
home_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vision Focus | Connecting China to Indonesia - Procurement & Sourcing Partner</title>
  <meta name="description" content="Vision Focus acts as a trusted bridge between Indonesian clients and reliable factories in China. Specializing in high-quality building and interior materials.">
  <link rel="icon" type="image/png" href="assets/logo/VISION FOCUS LOGO FIX SOFT GOLD.png">
  <link rel="stylesheet" href="css/main.css">
</head>
<body>
{header_part}

  <!-- ==========================================
       HERO BANNER (CLEAN, HIGH CONTRAST)
       ========================================== -->
  <section class="clear-hero-banner" id="home" aria-label="Hero section">
    <img src="assets/GuangZhou.png" alt="Guangzhou Pearl River & Canton Tower Skyline" class="clear-hero-bg">
    <div class="clear-hero-overlay"></div>
    <div class="clear-hero-content">
      <h1 class="clear-hero-title" data-i18n="hero_title">THE GATE TO CHINA</h1>
      <div class="clear-hero-subtitle">
        <span data-i18n="hero_sub1">ONE</span>
        <span class="highlight-stop" data-i18n="hero_sub2">STOP</span>
        <span data-i18n="hero_sub3">SOLUTION</span>
      </div>
      <div class="clear-hero-tagline" data-i18n="hero_tagline">FOR SUPPLY CHAIN MANAGEMENT</div>
      <div class="clear-hero-btns">
        <a href="#about" class="btn-clear-white" data-i18n="hero_btn_learn">LEARN MORE</a>
        <a href="https://wa.me/628113188878?text=Hello%20Vision%20Focus%2C%20I%20would%20like%20to%20inquire%20about%20sourcing%20services" target="_blank" rel="noopener noreferrer" class="btn-clear-wa" data-i18n="hero_btn_wa">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2zm.01 1.67c2.2 0 4.26.86 5.82 2.42a8.204 8.204 0 0 1 2.41 5.82c0 4.54-3.7 8.24-8.24 8.24-1.42 0-2.82-.37-4.06-1.08l-.29-.17-3.12.82.83-3.04-.19-.3a8.21 8.21 0 0 1-1.26-4.47c0-4.54 3.7-8.24 8.24-8.24zm4.52 11.64c-.25-.12-1.47-.72-1.7-.81-.23-.08-.39-.12-.56.12-.17.25-.64.81-.79.97-.14.17-.29.19-.54.07-.25-.12-1.05-.39-2-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.12-.14.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.4-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.23.25-.87.85-.87 2.08s.89 2.41 1.01 2.58c.12.17 1.75 2.67 4.24 3.75.59.26 1.05.41 1.41.53.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.07.15-1.18-.06-.11-.22-.18-.47-.3z"/></svg>
          CONTACT VIA WHATSAPP
        </a>
      </div>
    </div>
  </section>

  <!-- ==========================================
       SECTION: ABOUT VISION FOCUS
       ========================================== -->
  <section class="about-vision" id="about" style="padding: 80px 0; background: #ffffff;">
    <div class="container">
      <div style="display: grid; grid-template-columns: 360px 1fr; gap: 60px; align-items: center;">
        <div style="text-align: center;">
          <img src="assets/jason.JPG" alt="Vision Focus Founder Mr. Jason Shi" style="border-radius: 12px; box-shadow: 0 16px 36px rgba(17, 30, 46, 0.1); width: 100%; max-width: 340px; margin: 0 auto;">
        </div>
        <div>
          <h2 style="font-size: 2.2rem; font-weight: 800; color: #111e2e; margin-bottom: 20px; letter-spacing: 0.02em;" data-i18n="about_title">ABOUT VISION FOCUS</h2>
          <p style="font-size: 1.05rem; line-height: 1.8; color: #475569;" data-i18n="about_desc">
            Founded in 2016 by Mr. Jason Shi, Vision Focus acts as a trusted bridge between Indonesian clients and reliable factories in China. With offices in Surabaya, Jakarta, and Foshan (China), we specialize in sourcing high-quality building and interior materials—from granite tiles and mosaics to stainless steel panels—at competitive prices.<br><br>
            We are more than just a trader. Backed by strong business networks and deep understanding of Chinese work culture, our team delivers end-to-end solutions: from product sourcing and design to quality control and logistics—efficiently, transparently, and reliably.
          </p>
          <div style="margin-top: 24px;">
            <a href="about.html" class="btn btn-outline-gold" style="padding: 10px 22px;">Read Full Company Story →</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================
       SECTION: WHY CHOOSE US
       ========================================== -->
  <section class="why-section-clear" id="why-choose-us" style="padding: 70px 0; background: #fbfbfc; border-top: 1px solid #f1f5f9;">
    <div class="container">
      <div class="why-clean-header">
        <h2 class="why-clean-title" data-i18n="why_title">WHY CHOOSE US</h2>
        <p class="why-clean-sub1" data-i18n="why_sub1">Want to do business with China? But having difficulties?</p>
        <p class="why-clean-sub2" data-i18n="why_sub2">WE ARE THE SOLUTIONS!</p>
      </div>

      <div class="why-cards-grid">
        <div class="why-card-clear">
          <div class="why-card-icon-wrap">
            <img src="assets/ICON/group-chat.png" alt="Professional Teams Icon">
          </div>
          <p class="why-card-text" data-i18n="why_card1">
            We have professional teams both in Indonesia and China, making it easier for you to communicate.
          </p>
        </div>

        <div class="why-card-clear">
          <div class="why-card-icon-wrap">
            <img src="assets/ICON/handshake.png" alt="Partnership Icon">
          </div>
          <p class="why-card-text" data-i18n="why_card2">
            We partner with reputable manufacturers and suppliers who share our commitment to excellences.
          </p>
        </div>

        <div class="why-card-clear">
          <div class="why-card-icon-wrap">
            <img src="assets/ICON/distribution-network.png" alt="Customer Satisfaction Icon">
          </div>
          <p class="why-card-text" data-i18n="why_card3">
            We prioritize our customer satisfaction above all else from product selection to delivery!
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================
       SECTION: BRAND COLLABORATIONS
       ========================================== -->
  <section class="brands-section-clear" id="brand-collaborations" style="padding: 50px 0 60px;">
    <div class="container">
      <h3 class="brands-title" data-i18n="brands_title">OUR BRAND COLLABORATIONS</h3>
      <div class="brands-logos-grid">
        <div class="brand-logo-item">
          <img src="assets/logo/Shun jia xing 固特森LOGO商免版-转曲.png" alt="GREATESON Stainless Steel">
        </div>
        <div class="brand-logo-item">
          <img src="assets/logo/EMD Windoor.png" alt="EMD Windoor">
        </div>
        <div class="brand-logo-item">
          <img src="assets/logo/88.png" alt="88 Premium Decorative">
        </div>
        <div class="brand-logo-item">
          <img src="assets/logo/deco deco.png" alt="Deco Deco Resin Glass">
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================
       SECTION: OUR SERVICE (CONCISE SPLIT BANNER)
       ========================================== -->
  <section class="service-section" id="service" style="padding: 70px 0 60px; background: #ffffff; border-top: 1px solid #f1f5f9;">
    <div class="container" style="text-align: center; margin-bottom: 40px;">
      <h2 style="font-size: 2.3rem; font-weight: 800; font-style: italic; color: #c89b53; margin-bottom: 10px;" data-i18n="service_title">OUR SERVICE</h2>
      <p style="font-size: 1.15rem; color: #475569;" data-i18n="service_sub">Bridging Opportunities Between Indonesia and China</p>
    </div>

    <!-- 2 Split Gateway Banners -->
    <div class="service-split-grid">
      <!-- The Gate to Indonesia -->
      <div class="service-split-card" id="gate-indonesia">
        <img src="assets/images/developer.jpg" alt="The Gate to Indonesia" class="service-split-bg">
        <div class="service-split-overlay"></div>
        <div class="service-split-content">
          <h3 class="service-split-title" data-i18n="service_indo_title">THE GATE TO INDONESIA</h3>
          <div class="service-split-sub">ONE <span class="stop">STOP</span> SOLUTION</div>
          <div class="service-split-target" data-i18n="service_indo_target">FOR CHINA SUPPLIER</div>
          <a href="solutions.html#gate-indonesia" class="btn-clear-white">LEARN MORE →</a>
        </div>
      </div>

      <!-- The Gate to China -->
      <div class="service-split-card" id="gate-china">
        <img src="assets/images/project-commercial.jpg" alt="The Gate to China" class="service-split-bg">
        <div class="service-split-overlay"></div>
        <div class="service-split-content">
          <h3 class="service-split-title" data-i18n="service_china_title">THE GATE TO CHINA</h3>
          <div class="service-split-sub">ONE <span class="stop">STOP</span> SOLUTION</div>
          <div class="service-split-target" data-i18n="service_china_target">FOR INDONESIA CUSTOMER</div>
          <a href="solutions.html#gate-china" class="btn-clear-white">LEARN MORE →</a>
        </div>
      </div>
    </div>

    <div style="text-align: center; margin-top: 40px;">
      <a href="solutions.html" class="btn btn-gold" style="padding: 12px 28px;">
        EXPLORE ALL SUPPLY CHAIN SERVICES & GZDW →
      </a>
    </div>
  </section>

  <!-- ==========================================
       SECTION: PROJECT REFERENCE (COMPACT PREVIEW)
       ========================================== -->
  <section class="projects-section" id="projects" style="padding: 70px 0; background: #fbfbfc; border-top: 1px solid #f1f5f9;">
    <div class="container">
      <div class="solutions-header-row">
        <div>
          <span class="section-tag">PROVEN TRACK RECORD</span>
          <h2 class="section-title">PROJECT REFERENCE</h2>
          <p class="section-subtitle">
            Reliable materials procurement for prestigious hospitality, commercial towers, retail supermarket chains, and upscale residences.
          </p>
        </div>
        <div>
          <a href="projects.html" class="btn-link-gold" style="font-size: 0.95rem;">View All Projects →</a>
        </div>
      </div>

      <div class="projects-grid">
        <a href="projects.html#retail" class="project-item-card">
          <div class="project-card-thumb">
            <span class="project-card-tag">Retail Sourcing</span>
            <img src="assets/images/project-retail.jpg" alt="National Retail Chain Store Fitout">
          </div>
          <div class="project-card-body">
            <h4>National Supermarket Network Fitout</h4>
            <p>Commercial shelving, LED checkout systems, and refrigeration fixtures across 45+ locations.</p>
            <div class="project-specs-list">
              <span>Scope: Store Systems</span>
              <span class="project-card-link-badge">View Case Study →</span>
            </div>
          </div>
        </a>

        <a href="projects.html#hospitality" class="project-item-card">
          <div class="project-card-thumb">
            <span class="project-card-tag">Hospitality</span>
            <img src="assets/images/project-hospitality.jpg" alt="5-Star Luxury Resort & Hotel">
          </div>
          <div class="project-card-body">
            <h4>5-Star Beachfront Luxury Resort</h4>
            <p>Large format 800x1600mm porcelain slabs, handcrafted pool mosaics, and brass hardware.</p>
            <div class="project-specs-list">
              <span>Scope: FF&E Finishes</span>
              <span class="project-card-link-badge">View Case Study →</span>
            </div>
          </div>
        </a>

        <a href="projects.html#commercial" class="project-item-card">
          <div class="project-card-thumb">
            <span class="project-card-tag">Commercial</span>
            <img src="assets/images/project-commercial.jpg" alt="Grade-A Corporate Tower">
          </div>
          <div class="project-card-body">
            <h4>Grade-A Financial Tower</h4>
            <p>Architectural PVD mirror stainless steel elevator paneling and custom lobby finishes.</p>
            <div class="project-specs-list">
              <span>Scope: Façade & Interior</span>
              <span class="project-card-link-badge">View Case Study →</span>
            </div>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- ==========================================
       SECTION: EVENTS (COMPACT 6-PHOTO PREVIEW)
       ========================================== -->
  <section class="event-gallery-section" id="events" style="padding: 70px 0 80px;">
    <div class="container">
      <div class="event-gallery-header">
        <span class="section-tag" style="justify-content: center;">EXHIBITIONS & INDUSTRY MOMENTS</span>
        <h2 style="font-size: 2.2rem; font-weight: 800; color: #111e2e; margin: 10px 0 12px;" data-i18n="events_title">EVENTS & EXHIBITIONS</h2>
        <p style="color: #64748b; font-size: 1rem;" data-i18n="events_sub">IndoBuildTech 2025 & Global Design Delegations</p>
      </div>

      <!-- Curated 6-Photo Grid on Home -->
      <div class="event-gallery-grid">
        <div class="event-photo-tile">
          <img src="assets/IBT 2025/PHOTO/1.JPG" alt="VF Indonesia China, Okabe, EMD & Greateson Team" loading="lazy">
          <div class="event-photo-caption">VF Indonesia China, Okabe, EMD & Greateson Team</div>
        </div>
        <div class="event-photo-tile">
          <img src="assets/IBT 2025/PHOTO/2.JPG" alt="With Mrs. Patricia Gouw (Public Figure)" loading="lazy">
          <div class="event-photo-caption">With Mrs. Patricia Gouw (Public Figure)</div>
        </div>
        <div class="event-photo-tile">
          <img src="assets/IBT 2025/PHOTO/3.JPG" alt="With Mr. William K. Patty from Grahacipta Hadiprana" loading="lazy">
          <div class="event-photo-caption">With Mr. William K. Patty from Grahacipta Hadiprana</div>
        </div>
        <div class="event-photo-tile">
          <img src="assets/IBT 2025/PHOTO/4.JPG" alt="With Mr. Noto Sugondo from Paramount Group" loading="lazy">
          <div class="event-photo-caption">With Mr. Noto Sugondo from Paramount Group</div>
        </div>
        <div class="event-photo-tile">
          <img src="assets/IBT 2025/PHOTO/5.JPG" alt="With Representative from Paramount Group" loading="lazy">
          <div class="event-photo-caption">With Representative from Paramount Group</div>
        </div>
        <div class="event-photo-tile">
          <img src="assets/IBT 2025/PHOTO/6.JPG" alt="With Owner and Representative from Depo Bangunan" loading="lazy">
          <div class="event-photo-caption">With Owner and Representative from Depo Bangunan</div>
        </div>
      </div>

      <div style="text-align: center; margin-top: 36px;">
        <a href="events.html" class="btn btn-gold" style="padding: 12px 28px;">
          EXPLORE COMPLETE 18-PHOTO GALLERY & RECAPS →
        </a>
      </div>
    </div>
  </section>

{footer_part}
"""

with open('index.html', 'w') as f:
    f.write(home_content)
print("Updated index.html (compact & clean)")

# -------------------------------------------------------------
# 2. COMPLETE SOLUTIONS.HTML (Service Page)
# -------------------------------------------------------------
sol_header = header_part.replace('href="index.html" class="nav-link-item active"', 'href="index.html" class="nav-link-item"')
sol_header = sol_header.replace('href="#service" class="nav-link-item"', 'href="solutions.html" class="nav-link-item active"')

solutions_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Our Services & Solutions | Vision Focus</title>
  <meta name="description" content="Comprehensive supply chain management, direct China factory sourcing, and official Guangzhou Design Week strategic partnership.">
  <link rel="icon" type="image/png" href="assets/logo/VISION FOCUS LOGO FIX SOFT GOLD.png">
  <link rel="stylesheet" href="css/main.css">
</head>
<body>
{sol_header}

  <section class="page-hero-section">
    <div class="hero-background-wrapper">
      <img src="assets/GuangZhou.png" alt="Guangzhou Pearl River Canton Tower Skyline" class="hero-background-img">
    </div>
    <div class="hero-overlay"></div>
    <div class="container" style="position: relative; z-index: 3;">
      <div class="page-hero-content" style="text-align: center; max-width: 800px; margin: 0 auto;">
        <span class="page-hero-eyebrow" style="color: #dfb76c;">COMPREHENSIVE TRADE SOLUTIONS</span>
        <h1 class="page-hero-title" style="color: #ffffff;">Our Supply Chain Services</h1>
        <p class="page-hero-subtitle" style="color: #f1f5f9;">Bridging Opportunities Between Indonesia and China with End-to-End Procurement Excellence.</p>
      </div>
    </div>
  </section>

  <main style="background: #ffffff;">
    <!-- 2 Split Gateway Banners -->
    <section class="service-split-grid" style="margin-bottom: 70px;">
      <div class="service-split-card" id="gate-indonesia">
        <img src="assets/images/developer.jpg" alt="The Gate to Indonesia" class="service-split-bg">
        <div class="service-split-overlay"></div>
        <div class="service-split-content">
          <h3 class="service-split-title">THE GATE TO INDONESIA</h3>
          <div class="service-split-sub">ONE <span class="stop">STOP</span> SOLUTION</div>
          <div class="service-split-target">FOR CHINA SUPPLIER</div>
          <p style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.6; margin-bottom: 20px;">
            One-stop market entry for Chinese manufacturers looking to distribute in Indonesia. We provide project partnerships, showroom placement, and local distribution channels.
          </p>
          <a href="#gzdw-partnership" class="btn-clear-white">LEARN MORE →</a>
        </div>
      </div>

      <div class="service-split-card" id="gate-china">
        <img src="assets/images/project-commercial.jpg" alt="The Gate to China" class="service-split-bg">
        <div class="service-split-overlay"></div>
        <div class="service-split-content">
          <h3 class="service-split-title">THE GATE TO CHINA</h3>
          <div class="service-split-sub">ONE <span class="stop">STOP</span> SOLUTION</div>
          <div class="service-split-target">FOR INDONESIA CUSTOMER</div>
          <p style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.6; margin-bottom: 20px;">
            Connecting Indonesian businesses directly with tier-1 Chinese factories. Full support from material specification and factory audits to customs clearance and delivery.
          </p>
          <a href="#supply-chain" class="btn-clear-white">LEARN MORE →</a>
        </div>
      </div>
    </section>

    <!-- GZDW Strategic Partnership -->
    <section class="container" id="gzdw-partnership" style="margin-bottom: 80px;">
      <div style="display: grid; grid-template-columns: 1fr 280px; gap: 40px; align-items: center; margin-bottom: 60px;">
        <div>
          <h3 style="font-size: 1.7rem; font-weight: 800; font-style: italic; color: #c89b53; margin-bottom: 16px; line-height: 1.3;">
            STRATEGIC PARTNER OF GUANGZHOU DESIGN WEEK IN INDONESIA
          </h3>
          <p style="font-size: 1.05rem; line-height: 1.8; color: #475569;">
            As the official registered partner of Guangzhou Design Week (GZDW), we are committed to building an enduring bridge between China and Indonesia in design exhibitions and architectural innovations. Through this collaboration, we connect Chinese suppliers directly with Indonesia's booming market demand for high-quality building and interior materials.
          </p>
        </div>
        <div style="text-align: center;">
          <img src="assets/logo/GZDW as strategic partner.png" alt="GZDW Strategic Partner Badge" style="max-height: 160px; margin: 0 auto;">
        </div>
      </div>

      <!-- About GZDW -->
      <div style="display: grid; grid-template-columns: 360px 1fr; gap: 50px; align-items: center; background: #fbfbfc; border: 1px solid #f1f5f9; border-radius: 16px; padding: 40px; margin-bottom: 70px;">
        <div>
          <img src="assets/gzdw.png" alt="Guangzhou Design Week Exhibition" style="border-radius: 12px; width: 100%; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
        </div>
        <div>
          <h4 style="font-size: 1.45rem; font-weight: 800; font-style: italic; color: #c89b53; margin-bottom: 16px;">
            ABOUT GUANGZHOU DESIGN WEEK (GZDW)
          </h4>
          <p style="font-size: 0.98rem; line-height: 1.8; color: #475569;">
            Guangzhou Design Week has been the top design forum in China for the home furnishing and decoration industry. Jointly sponsored and promoted by FL-EXPO and CODA since 2007. For 18 years, GZDW has grown into the premier design event in Asia, exploring cross-border integration for designers worldwide.
          </p>
        </div>
      </div>

      <!-- What We Offer: 3 Cards -->
      <div style="text-align: center; margin-bottom: 40px;">
        <h3 style="font-size: 2rem; font-weight: 800; color: #c89b53;">WHAT WE OFFER</h3>
      </div>
      <div class="why-cards-grid" style="margin-bottom: 70px;">
        <div class="why-card-clear" style="align-items: flex-start; text-align: left;">
          <div class="why-card-icon-wrap">
            <img src="assets/ICON/group-chat.png" alt="Representative Office">
          </div>
          <h4 style="font-size: 1.15rem; font-weight: 700; color: #c89b53; margin-bottom: 14px;">REPRESENTATIVE OFFICE</h4>
          <ul style="color: #475569; font-size: 0.92rem; line-height: 2; margin-left: 20px;">
            <li>Market Surveys & Feasibility Studies</li>
            <li>Business Events & Networking</li>
            <li>Social Media & Brand Management</li>
            <li>Legal Documentation & Compliance</li>
            <li>Full Customer Support & Desk</li>
            <li>Operational Guidelines</li>
          </ul>
        </div>

        <div class="why-card-clear" style="align-items: flex-start; text-align: left;">
          <div class="why-card-icon-wrap">
            <img src="assets/ICON/TRANSPARANCY.png" alt="Import & Service">
          </div>
          <h4 style="font-size: 1.15rem; font-weight: 700; color: #c89b53; margin-bottom: 14px;">IMPORT & SERVICE</h4>
          <ul style="color: #475569; font-size: 0.92rem; line-height: 2; margin-left: 20px;">
            <li>Accurate Tax & Duty Calculations</li>
            <li>Official Indonesian Import Licenses</li>
            <li>Customs & Shipping Documents Clearance</li>
            <li>Tanjung Priok & Tanjung Perak Port Handling</li>
            <li>Installation Backup & Technical Advisory</li>
          </ul>
        </div>

        <div class="why-card-clear" style="align-items: flex-start; text-align: left;">
          <div class="why-card-icon-wrap">
            <img src="assets/ICON/handshake.png" alt="Supporting Order">
          </div>
          <h4 style="font-size: 1.15rem; font-weight: 700; color: #c89b53; margin-bottom: 14px;">SUPPORTING ORDER</h4>
          <ul style="color: #475569; font-size: 0.92rem; line-height: 2; margin-left: 20px;">
            <li>Strong Project Tenderer Connections</li>
            <li>Primary Project Sourcing Allocation</li>
            <li>Hotel & Resort FF&E Procurement</li>
            <li>Joint Venture Investment Channels</li>
            <li>Full-Time Onsite Quality Check Service</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Supply Chain Management (Before, During, After) -->
    <section id="supply-chain" style="padding: 70px 0; background: #fbfbfc; border-top: 1px solid #f1f5f9;">
      <div class="container">
        <div style="text-align: center; max-width: 750px; margin: 0 auto 50px;">
          <span class="section-tag" style="justify-content: center;">PROCUREMENT WORKFLOW</span>
          <h2 style="font-size: 2.2rem; font-weight: 800; color: #111e2e; margin-bottom: 10px;">Supply Chain Management</h2>
          <p style="color: #64748b; font-size: 1rem;">For Hospitals, Schools, Hotels, Corporate Offices, and Commercial Landmarks</p>
        </div>

        <div class="why-cards-grid" style="margin-bottom: 60px;">
          <div class="why-card-clear" style="align-items: flex-start; text-align: left;">
            <div class="why-card-icon-wrap">
              <img src="assets/ICON/before.png" alt="Before Production">
            </div>
            <h4 style="font-size: 1.25rem; font-weight: 800; color: #c89b53; margin-bottom: 12px;">BEFORE</h4>
            <ul style="color: #475569; font-size: 0.92rem; line-height: 1.8; margin-left: 20px;">
              <li>Factory Pre-Selection (Verified & reliable sources)</li>
              <li>Onsite Factory Survey in Foshan & Guangdong</li>
              <li>Material Sampling & Technical Specifications</li>
              <li>Import Regulations & Tariffs Consultation</li>
            </ul>
          </div>

          <div class="why-card-clear" style="align-items: flex-start; text-align: left;">
            <div class="why-card-icon-wrap">
              <img src="assets/ICON/during.png" alt="During Production">
            </div>
            <h4 style="font-size: 1.25rem; font-weight: 800; color: #c89b53; margin-bottom: 12px;">DURING</h4>
            <ul style="color: #475569; font-size: 0.92rem; line-height: 1.8; margin-left: 20px;">
              <li>Inline Production Monitoring & Quality Control</li>
              <li>Pre-Shipment Container Loading Count Checks</li>
              <li>Export Customs Clearance at Chinese Ports</li>
              <li>Ocean Freight Forwarding & Insurance</li>
              <li>Indonesian Customs & Port Handling</li>
            </ul>
          </div>

          <div class="why-card-clear" style="align-items: flex-start; text-align: left;">
            <div class="why-card-icon-wrap">
              <img src="assets/ICON/after.png" alt="After Delivery">
            </div>
            <h4 style="font-size: 1.25rem; font-weight: 800; color: #c89b53; margin-bottom: 12px;">AFTER</h4>
            <ul style="color: #475569; font-size: 0.92rem; line-height: 1.8; margin-left: 20px;">
              <li>Safe Onsite Job Delivery Coordination</li>
              <li>Installation Advisory & PM Supervision</li>
              <li>After-Sales Service & Spare Parts Sourcing</li>
              <li>Repeat Order Management & Warranty Resolution</li>
            </ul>
          </div>
        </div>

        <!-- Benefits Grid -->
        <div style="text-align: center; margin-bottom: 40px;">
          <h3 style="font-size: 1.8rem; font-weight: 800; color: #c89b53;">BENEFITS FOR OUR CLIENTS</h3>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px;">
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; text-align: center;">
            <img src="assets/ICON/benefit (1).png" alt="Reliable Factory" style="height: 48px; margin: 0 auto 14px;">
            <h5 style="font-size: 1rem; font-weight: 700; color: #111e2e; margin-bottom: 8px;">Reliable Factories</h5>
            <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6;">Direct access to vetted tier-1 factories filtered by capacity and quality.</p>
          </div>
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; text-align: center;">
            <img src="assets/ICON/LOW_RISK.png" alt="Low Risk" style="height: 48px; margin: 0 auto 14px;">
            <h5 style="font-size: 1rem; font-weight: 700; color: #111e2e; margin-bottom: 8px;">Low Risk</h5>
            <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6;">We guide documentation and clearance to prevent re-export or port delays.</p>
          </div>
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; text-align: center;">
            <img src="assets/ICON/benefit (4).png" alt="Value & Trust" style="height: 48px; margin: 0 auto 14px;">
            <h5 style="font-size: 1rem; font-weight: 700; color: #111e2e; margin-bottom: 8px;">Value & Trust</h5>
            <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6;">Pre-agreed quality standards strictly audited before container sealing.</p>
          </div>
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; text-align: center;">
            <img src="assets/ICON/benefit (5).png" alt="Taxation Compliance" style="height: 48px; margin: 0 auto 14px;">
            <h5 style="font-size: 1rem; font-weight: 700; color: #111e2e; margin-bottom: 8px;">Tax Compliance</h5>
            <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6;">Official Indonesian tax invoices (Faktur Pajak) for seamless bookkeeping.</p>
          </div>
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; text-align: center;">
            <img src="assets/ICON/benefit (2).png" alt="Installation" style="height: 48px; margin: 0 auto 14px;">
            <h5 style="font-size: 1rem; font-weight: 700; color: #111e2e; margin-bottom: 8px;">Installation Support</h5>
            <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6;">Factory PM supervision and technical training during onsite installation.</p>
          </div>
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; text-align: center;">
            <img src="assets/ICON/benefit.png" alt="After Sales" style="height: 48px; margin: 0 auto 14px;">
            <h5 style="font-size: 1rem; font-weight: 700; color: #111e2e; margin-bottom: 8px;">After-Sales Service</h5>
            <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6;">Direct factory representation for repeat orders, spare parts, and warranties.</p>
          </div>
        </div>

        <!-- WhatsApp CTA -->
        <div style="text-align: center; margin-top: 50px;">
          <a href="https://wa.me/628113188878?text=Hello%20Vision%20Focus%2C%20I%20would%20like%20to%20discuss%20supply%20chain%20services" target="_blank" class="btn-clear-wa" style="padding: 15px 32px; font-size: 1rem;">
            DISCUSS SOURCING VIA WHATSAPP (+62 811-3188-878)
          </a>
        </div>
      </div>
    </section>
  </main>

{footer_part}
"""

with open('solutions.html', 'w') as f:
    f.write(solutions_page)
print("Updated solutions.html (complete services & GZDW)")

# -------------------------------------------------------------
# 3. COMPLETE ABOUT.HTML
# -------------------------------------------------------------
ab_header = header_part.replace('href="index.html" class="nav-link-item active"', 'href="index.html" class="nav-link-item"')
ab_header = ab_header.replace('href="#about" class="nav-link-item"', 'href="about.html" class="nav-link-item active"')

about_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About Us | Vision Focus</title>
  <meta name="description" content="Founded in 2016 by Mr. Jason Shi, Vision Focus is the trusted bridge connecting Indonesian clients with reliable factories in China.">
  <link rel="icon" type="image/png" href="assets/logo/VISION FOCUS LOGO FIX SOFT GOLD.png">
  <link rel="stylesheet" href="css/main.css">
</head>
<body>
{ab_header}

  <section class="page-hero-section">
    <div class="hero-background-wrapper">
      <img src="assets/GuangZhou.png" alt="Guangzhou Pearl River Canton Tower Skyline" class="hero-background-img">
    </div>
    <div class="hero-overlay"></div>
    <div class="container" style="position: relative; z-index: 3;">
      <div class="page-hero-content" style="text-align: center; max-width: 800px; margin: 0 auto;">
        <span class="page-hero-eyebrow" style="color: #dfb76c;">ABOUT VISION FOCUS</span>
        <h1 class="page-hero-title" style="color: #ffffff;">Strategic Bridge Between China & Indonesia</h1>
        <p class="page-hero-subtitle" style="color: #f1f5f9;">Founded in 2016 by Mr. Jason Shi, empowering Indonesian businesses with direct Chinese manufacturing power and uncompromised quality assurance.</p>
      </div>
    </div>
  </section>

  <main style="background: #ffffff; padding: 80px 0;">
    <div class="container">
      <!-- Founder & Mission -->
      <div style="display: grid; grid-template-columns: 360px 1fr; gap: 60px; align-items: center; margin-bottom: 80px;">
        <div style="text-align: center;">
          <img src="assets/jason.JPG" alt="Vision Focus Founder Mr. Jason Shi" style="border-radius: 12px; box-shadow: 0 16px 36px rgba(17, 30, 46, 0.12); width: 100%; max-width: 340px; margin: 0 auto;">
          <div style="margin-top: 14px;">
            <h4 style="font-size: 1.15rem; font-weight: 700; color: #111e2e;">Mr. Jason Shi</h4>
            <span style="font-size: 0.85rem; color: #c89b53; font-weight: 600;">Founder & CEO</span>
          </div>
        </div>
        <div>
          <h2 style="font-size: 2.2rem; font-weight: 800; color: #111e2e; margin-bottom: 22px;">A Trusted Bridge Between Two Nations</h2>
          <p style="font-size: 1.05rem; line-height: 1.8; color: #475569; margin-bottom: 20px;">
            Founded in 2016 by Mr. Jason Shi, Vision Focus acts as a trusted bridge between Indonesian clients and reliable factories in China. With offices in Surabaya, Jakarta, and Foshan (China), we specialize in sourcing high-quality building and interior materials—from granite tiles and mosaics to stainless steel panels—at competitive prices.
          </p>
          <p style="font-size: 1.05rem; line-height: 1.8; color: #475569;">
            We are more than just a trader. Backed by strong business networks and deep understanding of Chinese work culture, our team delivers end-to-end solutions: from product sourcing and design to quality control and logistics—efficiently, transparently, and reliably.
          </p>
        </div>
      </div>

      <!-- Why Choose Us Cards -->
      <div style="text-align: center; margin-bottom: 40px;">
        <h3 style="font-size: 2rem; font-weight: 800; color: #c89b53;">WHY CHOOSE US</h3>
        <p style="color: #64748b; font-size: 1.05rem; margin-top: 6px;">Want to do business with China? But having difficulties? WE ARE THE SOLUTIONS!</p>
      </div>

      <div class="why-cards-grid" style="margin-bottom: 80px;">
        <div class="why-card-clear">
          <div class="why-card-icon-wrap">
            <img src="assets/ICON/group-chat.png" alt="Professional Teams">
          </div>
          <p class="why-card-text">
            We have professional teams both in Indonesia and China, making it easier for you to communicate.
          </p>
        </div>
        <div class="why-card-clear">
          <div class="why-card-icon-wrap">
            <img src="assets/ICON/handshake.png" alt="Reputable Manufacturers">
          </div>
          <p class="why-card-text">
            We partner with reputable manufacturers and suppliers who share our commitment to excellences.
          </p>
        </div>
        <div class="why-card-clear">
          <div class="why-card-icon-wrap">
            <img src="assets/ICON/distribution-network.png" alt="Customer Satisfaction">
          </div>
          <p class="why-card-text">
            We prioritize our customer satisfaction above all else from product selection to delivery!
          </p>
        </div>
      </div>

      <!-- Tri-City Physical Offices -->
      <div style="text-align: center; margin-bottom: 40px;">
        <h3 style="font-size: 2rem; font-weight: 800; color: #111e2e;">Our Tri-City Infrastructure</h3>
        <p style="color: #64748b; font-size: 1rem;">Direct permanent presence ensuring full accountability at every stage.</p>
      </div>

      <div class="why-cards-grid" style="margin-bottom: 70px;">
        <div class="why-card-clear" style="text-align: left; align-items: flex-start;">
          <h4 style="font-size: 1.25rem; font-weight: 700; color: #c89b53; margin-bottom: 8px;">China Partner Office</h4>
          <p style="color: #475569; font-size: 0.95rem; line-height: 1.7; margin-bottom: 14px;">
            Room 707, Building 2, Xingfa Building, Jihua Western Road, Chancheng District, Foshan Guangdong, China
          </p>
          <span style="font-size: 0.85rem; color: #94a3b8;">Daily factory audits &bull; In-line QC testing &bull; Container loading</span>
        </div>

        <div class="why-card-clear" style="text-align: left; align-items: flex-start;">
          <h4 style="font-size: 1.25rem; font-weight: 700; color: #c89b53; margin-bottom: 8px;">Surabaya Headquarters</h4>
          <p style="color: #475569; font-size: 0.95rem; line-height: 1.7; margin-bottom: 14px;">
            Pakuwon Tower Tunjungan Plaza 6, Lt. 23, Unit 02-03, Superblock, Tunjungan City, Surabaya
          </p>
          <span style="font-size: 0.85rem; color: #94a3b8;">Executive hub &bull; Tanjung Perak port operations &bull; Sampling showroom</span>
        </div>

        <div class="why-card-clear" style="text-align: left; align-items: flex-start;">
          <h4 style="font-size: 1.25rem; font-weight: 700; color: #c89b53; margin-bottom: 8px;">Jakarta Office</h4>
          <p style="color: #475569; font-size: 0.95rem; line-height: 1.7; margin-bottom: 14px;">
            Ruko 92 Avenix BSD, Blok E27, Sampora, Cisauk, Tangerang
          </p>
          <span style="font-size: 0.85rem; color: #94a3b8;">Developer relations &bull; National retail chains &bull; Project tenders</span>
        </div>
      </div>

      <!-- Brand Collaborations -->
      <div style="text-align: center; margin-bottom: 30px;">
        <h3 class="brands-title">OUR BRAND COLLABORATIONS</h3>
      </div>
      <div class="brands-logos-grid" style="margin-bottom: 60px;">
        <div class="brand-logo-item">
          <img src="assets/logo/Shun jia xing 固特森LOGO商免版-转曲.png" alt="GREATESON Stainless Steel">
        </div>
        <div class="brand-logo-item">
          <img src="assets/logo/EMD Windoor.png" alt="EMD Windoor">
        </div>
        <div class="brand-logo-item">
          <img src="assets/logo/88.png" alt="88 Premium Decorative">
        </div>
        <div class="brand-logo-item">
          <img src="assets/logo/deco deco.png" alt="Deco Deco Resin Glass">
        </div>
      </div>

      <!-- Action Button -->
      <div style="text-align: center;">
        <a href="https://wa.me/628113188878?text=Hello%20Vision%20Focus%2C%20I%20would%20like%20to%20discuss%20a%20partnership" target="_blank" class="btn-clear-wa" style="padding: 14px 32px;">
          CHAT WITH OUR TEAM ON WHATSAPP (+62 811-3188-878)
        </a>
      </div>
    </div>
  </main>

{footer_part}
"""

with open('about.html', 'w') as f:
    f.write(about_page)
print("Updated about.html (complete about page)")

# -------------------------------------------------------------
# 4. COMPLETE PROJECTS.HTML (Project Reference Page)
# -------------------------------------------------------------
pj_header = header_part.replace('href="index.html" class="nav-link-item active"', 'href="index.html" class="nav-link-item"')
pj_header = pj_header.replace('href="projects.html" class="nav-link-item"', 'href="projects.html" class="nav-link-item active"')

projects_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Project Reference & Portfolio | Vision Focus</title>
  <meta name="description" content="Explore Vision Focus verified procurement portfolio across retail supermarket chains, luxury beachfront resorts, commercial towers, and residential landmarks.">
  <link rel="icon" type="image/png" href="assets/logo/VISION FOCUS LOGO FIX SOFT GOLD.png">
  <link rel="stylesheet" href="css/main.css">
</head>
<body>
{pj_header}

  <section class="page-hero-section">
    <div class="hero-background-wrapper">
      <img src="assets/GuangZhou.png" alt="Guangzhou Pearl River Canton Tower Skyline" class="hero-background-img">
    </div>
    <div class="hero-overlay"></div>
    <div class="container" style="position: relative; z-index: 3;">
      <div class="page-hero-content" style="text-align: center; max-width: 800px; margin: 0 auto;">
        <span class="page-hero-eyebrow" style="color: #dfb76c;">VERIFIED TRACK RECORD</span>
        <h1 class="page-hero-title" style="color: #ffffff;">Project Reference & Portfolio</h1>
        <p class="page-hero-subtitle" style="color: #f1f5f9;">High-specification building materials, custom interior finishes, and retail systems delivered nationwide.</p>
      </div>
    </div>
  </section>

  <main style="padding: 70px 0 90px; background: #ffffff;">
    <div class="container">
      <div class="solutions-header-row" style="margin-bottom: 40px;">
        <div>
          <span class="section-tag">PORTFOLIO OVERVIEW</span>
          <h2 class="section-title">Verified Procurement Track Record</h2>
          <p class="section-subtitle">Delivering high-specification building materials, interior finishes, and retail systems for prestigious landmarks nationwide.</p>
        </div>
      </div>

      <div class="projects-grid" style="grid-template-columns: repeat(2, 1fr); gap: 30px; margin-bottom: 60px;">
        <!-- Project 1: Retail -->
        <div class="project-item-card" id="retail">
          <div class="project-card-thumb">
            <span class="project-card-tag">Retail Sourcing</span>
            <img src="assets/images/project-retail.jpg" alt="National Retail Chain Store Fitout">
          </div>
          <div class="project-card-body">
            <h4>National Supermarket Network Fitout</h4>
            <p>End-to-end procurement of commercial shelving, heavy-duty modular racking, LED checkout desks, and temperature-controlled chillers for 45+ retail supermarket locations across Indonesia.</p>
            <div class="project-specs-list" style="margin: 16px 0;">
              <span>Scope: Store Systems & Equipment</span>
              <span>Location: Java, Bali & Sumatra</span>
            </div>
            <a href="https://wa.me/628113188878?text=Hello%20Vision%20Focus%2C%20I%20am%20interested%20in%20Retail%20Supermarket%20Sourcing" target="_blank" class="btn btn-outline-gold" style="font-size: 0.85rem; padding: 8px 18px;">
              Inquire Retail Systems →
            </a>
          </div>
        </div>

        <!-- Project 2: Hospitality -->
        <div class="project-item-card" id="hospitality">
          <div class="project-card-thumb">
            <span class="project-card-tag">Hospitality & Hotels</span>
            <img src="assets/images/project-hospitality.jpg" alt="5-Star Luxury Resort & Hotel">
          </div>
          <div class="project-card-body">
            <h4>5-Star Beachfront Luxury Resort</h4>
            <p>Direct supply of large format 800x1600mm honed porcelain slabs, handcrafted iridescent pool mosaics, custom brushed titanium bathroom fixtures, and architectural decorative screens.</p>
            <div class="project-specs-list" style="margin: 16px 0;">
              <span>Scope: FF&E Materials & Mosaics</span>
              <span>Location: Bali & Lombok</span>
            </div>
            <a href="https://wa.me/628113188878?text=Hello%20Vision%20Focus%2C%20I%20am%20interested%20in%20Hospitality%20Materials%20Sourcing" target="_blank" class="btn btn-outline-gold" style="font-size: 0.85rem; padding: 8px 18px;">
              Inquire Hospitality Sourcing →
            </a>
          </div>
        </div>

        <!-- Project 3: Commercial -->
        <div class="project-item-card" id="commercial">
          <div class="project-card-thumb">
            <span class="project-card-tag">Commercial Towers</span>
            <img src="assets/images/project-commercial.jpg" alt="Grade-A Corporate Tower">
          </div>
          <div class="project-card-body">
            <h4>Grade-A Financial Tower Elevator & Lobby</h4>
            <p>Architectural PVD mirror-finish stainless steel panels (GREATESON), custom water-ripple elevator hall ceilings, acoustic composite cladding, and heavy-duty entry systems.</p>
            <div class="project-specs-list" style="margin: 16px 0;">
              <span>Scope: Stainless Steel & Façade</span>
              <span>Location: Jakarta CBD</span>
            </div>
            <a href="https://wa.me/628113188878?text=Hello%20Vision%20Focus%2C%20I%20am%20interested%20in%20Commercial%20Stainless%20Steel" target="_blank" class="btn btn-outline-gold" style="font-size: 0.85rem; padding: 8px 18px;">
              Inquire Commercial Sourcing →
            </a>
          </div>
        </div>

        <!-- Project 4: Residential -->
        <div class="project-item-card" id="residential">
          <div class="project-card-thumb">
            <span class="project-card-tag">Residential</span>
            <img src="assets/images/project-residential.jpg" alt="Luxury Residential Development">
          </div>
          <div class="project-card-body">
            <h4>Prestige Gated Community Master Residences</h4>
            <p>Multi-container supply of bookmatched calacatta porcelain tiles, slimline thermal-break aluminum windows (EMD Windoor), and high-security entrance door sets.</p>
            <div class="project-specs-list" style="margin: 16px 0;">
              <span>Scope: Windows & Porcelain Tiles</span>
              <span>Location: Surabaya Superblock</span>
            </div>
            <a href="https://wa.me/628113188878?text=Hello%20Vision%20Focus%2C%20I%20am%20interested%20in%20Residential%20Finishes" target="_blank" class="btn btn-outline-gold" style="font-size: 0.85rem; padding: 8px 18px;">
              Inquire Residential Sourcing →
            </a>
          </div>
        </div>
      </div>

      <!-- Action Card -->
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 45px; text-align: center; max-width: 800px; margin: 0 auto;">
        <h3 style="font-size: 1.6rem; font-weight: 800; color: #111e2e; margin-bottom: 12px;">Have a Bill of Quantities (BOQ) or Project Drawing?</h3>
        <p style="color: #64748b; font-size: 0.98rem; margin-bottom: 24px;">Send your specifications to our team for factory price benchmarking and sample delivery.</p>
        <a href="https://wa.me/628113188878?text=Hello%20Vision%20Focus%2C%20I%20have%20a%20project%20BOQ%20and%20would%20like%20a%20factory%20quote" target="_blank" class="btn-clear-wa" style="font-size: 1rem; padding: 14px 30px;">
          SUBMIT BOQ VIA WHATSAPP (+62 811-3188-878)
        </a>
      </div>
    </div>
  </main>

{footer_part}
"""

with open('projects.html', 'w') as f:
    f.write(projects_page)
print("Updated projects.html (complete project references)")

# -------------------------------------------------------------
# 5. COMPLETE EVENTS.HTML (Rich Photo Gallery Page)
# -------------------------------------------------------------
ev_header = header_part.replace('href="index.html" class="nav-link-item active"', 'href="index.html" class="nav-link-item"')
ev_header = ev_header.replace('href="#events" class="nav-link-item"', 'href="events.html" class="nav-link-item active"')

photos_18 = [
    ('assets/IBT 2025/PHOTO/1.JPG', 'VF Indonesia China, Okabe, EMD & Greateson Team'),
    ('assets/IBT 2025/PHOTO/2.JPG', 'With Mrs. Patricia Gouw (Public Figure)'),
    ('assets/IBT 2025/PHOTO/3.JPG', 'With Mr. William K. Patty from Grahacipta Hadiprana'),
    ('assets/IBT 2025/PHOTO/4.JPG', 'With Mr. Noto Sugondo from Paramount Group'),
    ('assets/IBT 2025/PHOTO/5.JPG', 'With Representative from Paramount Group'),
    ('assets/IBT 2025/PHOTO/6.JPG', 'With Owner and Representative from Depo Bangunan'),
    ('assets/IBT 2025/PHOTO/7.JPG', 'With Representative from Propan'),
    ('assets/IBT 2025/PHOTO/8.JPG', 'VIP Booth Consultation & Material Review'),
    ('assets/IBT 2025/PHOTO/9.JPG', 'IndoBuildTech 2025 Live Exhibition'),
    ('assets/IBT 2025/PHOTO/10.JPG', 'Architectural Surface Discussion'),
    ('assets/IBT 2025/PHOTO/11.JPG', 'EMD Windoor Product Showcase'),
    ('assets/IBT 2025/PHOTO/12.JPG', 'Stainless Steel Cladding Demonstration'),
    ('assets/IBT 2025/PHOTO/13.JPG', 'Deco Deco Resin Glass Presentation'),
    ('assets/IBT 2025/PHOTO/14.JPG', 'Factory Partner & Client Meeting'),
    ('assets/IBT 2025/PHOTO/15.JPG', 'Foshan Direct Procurement Discussion'),
    ('assets/IBT 2025/PHOTO/16.JPG', 'Material Specification Consultation'),
    ('assets/IBT 2025/PHOTO/17.JPG', 'Strategic Partnership Signing'),
    ('assets/IBT 2025/PHOTO/18.JPG', 'Vision Focus Exhibition Team')
]

gallery_tiles_html = ""
for src, cap in photos_18:
    gallery_tiles_html += f"""
        <div class="event-photo-tile">
          <img src="{src}" alt="{cap}" loading="lazy">
          <div class="event-photo-caption">{cap}</div>
        </div>"""

events_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Events & Industry Exhibitions | Vision Focus</title>
  <meta name="description" content="Explore Vision Focus events including IndoBuildTech Expo 2025, Guangzhou Design Week (GZDW) buyer delegations, and HomeLife trade fairs.">
  <link rel="icon" type="image/png" href="assets/logo/VISION FOCUS LOGO FIX SOFT GOLD.png">
  <link rel="stylesheet" href="css/main.css">
</head>
<body>
{ev_header}

  <section class="page-hero-section">
    <div class="hero-background-wrapper">
      <img src="assets/GuangZhou.png" alt="Guangzhou Pearl River Canton Tower Skyline" class="hero-background-img">
    </div>
    <div class="hero-overlay"></div>
    <div class="container" style="position: relative; z-index: 3;">
      <div class="page-hero-content" style="text-align: center; max-width: 800px; margin: 0 auto;">
        <span class="page-hero-eyebrow" style="color: #dfb76c;">GLOBAL INDUSTRY PRESENCE</span>
        <h1 class="page-hero-title" style="color: #ffffff;">Events & Exhibitions</h1>
        <p class="page-hero-subtitle" style="color: #f1f5f9;">Connecting international manufacturing innovations with Indonesian architecture and construction leaders.</p>
      </div>
    </div>
  </section>

  <main style="background: #ffffff; padding: 70px 0 90px;">
    <!-- Flagship IndoBuildTech 2025 Section -->
    <section class="container" style="margin-bottom: 70px;">
      <div style="background: #fbfbfc; border: 1px solid #f1f5f9; border-radius: 16px; padding: 40px; display: grid; grid-template-columns: 1fr 320px; gap: 40px; align-items: center;">
        <div>
          <span style="font-size: 0.8rem; color: #c89b53; font-weight: 700; text-transform: uppercase;">FLAGSHIP EXHIBITION RECAP</span>
          <h2 style="font-size: 2.2rem; font-weight: 800; color: #111e2e; margin: 8px 0 16px;">IndoBuildTech Expo 2025</h2>
          <p style="font-size: 1rem; color: #475569; line-height: 1.8; margin-bottom: 20px;">
            Held at the Indonesia Convention Exhibition (ICE) BSD City, Vision Focus presented architectural ceramic slabs, embossed PVD stainless steel systems (GREATESON), high-performance thermal break windows (EMD Windoor), and luxury decorative resin glass (DECO DECO). Over 8,000 developers, architects, and corporate clients visited our booth.
          </p>
          <a href="https://wa.me/628113188878?text=Hello%20Vision%20Focus%2C%20I%20would%20like%20to%20register%20for%20the%20next%20exhibition%20VIP%20pass" target="_blank" class="btn-clear-wa" style="padding: 12px 24px;">
            REGISTER FOR NEXT EXPO VIP PASS
          </a>
        </div>
        <div style="text-align: center;">
          <img src="assets/ibt banner.png" alt="IndoBuildTech Expo" style="border-radius: 12px; width: 100%; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
        </div>
      </div>
    </section>

    <!-- Massive 18 Photo Gallery -->
    <section class="container" style="margin-bottom: 80px;">
      <div style="text-align: center; max-width: 720px; margin: 0 auto 40px;">
        <span class="section-tag" style="justify-content: center;">FULL PHOTO MOSAIC</span>
        <h2 style="font-size: 2.2rem; font-weight: 800; color: #111e2e; margin: 10px 0 12px;">IndoBuildTech 2025 Photo Gallery</h2>
        <p style="color: #64748b; font-size: 1rem;">Click on any photo to view in high resolution with client and partner details.</p>
      </div>

      <div class="event-gallery-grid">
        {gallery_tiles_html}
      </div>
    </section>

    <!-- Guangzhou Design Week Delegation -->
    <section class="container" style="margin-bottom: 60px;">
      <div style="border-top: 1px solid #f1f5f9; padding-top: 60px; display: grid; grid-template-columns: 360px 1fr; gap: 50px; align-items: center;">
        <div>
          <img src="assets/gzdw.png" alt="Guangzhou Design Week Delegation" style="border-radius: 14px; width: 100%; box-shadow: 0 12px 30px rgba(0,0,0,0.1);">
        </div>
        <div>
          <span style="font-size: 0.8rem; color: #c89b53; font-weight: 700; text-transform: uppercase;">ANNUAL CHINA TOUR</span>
          <h3 style="font-size: 1.8rem; font-weight: 800; color: #111e2e; margin: 8px 0 16px;">The Architect's Sourcing Delegation to GZDW & Foshan</h3>
          <p style="color: #475569; font-size: 1rem; line-height: 1.8; margin-bottom: 20px;">
            Twice a year, Vision Focus hosts a curated 5-day VIP tour for Indonesian architects, interior designers, and property developers to visit world-leading factories in Foshan, Zhongshan, and Guangzhou, including exclusive access to the Guangzhou Design Week international pavilion.
          </p>
          <a href="https://wa.me/628113188878?text=Hello%20Vision%20Focus%2C%20I%20would%20like%20to%20inquire%20about%20the%20GZDW%20China%20Delegation%20Schedule" target="_blank" class="btn btn-gold" style="padding: 12px 24px;">
            INQUIRE GZDW DELEGATION SCHEDULE →
          </a>
        </div>
      </div>
    </section>
  </main>

{footer_part}
"""

with open('events.html', 'w') as f:
    f.write(events_page)
print("Updated events.html (rich 18-photo gallery & delegations)")

# -------------------------------------------------------------
# 6. COMPLETE CONTACT.HTML
# -------------------------------------------------------------
ct_header = header_part.replace('href="index.html" class="nav-link-item active"', 'href="index.html" class="nav-link-item"')

contact_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Us | Vision Focus</title>
  <meta name="description" content="Contact Vision Focus via WhatsApp, email, or visit our offices in Surabaya, Jakarta, and Foshan, China.">
  <link rel="icon" type="image/png" href="assets/logo/VISION FOCUS LOGO FIX SOFT GOLD.png">
  <link rel="stylesheet" href="css/main.css">
</head>
<body>
{ct_header}

  <section class="page-hero-section">
    <div class="hero-background-wrapper">
      <img src="assets/GuangZhou.png" alt="Guangzhou Pearl River Canton Tower Skyline" class="hero-background-img">
    </div>
    <div class="hero-overlay"></div>
    <div class="container" style="position: relative; z-index: 3;">
      <div class="page-hero-content" style="text-align: center; max-width: 800px; margin: 0 auto;">
        <span class="page-hero-eyebrow" style="color: #dfb76c;">DIRECT COMMUNICATION</span>
        <h1 class="page-hero-title" style="color: #ffffff;">Connect with Vision Focus</h1>
        <p class="page-hero-subtitle" style="color: #f1f5f9;">Direct consultation via WhatsApp with our procurement directors in Surabaya, Jakarta, and Foshan, China.</p>
        <div style="margin-top: 26px;">
          <a href="https://wa.me/628113188878?text=Hello%20Vision%20Focus%2C%20I%20would%20like%20to%20consult%20regarding%20sourcing%20services" target="_blank" rel="noopener noreferrer" class="btn-clear-wa" style="font-size: 1.05rem; padding: 15px 34px;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2zm.01 1.67c2.2 0 4.26.86 5.82 2.42a8.204 8.204 0 0 1 2.41 5.82c0 4.54-3.7 8.24-8.24 8.24-1.42 0-2.82-.37-4.06-1.08l-.29-.17-3.12.82.83-3.04-.19-.3a8.21 8.21 0 0 1-1.26-4.47c0-4.54 3.7-8.24 8.24-8.24zm4.52 11.64c-.25-.12-1.47-.72-1.7-.81-.23-.08-.39-.12-.56.12-.17.25-.64.81-.79.97-.14.17-.29.19-.54.07-.25-.12-1.05-.39-2-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.12-.14.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.4-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.23.25-.87.85-.87 2.08s.89 2.41 1.01 2.58c.12.17 1.75 2.67 4.24 3.75.59.26 1.05.41 1.41.53.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.07.15-1.18-.06-.11-.22-.18-.47-.3z"/></svg>
            CHAT DIRECTLY ON WHATSAPP (+62 811-3188-878)
          </a>
        </div>
      </div>
    </div>
  </section>

  <main style="padding: 80px 0; background: #ffffff;">
    <div class="container">
      <div style="text-align: center; max-width: 650px; margin: 0 auto 50px;">
        <span class="section-tag" style="justify-content: center;">OUR OFFICES</span>
        <h2 style="font-size: 2.2rem; font-weight: 800; color: #111e2e;">Our Tri-City Office Network</h2>
        <p style="color: #64748b; font-size: 1rem;">Visit our material galleries or schedule an in-person procurement meeting.</p>
      </div>

      <div class="why-cards-grid" style="margin-bottom: 60px;">
        <div class="why-card-clear" style="text-align: left; align-items: flex-start;">
          <div class="why-card-icon-wrap">
            <img src="assets/ICON/distribution-network.png" alt="China Partner">
          </div>
          <h4 style="font-size: 1.25rem; font-weight: 700; color: #c89b53; margin-bottom: 8px;">China Partner Office</h4>
          <p style="color: #475569; font-size: 0.95rem; line-height: 1.7; margin-bottom: 16px;">
            Room 707, Building 2, Xingfa Building, Jihua Western Road, Chancheng District, Foshan Guangdong, China
          </p>
          <span style="font-size: 0.85rem; color: #94a3b8;">Factory Audits &bull; QC Inspections &bull; Sourcing Coordination</span>
        </div>

        <div class="why-card-clear" style="text-align: left; align-items: flex-start;">
          <div class="why-card-icon-wrap">
            <img src="assets/ICON/group-chat.png" alt="Surabaya Office">
          </div>
          <h4 style="font-size: 1.25rem; font-weight: 700; color: #c89b53; margin-bottom: 8px;">Surabaya Office (HQ)</h4>
          <p style="color: #475569; font-size: 0.95rem; line-height: 1.7; margin-bottom: 16px;">
            Pakuwon Tower Tunjungan Plaza 6, Lt. 23, Unit 02-03, Superblock, Tunjungan City, Surabaya
          </p>
          <span style="font-size: 0.85rem; color: #94a3b8;">Operations Hub &bull; Port Coordination &bull; Material Showroom</span>
        </div>

        <div class="why-card-clear" style="text-align: left; align-items: flex-start;">
          <div class="why-card-icon-wrap">
            <img src="assets/ICON/handshake.png" alt="Jakarta Office">
          </div>
          <h4 style="font-size: 1.25rem; font-weight: 700; color: #c89b53; margin-bottom: 8px;">Jakarta Office</h4>
          <p style="color: #475569; font-size: 0.95rem; line-height: 1.7; margin-bottom: 16px;">
            Ruko 92 Avenix BSD, Blok E27, Sampora, Cisauk, Tangerang
          </p>
          <span style="font-size: 0.85rem; color: #94a3b8;">Capital Projects &bull; Client Relations &bull; Developer Advisory</span>
        </div>
      </div>

      <!-- Hotline banner -->
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 50px 30px; text-align: center; max-width: 800px; margin: 0 auto;">
        <h3 style="font-size: 1.7rem; font-weight: 800; color: #111e2e; margin-bottom: 12px;">Fast Response Hotline</h3>
        <p style="color: #64748b; font-size: 1rem; margin-bottom: 24px; max-width: 550px; margin-left: auto; margin-right: auto;">
          Contact our team directly on WhatsApp or email for immediate inquiry response.
        </p>
        <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
          <a href="https://wa.me/628113188878?text=Hello%20Vision%20Focus%2C%20I%20would%20like%20to%20inquire%20about%20procurement%20services" target="_blank" class="btn-clear-wa" style="font-size: 1rem;">
            START WHATSAPP CHAT
          </a>
          <a href="mailto:cs@visifokus.com" class="btn-clear-white" style="border: 1px solid #cbd5e1;">
            EMAIL CS@VISIFOKUS.COM
          </a>
        </div>
      </div>
    </div>
  </main>

{footer_part}
"""

with open('contact.html', 'w') as f:
    f.write(contact_page)
print("Updated contact.html (focused direct contact)")
