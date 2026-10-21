#!/usr/bin/env python3
import os

with open("/Users/mekari/Documents/Visifokus/generate_all.py", "r") as f:
    base = f.read()

header_template = base.split('HEADER_HTML = """')[1].split('"""\n\nFOOTER_HTML = """')[0]
footer_template = base.split('FOOTER_HTML = """')[1].split('"""\n\nprint("Building pages...")')[0]

def render_page(title, meta_desc, active_nav, eyebrow, hero_title, hero_subtitle, breadcrumb_label, body_content):
    header = header_template
    active_keys = ["ACTIVE_HOME", "ACTIVE_SOLUTIONS", "ACTIVE_PROJECTS", "ACTIVE_WORK", "ACTIVE_ABOUT", "ACTIVE_PRODUCT", "ACTIVE_INSIGHTS", "ACTIVE_CONTACT"]
    for k in active_keys:
        val = "active" if k == active_nav else ""
        header = header.replace("{" + k + "}", val)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Vision Focus</title>
  <meta name="description" content="{meta_desc}">
  <link rel="icon" type="image/png" href="assets/images/logo.png">
  <link rel="stylesheet" href="css/main.css">
</head>
<body>
{header}
  <!-- SUBPAGE HERO WITH CITY BACKGROUND -->
  <section class="page-hero-section">
    <div class="hero-background-wrapper">
      <img src="assets/images/guangzhou-hero.png" alt="Guangzhou Pearl River Canton Tower Skyline" class="hero-background-img">
    </div>
    <div class="hero-overlay"></div>

    <div class="container" style="position: relative; z-index: 3;">
      <div class="page-hero-content">
        <span class="page-hero-eyebrow">{eyebrow}</span>
        <h1 class="page-hero-title">{hero_title}</h1>
        <p class="page-hero-subtitle">{hero_subtitle}</p>
        <div class="page-breadcrumbs">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>{breadcrumb_label}</span>
        </div>
      </div>
    </div>
  </section>

  <!-- MAIN CONTENT -->
  <main>
    {body_content}
  </main>
{footer_template}"""
    return html

# 1. PROJECTS.HTML
projects_body = """
  <section class="projects-section" style="padding: 80px 0;">
    <div class="container">
      <div class="solutions-header-row">
        <div>
          <span class="section-tag">PROJECT REF</span>
          <h2 class="section-title">Verified Procurement Track Record</h2>
          <p class="section-subtitle">Delivering high-specification building materials, interior finishes, and retail systems for prestigious landmarks nationwide.</p>
        </div>
      </div>

      <div class="projects-filter-bar">
        <button type="button" class="filter-pill-btn active" data-filter="all">All Projects</button>
        <button type="button" class="filter-pill-btn" data-filter="commercial">Commercial</button>
        <button type="button" class="filter-pill-btn" data-filter="hospitality">Hospitality & Hotels</button>
        <button type="button" class="filter-pill-btn" data-filter="retail">Retail Chains</button>
        <button type="button" class="filter-pill-btn" data-filter="residential">Residential</button>
      </div>

      <div class="projects-grid">
        <div class="project-item-card" data-category="retail" id="retail">
          <div class="project-card-thumb">
            <span class="project-card-tag">Retail Sourcing</span>
            <img src="assets/images/project-retail.jpg" alt="Retail Store Fitout">
          </div>
          <div class="project-card-body">
            <h4>National Supermarket Network Fitout</h4>
            <p>End-to-end procurement of commercial shelving, LED checkout desks, and temperature-controlled chillers for 45+ retail locations across Indonesia.</p>
            <div class="project-specs-list"><span>Scope: Store Fixtures</span><span>Location: Nationwide</span></div>
          </div>
        </div>

        <div class="project-item-card" data-category="hospitality" id="hospitality">
          <div class="project-card-thumb">
            <span class="project-card-tag">Hospitality</span>
            <img src="assets/images/project-hospitality.jpg" alt="Luxury Hotel Resort">
          </div>
          <div class="project-card-body">
            <h4>5-Star Beachfront Luxury Resort</h4>
            <p>Direct supply of large format 800x1600mm honed porcelain, custom mosaic swimming pool tiles, and brushed brass bathroom fittings.</p>
            <div class="project-specs-list"><span>Scope: FF&E Materials</span><span>Location: Bali & Lombok</span></div>
          </div>
        </div>

        <div class="project-item-card" data-category="commercial" id="commercial">
          <div class="project-card-thumb">
            <span class="project-card-tag">Commercial</span>
            <img src="assets/images/project-commercial.jpg" alt="Grade-A Financial Tower">
          </div>
          <div class="project-card-body">
            <h4>Grade-A Financial Tower</h4>
            <p>Custom elevator hall claddings, 316-grade mirror stainless panels, and fire-resistant composite architectural panels.</p>
            <div class="project-specs-list"><span>Scope: Interior Paneling</span><span>Location: SCBD Jakarta</span></div>
          </div>
        </div>

        <div class="project-item-card" data-category="residential" id="residential">
          <div class="project-card-thumb">
            <span class="project-card-tag">Residential</span>
            <img src="assets/images/project-residential.jpg" alt="Luxury Residential Development">
          </div>
          <div class="project-card-body">
            <h4>High-End Residential Villas</h4>
            <p>Sourcing of bookmatched Calacatta sintered stone slabs, natural quartz counter surfaces, and frameless acoustic glass partitions.</p>
            <div class="project-specs-list"><span>Scope: Interior Finishes</span><span>Location: Surabaya West</span></div>
          </div>
        </div>

        <div class="project-item-card" data-category="commercial" id="healthcare">
          <div class="project-card-thumb">
            <span class="project-card-tag">Healthcare & Edu</span>
            <img src="assets/images/developer.jpg" alt="Modern Hospital Complex">
          </div>
          <div class="project-card-body">
            <h4>International Hospital Expansion</h4>
            <p>Antibacterial vinyl flooring, hygienic stainless steel wall protection, and sensored commercial scrub sinks.</p>
            <div class="project-specs-list"><span>Scope: Specialized Materials</span><span>Location: Surabaya</span></div>
          </div>
        </div>

        <div class="project-item-card" data-category="commercial" id="infrastructure">
          <div class="project-card-thumb">
            <span class="project-card-tag">Infrastructure</span>
            <img src="assets/images/logistics.jpg" alt="Modern Logistics Hub">
          </div>
          <div class="project-card-body">
            <h4>Logistics Center & Warehouse</h4>
            <p>Heavy-duty industrial floor coatings, high-bay LED floodlighting, and automated loading dock equipment.</p>
            <div class="project-specs-list"><span>Scope: Logistics Equipment</span><span>Location: Cikarang, West Java</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

