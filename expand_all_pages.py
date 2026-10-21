#!/usr/bin/env python3
"""
Expands all detail pages with 3-5 rich, minimalist sections.
"""
import os

with open("/Users/mekari/Documents/Visifokus/index.html", "r") as f:
    idx_content = f.read()

# Header in index is from <header to </aside>
header_clean = idx_content.split("  <!-- ==========================================\n       HEADER & NAVIGATION BAR")[1].split("  <!-- ==========================================\n       HERO SECTION")[0]
header_clean = "  <!-- ==========================================\n       HEADER & NAVIGATION BAR" + header_clean

# Footer in index is from <!-- ==========================================\n       FOOTER to </body>
footer_clean = "  <!-- ==========================================\n       FOOTER" + idx_content.split("  <!-- ==========================================\n       FOOTER")[1]

def build_page(filename, title, meta_desc, active_key, eyebrow, hero_title, hero_subtitle, breadcrumb, body_html):
    page_header = header_clean
    page_header = page_header.replace('nav-link-item active', 'nav-link-item')
    page_header = page_header.replace('mobile-nav-link active', 'mobile-nav-link')
    page_header = page_header.replace('mobile-accordion-trigger active', 'mobile-accordion-trigger')
    
    if active_key == "SOLUTIONS":
        page_header = page_header.replace('href="solutions.html" class="nav-link-item', 'href="solutions.html" class="nav-link-item active')
        page_header = page_header.replace('href="solutions.html" class="mobile-nav-link', 'href="solutions.html" class="mobile-nav-link active')
    elif active_key == "HOW_WE_WORK":
        page_header = page_header.replace('href="how-we-work.html" class="nav-link-item', 'href="how-we-work.html" class="nav-link-item active')
        page_header = page_header.replace('href="how-we-work.html" class="mobile-nav-link', 'href="how-we-work.html" class="mobile-nav-link active')
    elif active_key == "ABOUT":
        page_header = page_header.replace('href="about.html" class="nav-link-item', 'href="about.html" class="nav-link-item active')
        page_header = page_header.replace('href="about.html" class="mobile-nav-link', 'href="about.html" class="mobile-nav-link active')
        if filename == "events.html":
            page_header = page_header.replace('href="events.html" class="dropdown-item"', 'href="events.html" class="dropdown-item active"')
            page_header = page_header.replace('href="events.html">Event</a>', 'href="events.html" class="active">Event</a>')
        elif filename == "why.html":
            page_header = page_header.replace('href="why.html" class="dropdown-item"', 'href="why.html" class="dropdown-item active"')
            page_header = page_header.replace('href="why.html">Why Us</a>', 'href="why.html" class="active">Why Us</a>')
        elif filename == "showroom.html":
            page_header = page_header.replace('href="showroom.html" class="dropdown-item"', 'href="showroom.html" class="dropdown-item active"')
            page_header = page_header.replace('href="showroom.html">Showroom</a>', 'href="showroom.html" class="active">Showroom</a>')
    elif active_key == "PRODUCT":
        page_header = page_header.replace('href="product-library.html" class="nav-link-item', 'href="product-library.html" class="nav-link-item active')
        page_header = page_header.replace('href="product-library.html" class="mobile-nav-link', 'href="product-library.html" class="mobile-nav-link active')
    elif active_key == "INSIGHTS":
        page_header = page_header.replace('href="insights.html" class="nav-link-item', 'href="insights.html" class="nav-link-item active')
        page_header = page_header.replace('href="insights.html" class="mobile-nav-link', 'href="insights.html" class="mobile-nav-link active')
    elif active_key == "CONTACT":
        page_header = page_header.replace('href="contact.html" class="nav-link-item', 'href="contact.html" class="nav-link-item active')
        page_header = page_header.replace('href="contact.html" class="mobile-nav-link', 'href="contact.html" class="mobile-nav-link active')

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
{page_header}
  <!-- ==========================================
       SUBPAGE HERO WITH CITY BACKGROUND
       ========================================== -->
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
          <span>{breadcrumb}</span>
        </div>
      </div>
    </div>
  </section>

  <!-- MAIN CONTENT -->
  <main>
    {body_html}
  </main>

{footer_clean}"""

    with open(f"/Users/mekari/Documents/Visifokus/{filename}", "w") as f:
        f.write(html)
    print(f"Expanded {filename} successfully.")

# ==============================================================================
# 1. SOLUTIONS.HTML (5 ADDITIONAL RICH SECTIONS)
# ==============================================================================
solutions_body = """
    <!-- Section 1: Industry Cards -->
    <section class="solutions-section" style="padding-top: 60px; padding-bottom: 40px;">
      <div class="container">
        <!-- 1. Supermarket -->
        <div id="supermarket" style="scroll-margin-top: 100px; margin-bottom: 60px; background: #ffffff; border: 1px solid var(--color-border); border-radius: 16px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div class="feature-split-inner">
            <div>
              <span class="section-tag">RETAIL SOURCING</span>
              <h2 style="font-family: var(--font-serif); font-size: 1.85rem; color: var(--color-primary); margin-bottom: 14px;">Supermarket & Retail Chains</h2>
              <p style="color: #64748b; line-height: 1.6; margin-bottom: 20px;">
                Direct factory procurement for modern retail formats, from large hypermarkets to boutique convenience networks. We optimize modular design, custom finish options, and bulk packing for nationwide rollout.
              </p>
              <ul class="solution-card-points" style="margin-bottom: 24px;">
                <li><strong>Heavy-Duty Display Racking:</strong> Powder-coated steel gondolas, cantilever shelving, and warehouse storage racks.</li>
                <li><strong>Commercial Refrigeration:</strong> Plug-in and remote chiller cabinets, island freezers, and cold room insulation panels.</li>
                <li><strong>Checkout & POS Counters:</strong> Ergonomic conveyor cash desks, motorized checkouts, and customer flow barriers.</li>
                <li><strong>Private Label & OEM Supply:</strong> Custom store fixtures produced to exact corporate identity brand guidelines.</li>
              </ul>
              <button type="button" class="btn btn-gold open-quote-modal">Request Retail Sourcing Proposal →</button>
            </div>
            <div class="feature-split-media">
              <img src="assets/images/supermarket.jpg" alt="Supermarket Shelving & Equipment" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
          </div>
        </div>

        <!-- 2. Manufacturing -->
        <div id="manufacturing" style="scroll-margin-top: 100px; margin-bottom: 60px; background: #ffffff; border: 1px solid var(--color-border); border-radius: 16px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div class="feature-split-inner">
            <div class="feature-split-media">
              <img src="assets/images/manufacturing.jpg" alt="Manufacturing & Raw Materials" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <div>
              <span class="section-tag">INDUSTRIAL SUPPLY</span>
              <h2 style="font-family: var(--font-serif); font-size: 1.85rem; color: var(--color-primary); margin-bottom: 14px;">Manufacturing & Raw Materials</h2>
              <p style="color: #64748b; line-height: 1.6; margin-bottom: 20px;">
                Connecting Indonesian manufacturing plants with reliable Chinese upstream producers. We facilitate precision tooling, raw industrial materials, and specialized processing machinery.
              </p>
              <ul class="solution-card-points" style="margin-bottom: 24px;">
                <li><strong>Components & Spare Parts:</strong> Precision stamping, die-cast molds, electrical switches, and pneumatic fittings.</li>
                <li><strong>Raw Material Sourcing:</strong> Industrial coil stainless steel, acrylic sheets, ceramic frit, and polymer compounds.</li>
                <li><strong>Machinery & Production Lines:</strong> Automated packaging machinery, tile polishing equipment, and robotic cutters.</li>
                <li><strong>Factory Auditing & ISO Inspection:</strong> Comprehensive verification of factory capacity, certifications, and QC labs.</li>
              </ul>
              <button type="button" class="btn btn-gold open-quote-modal">Discuss Industrial Requirements →</button>
            </div>
          </div>
        </div>

        <!-- 3. Developer -->
        <div id="developer" style="scroll-margin-top: 100px; margin-bottom: 60px; background: #ffffff; border: 1px solid var(--color-border); border-radius: 16px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div class="feature-split-inner">
            <div>
              <span class="section-tag">REAL ESTATE PROCUREMENT</span>
              <h2 style="font-family: var(--font-serif); font-size: 1.85rem; color: var(--color-primary); margin-bottom: 14px;">Developer & Project Owners</h2>
              <p style="color: #64748b; line-height: 1.6; margin-bottom: 20px;">
                Streamlining high-volume building material procurement for property developers, masterplanners, and commercial contractors. We eliminate markups and streamline staged container logistics.
              </p>
              <ul class="solution-card-points" style="margin-bottom: 24px;">
                <li><strong>Multi-Vendor Sourcing:</strong> Single-contract consolidation across tile, stone, glass, sanitary, and metal manufacturers.</li>
                <li><strong>Staged Construction Shipments:</strong> Timed port arrivals synchronized with your project construction schedule.</li>
                <li><strong>SNI & Import Compliance:</strong> Full documentation handling for legal import into Jakarta, Surabaya, and Semarang ports.</li>
                <li><strong>Strict Cost Management:</strong> Direct factory pricing with volume discounts of 20% to 35% compared to local stockists.</li>
              </ul>
              <button type="button" class="btn btn-gold open-quote-modal">Submit Project Bill of Quantities →</button>
            </div>
            <div class="feature-split-media">
              <img src="assets/images/developer.jpg" alt="Commercial Real Estate Construction" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
          </div>
        </div>

        <!-- 4. Architects -->
        <div id="architects" style="scroll-margin-top: 100px; background: #ffffff; border: 1px solid var(--color-border); border-radius: 16px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div class="feature-split-inner">
            <div class="feature-split-media">
              <img src="assets/images/architect.jpg" alt="Luxury Architectural Interior" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <div>
              <span class="section-tag">DESIGN SPECIFICATION</span>
              <h2 style="font-family: var(--font-serif); font-size: 1.85rem; color: var(--color-primary); margin-bottom: 14px;">Architects & Interior Designers</h2>
              <p style="color: #64748b; line-height: 1.6; margin-bottom: 20px;">
                Bringing design visions to life with rare and custom finishes. We match design specifications with specialized artisans and high-tech factories in Foshan, providing fast sampling and bespoke craftsmanship.
              </p>
              <ul class="solution-card-points" style="margin-bottom: 24px;">
                <li><strong>Bespoke Surface Matching:</strong> Sintered stone, bookmatched slabs, custom water ripple stainless steel, and textured glass.</li>
                <li><strong>Physical Sample Express:</strong> Rapid door-to-door courier dispatch of material sample boxes to your Jakarta or Surabaya studio.</li>
                <li><strong>Technical Submittals:</strong> Comprehensive test reports, slip resistance ratings, and shop drawing verification.</li>
                <li><strong>Factory Delegation Tours:</strong> VIP factory walkthroughs in China during Guangzhou Design Week or custom sourcing trips.</li>
              </ul>
              <button type="button" class="btn btn-gold open-quote-modal">Request Sample Box →</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: OPERATIONAL STATS & METRICS -->
    <section style="padding: 70px 0; background: var(--color-surface-soft); border-top: 1px solid var(--color-border); border-bottom: 1px solid var(--color-border);">
      <div class="container">
        <div style="text-align: center; max-width: 680px; margin: 0 auto 30px;">
          <span class="section-tag" style="justify-content: center;">PROCUREMENT IMPACT</span>
          <h2 class="section-title">Measurable Advantage for Your Business</h2>
          <p class="section-subtitle" style="margin: 10px auto 0;">Delivering verified factory-direct capabilities that elevate profit margins and eliminate procurement bottlenecks.</p>
        </div>

        <div class="stats-counter-grid">
          <div class="stat-card">
            <div class="stat-number">500+</div>
            <div class="stat-label">Tier-1 Factories</div>
            <p class="stat-sub">Audited manufacturing partners across Foshan & Guangdong</p>
          </div>
          <div class="stat-card">
            <div class="stat-number">2,400+</div>
            <div class="stat-label">Containers Shipped</div>
            <p class="stat-sub">Successfully cleared through Indonesian customs since 2016</p>
          </div>
          <div class="stat-card">
            <div class="stat-number">25-40%</div>
            <div class="stat-label">Cost Reduction</div>
            <p class="stat-sub">Direct factory pricing eliminating domestic middleman markups</p>
          </div>
          <div class="stat-card">
            <div class="stat-number">99.4%</div>
            <div class="stat-label">Inspection Pass Rate</div>
            <p class="stat-sub">Strict pre-shipment quality audits on every container batch</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: COMPARISON TABLE (DIRECT SOURCING VS LOCAL BROKERS) -->
    <section style="padding: 80px 0; background: #ffffff;">
      <div class="container">
        <div style="text-align: center; max-width: 720px; margin: 0 auto 30px;">
          <span class="section-tag" style="justify-content: center;">WHY VISION FOCUS</span>
          <h2 class="section-title">Vision Focus vs. Traditional Importers</h2>
          <p class="section-subtitle" style="margin: 10px auto 0;">See how our direct presence in China fundamentally transforms your procurement economics.</p>
        </div>

        <div class="comparison-table-wrap">
          <table class="data-table">
            <thead>
              <tr>
                <th style="width: 32%;">Procurement Factors</th>
                <th class="highlight-col" style="width: 38%;">Vision Focus Trade Line</th>
                <th style="width: 30%;">Traditional Local Stockists / Brokers</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Pricing Transparency</strong></td>
                <td class="highlight-col"><span class="check-green">✔</span> 100% Direct Factory Price + Transparent Sourcing Fee</td>
                <td><span class="cross-gray">✖</span> 30% - 60% Hidden Markup & Agent Margins</td>
              </tr>
              <tr>
                <td><strong>On-Site Quality Control</strong></td>
                <td class="highlight-col"><span class="check-green">✔</span> Full-Time Foshan Engineers Inspecting Every Batch</td>
                <td><span class="cross-gray">✖</span> Blind Third-Party Sourcing with No QC Defense</td>
              </tr>
              <tr>
                <td><strong>Custom Specifications & Branding</strong></td>
                <td class="highlight-col"><span class="check-green">✔</span> Custom Sizing, Private Labeling & Tailored Finishes</td>
                <td><span class="cross-gray">✖</span> Limited to Existing Surplus Warehouse Catalog</td>
              </tr>
              <tr>
                <td><strong>Container Consolidation</strong></td>
                <td class="highlight-col"><span class="check-green">✔</span> Combine 5-10 Vendors into Single Container Load</td>
                <td><span class="cross-gray">✖</span> High Minimums for Each Disconnected Vendor</td>
              </tr>
              <tr>
                <td><strong>Import Clearance & SNI Handling</strong></td>
                <td class="highlight-col"><span class="check-green">✔</span> Complete Legal Import, Form E, SNI & Door Delivery</td>
                <td><span class="cross-gray">✖</span> Varies, Often Unpredictable Customs Holds</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- SECTION 4: CONTAINER CONSOLIDATION ARCHITECTURE -->
    <section style="padding: 80px 0; background: var(--color-surface-soft);">
      <div class="container">
        <div class="resp-grid-2">
          <div>
            <span class="section-tag">LOGISTICS OPTIMIZATION</span>
            <h2 class="section-title">Multi-Vendor Container Consolidation</h2>
            <p style="color: #64748b; line-height: 1.7; margin: 16px 0 24px;">
              Large projects rarely need materials from just one factory. Our 3,500 m² staging warehouse in Foshan allows us to receive shipments from multiple specialized factories—granite slabs from factory A, stainless steel trims from factory B, and sanitaryware from factory C—and consolidate them into a single, perfectly packed container.
            </p>
            <div style="display: flex; flex-direction: column; gap: 14px;">
              <div style="display: flex; gap: 12px; align-items: flex-start;">
                <span class="check-green">✔</span>
                <span style="font-size: 0.88rem; color: #334155;"><strong>Save Up to 40% on Shipping Costs:</strong> Eliminate LCL (Less than Container Load) premium freight rates.</span>
              </div>
              <div style="display: flex; gap: 12px; align-items: flex-start;">
                <span class="check-green">✔</span>
                <span style="font-size: 0.88rem; color: #334155;"><strong>Single Customs Entry:</strong> Only one bill of lading and single customs declaration in Tanjung Perak / Tanjung Priok.</span>
              </div>
              <div style="display: flex; gap: 12px; align-items: flex-start;">
                <span class="check-green">✔</span>
                <span style="font-size: 0.88rem; color: #334155;"><strong>Fumigated Timber Crating:</strong> Customized shockproof wooden crates prevent transit breakage.</span>
              </div>
            </div>
          </div>
          <div style="height: 380px; border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-md);">
            <img src="assets/images/logistics.jpg" alt="Container Consolidation Warehouse Foshan" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: SOLUTIONS FAQ -->
    <section style="padding: 80px 0; background: #ffffff;">
      <div class="container">
        <div style="text-align: center; max-width: 680px; margin: 0 auto 40px;">
          <span class="section-tag" style="justify-content: center;">SOLUTIONS FAQ</span>
          <h2 class="section-title">Frequently Asked Questions</h2>
          <p class="section-subtitle" style="margin: 10px auto 0;">Everything you need to know about partnering with Vision Focus for direct China sourcing.</p>
        </div>

        <div class="faq-grid">
          <div class="faq-card">
            <h4>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
              What is the typical minimum order quantity (MOQ)?
            </h4>
            <p>Because we consolidate orders across our active network, we negotiate flexible MOQs. For tiles and stone, minimums typically start at 1 full 20ft container (approx. 1,000–1,200 m²), but mixed material containers are welcome.</p>
          </div>

          <div class="faq-card">
            <h4>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
              How do you guarantee quality before shipping?
            </h4>
            <p>Our bilingual inspection engineers are stationed in Foshan. Before container loading, we run color shade tests, dimensional tolerances, flexural strength tests, and drop packaging audits with live video reports for you.</p>
          </div>

          <div class="faq-card">
            <h4>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
              How long is the typical lead time from China to Indonesia?
            </h4>
            <p>Standard production takes 15–25 days depending on customization. Direct sea freight from Guangzhou/Shenzhen to Jakarta or Surabaya is approximately 10–14 days, followed by 3–5 days customs clearance.</p>
          </div>

          <div class="faq-card">
            <h4>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
              What payment terms and safeguards do you provide?
            </h4>
            <p>We operate with secure milestone contracts: standard deposit upon sample approval, staged progress upon factory audit, and balance only upon passing our comprehensive pre-shipment quality inspection report.</p>
          </div>
        </div>
      </div>
    </section>
"""

build_page(
    "solutions.html",
    "Solutions",
    "Direct sourcing and integrated supply chain solutions from China to Indonesia for retail, manufacturing, developers, and architects.",
    "SOLUTIONS",
    "INTEGRATED SOURCING",
    "Solutions Built Around Your Business",
    "Connecting Indonesian enterprises with world-class Chinese factories across retail, manufacturing, real estate, and architectural design.",
    "Solutions",
    solutions_body
)

# ==============================================================================
# 2. PROJECTS.HTML (5 ADDITIONAL RICH SECTIONS)
# ==============================================================================
projects_body = """
  <!-- Section 1: Portfolio Grid -->
  <section class="projects-section" style="padding: 70px 0 40px;">
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
        <a href="project-detail.html?id=retail" class="project-item-card" data-category="retail" id="retail">
          <div class="project-card-thumb">
            <span class="project-card-tag">Retail Sourcing</span>
            <img src="assets/images/project-retail.jpg" alt="Retail Store Fitout">
          </div>
          <div class="project-card-body">
            <h4>National Supermarket Network Fitout</h4>
            <p>End-to-end procurement of commercial shelving, LED checkout desks, and temperature-controlled chillers for 45+ retail locations across Indonesia.</p>
            <div class="project-specs-list">
              <span>Scope: Store Fixtures</span>
              <span class="project-card-link-badge">View Case Study →</span>
            </div>
          </div>
        </a>

        <a href="project-detail.html?id=hospitality" class="project-item-card" data-category="hospitality" id="hospitality">
          <div class="project-card-thumb">
            <span class="project-card-tag">Hospitality</span>
            <img src="assets/images/project-hospitality.jpg" alt="Luxury Hotel Resort">
          </div>
          <div class="project-card-body">
            <h4>5-Star Beachfront Luxury Resort</h4>
            <p>Direct supply of large format 800x1600mm honed porcelain, custom mosaic swimming pool tiles, and brushed brass bathroom fittings.</p>
            <div class="project-specs-list">
              <span>Scope: FF&E Materials</span>
              <span class="project-card-link-badge">View Case Study →</span>
            </div>
          </div>
        </a>

        <a href="project-detail.html?id=commercial" class="project-item-card" data-category="commercial" id="commercial">
          <div class="project-card-thumb">
            <span class="project-card-tag">Commercial</span>
            <img src="assets/images/project-commercial.jpg" alt="Grade-A Financial Tower">
          </div>
          <div class="project-card-body">
            <h4>Grade-A Financial Tower</h4>
            <p>Custom elevator hall claddings, 316-grade mirror stainless panels, and fire-resistant composite architectural panels.</p>
            <div class="project-specs-list">
              <span>Scope: Interior Paneling</span>
              <span class="project-card-link-badge">View Case Study →</span>
            </div>
          </div>
        </a>

        <a href="project-detail.html?id=residential" class="project-item-card" data-category="residential" id="residential">
          <div class="project-card-thumb">
            <span class="project-card-tag">Residential</span>
            <img src="assets/images/project-residential.jpg" alt="Luxury Residential Development">
          </div>
          <div class="project-card-body">
            <h4>High-End Residential Villas</h4>
            <p>Sourcing of bookmatched Calacatta sintered stone slabs, natural quartz counter surfaces, and frameless acoustic glass partitions.</p>
            <div class="project-specs-list">
              <span>Scope: Interior Finishes</span>
              <span class="project-card-link-badge">View Case Study →</span>
            </div>
          </div>
        </a>

        <a href="project-detail.html?id=healthcare" class="project-item-card" data-category="commercial" id="healthcare">
          <div class="project-card-thumb">
            <span class="project-card-tag">Healthcare & Edu</span>
            <img src="assets/images/developer.jpg" alt="Modern Hospital Complex">
          </div>
          <div class="project-card-body">
            <h4>International Hospital Expansion</h4>
            <p>Antibacterial vinyl flooring, hygienic stainless steel wall protection, and sensored commercial scrub sinks.</p>
            <div class="project-specs-list">
              <span>Scope: Specialized Materials</span>
              <span class="project-card-link-badge">View Case Study →</span>
            </div>
          </div>
        </a>

        <a href="project-detail.html?id=infrastructure" class="project-item-card" data-category="commercial" id="infrastructure">
          <div class="project-card-thumb">
            <span class="project-card-tag">Infrastructure</span>
            <img src="assets/images/logistics.jpg" alt="Modern Logistics Hub">
          </div>
          <div class="project-card-body">
            <h4>Logistics Center & Warehouse</h4>
            <p>Heavy-duty industrial floor coatings, high-bay LED floodlighting, and automated loading dock equipment.</p>
            <div class="project-specs-list">
              <span>Scope: Logistics Equipment</span>
              <span class="project-card-link-badge">View Case Study →</span>
            </div>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- SECTION 2: PROJECT TIMELINE & STAGES -->
  <section style="padding: 70px 0; background: #ffffff; border-top: 1px solid var(--color-border);">
    <div class="container">
      <div style="text-align: center; max-width: 680px; margin: 0 auto 30px;">
        <span class="section-tag" style="justify-content: center;">EXECUTION ROADMAP</span>
        <h2 class="section-title">Standard 10-Week Project Procurement Cycle</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">From technical takeoff to on-site installation buffer, structured for zero contractor downtime.</p>
      </div>

      <div class="timeline-grid">
        <div class="timeline-card">
          <span class="timeline-badge">Weeks 1 - 2</span>
          <h4>BOQ Analysis & Sampling</h4>
          <p>Technical drawing review, tolerance validation, and express air courier of material samples to Indonesia.</p>
        </div>
        <div class="timeline-card">
          <span class="timeline-badge">Weeks 3 - 4</span>
          <h4>Factory Contracting & Setup</h4>
          <p>Contract negotiation with audited Foshan tier-1 plants, mold fabrication, and initial batch calibration.</p>
        </div>
        <div class="timeline-card">
          <span class="timeline-badge">Weeks 5 - 6</span>
          <h4>Mass Production & Inline QC</h4>
          <p>Full manufacturing run with Vision Focus on-site engineers checking shade uniformity and dimensions.</p>
        </div>
        <div class="timeline-card">
          <span class="timeline-badge">Weeks 7 - 8</span>
          <h4>Consolidation & Sea Freight</h4>
          <p>Shockproof export crating, container loading, and direct sailing from Guangzhou/Shenzhen port.</p>
        </div>
        <div class="timeline-card">
          <span class="timeline-badge">Weeks 9 - 10</span>
          <h4>Customs & Job-Site Delivery</h4>
          <p>Fast Indonesian customs release, port de-stuffing, and insured flatbed transport direct to your site.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: CLIENT TESTIMONIALS & CASE STUDIES -->
  <section style="padding: 70px 0; background: var(--color-surface-soft);">
    <div class="container">
      <div style="text-align: center; max-width: 680px; margin: 0 auto 30px;">
        <span class="section-tag" style="justify-content: center;">DEVELOPER TESTIMONIALS</span>
        <h2 class="section-title">Trusted by Indonesia's Leading Builders</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">What project directors and architects say about our procurement reliability.</p>
      </div>

      <div class="testimonial-grid">
        <div class="testimonial-card">
          <p class="testimonial-quote">
            "Vision Focus saved us nearly 30% on our retail chain fixtures while accelerating rollout speed. Their ability to consolidate shelving, POS desks, and lighting into synchronized container deliveries is unmatched."
          </p>
          <div class="testimonial-author">
            <div class="author-info">
              <h5>Budi Wicaksono</h5>
              <p>Project Director, National Supermarket Chain</p>
            </div>
          </div>
        </div>

        <div class="testimonial-card">
          <p class="testimonial-quote">
            "Finding flawless 1200x2700mm bookmatched porcelain slabs was a nightmare until we partnered with Mr. Jason Shi's team in Foshan. Every single crate arrived undamaged and precisely color-matched to our 3D render."
          </p>
          <div class="testimonial-author">
            <div class="author-info">
              <h5>Melinda Kusuma, IAI</h5>
              <p>Principal Architect, Luxury Hospitality Studio</p>
            </div>
          </div>
        </div>

        <div class="testimonial-card">
          <p class="testimonial-quote">
            "For our 32-story commercial tower, custom water ripple stainless panels required strict fire compliance and scratch-resistant PVD coating. Vision Focus handled testing, inspection, and port clearance flawlessly."
          </p>
          <div class="testimonial-author">
            <div class="author-info">
              <h5>Hendrik Tan</h5>
              <p>Senior VP Procurement, Commercial Real Estate Developer</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 4: NATIONWIDE PORT LOGISTICS COVERAGE -->
  <section style="padding: 80px 0; background: #ffffff;">
    <div class="container">
      <div class="resp-grid-2">
        <div style="height: 360px; border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-md);">
          <img src="assets/images/guangzhou-hero.png" alt="Shipping routes from China to Indonesian ports" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
        <div>
          <span class="section-tag">LOGISTICS NETWORK</span>
          <h2 class="section-title">Direct Port Clearances Across Indonesia</h2>
          <p style="color: #64748b; line-height: 1.7; margin: 14px 0 20px;">
            We operate regular container shipping routes from Pearl River Delta ports (Nansha, Chiwan, Shekou) directly to major Indonesian commercial ports:
          </p>
          <div class="resp-grid-2" style="gap: 14px;">
            <div style="background: var(--color-surface-soft); padding: 14px; border-radius: 8px; border: 1px solid var(--color-border);">
              <strong style="color: var(--color-primary); display: block; font-size: 0.9rem;">Surabaya Hub:</strong>
              <span style="font-size: 0.8rem; color: #64748b;">Tanjung Perak Port &bull; 11-13 days sailing</span>
            </div>
            <div style="background: var(--color-surface-soft); padding: 14px; border-radius: 8px; border: 1px solid var(--color-border);">
              <strong style="color: var(--color-primary); display: block; font-size: 0.9rem;">Jakarta Hub:</strong>
              <span style="font-size: 0.8rem; color: #64748b;">Tanjung Priok Port &bull; 10-12 days sailing</span>
            </div>
            <div style="background: var(--color-surface-soft); padding: 14px; border-radius: 8px; border: 1px solid var(--color-border);">
              <strong style="color: var(--color-primary); display: block; font-size: 0.9rem;">Semarang Hub:</strong>
              <span style="font-size: 0.8rem; color: #64748b;">Tanjung Emas Port &bull; 13-15 days sailing</span>
            </div>
            <div style="background: var(--color-surface-soft); padding: 14px; border-radius: 8px; border: 1px solid var(--color-border);">
              <strong style="color: var(--color-primary); display: block; font-size: 0.9rem;">Medan & Regional:</strong>
              <span style="font-size: 0.8rem; color: #64748b;">Belawan, Bali, Makassar door-to-site</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: PROJECT INQUIRY CTA -->
  <section style="padding: 70px 0; background: linear-gradient(135deg, #111e2e 0%, #1e334c 100%); color: #ffffff;">
    <div class="container" style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 30px;">
      <div style="max-width: 640px;">
        <span style="color: var(--color-gold); font-size: 0.78rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;">START YOUR PROCUREMENT</span>
        <h3 style="font-family: var(--font-serif); font-size: 2.2rem; margin: 10px 0 14px;">Have an Upcoming Project or Tender?</h3>
        <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">Send us your Bill of Quantities (BOQ) or architectural design package. Our engineering desk will deliver a comparative landed cost estimate within 48 business hours.</p>
      </div>
      <div>
        <button type="button" class="btn btn-gold open-quote-modal" style="padding: 16px 36px; font-size: 0.95rem;">REQUEST BOQ REVIEW →</button>
      </div>
    </div>
  </section>