with open("/Users/mekari/Documents/Visifokus/projects.html", "w") as f:
    f.write(render_page(
        "Project References",
        "Project procurement references and track record across hospitality, commercial towers, retail chains, and residential developments in Indonesia.",
        "ACTIVE_PROJECTS",
        "PROJECT REFERENCES",
        "From Concept to Completion",
        "Explore our proven procurement portfolio delivering high-specification building materials and commercial solutions across Indonesia.",
        "Projects",
        projects_body
    ))
print("Created projects.html")

# 2. HOW-WE-WORK.HTML
how_body = """
  <section class="how-it-works-section" style="padding: 80px 0;">
    <div class="container">
      <div style="text-align: center; max-width: 760px; margin: 0 auto 50px;">
        <span class="section-tag" style="justify-content: center;">PROCUREMENT METHODOLOGY</span>
        <h2 class="section-title">A Clear Process from Start to Success</h2>
        <p class="section-subtitle" style="margin: 12px auto 0;">
          Our 5-stage procurement framework guarantees transparency, uncompromised quality, and punctuality at every milestone.
        </p>
      </div>

      <div style="display: flex; flex-direction: column; gap: 40px;">
        <div id="step-1" style="display: grid; grid-template-columns: 120px 1fr 1fr; gap: 30px; background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; padding: 30px; align-items: center; box-shadow: var(--shadow-sm);">
          <div style="font-size: 3rem; font-weight: 800; color: var(--color-gold); font-family: var(--font-serif); text-align: center;">01</div>
          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin-bottom: 8px;">Understand Your Needs</h3>
            <p style="color: #64748b; line-height: 1.6;">We analyze your architectural drawings, bills of quantities (BOQ), technical tolerances, target budget, and required delivery timeline to determine the most competitive manufacturing route in China.</p>
          </div>
          <div style="height: 180px; border-radius: 8px; overflow: hidden;"><img src="assets/images/step-needs.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
        </div>

        <div id="step-2" style="display: grid; grid-template-columns: 120px 1fr 1fr; gap: 30px; background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; padding: 30px; align-items: center; box-shadow: var(--shadow-sm);">
          <div style="font-size: 3rem; font-weight: 800; color: var(--color-gold); font-family: var(--font-serif); text-align: center;">02</div>
          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin-bottom: 8px;">Source & Verify Factory Capacity</h3>
            <p style="color: #64748b; line-height: 1.6;">Our team stationed on the ground in Foshan and Guangzhou performs on-site audits of certified tier-1 factories. We examine production lines, verify ISO/CE/SNI credentials, and send physical sample boxes for your client approval.</p>
          </div>
          <div style="height: 180px; border-radius: 8px; overflow: hidden;"><img src="assets/images/step-source.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
        </div>

        <div id="step-3" style="display: grid; grid-template-columns: 120px 1fr 1fr; gap: 30px; background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; padding: 30px; align-items: center; box-shadow: var(--shadow-sm);">
          <div style="font-size: 3rem; font-weight: 800; color: var(--color-gold); font-family: var(--font-serif); text-align: center;">03</div>
          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin-bottom: 8px;">Procurement & Quality Control (QC)</h3>
            <p style="color: #64748b; line-height: 1.6;">During manufacturing, our engineers conduct continuous inline checks. We perform shade variation tests, dimensional checks, stress tests, and pre-packing inspections, ensuring zero defective units enter the container.</p>
          </div>
          <div style="height: 180px; border-radius: 8px; overflow: hidden;"><img src="assets/images/step-shipping.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
        </div>

        <div id="step-4" style="display: grid; grid-template-columns: 120px 1fr 1fr; gap: 30px; background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; padding: 30px; align-items: center; box-shadow: var(--shadow-sm);">
          <div style="font-size: 3rem; font-weight: 800; color: var(--color-gold); font-family: var(--font-serif); text-align: center;">04</div>
          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin-bottom: 8px;">Delivery & Port Clearance to Indonesia</h3>
            <p style="color: #64748b; line-height: 1.6;">Full international export packing with reinforced fumigated timber crates. We coordinate sea freight, bill of lading, Indonesian customs clearance, and inland delivery direct to your job site or warehouse.</p>
          </div>
          <div style="height: 180px; border-radius: 8px; overflow: hidden;"><img src="assets/images/step-delivery.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
        </div>

        <div id="step-5" style="display: grid; grid-template-columns: 120px 1fr 1fr; gap: 30px; background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; padding: 30px; align-items: center; box-shadow: var(--shadow-sm);">
          <div style="font-size: 3rem; font-weight: 800; color: var(--color-gold); font-family: var(--font-serif); text-align: center;">05</div>
          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin-bottom: 8px;">After-Sales & Continuous Replenishment</h3>
            <p style="color: #64748b; line-height: 1.6;">We supervise container de-stuffing, provide installation technical advisory, manage defect warranty replacements, and establish continuous repeat supply channels for multi-phase projects.</p>
          </div>
          <div style="height: 180px; border-radius: 8px; overflow: hidden;"><img src="assets/images/step-support.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
        </div>
      </div>
    </div>
  </section>
"""