"""

build_page(
    "projects.html",
    "Project References",
    "Project procurement references and track record across hospitality, commercial towers, retail chains, and residential developments in Indonesia.",
    "PROJECTS",
    "PROJECT REFERENCES",
    "From Concept to Completion",
    "Explore our proven procurement portfolio delivering high-specification building materials and commercial solutions across Indonesia.",
    "Projects",
    projects_body
)

# ==============================================================================
# 3. HOW-WE-WORK.HTML (5 ADDITIONAL RICH SECTIONS)
# ==============================================================================
how_body = """
  <!-- Section 1: 5 Step Stepper -->
  <section class="how-it-works-section" style="padding: 70px 0 40px;">
    <div class="container">
      <div style="text-align: center; max-width: 760px; margin: 0 auto 50px;">
        <span class="section-tag" style="justify-content: center;">PROCUREMENT METHODOLOGY</span>
        <h2 class="section-title">A Clear Process from Start to Success</h2>
        <p class="section-subtitle" style="margin: 12px auto 0;">
          Our 5-stage procurement framework guarantees transparency, uncompromised quality, and punctuality at every milestone.
        </p>
      </div>

      <div style="display: flex; flex-direction: column; gap: 30px;">
        <div id="step-1" class="step-process-card">
          <div class="step-process-num">01</div>
          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin-bottom: 8px;">Understand Your Needs</h3>
            <p style="color: #64748b; line-height: 1.6;">We analyze your architectural drawings, bills of quantities (BOQ), technical tolerances, target budget, and required delivery timeline to determine the most competitive manufacturing route in China.</p>
          </div>
          <div class="step-process-media"><img src="assets/images/step-needs.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
        </div>

        <div id="step-2" class="step-process-card">
          <div class="step-process-num">02</div>
          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin-bottom: 8px;">Source & Verify Factory Capacity</h3>
            <p style="color: #64748b; line-height: 1.6;">Our team stationed on the ground in Foshan and Guangzhou performs on-site audits of certified tier-1 factories. We examine production lines, verify ISO/CE/SNI credentials, and send physical sample boxes for your client approval.</p>
          </div>
          <div class="step-process-media"><img src="assets/images/step-source.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
        </div>

        <div id="step-3" class="step-process-card">
          <div class="step-process-num">03</div>
          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin-bottom: 8px;">Procurement & Quality Control (QC)</h3>
            <p style="color: #64748b; line-height: 1.6;">During manufacturing, our engineers conduct continuous inline checks. We perform shade variation tests, dimensional checks, stress tests, and pre-packing inspections, ensuring zero defective units enter the container.</p>
          </div>
          <div class="step-process-media"><img src="assets/images/step-shipping.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
        </div>

        <div id="step-4" class="step-process-card">
          <div class="step-process-num">04</div>
          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin-bottom: 8px;">Delivery & Port Clearance to Indonesia</h3>
            <p style="color: #64748b; line-height: 1.6;">Full international export packing with reinforced fumigated timber crates. We coordinate sea freight, bill of lading, Indonesian customs clearance, and inland delivery direct to your job site or warehouse.</p>
          </div>
          <div class="step-process-media"><img src="assets/images/step-delivery.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
        </div>

        <div id="step-5" class="step-process-card">
          <div class="step-process-num">05</div>
          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin-bottom: 8px;">After-Sales & Continuous Replenishment</h3>
            <p style="color: #64748b; line-height: 1.6;">We supervise container de-stuffing, provide installation technical advisory, manage defect warranty replacements, and establish continuous repeat supply channels for multi-phase projects.</p>
          </div>
          <div class="step-process-media"><img src="assets/images/step-support.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: THE FOSHAN QC CHECKLIST PROTOCOL -->
  <section style="padding: 70px 0; background: #ffffff; border-top: 1px solid var(--color-border);">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto 40px;">
        <span class="section-tag" style="justify-content: center;">QUALITY PROTOCOL</span>
        <h2 class="section-title">The 8-Point Pre-Shipment Inspection</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">Before any container door is sealed in China, our QA engineers execute mandatory testing protocols.</p>
      </div>

      <div class="resp-grid-4">
        <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 22px;">
          <strong style="color: var(--color-gold); font-size: 1rem; display: block; margin-bottom: 6px;">01. Dimensional Caliper</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Laser micrometer measurement of diagonal, thickness, and edge straightness to within &plusmn;0.2mm tolerance.</p>
        </div>
        <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 22px;">
          <strong style="color: var(--color-gold); font-size: 1rem; display: block; margin-bottom: 6px;">02. Color Shade Matching</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Spectrophotometer analysis and dry-lay inspection under standard D65 daylight simulator booths.</p>
        </div>
        <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 22px;">
          <strong style="color: var(--color-gold); font-size: 1rem; display: block; margin-bottom: 6px;">03. Water Absorption</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Vacuum boiling test confirming porcelain water absorption remains strictly under 0.1% for frost and mold proofing.</p>
        </div>
        <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 22px;">
          <strong style="color: var(--color-gold); font-size: 1rem; display: block; margin-bottom: 6px;">04. Surface Hardness & Stain</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Mohs hardness scratch testing and 24-hour methylene blue stain resistance evaluation.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: REAL-TIME CLIENT INSPECTION DASHBOARD -->
  <section style="padding: 80px 0; background: var(--color-surface-soft);">
    <div class="container">
      <div class="resp-grid-2">
        <div>
          <span class="section-tag">FULL TRANSPARENCY</span>
          <h2 class="section-title">Live Production Photo & Video Reporting</h2>
          <p style="color: #64748b; line-height: 1.7; margin: 16px 0 20px;">
            Never wonder what is happening to your order in China. We assign a dedicated bilingual project coordinator who streams high-definition video inspections, sends batch photo logs, and provides container loading count verification directly via WhatsApp and digital portal.
          </p>
          <div style="background: #ffffff; border-radius: 10px; padding: 18px; border: 1px solid var(--color-border); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem;">
              <span><strong>Inspection Report Format:</strong></span>
              <span style="color: var(--color-gold); font-weight: 700;">PDF Certificate + High-Res Photos</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem;">
              <span><strong>Container Sealing Verification:</strong></span>
              <span style="color: var(--color-gold); font-weight: 700;">Customs Bolt Seal Serial Log</span>
            </div>
          </div>
        </div>
        <div style="height: 340px; border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-md);">
          <img src="assets/images/step-shipping.jpg" alt="Live QC Inspection" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 4: RISK MITIGATION & ESCROW SAFEGUARDS -->
  <section style="padding: 80px 0; background: #ffffff;">
    <div class="container">
      <div style="text-align: center; max-width: 700px; margin: 0 auto 40px;">
        <span class="section-tag" style="justify-content: center;">FINANCIAL SECURITY</span>
        <h2 class="section-title">Risk Mitigation & Escrow Protection</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">Protecting your capital against supply chain fraud, factory insolvency, and material non-conformity.</p>
      </div>

      <div class="resp-grid-3">
        <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 28px;">
          <h4 style="font-size: 1.1rem; color: var(--color-primary); margin-bottom: 10px;">Indonesian Legal Contracts</h4>
          <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6;">Contracts governed under Indonesian commercial law through our registered corporate entity in Surabaya & Jakarta.</p>
        </div>
        <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 28px;">
          <h4 style="font-size: 1.1rem; color: var(--color-primary); margin-bottom: 10px;">Factory Escrow Holdback</h4>
          <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6;">Chinese manufacturers only receive final settlement after our engineering team clears container stuffing inspections.</p>
        </div>
        <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 28px;">
          <h4 style="font-size: 1.1rem; color: var(--color-primary); margin-bottom: 10px;">Transit Cargo Insurance</h4>
          <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6;">Full Institute Cargo Clauses (A) all-risk maritime insurance covering 110% of total invoice value from warehouse to site.</p>
        </div>
      </div>
    </div>
  </section>
"""

build_page(
    "how-we-work.html",
    "How We Work",
    "Our 5-stage procurement framework guarantees transparency, quality, and on-time delivery from China to Indonesia.",
    "HOW_WE_WORK",
    "OUR METHODOLOGY",
    "A Clear Process from Start to Success",
    "Step-by-step transparency from initial technical specification to job-site delivery in Indonesia.",
    "How We Work",
    how_body
)

# ==============================================================================
# 4. ABOUT.HTML (5 ADDITIONAL RICH SECTIONS)
# ==============================================================================
about_body = """
  <!-- Section 1: CEO & Story -->
  <section class="about-section" style="padding: 70px 0 40px;">
    <div class="container">
      <div class="about-split-layout" id="ceo" style="margin-bottom: 60px;">
        <div class="about-visual-column">
          <div class="ceo-card-frame">
            <div class="ceo-photo-wrap" style="height: 480px;">
              <img src="assets/images/project-commercial.jpg" alt="Vision Focus Trade Line - Strategic China to Indonesia Bridge" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <div class="ceo-signature-badge">
              <h4>Vision Focus Trade Line</h4>
              <p>Strategic China to Indonesia Supply Chain Bridge</p>
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
    </div>
  </section>

  <!-- SECTION 2: 10-YEAR COMPANY MILESTONES (2016 - 2026) -->
  <section style="padding: 70px 0; background: #ffffff; border-top: 1px solid var(--color-border);">
    <div class="container">
      <div style="text-align: center; max-width: 680px; margin: 0 auto 40px;">
        <span class="section-tag" style="justify-content: center;">GROWTH JOURNEY</span>
        <h2 class="section-title">A Decade of Cross-Border Leadership</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">From a specialized stone sourcing agency to Indonesia's trusted procurement bridge.</p>
      </div>

      <div class="timeline-grid">
        <div class="timeline-card">
          <span class="timeline-badge">2016</span>
          <h4>Company Founded</h4>
          <p>Founded by Mr. Jason Shi in Surabaya, specializing in direct porcelain and natural granite procurement.</p>
        </div>
        <div class="timeline-card">
          <span class="timeline-badge">2018</span>
          <h4>Foshan QC Hub</h4>
          <p>Opened our permanent inspection facility in Chancheng, Foshan, placing full-time engineers inside factories.</p>
        </div>
        <div class="timeline-card">
          <span class="timeline-badge">2021</span>
          <h4>Jakarta Expansion</h4>
          <p>Established our corporate representative office in Jakarta SCBD to serve major property developer accounts.</p>
        </div>
        <div class="timeline-card">
          <span class="timeline-badge">2024</span>
          <h4>Retail & Steel Line</h4>
          <p>Expanded into supermarket display equipment and architectural decorative PVD stainless steel systems.</p>
        </div>
        <div class="timeline-card">
          <span class="timeline-badge">2026</span>
          <h4>Digital Sourcing Desk</h4>
          <p>Connecting 500+ Chinese manufacturers with real-time digital inspection tracking and nationwide delivery.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: TRI-CITY PHYSICAL INFRASTRUCTURE -->
  <section style="padding: 80px 0; background: var(--color-surface-soft);">
    <div class="container">
      <div style="text-align: center; max-width: 680px; margin: 0 auto 40px;">
        <span class="section-tag" style="justify-content: center;">STRATEGIC FOOTPRINT</span>
        <h2 class="section-title">Our Tri-City Infrastructure</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">Permanent physical presence ensuring direct accountability from source to destination.</p>
      </div>

      <div class="resp-grid-3">
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 180px; overflow: hidden;"><img src="assets/images/project-commercial.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
          <div style="padding: 24px;">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">EAST JAVA HUB</span>
            <h4 style="font-size: 1.1rem; color: var(--color-primary); margin: 6px 0 8px;">Surabaya Headquarters</h4>
            <p style="font-size: 0.84rem; color: #64748b; line-height: 1.5;">Houses our core executive team, physical material sample galleries, and logistics tracking control for Tanjung Perak port handling.</p>
          </div>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 180px; overflow: hidden;"><img src="assets/images/developer.jpg" style="width: 100%; height: 100%; object-fit: cover;"></div>
          <div style="padding: 24px;">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">CAPITAL CITY OFFICE</span>
            <h4 style="font-size: 1.1rem; color: var(--color-primary); margin: 6px 0 8px;">Jakarta SCBD Center</h4>
            <p style="font-size: 0.84rem; color: #64748b; line-height: 1.5;">Dedicated enterprise account management for national real estate developers, chain retailers, and architectural practices.</p>
          </div>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 180px; overflow: hidden;"><img src="assets/images/guangzhou-hero.png" style="width: 100%; height: 100%; object-fit: cover;"></div>
          <div style="padding: 24px;">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">CHINA SOURCING & QC</span>
            <h4 style="font-size: 1.1rem; color: var(--color-primary); margin: 6px 0 8px;">Foshan Operations Hub</h4>
            <p style="font-size: 0.84rem; color: #64748b; line-height: 1.5;">3,500 m² container staging warehouse, bilingual QA laboratories, and daily factory auditing units in Guangdong Province.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 4: SUSTAINABILITY & GREEN PROCUREMENT -->
  <section style="padding: 80px 0; background: #ffffff;">
    <div class="container">
      <div class="resp-grid-2">
        <div>
          <span class="section-tag">RESPONSIBLE SOURCING</span>
          <h2 class="section-title">Committed to Green Building Standards</h2>
          <p style="color: #64748b; line-height: 1.7; margin: 16px 0 20px;">
            We actively prioritize Chinese manufacturers utilizing energy-efficient kilns, zero-wastewater discharge processes, and recyclable composite materials that qualify projects for Green Building Council Indonesia (GBCI) Greenship certification.
          </p>
          <ul class="solution-card-points">
            <li><strong>Low VOC & Formaldehyde Free:</strong> All adhesives, finishes, and stone sealers tested to strict indoor air quality norms.</li>
            <li><strong>LEED & Greenship Credits:</strong> Materials eligible for Regional Materials and Recycled Content credit categories.</li>
            <li><strong>Ethical Labor Compliance:</strong> Zero-tolerance audit policy for workplace safety and fair labor standards.</li>
          </ul>
        </div>
        <div style="height: 340px; border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-md);">
          <img src="assets/images/architect.jpg" alt="Green Building Architecture" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
      </div>
    </div>
  </section>