with open("/Users/mekari/Documents/Visifokus/how-we-work.html", "w") as f:
    f.write(render_page(
        "How We Work",
        "Our 5-stage procurement framework guarantees transparency, quality, and on-time delivery from China to Indonesia.",
        "ACTIVE_WORK",
        "OUR METHODOLOGY",
        "A Clear Process from Start to Success",
        "Step-by-step transparency from initial technical specification to job-site delivery in Indonesia.",
        "How We Work",
        how_body
    ))
print("Created how-we-work.html")

# 3. ABOUT.HTML
about_body = """
  <section class="about-section" style="padding: 80px 0;">
    <div class="container">
      <div class="about-split-layout" id="ceo" style="margin-bottom: 80px;">
        <div class="about-visual-column">
          <div class="ceo-card-frame">
            <div class="ceo-photo-wrap" style="height: 520px;">
              <img src="assets/images/jason-ceo.jpg" alt="Mr. Jason Shi - Founder & CEO Vision Focus">
            </div>
            <div class="ceo-signature-badge">
              <h4>Mr. Jason Shi</h4>
              <p>Founder & Chief Executive Officer</p>
            </div>
          </div>
          <div class="founded-floating-badge">
            <span class="year">2016</span>
            <span class="label">ESTABLISHED</span>
          </div>
        </div>

        <div class="about-text-column" id="bridge">
          <span class="section-tag">COMPANY LEADERSHIP & HERITAGE</span>
          <h2 class="section-title">A Trusted Bridge Between Indonesia & China</h2>
          
          <p class="lead-quote">
            "Founded in 2016 by Mr. Jason Shi, Vision Focus acts as a trusted bridge between Indonesian clients and reliable factories in China. With offices in Surabaya, Jakarta, and Foshan (China), we specialize in sourcing high-quality building and interior materials—from granite tiles and mosaics to stainless steel panels—at competitive prices."
          </p>

          <p style="font-size: 0.95rem; color: #64748b; line-height: 1.7; margin-bottom: 24px;">
            Under the visionary leadership of Mr. Jason Shi, Vision Focus was established to dismantle the hurdles of cross-border procurement: language misunderstandings, fluctuating quality standards, and hidden middleman commissions. Today, our bi-national engineering and sourcing team offers seamless turnkey project solutions.
          </p>

          <div class="offices-tabs-container" id="offices">
            <div class="offices-tabs-nav">
              <button type="button" class="office-tab-btn active" data-target="officeSurabaya">Surabaya (HQ)</button>
              <button type="button" class="office-tab-btn" data-target="officeJakarta">Jakarta</button>
              <button type="button" class="office-tab-btn" data-target="officeFoshan">Foshan (China)</button>
            </div>

            <div class="office-pane-content active" id="officeSurabaya">
              <p><strong>Vision Focus Surabaya Headquarters:</strong></p>
              <p style="color: #64748b; margin-top: 6px;">Coordinating maritime logistics, port operations at Tanjung Perak, sample library showrooms, and enterprise customer service across Central and Eastern Indonesia.</p>
            </div>

            <div class="office-pane-content" id="officeJakarta">
              <p><strong>Vision Focus Jakarta Representative Office:</strong></p>
              <p style="color: #64748b; margin-top: 6px;">Focused on major developer project management, corporate real estate procurement, architectural consultancies, and national retail chains.</p>
            </div>

            <div class="office-pane-content" id="officeFoshan">
              <p><strong>Vision Focus Foshan / Guangdong Sourcing Hub:</strong></p>
              <p style="color: #64748b; margin-top: 6px;">Situated in the heart of China's ceramic and industrial manufacturing center, overseeing daily factory audits, production tracking, and container packing inspections.</p>
            </div>
          </div>
        </div>
      </div>

      <div id="compliance" style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 16px; padding: 50px; box-shadow: var(--shadow-sm);">
        <div style="text-align: center; max-width: 600px; margin: 0 auto 40px;">
          <span class="section-tag" style="justify-content: center;">OUR FOUNDATIONAL PILLARS</span>
          <h3 style="font-family: var(--font-serif); font-size: 1.8rem; color: var(--color-primary);">Why Industry Leaders Partner with Vision Focus</h3>
        </div>

        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px;">
          <div>
            <h4 style="color: var(--color-gold); font-size: 1.1rem; margin-bottom: 8px;">Zero Middleman Markups</h4>
            <p style="color: #64748b; font-size: 0.9rem; line-height: 1.6;">Direct manufacturer pricing with transparent volume discounting, ensuring true factory value without third-party broker markups.</p>
          </div>
          <div>
            <h4 style="color: var(--color-gold); font-size: 1.1rem; margin-bottom: 8px;">Stationed On-Site Engineers</h4>
            <p style="color: #64748b; font-size: 0.9rem; line-height: 1.6;">Our full-time inspectors in Foshan conduct physical inline testing and pre-shipment quality audits on every single order batch.</p>
          </div>
          <div>
            <h4 style="color: var(--color-gold); font-size: 1.1rem; margin-bottom: 8px;">Legal Import & SNI Mastery</h4>
            <p style="color: #64748b; font-size: 0.9rem; line-height: 1.6;">End-to-end management of Indonesian customs documentation, certificates of origin, SNI conformity, and safe delivery.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

with open("/Users/mekari/Documents/Visifokus/about.html", "w") as f:
    f.write(render_page(
        "About Us",
        "Founded in 2016 by Mr. Jason Shi, Vision Focus is the trusted bridge connecting Indonesian clients with reliable factories in China.",
        "ACTIVE_ABOUT",
        "ABOUT VISION FOCUS",
        "Strategic Bridge Between China & Indonesia",
        "Founded in 2016 by Mr. Jason Shi, empowering Indonesian businesses with direct Chinese manufacturing power and uncompromised quality assurance.",
        "About Us",
        about_body
    ))
print("Created about.html")

# 4. EVENTS.HTML
events_body = """
  <section class="how-it-works-section" style="padding: 80px 0;">
    <div class="container">
      <div style="text-align: center; max-width: 680px; margin: 0 auto 50px;">
        <span class="section-tag" style="justify-content: center;">EXHIBITIONS & CONFERENCES</span>
        <h2 class="section-title">Industry Presence & Trade Exhibitions</h2>
        <p class="section-subtitle" style="margin: 12px auto 0;">Connecting global manufacturing innovations with Indonesian architecture and construction leaders.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 30px;">
        <div id="ibt" style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 240px; overflow: hidden;"><img src="assets/images/step-needs.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
          <div style="padding: 30px;">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">UPCOMING FLAGSHIP EXPO</span>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin: 6px 0 12px;">IndoBuildTech Expo 2025</h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 18px;">Indonesia Convention Exhibition (ICE) BSD City. Visit Vision Focus to experience next-generation large porcelain slabs, antibacterial hospital surfaces, and textured architectural metal cladding.</p>
            <button type="button" class="btn btn-outline-gold open-quote-modal">Register for VIP Booth Access →</button>
          </div>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 240px; overflow: hidden;"><img src="assets/images/step-source.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
          <div style="padding: 30px;">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">PAST EVENT SHOWCASE</span>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin: 6px 0 12px;">IndoBuildTech Expo 2024</h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 18px;">Showcasing embossed PVD stainless steel panels and terrazzo collections to over 5,000 architects, developers, and interior designers from across Southeast Asia.</p>
            <a href="product-library.html" class="btn-link-gold">View Showcased Materials →</a>
          </div>
        </div>

        <div id="gzdw" style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 240px; overflow: hidden;"><img src="assets/images/guangzhou-hero.png" style="width: 100%; height: 100%; object-fit: cover;"></div>
          <div style="padding: 30px;">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">ANNUAL CHINA DELEGATION</span>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin: 6px 0 12px;">Guangzhou Design Week (GZDW)</h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 18px;">Guangzhou Poly World Trade Center & Nan Fung Expo. Vision Focus organizes exclusive buyer delegations for prominent Indonesian architects to tour world-leading factories in Foshan.</p>
            <a href="contact.html" class="btn-link-gold">Inquire Delegation Schedule →</a>
          </div>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 240px; overflow: hidden;"><img src="assets/images/logistics.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
          <div style="padding: 30px;">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">INTERNATIONAL TRADE FAIR</span>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin: 6px 0 12px;">HomeLife Indonesia Expo</h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 18px;">Jakarta International Expo (JIExpo) Kemayoran. Connecting top-tier manufacturers of hardware, lighting, sanitaryware, and building appliances directly with Indonesian distributors.</p>
            <button type="button" class="btn btn-gold open-quote-modal">Schedule Business Meeting →</button>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