"""

build_page(
    "about.html",
    "About Us",
    "Founded in 2016 by Mr. Jason Shi, Vision Focus is the trusted bridge connecting Indonesian clients with reliable factories in China.",
    "ABOUT",
    "ABOUT VISION FOCUS",
    "Strategic Bridge Between China & Indonesia",
    "Founded in 2016 by Mr. Jason Shi, empowering Indonesian businesses with direct Chinese manufacturing power and uncompromised quality assurance.",
    "About Us",
    about_body
)

# ==============================================================================
# 4B. WHY.HTML (WHY VISION FOCUS)
# ==============================================================================
why_body = """
  <!-- SECTION 1: 6 CORE ADVANTAGES -->
  <section style="padding: 80px 0 50px;">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto 50px;">
        <span class="section-tag" style="justify-content: center;">THE VISION FOCUS ADVANTAGE</span>
        <h2 class="section-title">Eliminating Cross-Border Friction</h2>
        <p class="section-subtitle" style="margin: 12px auto 0;">
          Traditional sourcing from China often carries risks of inconsistent quality, language barriers, and inflated broker fees. We offer a secure, transparent, and direct bridge.
        </p>
      </div>

      <div class="resp-grid-3">
        <!-- Advantage 1 -->
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; padding: 32px 28px; box-shadow: var(--shadow-sm); transition: all var(--transition-fast);">
          <div style="width: 48px; height: 48px; border-radius: 12px; background: var(--color-gold-light); color: var(--color-gold); display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><path d="M12 18V6"/></svg>
          </div>
          <h3 style="font-size: 1.2rem; color: var(--color-primary); margin-bottom: 12px;">100% Direct Factory Pricing</h3>
          <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
            We connect you directly to certified tier-1 manufacturers without layers of commercial brokers or local stockist markups, saving you 20% to 40% on overall procurement.
          </p>
        </div>

        <!-- Advantage 2 -->
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; padding: 32px 28px; box-shadow: var(--shadow-sm); transition: all var(--transition-fast);">
          <div style="width: 48px; height: 48px; border-radius: 12px; background: var(--color-gold-light); color: var(--color-gold); display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>
          </div>
          <h3 style="font-size: 1.2rem; color: var(--color-primary); margin-bottom: 12px;">On-Site Foshan Engineering QC</h3>
          <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
            Our full-time team of QA engineers conducts raw material verification, in-line production checks, and 8-point pre-shipment testing before container sealing.
          </p>
        </div>

        <!-- Advantage 3 -->
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; padding: 32px 28px; box-shadow: var(--shadow-sm); transition: all var(--transition-fast);">
          <div style="width: 48px; height: 48px; border-radius: 12px; background: var(--color-gold-light); color: var(--color-gold); display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
          </div>
          <h3 style="font-size: 1.2rem; color: var(--color-primary); margin-bottom: 12px;">Door-to-Door Indo Logistics</h3>
          <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
            Seamless port handling at Tanjung Priok and Tanjung Perak. We take care of ocean freight, customs clearance, import tax documentation, and job-site delivery.
          </p>
        </div>

        <!-- Advantage 4 -->
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; padding: 32px 28px; box-shadow: var(--shadow-sm); transition: all var(--transition-fast);">
          <div style="width: 48px; height: 48px; border-radius: 12px; background: var(--color-gold-light); color: var(--color-gold); display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>
          </div>
          <h3 style="font-size: 1.2rem; color: var(--color-primary); margin-bottom: 12px;">Physical Sample Express</h3>
          <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
            Touch, test, and approve actual material samples before volume production. We dispatch curated sample swatch boxes by air courier to your studio in 3–5 days.
          </p>
        </div>

        <!-- Advantage 5 -->
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; padding: 32px 28px; box-shadow: var(--shadow-sm); transition: all var(--transition-fast);">
          <div style="width: 48px; height: 48px; border-radius: 12px; background: var(--color-gold-light); color: var(--color-gold); display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
          </div>
          <h3 style="font-size: 1.2rem; color: var(--color-primary); margin-bottom: 12px;">Indonesian Legal Contract</h3>
          <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
            All transactions are protected under Indonesian commercial jurisdiction via our domestic PT entity, shielding your investment against international supplier default.
          </p>
        </div>

        <!-- Advantage 6 -->
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; padding: 32px 28px; box-shadow: var(--shadow-sm); transition: all var(--transition-fast);">
          <div style="width: 48px; height: 48px; border-radius: 12px; background: var(--color-gold-light); color: var(--color-gold); display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
          </div>
          <h3 style="font-size: 1.2rem; color: var(--color-primary); margin-bottom: 12px;">Staged Project Consolidation</h3>
          <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
            For developers and contractors, we consolidate materials from multiple specialized factories into synchronized container shipments aligned with site timelines.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: COMPARISON TABLE -->
  <section style="padding: 80px 0; background: var(--color-surface-soft);">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto 40px;">
        <span class="section-tag" style="justify-content: center;">HEAD-TO-HEAD COMPARISON</span>
        <h2 class="section-title">Why Vision Focus Outperforms Alternatives</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">See how direct presence in China fundamentally transforms your procurement economics and quality defense.</p>
      </div>

      <div class="comparison-table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th style="width: 30%;">Procurement Factors</th>
              <th class="highlight-col" style="width: 40%;">Vision Focus Trade Line</th>
              <th style="width: 30%;">Traditional Brokers & Middlemen</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Pricing Transparency</strong></td>
              <td class="highlight-col"><span class="check-green">✔</span> 100% Direct Factory Pricing + Transparent Fixed Fee</td>
              <td><span class="cross-gray">✖</span> 30% to 60% Hidden Markups & Broker Cuts</td>
            </tr>
            <tr>
              <td><strong>Quality Control (QC)</strong></td>
              <td class="highlight-col"><span class="check-green">✔</span> In-House Full-Time Foshan Engineers on Factory Floor</td>
              <td><span class="cross-gray">✖</span> Blind Sourcing with Zero Inspection Verification</td>
            </tr>
            <tr>
              <td><strong>Legal Jurisdiction</strong></td>
              <td class="highlight-col"><span class="check-green">✔</span> Legally Binding Indonesian Commercial Contracts</td>
              <td><span class="cross-gray">✖</span> High-Risk Overseas Wire Transfers with No Recourse</td>
            </tr>
            <tr>
              <td><strong>Customization & OEM</strong></td>
              <td class="highlight-col"><span class="check-green">✔</span> Custom Dimensions, Private Labeling, and Special Colors</td>
              <td><span class="cross-gray">✖</span> Limited to Stock Items Only with Rigid Minimums</td>
            </tr>
            <tr>
              <td><strong>Door-to-Door Delivery</strong></td>
              <td class="highlight-col"><span class="check-green">✔</span> Full Customs Clearance, Green-Line Port Clearance</td>
              <td><span class="cross-gray">✖</span> Client Left to Deal with Port Delays & Customs Issues</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- SECTION 3: PROVEN METRICS -->
  <section style="padding: 70px 0; background: #ffffff;">
    <div class="container">
      <div style="text-align: center; max-width: 680px; margin: 0 auto 40px;">
        <span class="section-tag" style="justify-content: center;">PROVEN TRACK RECORD</span>
        <h2 class="section-title">Delivering Measurable Impact</h2>
      </div>

      <div class="stats-counter-grid">
        <div class="stat-card">
          <div class="stat-number">500+</div>
          <div class="stat-label">Audited Factories</div>
          <p class="stat-sub">Verified manufacturing partners across Foshan & Guangdong</p>
        </div>
        <div class="stat-card">
          <div class="stat-number">2,400+</div>
          <div class="stat-label">Containers Shipped</div>
          <p class="stat-sub">Successfully cleared through Indonesian customs since 2016</p>
        </div>
        <div class="stat-card">
          <div class="stat-number">25-40%</div>
          <div class="stat-label">Cost Reduction</div>
          <p class="stat-sub">Direct factory pricing eliminating domestic stockist margins</p>
        </div>
        <div class="stat-card">
          <div class="stat-number">99.4%</div>
          <div class="stat-label">Inspection Pass Rate</div>
          <p class="stat-sub">Strict pre-shipment quality audits on every container batch</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 4: CTA CONSULTATION -->
  <section style="padding: 80px 0; background: linear-gradient(135deg, #111e2e 0%, #1b324c 100%); color: #ffffff; text-align: center;">
    <div class="container" style="max-width: 720px;">
      <span class="section-tag" style="color: #dfb76c; border-color: rgba(223, 183, 108, 0.4); justify-content: center;">GET STARTED</span>
      <h2 style="font-family: var(--font-serif); font-size: 2.2rem; margin: 16px 0;">Ready to Experience Direct Factory Sourcing?</h2>
      <p style="color: #cbd5e1; font-size: 1rem; line-height: 1.7; margin-bottom: 30px;">
        Consult with our sourcing specialists in Surabaya, Jakarta, or Foshan. Send your Bill of Quantities (BOQ) or design brief for a transparent cost estimate.
      </p>
      <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
        <button type="button" class="btn btn-gold open-quote-modal">Submit Project Inquiry →</button>
        <a href="https://wa.me/6281234567890?text=Halo%20Vision%20Focus%20Trade%20Line%2C%20saya%20ingin%20konsultasi%20sourcing%20langsung%20dari%20pabrik%20China" target="_blank" rel="noopener noreferrer" class="btn-wa-solutions">
          Chat via WhatsApp
        </a>
      </div>
    </div>
  </section>
"""

build_page(
    "why.html",
    "Why Vision Focus",
    "Discover why Indonesian developers, architects, and retail enterprises trust Vision Focus for direct China factory procurement, Foshan on-site inspection, and legal contract protection.",
    "ABOUT",
    "ABOUT VISION FOCUS",
    "Why Vision Focus Trade Line",
    "Direct tier-1 factory relationships, full-time Foshan on-site quality engineering, and Indonesian legal contract security.",
    '<a href="about.html">About Us</a> <span class="separator">/</span> <span>Why Vision Focus</span>',
    why_body
)

# ==============================================================================
# 4C. SHOWROOM.HTML (MATERIAL GALLERIES & HUBS)
# ==============================================================================
showroom_body = """
  <!-- SECTION 1: TRI-CITY SHOWROOM HUBS -->
  <section style="padding: 80px 0 50px;">
    <div class="container">
      <div style="text-align: center; max-width: 740px; margin: 0 auto 50px;">
        <span class="section-tag" style="justify-content: center;">PHYSICAL LOCATIONS</span>
        <h2 class="section-title">Experience Materials in Person</h2>
        <p class="section-subtitle" style="margin: 12px auto 0;">
          We operate fully equipped material experience centers where architects, developers, and purchasing directors can inspect sample swatches, verify mockups, and consult with procurement engineers.
        </p>
      </div>

      <div class="resp-grid-3">
        <!-- Showroom 1: Surabaya -->
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 16px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 220px; overflow: hidden;">
            <img src="assets/images/project-commercial.jpg" alt="Surabaya Showroom" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="padding: 26px;">
            <span style="display: inline-block; font-size: 0.72rem; font-weight: 700; color: var(--color-gold); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px;">HEADQUARTERS & GALLERY</span>
            <h3 style="font-size: 1.25rem; color: var(--color-primary); margin-bottom: 10px;">Surabaya Experience Center</h3>
            <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6; margin-bottom: 16px;">
              800 sqm flagship showroom featuring full-scale sintered stone displays, vitrified tile libraries, and commercial refrigeration equipment.
            </p>
            <ul style="font-size: 0.82rem; color: #475569; list-style: none; display: flex; flex-direction: column; gap: 6px; margin-bottom: 20px;">
              <li>📍 HR Muhammad / West Surabaya</li>
              <li>⏰ Mon - Fri: 08:30 - 17:30 WIB</li>
              <li>📞 +62 31 5566 7788</li>
            </ul>
            <button type="button" class="btn btn-gold open-quote-modal" style="width: 100%; font-size: 0.82rem; padding: 10px;">Book Private Visit →</button>
          </div>
        </div>

        <!-- Showroom 2: Jakarta -->
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 16px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 220px; overflow: hidden;">
            <img src="assets/images/architect.jpg" alt="Jakarta Design Hub" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="padding: 26px;">
            <span style="display: inline-block; font-size: 0.72rem; font-weight: 700; color: var(--color-gold); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px;">DESIGN SPECIFICATION HUB</span>
            <h3 style="font-size: 1.25rem; color: var(--color-primary); margin-bottom: 10px;">Jakarta Design Lounge</h3>
            <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6; margin-bottom: 16px;">
              Dedicated specification studio in Pantai Indah Kapuk (PIK), tailored for architectural consultancies, luxury residential finishes, and sample box dispatch.
            </p>
            <ul style="font-size: 0.82rem; color: #475569; list-style: none; display: flex; flex-direction: column; gap: 6px; margin-bottom: 20px;">
              <li>📍 Pantai Indah Kapuk (PIK), North Jakarta</li>
              <li>⏰ Mon - Fri: 09:00 - 18:00 WIB</li>
              <li>📞 +62 21 8899 0011</li>
            </ul>
            <button type="button" class="btn btn-gold open-quote-modal" style="width: 100%; font-size: 0.82rem; padding: 10px;">Book Private Visit →</button>
          </div>
        </div>

        <!-- Showroom 3: Foshan -->
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 16px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 220px; overflow: hidden;">
            <img src="assets/images/supermarket.jpg" alt="Foshan VIP Showcase" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="padding: 26px;">
            <span style="display: inline-block; font-size: 0.72rem; font-weight: 700; color: var(--color-gold); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px;">CHINA MANUFACTURING HUB</span>
            <h3 style="font-size: 1.25rem; color: var(--color-primary); margin-bottom: 10px;">Foshan VIP Showcase</h3>
            <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6; margin-bottom: 16px;">
              1,200 sqm international trade pavilion connecting you to 5,000+ factory-direct products, private label fixtures, and direct factory tour access.
            </p>
            <ul style="font-size: 0.82rem; color: #475569; list-style: none; display: flex; flex-direction: column; gap: 6px; margin-bottom: 20px;">
              <li>📍 Chancheng District, Foshan, Guangdong</li>
              <li>⏰ Mon - Sat: 09:00 - 18:00 CST</li>
              <li>📞 +86 757 8899 2233</li>
            </ul>
            <button type="button" class="btn btn-gold open-quote-modal" style="width: 100%; font-size: 0.82rem; padding: 10px;">Book VIP Delegation Tour →</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: CURATED MATERIAL GALLERIES -->
  <section style="padding: 80px 0; background: var(--color-surface-soft);">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto 40px;">
        <span class="section-tag" style="justify-content: center;">EXHIBIT CATEGORIES</span>
        <h2 class="section-title">Featured Showroom Collections</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">Explore our permanently displayed commercial and residential product categories.</p>
      </div>

      <div class="resp-grid-4">
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 22px; text-align: center;">
          <div style="height: 130px; border-radius: 8px; overflow: hidden; margin-bottom: 14px;">
            <img src="assets/images/prod-granite.jpg" alt="Sintered Stone Slabs" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <h4 style="font-size: 1.05rem; color: var(--color-primary); margin-bottom: 6px;">Sintered Stone Slabs</h4>
          <p style="font-size: 0.8rem; color: #64748b;">1600x3200mm, zero porosity, bookmatched vein matching.</p>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 22px; text-align: center;">
          <div style="height: 130px; border-radius: 8px; overflow: hidden; margin-bottom: 14px;">
            <img src="assets/images/prod-stainless.jpg" alt="Stainless Steel Finishes" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <h4 style="font-size: 1.05rem; color: var(--color-primary); margin-bottom: 6px;">Ripple Stainless Steel</h4>
          <p style="font-size: 0.8rem; color: #64748b;">PVD champagne gold, black titanium, mirror water ripple.</p>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 22px; text-align: center;">
          <div style="height: 130px; border-radius: 8px; overflow: hidden; margin-bottom: 14px;">
            <img src="assets/images/prod-sanitary.jpg" alt="Sanitary Ware" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <h4 style="font-size: 1.05rem; color: var(--color-primary); margin-bottom: 6px;">Commercial Sanitary</h4>
          <p style="font-size: 0.8rem; color: #64748b;">Smart sensor WC, matte black faucets, freestanding bathtubs.</p>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 22px; text-align: center;">
          <div style="height: 130px; border-radius: 8px; overflow: hidden; margin-bottom: 14px;">
            <img src="assets/images/supermarket.jpg" alt="Retail Fixtures" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <h4 style="font-size: 1.05rem; color: var(--color-primary); margin-bottom: 6px;">Retail Gondola & Display</h4>
          <p style="font-size: 0.8rem; color: #64748b;">Heavy-duty store shelving, island chillers, checkout counters.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: PHYSICAL SAMPLE BOX REQUEST -->
  <section style="padding: 80px 0; background: #ffffff;">
    <div class="container">
      <div class="resp-grid-2">
        <div>
          <span class="section-tag">SAMPLE ON DEMAND</span>
          <h2 class="section-title">Cannot Visit In Person? Order a Physical Sample Box</h2>
          <p style="color: #64748b; line-height: 1.7; margin: 16px 0 24px;">
            We understand that design timelines are demanding. Our studio sample service couriers tailored material swatch boxes directly to your architecture or developer office across Jakarta, Surabaya, Bali, Semarang, and Medan in 3–5 business days.
          </p>
          <ul class="solution-card-points" style="margin-bottom: 28px;">
            <li><strong>Precision Cutting:</strong> 150x150mm & 300x300mm authentic factory production samples.</li>
            <li><strong>Technical Test Sheets:</strong> Slip resistance ratings, chemical resistance data, and spec sheets included.</li>
            <li><strong>Free Sourcing Consultation:</strong> Dedicated engineer review of your BOQ specifications.</li>
          </ul>
          <div style="display: flex; gap: 14px; flex-wrap: wrap;">
            <button type="button" class="btn btn-gold open-quote-modal">Request Material Sample Box →</button>
            <a href="product-library.html" class="btn btn-outline-gold">Explore Product Library</a>
          </div>
        </div>
        <div style="height: 340px; border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-md);">
          <img src="assets/images/developer.jpg" alt="Material Samples Box Dispatch" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
      </div>
    </div>
  </section>