with open("/Users/mekari/Documents/Visifokus/events.html", "w") as f:
    f.write(render_page(
        "Events & Exhibitions",
        "Explore Vision Focus events including IndoBuildTech, Guangzhou Design Week (GZDW), and HomeLife trade fairs.",
        "ACTIVE_ABOUT",
        "GLOBAL INDUSTRY EVENTS",
        "Events & Industry Exhibitions",
        "Showcasing next-generation building materials, architectural textures, and cross-border trade summits.",
        "Events",
        events_body
    ))
print("Created events.html")

# 5. PRODUCT-LIBRARY.HTML
products_body = """
  <section class="products-section" style="padding: 80px 0;">
    <div class="container">
      <div class="solutions-header-row">
        <div>
          <span class="section-tag">CURATED MATERIALS</span>
          <h2 class="section-title">Architectural Material Library</h2>
          <p class="section-subtitle">Direct from certified manufacturing centers in Foshan, Guangdong. Request physical sample boxes delivered directly to your studio.</p>
        </div>
        <div>
          <button type="button" class="btn btn-gold open-quote-modal">Request Sample Box →</button>
        </div>
      </div>

      <div class="products-grid-preview" style="margin-bottom: 60px;">
        <div class="product-tile">
          <div class="product-tile-img"><img src="assets/images/prod-granite.jpg" alt="Granite Tiles & Porcelain Slabs"></div>
          <div class="product-tile-info">
            <h5>Large Format Porcelain & Granite Slabs</h5>
            <p style="margin-bottom: 8px;">Available in 750x1500mm, 800x2600mm, and 1200x2700mm bookmatched formats for continuous vein wall and floor applications.</p>
            <span style="font-size: 0.76rem; color: var(--color-gold); font-weight: 700;">Honed, Polished, Soft-Matte</span>
          </div>
        </div>

        <div class="product-tile">
          <div class="product-tile-img"><img src="assets/images/prod-stainless.jpg" alt="Architectural Stainless Steel"></div>
          <div class="product-tile-info">
            <h5>Architectural Stainless Steel Panels</h5>
            <p style="margin-bottom: 8px;">Water ripple, mirror hairline, and embossed textures with PVD titanium vacuum plating in champagne gold, rose gold, and black.</p>
            <span style="font-size: 0.76rem; color: var(--color-gold); font-weight: 700;">Grade 304 & 316 Architectural</span>
          </div>
        </div>

        <div class="product-tile">
          <div class="product-tile-img"><img src="assets/images/prod-sanitary.jpg" alt="Commercial Sanitaryware"></div>
          <div class="product-tile-info">
            <h5>Commercial Sanitary & Hardware</h5>
            <p style="margin-bottom: 8px;">Commercial-grade sensor taps, water-saving wall-hung WCs, and architectural hardware engineered for high-traffic environments.</p>
            <span style="font-size: 0.76rem; color: var(--color-gold); font-weight: 700;">SNI & WaterMark Certified</span>
          </div>
        </div>
      </div>

      <div style="background: linear-gradient(135deg, #111e2e 0%, #1e334c 100%); border-radius: 16px; padding: 50px; color: #ffffff; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 30px;">
        <div style="max-width: 640px;">
          <span style="color: var(--color-gold); font-size: 0.8rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;">DESIGNER SERVICE</span>
          <h3 style="font-family: var(--font-serif); font-size: 2rem; margin: 8px 0 12px;">Need Physical Material Samples?</h3>
          <p style="color: #cbd5e1; line-height: 1.6;">We ship curated sample binders containing granite cuttings, stainless steel color chips, and tile swatches directly to your firm in Indonesia.</p>
        </div>
        <div>
          <button type="button" class="btn btn-gold open-quote-modal" style="padding: 16px 32px; font-size: 0.95rem;">ORDER SAMPLE BOX →</button>
        </div>
      </div>
    </div>
  </section>
"""

with open("/Users/mekari/Documents/Visifokus/product-library.html", "w") as f:
    f.write(render_page(
        "Product Library",
        "Curated material and product library from Vision Focus: large granite tiles, architectural stainless steel, mosaics, and sanitaryware.",
        "ACTIVE_PRODUCT",
        "CURATED MATERIALS",
        "Product & Material Library",
        "High-performance architectural surfaces, engineered stones, and decorative metals direct from China.",
        "Product Library",
        products_body
    ))
print("Created product-library.html")

# 6. INSIGHTS.HTML
insights_body = """
  <section class="products-section" style="padding: 80px 0;">
    <div class="container">
      <div class="solutions-header-row">
        <div>
          <span class="section-tag">KNOWLEDGE FOR SMARTER DECISIONS</span>
          <h2 class="section-title">Industry Intelligence & Sourcing Guides</h2>
          <p class="section-subtitle">In-depth market updates, regulatory guides, and strategic supply chain analysis from our bilingual teams in Foshan and Indonesia.</p>
        </div>
      </div>

      <div class="projects-grid">
        <div class="project-item-card" id="china-supply">
          <div class="project-card-thumb"><img src="assets/images/insights-featured.jpg" alt="China Supply Chain Update"></div>
          <div class="project-card-body">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700; text-transform: uppercase;">MARKET ANALYSIS</span>
            <h4 style="margin-top: 6px;">China Supply Chain Update 2026: Trends & Mandates</h4>
            <p>How factory automation and green building mandates in Guangdong are reshaping lead times and competitive pricing structures.</p>
            <div class="project-specs-list"><span>5 min read</span><span>Updated Oct 2026</span></div>
          </div>
        </div>

        <div class="project-item-card" id="how-to-source">
          <div class="project-card-thumb"><img src="assets/images/step-shipping.jpg" alt="How to Direct Source from China"></div>
          <div class="project-card-body">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700; text-transform: uppercase;">SOURCING GUIDE</span>
            <h4 style="margin-top: 6px;">Direct Factory Sourcing in Foshan: The Practical Guide</h4>
            <p>Essential checklist for evaluating manufacturer capabilities, payment escrow, bilingual contracts, and avoiding common pitfalls.</p>
            <div class="project-specs-list"><span>8 min read</span><span>Practical Guide</span></div>
          </div>
        </div>

        <div class="project-item-card" id="customs">
          <div class="project-card-thumb"><img src="assets/images/logistics.jpg" alt="Import Regulations & SNI Guide"></div>
          <div class="project-card-body">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700; text-transform: uppercase;">TRADE REGULATIONS</span>
            <h4 style="margin-top: 6px;">Navigating Indonesian Customs & SNI Certifications</h4>
            <p>A step-by-step roadmap for clearing building materials, understanding import tariffs, and container port handling in Jakarta and Surabaya.</p>
            <div class="project-specs-list"><span>6 min read</span><span>Compliance Guide</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

with open("/Users/mekari/Documents/Visifokus/insights.html", "w") as f:
    f.write(render_page(
        "Insights & Resources",
        "Expert guides and market updates on China sourcing, trade regulations, and architectural material trends.",
        "ACTIVE_INSIGHTS",
        "INSIGHTS & RESOURCES",
        "Knowledge for Smarter Decisions",
        "Industry insights, product trends, market updates, and practical guides to empower your procurement decisions.",
        "Insights",
        insights_body
    ))
print("Created insights.html")

# 7. CONTACT.HTML
contact_body = """
  <section class="about-section" style="padding: 80px 0; background: #ffffff;">
    <div class="container">
      <div class="about-split-layout">
        <div>
          <span class="section-tag">GET IN TOUCH</span>
          <h2 class="section-title">Let's Discuss Your Sourcing Requirements</h2>
          <p style="font-size: 1rem; color: #64748b; line-height: 1.6; margin-top: 14px; margin-bottom: 30px;">
            Whether you are planning a commercial development, upgrading retail chain store fitouts, or seeking reliable factory direct supply from China, our procurement specialists are ready to help.
          </p>

          <div style="display: flex; flex-direction: column; gap: 20px;">
            <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 20px;">
              <strong style="color: var(--color-primary); font-size: 1rem; display: block; margin-bottom: 4px;">Surabaya Headquarters (East Java Hub):</strong>
              <p style="color: #64748b; font-size: 0.88rem; margin-bottom: 6px;">Coordinating maritime logistics, showroom sampling, and customer accounts.</p>
              <span style="font-size: 0.85rem; color: var(--color-gold); font-weight: 600;">+62 31 555-1234 &bull; surabaya@visifokus.com</span>
            </div>

            <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 20px;">
              <strong style="color: var(--color-primary); font-size: 1rem; display: block; margin-bottom: 4px;">Jakarta Representative Office:</strong>
              <p style="color: #64748b; font-size: 0.88rem; margin-bottom: 6px;">SCBD Jakarta. Corporate real estate accounts and national developer consultancies.</p>
              <span style="font-size: 0.85rem; color: var(--color-gold); font-weight: 600;">+62 21 888-5678 &bull; jakarta@visifokus.com</span>
            </div>

            <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 20px;">
              <strong style="color: var(--color-primary); font-size: 1rem; display: block; margin-bottom: 4px;">Foshan / Guangdong Sourcing & QC Office:</strong>
              <p style="color: #64748b; font-size: 0.88rem; margin-bottom: 6px;">Chancheng District, Foshan, Guangdong Province, China.</p>
              <span style="font-size: 0.85rem; color: var(--color-gold); font-weight: 600;">china@visifokus.com &bull; Mon - Fri, 09:00 - 18:00 (GMT+8)</span>
            </div>
          </div>
        </div>

        <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 16px; padding: 40px; box-shadow: var(--shadow-md);">
          <h3 style="font-family: var(--font-serif); font-size: 1.5rem; color: var(--color-primary); margin-bottom: 8px;">Request a Quotation</h3>
          <p style="font-size: 0.85rem; color: #64748b; margin-bottom: 24px;">Submit your requirements below and an account director will reach out within 24 hours.</p>

          <form onsubmit="event.preventDefault(); alert('Thank you! Your quotation inquiry has been received. Our team will contact you shortly.'); this.reset();">
            <div style="display: flex; flex-direction: column; gap: 16px;">
              <div>
                <label class="form-label">Full Name *</label>
                <input type="text" class="form-input" placeholder="e.g. Budi Santoso" required>
              </div>
              <div>
                <label class="form-label">Company / Organization *</label>
                <input type="text" class="form-input" placeholder="e.g. PT Artha Perkasa" required>
              </div>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                <div>
                  <label class="form-label">Work Email *</label>
                  <input type="email" class="form-input" placeholder="name@company.com" required>
                </div>
                <div>
                  <label class="form-label">Phone / WhatsApp *</label>
                  <input type="tel" class="form-input" placeholder="+62 8..." required>
                </div>
              </div>
              <div>
                <label class="form-label">Procurement Category</label>
                <select class="form-select">
                  <option value="Supermarket Retail Sourcing">Supermarket & Retail Chains Equipment</option>
                  <option value="Manufacturing Materials">Manufacturing Raw Materials & Machinery</option>
                  <option value="Developer Project">Developer & Real Estate Procurement</option>
                  <option value="Architectural Interior">Architectural Finishes & Slabs</option>
                  <option value="Other">Custom Product Sourcing</option>
                </select>
              </div>
              <div>
                <label class="form-label">Project Details / Message</label>
                <textarea class="form-textarea" rows="4" placeholder="Detail specifications, container volume, target lead times, or any specific factory requirements..."></textarea>
              </div>
              <button type="submit" class="btn btn-gold" style="width: 100%; padding: 14px;">
                SUBMIT QUOTATION REQUEST →
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
"""

with open("/Users/mekari/Documents/Visifokus/contact.html", "w") as f:
    f.write(render_page(
        "Contact Us",
        "Contact Vision Focus offices in Surabaya, Jakarta, and Foshan (China) for project procurement and sourcing inquiries.",
        "ACTIVE_CONTACT",
        "GET IN TOUCH",
        "Let's Build Your Next Project",
        "Contact our dedicated sourcing team to discuss requirements or explore long-term factory supply agreements.",
        "Contact",
        contact_body
    ))
print("Created contact.html")

print("All pages successfully built!")