"""

build_page(
    "showroom.html",
    "Showrooms & Material Galleries",
    "Visit Vision Focus physical material showrooms in Surabaya, Jakarta, and Foshan (China). Touch and test sintered stone, architectural stainless steel, and commercial fixtures.",
    "ABOUT",
    "PHYSICAL MATERIAL HUBS",
    "Experience Showrooms & Material Galleries",
    "Physical material galleries in Surabaya, Jakarta, and Foshan (China) - touch, test, and specify premium architectural finishes.",
    '<a href="about.html">About Us</a> <span class="separator">/</span> <span>Showrooms</span>',
    showroom_body
)

# ==============================================================================
# 5. EVENTS.HTML (5 ADDITIONAL RICH SECTIONS)
# ==============================================================================
events_body = """
  <!-- Section 1: Major Events -->
  <section class="how-it-works-section" style="padding: 70px 0 40px;">
    <div class="container">
      <div style="text-align: center; max-width: 680px; margin: 0 auto 50px;">
        <span class="section-tag" style="justify-content: center;">EXHIBITIONS & CONFERENCES</span>
        <h2 class="section-title">Industry Presence & Trade Exhibitions</h2>
        <p class="section-subtitle" style="margin: 12px auto 0;">Connecting global manufacturing innovations with Indonesian architecture and construction leaders.</p>
      </div>

      <div class="resp-grid-2">
        <div id="ibt" style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 240px; overflow: hidden;"><a href="event-detail.html?id=ibt2025"><img src="assets/images/step-needs.jpg" alt="IndoBuildTech 2025" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;"></a></div>
          <div style="padding: 30px;">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">UPCOMING FLAGSHIP EXPO</span>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin: 6px 0 12px;"><a href="event-detail.html?id=ibt2025" style="color: inherit; text-decoration: none;">IndoBuildTech Expo 2025</a></h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 18px;">Indonesia Convention Exhibition (ICE) BSD City. Visit Vision Focus to experience next-generation large porcelain slabs, antibacterial hospital surfaces, and textured architectural metal cladding.</p>
            <div style="display: flex; gap: 12px; flex-wrap: wrap;">
              <a href="event-detail.html?id=ibt2025" class="btn btn-gold">Read Event Article →</a>
              <button type="button" class="btn btn-outline-gold open-quote-modal">VIP Booth Access</button>
            </div>
          </div>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 240px; overflow: hidden;"><a href="event-detail.html?id=ibt2024"><img src="assets/images/step-source.jpg" alt="IndoBuildTech 2024" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;"></a></div>
          <div style="padding: 30px;">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">PAST EVENT SHOWCASE</span>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin: 6px 0 12px;"><a href="event-detail.html?id=ibt2024" style="color: inherit; text-decoration: none;">IndoBuildTech Expo 2024</a></h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 18px;">Showcasing embossed PVD stainless steel panels and terrazzo collections to over 5,000 architects, developers, and interior designers from across Southeast Asia.</p>
            <div style="display: flex; gap: 12px; flex-wrap: wrap;">
              <a href="event-detail.html?id=ibt2024" class="btn btn-gold">Read Full Event Article →</a>
              <a href="product-library.html" class="btn btn-outline-gold">View Showcased Materials</a>
            </div>
          </div>
        </div>

        <div id="gzdw" style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 240px; overflow: hidden;"><a href="event-detail.html?id=gzdw"><img src="assets/images/guangzhou-hero.png" alt="Guangzhou Design Week" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;"></a></div>
          <div style="padding: 30px;">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">ANNUAL CHINA DELEGATION</span>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin: 6px 0 12px;"><a href="event-detail.html?id=gzdw" style="color: inherit; text-decoration: none;">Guangzhou Design Week (GZDW)</a></h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 18px;">Guangzhou Poly World Trade Center & Nan Fung Expo. Vision Focus organizes exclusive buyer delegations for prominent Indonesian architects to tour world-leading factories in Foshan.</p>
            <div style="display: flex; gap: 12px; flex-wrap: wrap;">
              <a href="event-detail.html?id=gzdw" class="btn btn-gold">Read Delegation Article →</a>
              <a href="contact.html" class="btn btn-outline-gold">Inquire Schedule</a>
            </div>
          </div>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-sm);">
          <div style="height: 240px; overflow: hidden;"><a href="event-detail.html?id=homelife"><img src="assets/images/logistics.jpg" alt="HomeLife Indonesia Expo" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;"></a></div>
          <div style="padding: 30px;">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">INTERNATIONAL TRADE FAIR</span>
            <h3 style="font-size: 1.35rem; color: var(--color-primary); margin: 6px 0 12px;"><a href="event-detail.html?id=homelife" style="color: inherit; text-decoration: none;">HomeLife Indonesia Expo</a></h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 18px;">Jakarta International Expo (JIExpo) Kemayoran. Connecting top-tier manufacturers of hardware, lighting, sanitaryware, and building appliances directly with Indonesian distributors.</p>
            <div style="display: flex; gap: 12px; flex-wrap: wrap;">
              <a href="event-detail.html?id=homelife" class="btn btn-gold">Read Trade Fair Article →</a>
              <button type="button" class="btn btn-outline-gold open-quote-modal">Schedule B2B Meeting</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: GZDW DELEGATION PROGRAM DETAILS -->
  <section style="padding: 80px 0; background: #ffffff; border-top: 1px solid var(--color-border);">
    <div class="container">
      <div class="resp-grid-2">
        <div>
          <span class="section-tag">EXCLUSIVE INVITATION</span>
          <h2 class="section-title">The Architect's Sourcing Delegation to Foshan</h2>
          <p style="color: #64748b; line-height: 1.7; margin: 16px 0 20px;">
            Twice a year, Vision Focus hosts a curated 5-day VIP tour for Indonesian architects, interior designers, and property developers to visit cutting-edge ceramics, metal, and smart-lighting factories in Foshan, Zhongshan, and Guangzhou.
          </p>
          <div style="display: flex; flex-direction: column; gap: 12px;">
            <div style="background: var(--color-surface-soft); padding: 14px; border-radius: 8px; border: 1px solid var(--color-border);">
              <strong style="color: var(--color-primary);">Day 1-2: Guangzhou Design Week VIP Pass</strong>
              <p style="font-size: 0.8rem; color: #64748b; margin-top: 2px;">Private lounge access and guided tour of curated international pavilions.</p>
            </div>
            <div style="background: var(--color-surface-soft); padding: 14px; border-radius: 8px; border: 1px solid var(--color-border);">
              <strong style="color: var(--color-primary);">Day 3-4: Factory Walkthroughs & Custom Lab</strong>
              <p style="font-size: 0.8rem; color: #64748b; margin-top: 2px;">Behind-the-scenes visits to robotic slab pressing kilns and bespoke surface workshops.</p>
            </div>
            <div style="background: var(--color-surface-soft); padding: 14px; border-radius: 8px; border: 1px solid var(--color-border);">
              <strong style="color: var(--color-primary);">Day 5: Business Roundtable & B2B Matchmaking</strong>
              <p style="font-size: 0.8rem; color: #64748b; margin-top: 2px;">Private dinners with factory CEOs to lock in exclusive project pricing.</p>
            </div>
          </div>
          <div style="margin-top: 24px;">
            <a href="event-detail.html?id=gzdw" class="btn btn-gold">Read Full Delegation Article & Agenda →</a>
          </div>
        </div>
        <div style="height: 380px; border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-md);">
          <img src="assets/images/insights-featured.jpg" alt="Guangzhou Delegation Tour" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
      </div>
    </div>
  </section>
        <div style="height: 380px; border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-md);">
          <img src="assets/images/insights-featured.jpg" alt="Guangzhou Delegation Tour" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: MEDIA & PRESS KIT -->
  <section style="padding: 70px 0; background: var(--color-surface-soft);">
    <div class="container">
      <div style="text-align: center; max-width: 680px; margin: 0 auto 30px;">
        <span class="section-tag" style="justify-content: center;">PRESS & MEDIA</span>
        <h2 class="section-title">Vision Focus in the Industry Press</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">Featured coverage on trade breakthroughs, building technology, and cross-border logistics.</p>
      </div>

      <div class="resp-grid-3">
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 24px;">
          <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">CONSTRUCTION ASIA</span>
          <h4 style="font-size: 1rem; color: var(--color-primary); margin: 6px 0 8px;">How Vision Focus Eliminated Sourcing Risks</h4>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Feature article analyzing our stationing of full-time inspection engineers in China to secure flawless SNI imports.</p>
        </div>
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 24px;">
          <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">INDONESIAN ARCHITECT DIGEST</span>
          <h4 style="font-size: 1rem; color: var(--color-primary); margin: 6px 0 8px;">The Sintered Stone Sensation</h4>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Showcasing how our custom porcelain slabs transformed luxury villa developments in Bali and Lombok.</p>
        </div>
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 24px;">
          <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">SUPPLY CHAIN INDONESIA</span>
          <h4 style="font-size: 1rem; color: var(--color-primary); margin: 6px 0 8px;">Container Consolidation Breakthrough</h4>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Report on our multi-vendor logistics hub in Foshan reducing transport friction for retail chain rollouts.</p>
        </div>
      </div>
    </div>
  </section>
"""

build_page(
    "events.html",
    "Events & Exhibitions",
    "Explore Vision Focus events including IndoBuildTech, Guangzhou Design Week (GZDW), and HomeLife trade fairs.",
    "ABOUT",
    "GLOBAL INDUSTRY EVENTS",
    "Events & Industry Exhibitions",
    "Showcasing next-generation building materials, architectural textures, and cross-border trade summits.",
    "Events",
    events_body
)

# ==============================================================================
# 6. PRODUCT-LIBRARY.HTML (5 ADDITIONAL RICH SECTIONS)
# ==============================================================================
products_body = """
  <!-- Section 1: Product Grid -->
  <section class="products-section" style="padding: 70px 0 40px;">
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

      <div class="products-grid-preview" style="margin-bottom: 50px;">
        <a href="product-detail.html?id=porcelain" class="product-tile">
          <div class="product-tile-img"><img src="assets/images/prod-granite.jpg" alt="Granite Tiles & Porcelain Slabs"></div>
          <div class="product-tile-info">
            <h5>Large Format Porcelain & Granite Slabs</h5>
            <p style="margin-bottom: 8px;">Available in 750x1500mm, 800x2600mm, and 1200x2700mm bookmatched formats for continuous vein wall and floor applications.</p>
            <div class="product-tile-footer">
              <span style="font-size: 0.76rem; color: var(--color-gold); font-weight: 700;">Honed, Polished, Soft-Matte</span>
              <span class="product-tile-footer-badge">View Tech Specs →</span>
            </div>
          </div>
        </a>

        <a href="product-detail.html?id=stainless" class="product-tile">
          <div class="product-tile-img"><img src="assets/images/prod-stainless.jpg" alt="Architectural Stainless Steel"></div>
          <div class="product-tile-info">
            <h5>Architectural Stainless Steel Panels</h5>
            <p style="margin-bottom: 8px;">Water ripple, mirror hairline, and embossed textures with PVD titanium vacuum plating in champagne gold, rose gold, and black.</p>
            <div class="product-tile-footer">
              <span style="font-size: 0.76rem; color: var(--color-gold); font-weight: 700;">Grade 304 & 316 Architectural</span>
              <span class="product-tile-footer-badge">View Tech Specs →</span>
            </div>
          </div>
        </a>

        <a href="product-detail.html?id=sanitary" class="product-tile">
          <div class="product-tile-img"><img src="assets/images/prod-sanitary.jpg" alt="Commercial Sanitaryware"></div>
          <div class="product-tile-info">
            <h5>Commercial Sanitary & Hardware</h5>
            <p style="margin-bottom: 8px;">Commercial-grade sensor taps, water-saving wall-hung WCs, and architectural hardware engineered for high-traffic environments.</p>
            <div class="product-tile-footer">
              <span style="font-size: 0.76rem; color: var(--color-gold); font-weight: 700;">SNI & WaterMark Certified</span>
              <span class="product-tile-footer-badge">View Tech Specs →</span>
            </div>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- SECTION 2: TECHNICAL SPECIFICATIONS MATRIX -->
  <section style="padding: 70px 0; background: var(--color-surface-soft); border-top: 1px solid var(--color-border);">
    <div class="container">
      <div style="text-align: center; max-width: 680px; margin: 0 auto 30px;">
        <span class="section-tag" style="justify-content: center;">ENGINEERING STANDARDS</span>
        <h2 class="section-title">Technical Performance Ratings</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">Every production run is calibrated against rigorous architectural mechanical criteria.</p>
      </div>

      <div class="comparison-table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Material Category</th>
              <th>Standard Sizes</th>
              <th>Thickness</th>
              <th>Water Absorption</th>
              <th>Slip Rating</th>
              <th>Surface Hardness</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Sintered Stone Slabs</strong></td>
              <td>1200x2700mm, 800x2600mm</td>
              <td>6mm, 9mm, 12mm</td>
              <td>&lt; 0.05%</td>
              <td>R10 - R11</td>
              <td>Mohs 7 (Scratch Proof)</td>
            </tr>
            <tr>
              <td><strong>Porcelain Floor Tiles</strong></td>
              <td>750x1500mm, 600x1200mm</td>
              <td>9.5mm, 11mm</td>
              <td>&lt; 0.1%</td>
              <td>R9 - R10</td>
              <td>Mohs 6.5</td>
            </tr>
            <tr>
              <td><strong>Architectural Stainless Steel</strong></td>
              <td>1219x2438mm, 1219x3048mm</td>
              <td>0.8mm - 2.0mm</td>
              <td>Non-Porous</td>
              <td>N/A</td>
              <td>PVD Titanium Coated</td>
            </tr>
            <tr>
              <td><strong>Crystal & Glass Mosaics</strong></td>
              <td>Sheet 300x300mm (Chip 25x25)</td>
              <td>4mm, 6mm, 8mm</td>
              <td>0.00% (Zero)</td>
              <td>R10 Anti-Slip Mesh</td>
              <td>Chemical Resistant</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- SECTION 3: SURFACE FINISHES & TEXTURES GUIDE -->
  <section style="padding: 80px 0; background: #ffffff;">
    <div class="container">
      <div style="text-align: center; max-width: 680px; margin: 0 auto 40px;">
        <span class="section-tag" style="justify-content: center;">SURFACE TEXTURES</span>
        <h2 class="section-title">Curated Architectural Textures</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">Tailored tactile experiences for floors, feature facades, and wet areas.</p>
      </div>

      <div class="resp-grid-4">
        <div style="border: 1px solid var(--color-border); border-radius: 12px; padding: 22px; background: var(--color-surface-soft);">
          <strong style="color: var(--color-primary); font-size: 1rem; display: block; margin-bottom: 6px;">Soft-Matte Honed</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Low sheen with a silky baby-skin touch. Ideal for modern minimal residential floors and gallery walls.</p>
        </div>
        <div style="border: 1px solid var(--color-border); border-radius: 12px; padding: 22px; background: var(--color-surface-soft);">
          <strong style="color: var(--color-primary); font-size: 1rem; display: block; margin-bottom: 6px;">Mirror Polished & Nano</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">High gloss &gt;95 degree clarity with nano stain seal coat for hotel lobbies and grand ballroom entrances.</p>
        </div>
        <div style="border: 1px solid var(--color-border); border-radius: 12px; padding: 22px; background: var(--color-surface-soft);">
          <strong style="color: var(--color-primary); font-size: 1rem; display: block; margin-bottom: 6px;">Water Ripple Stainless</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Dynamic stamped 3D fluid reflections for elevator ceilings, reception backdrops, and commercial ceilings.</p>
        </div>
        <div style="border: 1px solid var(--color-border); border-radius: 12px; padding: 22px; background: var(--color-surface-soft);">
          <strong style="color: var(--color-primary); font-size: 1rem; display: block; margin-bottom: 6px;">Flamed & Bush-Hammered</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Heavy mechanical slip resistance (R11/R12) for exterior plaza walkways, pool copings, and driveways.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 4: CUSTOM FABRICATION SERVICES -->
  <section style="padding: 80px 0; background: var(--color-surface-soft);">
    <div class="container">
      <div class="resp-grid-2">
        <div>
          <span class="section-tag">BESPOKE WORKMANSHIP</span>
          <h2 class="section-title">CNC Waterjet & Custom Metal Fabrication</h2>
          <p style="color: #64748b; line-height: 1.7; margin: 16px 0 20px;">
            Eliminate on-site dust and cutting errors. We pre-fabricate materials in China according to your CAD shop drawings: 45-degree mitered edge bonding for kitchen islands, bookmatched layout simulations, curved stainless column wrapping, and integrated sink cutouts.
          </p>
          <ul class="solution-card-points">
            <li><strong>5-Axis Waterjet Precision:</strong> Seamless floral inlays and geometric marble medallions.</li>
            <li><strong>Pre-Numbered Installation Layout:</strong> Slabs labeled sequentially matching your floorplan.</li>
            <li><strong>Dry-Lay Photos Before Packing:</strong> Full warehouse dry-lay approved by you prior to crating.</li>
          </ul>
        </div>
        <div style="height: 360px; border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-md);">
          <img src="assets/images/manufacturing.jpg" alt="CNC Precision Fabrication" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: SAMPLE BOX CALLOUT -->
  <section style="padding: 70px 0; background: linear-gradient(135deg, #111e2e 0%, #1e334c 100%); color: #ffffff;">
    <div class="container" style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 30px;">
      <div style="max-width: 640px;">
        <span style="color: var(--color-gold); font-size: 0.78rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;">DESIGNER SERVICE</span>
        <h3 style="font-family: var(--font-serif); font-size: 2.2rem; margin: 10px 0 14px;">Order a Physical Material Sample Box</h3>
        <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">Curated stone cuttings, stainless steel color swatches, and mosaic binders shipped express to your architectural practice in Jakarta or Surabaya.</p>
      </div>
      <div>
        <button type="button" class="btn btn-gold open-quote-modal" style="padding: 16px 36px; font-size: 0.95rem;">DISPATCH SAMPLE BOX →</button>
      </div>
    </div>
  </section>
"""

build_page(
    "product-library.html",
    "Product Library",
    "Curated material and product library from Vision Focus: large granite tiles, architectural stainless steel, mosaics, and sanitaryware.",
    "PRODUCT",
    "CURATED MATERIALS",
    "Product & Material Library",
    "High-performance architectural surfaces, engineered stones, and decorative metals direct from China.",
    "Product Library",
    products_body
)

# ==============================================================================
# 7. INSIGHTS.HTML (5 ADDITIONAL RICH SECTIONS)
# ==============================================================================
insights_body = """
  <!-- Section 1: Articles Grid -->
  <section class="products-section" style="padding: 70px 0 40px;">
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
          <div class="project-card-thumb"><a href="insight-detail.html?id=china-supply"><img src="assets/images/insights-featured.jpg" alt="China Supply Chain Update" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;"></a></div>
          <div class="project-card-body">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700; text-transform: uppercase;">MARKET ANALYSIS</span>
            <h4 style="margin-top: 6px;"><a href="insight-detail.html?id=china-supply" style="color: inherit; text-decoration: none;">China Supply Chain Update 2026: Trends & Mandates</a></h4>
            <p>How factory automation and green building mandates in Guangdong are reshaping lead times and competitive pricing structures.</p>
            <div class="project-specs-list" style="margin-bottom: 16px;"><span>5 min read</span><span>Updated Oct 2026</span></div>
            <a href="insight-detail.html?id=china-supply" class="btn btn-gold" style="width: 100%; text-align: center;">Read Full Article →</a>
          </div>
        </div>

        <div class="project-item-card" id="how-to-source">
          <div class="project-card-thumb"><a href="insight-detail.html?id=how-to-source"><img src="assets/images/step-shipping.jpg" alt="How to Direct Source from China" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;"></a></div>
          <div class="project-card-body">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700; text-transform: uppercase;">SOURCING GUIDE</span>
            <h4 style="margin-top: 6px;"><a href="insight-detail.html?id=how-to-source" style="color: inherit; text-decoration: none;">Direct Factory Sourcing in Foshan: The Practical Guide</a></h4>
            <p>Essential checklist for evaluating manufacturer capabilities, payment escrow, bilingual contracts, and avoiding common pitfalls.</p>
            <div class="project-specs-list" style="margin-bottom: 16px;"><span>8 min read</span><span>Practical Guide</span></div>
            <a href="insight-detail.html?id=how-to-source" class="btn btn-gold" style="width: 100%; text-align: center;">Read Full Article →</a>
          </div>
        </div>

        <div class="project-item-card" id="customs">
          <div class="project-card-thumb"><a href="insight-detail.html?id=customs"><img src="assets/images/logistics.jpg" alt="Import Regulations & SNI Guide" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;"></a></div>
          <div class="project-card-body">
            <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700; text-transform: uppercase;">TRADE REGULATIONS</span>
            <h4 style="margin-top: 6px;"><a href="insight-detail.html?id=customs" style="color: inherit; text-decoration: none;">Navigating Indonesian Customs & SNI Certifications</a></h4>
            <p>A step-by-step roadmap for clearing building materials, understanding import tariffs, and container port handling in Jakarta and Surabaya.</p>
            <div class="project-specs-list" style="margin-bottom: 16px;"><span>6 min read</span><span>Compliance Guide</span></div>
            <a href="insight-detail.html?id=customs" class="btn btn-gold" style="width: 100%; text-align: center;">Read Full Article →</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: LANDED COST FORMULA FRAMEWORK -->
  <section style="padding: 70px 0; background: var(--color-surface-soft); border-top: 1px solid var(--color-border);">
    <div class="container">
      <div style="text-align: center; max-width: 700px; margin: 0 auto 30px;">
        <span class="section-tag" style="justify-content: center;">COST TRANSPARENCY</span>
        <h2 class="section-title">The Complete Landed Cost Breakdown</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">Understanding every cost element between factory gate in China and your job site in Indonesia.</p>
      </div>

      <div class="resp-grid-4">
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 24px;">
          <strong style="color: var(--color-gold); font-size: 1.1rem; display: block; margin-bottom: 6px;">1. Ex-Factory / FOB</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Direct production cost in Foshan with volume tier discounts. We eliminate all local trade broker markups.</p>
        </div>
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 24px;">
          <strong style="color: var(--color-gold); font-size: 1.1rem; display: block; margin-bottom: 6px;">2. Sea Freight & Insurance</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Direct ocean carrier contracts from Nansha/Chiwan with comprehensive all-risk transit cargo insurance.</p>
        </div>
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 24px;">
          <strong style="color: var(--color-gold); font-size: 1.1rem; display: block; margin-bottom: 6px;">3. Form E & Duty Benefits</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">ACFTA Certificate of Origin (Form E) utilized to reduce or eliminate import tariffs legally.</p>
        </div>
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 24px;">
          <strong style="color: var(--color-gold); font-size: 1.1rem; display: block; margin-bottom: 6px;">4. Inland Port to Site</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Tanjung Perak or Tanjung Priok port terminal handling, customs release, and insured flatbed trucking.</p>
        </div>
      </div>
      <div style="text-align: center; margin-top: 30px;">
        <a href="insight-detail.html?id=landed-cost" class="btn btn-gold">Read Full Landed Cost Article & Case Study →</a>
      </div>
    </div>
  </section>

  <!-- SECTION 3: DOWNLOADABLE WHITEPAPERS -->
  <section style="padding: 80px 0; background: #ffffff;">
    <div class="container">
      <div style="text-align: center; max-width: 680px; margin: 0 auto 40px;">
        <span class="section-tag" style="justify-content: center;">RESEARCH & WHITEPAPERS</span>
        <h2 class="section-title">Quarterly Sourcing Whitepapers</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">Authoritative research compiled by our engineering and logistics analysts.</p>
      </div>

      <div class="resp-grid-3">
        <div style="border: 1px solid var(--color-border); border-radius: 12px; padding: 28px; background: var(--color-surface-soft);">
          <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">PDF REPORT &bull; 18 PAGES</span>
          <h4 style="font-size: 1.1rem; color: var(--color-primary); margin: 8px 0 10px;">Ceramics & Stone Price Index 2026</h4>
          <p style="font-size: 0.84rem; color: #64748b; line-height: 1.5; margin-bottom: 18px;">Analysis of raw natural gas prices, porcelain slab production capacity, and ocean container rate outlook.</p>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <a href="insight-detail.html?id=china-supply" class="btn btn-gold" style="font-size: 0.8rem; padding: 8px 14px;">Read Analysis →</a>
            <button type="button" class="btn btn-outline-gold open-quote-modal" style="font-size: 0.8rem; padding: 8px 14px;">Download PDF</button>
          </div>
        </div>

        <div style="border: 1px solid var(--color-border); border-radius: 12px; padding: 28px; background: var(--color-surface-soft);">
          <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">PDF REPORT &bull; 24 PAGES</span>
          <h4 style="font-size: 1.1rem; color: var(--color-primary); margin: 8px 0 10px;">The Indonesia SNI Compliance Guide</h4>
          <p style="font-size: 0.84rem; color: #64748b; line-height: 1.5; margin-bottom: 18px;">Complete legal reference on mandatory SNI testing, factory audit certification, and port release procedures.</p>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <a href="insight-detail.html?id=customs" class="btn btn-gold" style="font-size: 0.8rem; padding: 8px 14px;">Read Guide →</a>
            <button type="button" class="btn btn-outline-gold open-quote-modal" style="font-size: 0.8rem; padding: 8px 14px;">Download PDF</button>
          </div>
        </div>

        <div style="border: 1px solid var(--color-border); border-radius: 12px; padding: 28px; background: var(--color-surface-soft);">
          <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">PDF REPORT &bull; 15 PAGES</span>
          <h4 style="font-size: 1.1rem; color: var(--color-primary); margin: 8px 0 10px;">Retail Chain Fitout Sourcing Playbook</h4>
          <p style="font-size: 0.84rem; color: #64748b; line-height: 1.5; margin-bottom: 18px;">How Indonesia's top supermarkets standardize fixture specifications, reduce roll-out lead time, and cut costs.</p>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <a href="insight-detail.html?id=retail-playbook" class="btn btn-gold" style="font-size: 0.8rem; padding: 8px 14px;">Read Playbook →</a>
            <button type="button" class="btn btn-outline-gold open-quote-modal" style="font-size: 0.8rem; padding: 8px 14px;">Download PDF</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 4: NEWSLETTER SIGNUP -->
  <section style="padding: 70px 0; background: linear-gradient(135deg, #111e2e 0%, #1e334c 100%); color: #ffffff;">
    <div class="container" style="text-align: center; max-width: 640px; margin: 0 auto;">
      <span style="color: var(--color-gold); font-size: 0.78rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;">STAY AHEAD</span>
      <h3 style="font-family: var(--font-serif); font-size: 2.2rem; margin: 10px 0 14px;">China Trade & Material Briefing</h3>
      <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6; margin-bottom: 24px;">Join 3,000+ developers, architects, and procurement managers receiving our monthly analysis on factory holidays, currency exchange, and new material releases.</p>
      <form onsubmit="event.preventDefault(); alert('Thank you for subscribing to Vision Focus Market Intelligence!'); this.reset();" style="display: flex; gap: 10px; max-width: 480px; margin: 0 auto;">
        <input type="email" class="form-input" placeholder="Your work email address" required style="background: #ffffff; color: #1e293b;">
        <button type="submit" class="btn btn-gold" style="white-space: nowrap;">SUBSCRIBE →</button>
      </form>
    </div>
  </section>
"""

build_page(
    "insights.html",
    "Insights & Resources",
    "Expert guides and market updates on China sourcing, trade regulations, and architectural material trends.",
    "INSIGHTS",
    "INSIGHTS & RESOURCES",
    "Knowledge for Smarter Decisions",
    "Industry insights, product trends, market updates, and practical guides to empower your procurement decisions.",
    "Insights",
    insights_body
)

# ==============================================================================
# 8. CONTACT.HTML (5 ADDITIONAL RICH SECTIONS)
# ==============================================================================
contact_body = """
  <!-- Section 1: Office Cards & Form -->
  <section class="about-section" style="padding: 70px 0 40px; background: #ffffff;">
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
              <p style="color: #64748b; font-size: 0.88rem; margin-bottom: 6px;">Jl. Mayjen Sungkono, Surabaya, Indonesia. Material showroom, sampling library & maritime dispatch.</p>
              <span style="font-size: 0.85rem; color: var(--color-gold); font-weight: 600;">+62 31 555-1234 &bull; surabaya@visifokus.com</span>
            </div>

            <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 20px;">
              <strong style="color: var(--color-primary); font-size: 1rem; display: block; margin-bottom: 4px;">Jakarta Representative Office:</strong>
              <p style="color: #64748b; font-size: 0.88rem; margin-bottom: 6px;">Sudirman Central Business District (SCBD), Jakarta. Corporate real estate & developer consultancies.</p>
              <span style="font-size: 0.85rem; color: var(--color-gold); font-weight: 600;">+62 21 888-5678 &bull; jakarta@visifokus.com</span>
            </div>

            <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 20px;">
              <strong style="color: var(--color-primary); font-size: 1rem; display: block; margin-bottom: 4px;">Foshan / Guangdong Sourcing & QC Office:</strong>
              <p style="color: #64748b; font-size: 0.88rem; margin-bottom: 6px;">Chancheng District, Foshan, Guangdong Province, China. Factory audits, QC labs & staging hub.</p>
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
              <div class="resp-grid-2" style="gap: 14px;">
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

  <!-- SECTION 2: LIVE VIDEO CONSULTATION WITH FOSHAN DESK -->
  <section style="padding: 70px 0; background: var(--color-surface-soft); border-top: 1px solid var(--color-border);">
    <div class="container">
      <div class="resp-grid-2">
        <div>
          <span class="section-tag">VIRTUAL SHOWROOM</span>
          <h2 class="section-title">Schedule a Live Video Consultation</h2>
          <p style="color: #64748b; line-height: 1.7; margin: 16px 0 20px;">
            Can't travel to China right now? Book a live Zoom or Microsoft Teams session with our bilingual sourcing engineers directly from our Foshan material staging center. We inspect slab veins, test stainless finishes under direct lighting, and discuss technical parameters in real time.
          </p>
          <button type="button" class="btn btn-gold open-quote-modal">Book Video Sourcing Session →</button>
        </div>
        <div style="height: 340px; border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-md);">
          <img src="assets/images/step-needs.jpg" alt="Video Sourcing Consultation" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: CHINA BUSINESS TRAVEL & VISIT CONCIERGE -->
  <section style="padding: 80px 0; background: #ffffff;">
    <div class="container">
      <div style="text-align: center; max-width: 680px; margin: 0 auto 40px;">
        <span class="section-tag" style="justify-content: center;">CHINA VISIT CONCIERGE</span>
        <h2 class="section-title">Visiting China Factories with Us</h2>
        <p class="section-subtitle" style="margin: 10px auto 0;">Comprehensive on-the-ground support for Indonesian business delegations traveling to Guangdong.</p>
      </div>

      <div class="resp-grid-4">
        <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 22px;">
          <strong style="color: var(--color-gold); font-size: 1rem; display: block; margin-bottom: 6px;">Official Invitation</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Official business visa (M Visa) invitation letters issued through our Chinese entity.</p>
        </div>
        <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 22px;">
          <strong style="color: var(--color-gold); font-size: 1rem; display: block; margin-bottom: 6px;">Airport Pickup</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Private vehicle pickup from Guangzhou Baiyun (CAN) or Hong Kong airport to Foshan.</p>
        </div>
        <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 22px;">
          <strong style="color: var(--color-gold); font-size: 1rem; display: block; margin-bottom: 6px;">Bilingual Chaperone</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Dedicated Indonesian & Mandarin speaking technical manager accompanying every factory visit.</p>
        </div>
        <div style="background: var(--color-surface-soft); border: 1px solid var(--color-border); border-radius: 12px; padding: 22px;">
          <strong style="color: var(--color-gold); font-size: 1rem; display: block; margin-bottom: 6px;">Curated Accommodations</strong>
          <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5;">Recommended 5-star hotel partnerships and halal dining recommendations in Foshan.</p>
        </div>
      </div>
    </div>
  </section>
"""

build_page(
    "contact.html",
    "Contact Us",
    "Contact Vision Focus offices in Surabaya, Jakarta, and Foshan (China) for project procurement and sourcing inquiries.",
    "CONTACT",
    "GET IN TOUCH",
    "Let's Build Your Next Project",
    "Contact our dedicated sourcing team to discuss requirements or explore long-term factory supply agreements.",
    "Contact",
    contact_body
)

print("All detail pages successfully expanded with 3-5 rich sections!")
