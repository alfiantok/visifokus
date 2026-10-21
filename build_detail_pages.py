#!/usr/bin/env python3
"""
Generates project-detail.html and product-detail.html with rich interactive switchers,
technical spec matrices, image galleries, and client case study data.
"""
import os

with open("/Users/mekari/Documents/Visifokus/index.html", "r") as f:
    idx_content = f.read()

# Extract exact header and footer
header_clean = "  <!-- ==========================================\n       HEADER & NAVIGATION BAR" + idx_content.split("  <!-- ==========================================\n       HEADER & NAVIGATION BAR")[1].split("  <!-- ==========================================\n       HERO SECTION")[0]
footer_clean = "  <!-- ==========================================\n       FOOTER" + idx_content.split("  <!-- ==========================================\n       FOOTER")[1]

# -------------------------------------------------------------
# 1. PROJECT DETAIL HTML GENERATOR
# -------------------------------------------------------------
project_header = header_clean.replace('nav-link-item active', 'nav-link-item')
project_header = project_header.replace('mobile-nav-link active', 'mobile-nav-link')

project_detail_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Project Case Study & Portfolio Details | Vision Focus</title>
  <meta name="description" content="Detailed procurement case studies for commercial, hospitality, retail, and residential projects sourced directly from China to Indonesia.">
  <link rel="icon" type="image/png" href="assets/images/logo.png">
  <link rel="stylesheet" href="css/main.css">
  <style>
    .detail-tabs-bar {{
      display: flex;
      gap: 10px;
      overflow-x: auto;
      padding: 12px 0 24px;
      scrollbar-width: none;
    }}
    .detail-tabs-bar::-webkit-scrollbar {{ display: none; }}
    .detail-tab-btn {{
      padding: 10px 20px;
      border-radius: 50px;
      border: 1px solid var(--color-border);
      background: #ffffff;
      color: var(--color-primary);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all var(--transition-fast);
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .detail-tab-btn:hover,
    .detail-tab-btn.active {{
      background: var(--color-primary);
      color: #ffffff;
      border-color: var(--color-primary);
      box-shadow: 0 4px 14px rgba(17, 30, 46, 0.15);
    }}
    .detail-tab-btn.active .tab-badge {{
      background: var(--color-gold);
      color: #ffffff;
    }}
    .tab-badge {{
      font-size: 0.7rem;
      padding: 2px 8px;
      border-radius: 12px;
      background: var(--color-surface-soft);
      color: #64748b;
    }}
    .project-detail-panel {{
      display: none;
    }}
    .project-detail-panel.active {{
      display: block;
      animation: fadeIn 0.4s ease;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    .detail-meta-card {{
      background: #ffffff;
      border-radius: 14px;
      border: 1px solid var(--color-border);
      padding: 28px;
      box-shadow: var(--shadow-sm);
    }}
    .meta-stat-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-bottom: 24px;
      padding-bottom: 20px;
      border-bottom: 1px solid var(--color-border);
    }}
    .meta-stat-item h6 {{
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #94a3b8;
      margin-bottom: 4px;
    }}
    .meta-stat-item p {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--color-primary);
      margin: 0;
    }}
    .gallery-main-img {{
      width: 100%;
      height: 440px;
      object-fit: cover;
      border-radius: 12px;
    }}
    .gallery-thumbs {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin-top: 14px;
    }}
    .gallery-thumb-item {{
      height: 90px;
      border-radius: 8px;
      overflow: hidden;
      cursor: pointer;
      border: 2px solid transparent;
      transition: all var(--transition-fast);
    }}
    .gallery-thumb-item.active,
    .gallery-thumb-item:hover {{
      border-color: var(--color-gold);
    }}
    .gallery-thumb-item img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .spec-table-row {{
      display: flex;
      justify-content: space-between;
      padding: 10px 0;
      border-bottom: 1px solid rgba(0, 0, 0, 0.05);
      font-size: 0.88rem;
    }}
    .spec-table-row strong {{
      color: var(--color-primary);
    }}
    .spec-table-row span {{
      color: #64748b;
      text-align: right;
    }}
    @media (max-width: 992px) {{
      .meta-stat-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .gallery-main-img {{ height: 280px; }}
    }}
    @media (max-width: 640px) {{
      .meta-stat-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
{project_header}

  <!-- PAGE HERO -->
  <section class="page-hero-section">
    <div class="hero-background-wrapper">
      <img src="assets/images/guangzhou-hero.png" alt="Guangzhou Pearl River Canton Tower Skyline" class="hero-background-img">
    </div>
    <div class="hero-overlay"></div>

    <div class="container" style="position: relative; z-index: 3;">
      <div class="page-hero-content">
        <span class="hero-eyebrow">PORTFOLIO CASE STUDY</span>
        <h1 class="page-hero-title">Selected Project Details</h1>
        <p class="page-hero-subtitle">
          In-depth technical breakdown, direct factory sourcing logistics, and verified on-site installation references across Indonesia.
        </p>

        <div class="page-breadcrumbs">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <a href="projects.html">Projects</a>
          <span class="separator">/</span>
          <span id="breadcrumbCurrent">National Retail Chain</span>
        </div>
      </div>
    </div>
  </section>

  <!-- MAIN DETAIL CONTENT -->
  <main style="padding: 50px 0 90px; background: #fafbfc;">
    <div class="container">

      <!-- Interactive Project Selector Tabs -->
      <div class="detail-tabs-bar" role="tablist" aria-label="Select Project Case Study">
        <button type="button" class="detail-tab-btn active" data-target="retail">
          <span>Retail Chain Fitout</span>
          <span class="tab-badge">45+ Stores</span>
        </button>
        <button type="button" class="detail-tab-btn" data-target="hospitality">
          <span>5-Star Luxury Resort</span>
          <span class="tab-badge">Bali & Lombok</span>
        </button>
        <button type="button" class="detail-tab-btn" data-target="commercial">
          <span>Grade-A Financial Tower</span>
          <span class="tab-badge">Jakarta SCBD</span>
        </button>
        <button type="button" class="detail-tab-btn" data-target="residential">
          <span>High-End Residential Villas</span>
          <span class="tab-badge">Surabaya West</span>
        </button>
        <button type="button" class="detail-tab-btn" data-target="healthcare">
          <span>International Hospital</span>
          <span class="tab-badge">Medical Grade</span>
        </button>
        <button type="button" class="detail-tab-btn" data-target="infrastructure">
          <span>Logistics Hub & Warehouse</span>
          <span class="tab-badge">Industrial</span>
        </button>
      </div>

      <!-- ==============================================================
           PANEL 1: RETAIL FITOUT
           ============================================================== -->
      <div class="project-detail-panel active" id="panel-retail">
        <div style="display: grid; grid-template-columns: 1.25fr 1fr; gap: 36px; margin-bottom: 50px;">
          <!-- Left: Gallery -->
          <div>
            <div style="position: relative; overflow: hidden; border-radius: 14px; box-shadow: var(--shadow-sm);">
              <img id="mainImg-retail" src="assets/images/project-retail.jpg" alt="National Retail Chain Store Fitout" class="gallery-main-img">
              <span class="project-card-tag" style="top: 18px; left: 18px;">Retail Sourcing & Rollout</span>
            </div>
            <div class="gallery-thumbs">
              <div class="gallery-thumb-item active" onclick="switchMainImage('retail', 'assets/images/project-retail.jpg', this)">
                <img src="assets/images/project-retail.jpg" alt="Store Display Fitout">
              </div>
              <div class="gallery-thumb-item" onclick="switchMainImage('retail', 'assets/images/supermarket.jpg', this)">
                <img src="assets/images/supermarket.jpg" alt="Aisle Shelving">
              </div>
              <div class="gallery-thumb-item" onclick="switchMainImage('retail', 'assets/images/step-delivery.jpg', this)">
                <img src="assets/images/step-delivery.jpg" alt="Container Offloading">
              </div>
              <div class="gallery-thumb-item" onclick="switchMainImage('retail', 'assets/images/step-shipping.jpg', this)">
                <img src="assets/images/step-shipping.jpg" alt="Foshan Factory Packing">
              </div>
            </div>
          </div>

          <!-- Right: Summary & Key Metadata -->
          <div class="detail-meta-card">
            <span class="section-tag">COMMERCIAL RETAIL CHAIN</span>
            <h2 style="font-size: 1.8rem; font-weight: 700; color: var(--color-primary); margin: 6px 0 16px;">
              National Supermarket Network Fitout
            </h2>
            <p style="color: #64748b; font-size: 0.92rem; line-height: 1.6; margin-bottom: 24px;">
              Turnkey procurement, custom steel fabrication, and multi-port staged delivery of modular supermarket display gondolas, refrigerated showcase cabinets, and checkout cashwrap desks across 45+ retail outlets in Indonesia.
            </p>

            <div class="meta-stat-grid">
              <div class="meta-stat-item">
                <h6>Location</h6>
                <p>Nationwide (14 Cities)</p>
              </div>
              <div class="meta-stat-item">
                <h6>Timeframe</h6>
                <p>90 Days (Multi-batch)</p>
              </div>
              <div class="meta-stat-item">
                <h6>Volume</h6>
                <p>38 x 40ft HQ Containers</p>
              </div>
              <div class="meta-stat-item">
                <h6>Cost Savings</h6>
                <p style="color: var(--color-gold);">28.5% Direct-from-Factory</p>
              </div>
            </div>

            <h4 style="font-size: 1.05rem; font-weight: 700; color: var(--color-primary); margin-bottom: 12px;">Scope of Procurement</h4>
            <div class="spec-table-row"><strong>Heavy-Duty Gondolas</strong><span>Cold-rolled steel, epoxy powder finish</span></div>
            <div class="spec-table-row"><strong>Commercial Display Chillers</strong><span>CE / SNI compliant hermetic compressors</span></div>
            <div class="spec-table-row"><strong>Checkout Counters</strong><span>Brushed stainless steel surface + POS integration</span></div>
            <div class="spec-table-row"><strong>Quality Inspection</strong><span>100% pre-shipment assembly test in Foshan</span></div>
            <div class="spec-table-row"><strong>Customs Clearance</strong><span>Direct delivery to Tanjung Priok & Perak</span></div>

            <div style="display: flex; gap: 14px; margin-top: 26px;">
              <button type="button" class="btn btn-gold open-quote-modal" style="flex: 1;">Request Retail Proposal →</button>
              <a href="https://wa.me/6281234567890?text=Halo%20Vision%20Focus%2C%20saya%20tertarik%20dengan%20studi%20kasus%20Retail%20Fitout" target="_blank" rel="noopener noreferrer" class="btn-wa-solutions" style="padding: 12px 18px;">
                Chat WhatsApp
              </a>
            </div>
          </div>
        </div>

        <!-- Section: Challenge, Solution, Outcome -->
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;">
          <div style="background: #ffffff; border-radius: 12px; border: 1px solid var(--color-border); padding: 26px;">
            <div style="width: 40px; height: 40px; border-radius: 8px; background: rgba(220, 38, 38, 0.1); color: #dc2626; display: flex; align-items: center; justify-content: center; font-weight: 700; margin-bottom: 14px;">01</div>
            <h4 style="font-size: 1.1rem; font-weight: 700; color: var(--color-primary); margin-bottom: 10px;">The Challenge</h4>
            <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6;">
              Client was opening 45 branches simultaneously with strict grand opening deadlines. Local vendors quoted high markups (+35%) and couldn't guarantee uniform powder-coat RAL color matching across high quantities.
            </p>
          </div>

          <div style="background: #ffffff; border-radius: 12px; border: 1px solid var(--color-border); padding: 26px;">
            <div style="width: 40px; height: 40px; border-radius: 8px; background: var(--color-gold-light); color: var(--color-gold); display: flex; align-items: center; justify-content: center; font-weight: 700; margin-bottom: 14px;">02</div>
            <h4 style="font-size: 1.1rem; font-weight: 700; color: var(--color-primary); margin-bottom: 10px;">Vision Focus Solution</h4>
            <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6;">
              Direct contract with Foshan Tier-1 display manufacturing facility. Implemented an engineering pre-production prototype, conducted dry-fit tests, and locked in uniform RAL 9005 black matte finish across 38 containers.
            </p>
          </div>

          <div style="background: #ffffff; border-radius: 12px; border: 1px solid var(--color-border); padding: 26px;">
            <div style="width: 40px; height: 40px; border-radius: 8px; background: rgba(22, 163, 74, 0.1); color: #16a34a; display: flex; align-items: center; justify-content: center; font-weight: 700; margin-bottom: 14px;">03</div>
            <h4 style="font-size: 1.1rem; font-weight: 700; color: var(--color-primary); margin-bottom: 10px;">The Outcome</h4>
            <p style="font-size: 0.85rem; color: #64748b; line-height: 1.6;">
              100% on-time rollout with 0% defective shipments upon container destuffing. Client saved over Rp 2.4 Billion compared to traditional middleman importing and achieved standardized modular store interiors.
            </p>
          </div>
        </div>
      </div>

      <!-- ==============================================================
           PANEL 2: HOSPITALITY
           ============================================================== -->
      <div class="project-detail-panel" id="panel-hospitality">
        <div style="display: grid; grid-template-columns: 1.25fr 1fr; gap: 36px; margin-bottom: 50px;">
          <div>
            <div style="position: relative; overflow: hidden; border-radius: 14px; box-shadow: var(--shadow-sm);">
              <img id="mainImg-hospitality" src="assets/images/project-hospitality.jpg" alt="5-Star Luxury Resort" class="gallery-main-img">
              <span class="project-card-tag" style="top: 18px; left: 18px;">Luxury Hospitality & Resort</span>
            </div>
            <div class="gallery-thumbs">
              <div class="gallery-thumb-item active" onclick="switchMainImage('hospitality', 'assets/images/project-hospitality.jpg', this)">
                <img src="assets/images/project-hospitality.jpg" alt="Resort Villa">
              </div>
              <div class="gallery-thumb-item" onclick="switchMainImage('hospitality', 'assets/images/prod-granite.jpg', this)">
                <img src="assets/images/prod-granite.jpg" alt="Honed Porcelain">
              </div>
              <div class="gallery-thumb-item" onclick="switchMainImage('hospitality', 'assets/images/prod-sanitary.jpg', this)">
                <img src="assets/images/prod-sanitary.jpg" alt="Brushed Brass Taps">
              </div>
              <div class="gallery-thumb-item" onclick="switchMainImage('hospitality', 'assets/images/step-qc.jpg', this)">
                <img src="assets/images/step-qc.jpg" alt="QC Inspection">
              </div>
            </div>
          </div>

          <div class="detail-meta-card">
            <span class="section-tag">HOSPITALITY LANDMARK</span>
            <h2 style="font-size: 1.8rem; font-weight: 700; color: var(--color-primary); margin: 6px 0 16px;">
              5-Star Beachfront Luxury Resort & Spa
            </h2>
            <p style="color: #64748b; font-size: 0.92rem; line-height: 1.6; margin-bottom: 24px;">
              Procurement of large format 800x1600mm slip-resistant honed porcelain, artisan glass pool mosaics, and custom brushed brass bathroom fixtures for 120 luxury villas and public clubhouses in Bali and Lombok.
            </p>

            <div class="meta-stat-grid">
              <div class="meta-stat-item">
                <h6>Location</h6>
                <p>Bali & Lombok</p>
              </div>
              <div class="meta-stat-item">
                <h6>Timeframe</h6>
                <p>120 Days Staged Delivery</p>
              </div>
              <div class="meta-stat-item">
                <h6>Volume</h6>
                <p>24,000 sqm Slabs & Tiles</p>
              </div>
              <div class="meta-stat-item">
                <h6>Cost Savings</h6>
                <p style="color: var(--color-gold);">31.2% Direct Factory</p>
              </div>
            </div>

            <h4 style="font-size: 1.05rem; font-weight: 700; color: var(--color-primary); margin-bottom: 12px;">Supplied Materials</h4>
            <div class="spec-table-row"><strong>Porcelain Slabs</strong><span>800x1600mm honed matte, R11 slip rating</span></div>
            <div class="spec-table-row"><strong>Pool Glass Mosaics</strong><span>Deep cobalt custom blend, frost & chemical proof</span></div>
            <div class="spec-table-row"><strong>Sanitaryware & Taps</strong><span>Brushed champagne PVD brassware, water-saving</span></div>
            <div class="spec-table-row"><strong>Packaging Standard</strong><span>Fumigated seaworthy A-frame wooden crates</span></div>
            <div class="spec-table-row"><strong>Breakage Rate</strong><span>Zero broken slabs on site inspection</span></div>

            <div style="display: flex; gap: 14px; margin-top: 26px;">
              <button type="button" class="btn btn-gold open-quote-modal" style="flex: 1;">Inquire Hospitality Sourcing →</button>
              <a href="https://wa.me/6281234567890?text=Halo%20Vision%20Focus%2C%20saya%20tertarik%20dengan%20proyek%20Hospitality%20Resort" target="_blank" rel="noopener noreferrer" class="btn-wa-solutions" style="padding: 12px 18px;">
                Chat WhatsApp
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==============================================================
           PANEL 3: COMMERCIAL TOWER
           ============================================================== -->
      <div class="project-detail-panel" id="panel-commercial">
        <div style="display: grid; grid-template-columns: 1.25fr 1fr; gap: 36px; margin-bottom: 50px;">
          <div>
            <div style="position: relative; overflow: hidden; border-radius: 14px; box-shadow: var(--shadow-sm);">
              <img id="mainImg-commercial" src="assets/images/project-commercial.jpg" alt="Grade-A Corporate Tower" class="gallery-main-img">
              <span class="project-card-tag" style="top: 18px; left: 18px;">Grade-A Corporate Tower</span>
            </div>
            <div class="gallery-thumbs">
              <div class="gallery-thumb-item active" onclick="switchMainImage('commercial', 'assets/images/project-commercial.jpg', this)">
                <img src="assets/images/project-commercial.jpg" alt="Corporate Lobby">
              </div>
              <div class="gallery-thumb-item" onclick="switchMainImage('commercial', 'assets/images/prod-stainless.jpg', this)">
                <img src="assets/images/prod-stainless.jpg" alt="Stainless Panels">
              </div>
              <div class="gallery-thumb-item" onclick="switchMainImage('commercial', 'assets/images/manufacturing.jpg', this)">
                <img src="assets/images/manufacturing.jpg" alt="Metal Shearing">
              </div>
              <div class="gallery-thumb-item" onclick="switchMainImage('commercial', 'assets/images/developer.jpg', this)">
                <img src="assets/images/developer.jpg" alt="Facade Installation">
              </div>
            </div>
          </div>

          <div class="detail-meta-card">
            <span class="section-tag">COMMERCIAL HIGH-RISE</span>
            <h2 style="font-size: 1.8rem; font-weight: 700; color: var(--color-primary); margin: 6px 0 16px;">
              Grade-A Financial Tower & Elevator Halls
            </h2>
            <p style="color: #64748b; font-size: 0.92rem; line-height: 1.6; margin-bottom: 24px;">
              Architectural grade 316 titanium mirror stainless steel wall paneling, elevator surround portals, and fire-rated composite stone flooring for 42 floors of prestigious commercial office space in SCBD Jakarta.
            </p>

            <div class="meta-stat-grid">
              <div class="meta-stat-item">
                <h6>Location</h6>
                <p>SCBD, Jakarta</p>
              </div>
              <div class="meta-stat-item">
                <h6>Timeframe</h6>
                <p>150 Days Staged Batches</p>
              </div>
              <div class="meta-stat-item">
                <h6>Scope</h6>
                <p>42 Floors Elevator & Lobby</p>
              </div>
              <div class="meta-stat-item">
                <h6>Certification</h6>
                <p style="color: var(--color-gold);">ASTM & Fire-Rated A1</p>
              </div>
            </div>

            <h4 style="font-size: 1.05rem; font-weight: 700; color: var(--color-primary); margin-bottom: 12px;">Technical Specs</h4>
            <div class="spec-table-row"><strong>Stainless Steel</strong><span>316 Grade, 1.5mm thickness, PVD champagne gold</span></div>
            <div class="spec-table-row"><strong>Surface Finish</strong><span>Hairline + Anti-fingerprint nano-coating</span></div>
            <div class="spec-table-row"><strong>Lobby Stone</strong><span>1200x2700mm sintered stone Calacatta gold</span></div>
            <div class="spec-table-row"><strong>Laser Cutting</strong><span>Foshan factory computerized precision CNC</span></div>

            <div style="display: flex; gap: 14px; margin-top: 26px;">
              <button type="button" class="btn btn-gold open-quote-modal" style="flex: 1;">Request Commercial Specs →</button>
              <a href="https://wa.me/6281234567890?text=Halo%20Vision%20Focus%2C%20saya%20ingin%20tanya%20proyek%20Stainless%20Commercial" target="_blank" rel="noopener noreferrer" class="btn-wa-solutions" style="padding: 12px 18px;">
                Chat WhatsApp
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==============================================================
           PANEL 4: RESIDENTIAL
           ============================================================== -->
      <div class="project-detail-panel" id="panel-residential">
        <div style="display: grid; grid-template-columns: 1.25fr 1fr; gap: 36px; margin-bottom: 50px;">
          <div>
            <div style="position: relative; overflow: hidden; border-radius: 14px; box-shadow: var(--shadow-sm);">
              <img id="mainImg-residential" src="assets/images/project-residential.jpg" alt="High-End Residential Villas" class="gallery-main-img">
              <span class="project-card-tag" style="top: 18px; left: 18px;">Private Residential Estate</span>
            </div>
            <div class="gallery-thumbs">
              <div class="gallery-thumb-item active" onclick="switchMainImage('residential', 'assets/images/project-residential.jpg', this)">
                <img src="assets/images/project-residential.jpg" alt="Villa Interior">
              </div>
              <div class="gallery-thumb-item" onclick="switchMainImage('residential', 'assets/images/prod-granite.jpg', this)">
                <img src="assets/images/prod-granite.jpg" alt="Quartz Counter">
              </div>
            </div>
          </div>

          <div class="detail-meta-card">
            <span class="section-tag">RESIDENTIAL ESTATE</span>
            <h2 style="font-size: 1.8rem; font-weight: 700; color: var(--color-primary); margin: 6px 0 16px;">
              High-End Residential Villas
            </h2>
            <p style="color: #64748b; font-size: 0.92rem; line-height: 1.6; margin-bottom: 24px;">
              Custom sourcing of bookmatched Calacatta sintered stone slabs, quartz island counters, and bespoke minimalist aluminum slim-frame glass sliding partitions for 28 private luxury residences.
            </p>

            <div class="meta-stat-grid">
              <div class="meta-stat-item">
                <h6>Location</h6>
                <p>Surabaya West</p>
              </div>
              <div class="meta-stat-item">
                <h6>Volume</h6>
                <p>28 Luxury Units</p>
              </div>
              <div class="meta-stat-item">
                <h6>Timeframe</h6>
                <p>60 Days Delivery</p>
              </div>
              <div class="meta-stat-item">
                <h6>Saving</h6>
                <p style="color: var(--color-gold);">34% vs Local Importer</p>
              </div>
            </div>

            <div style="display: flex; gap: 14px; margin-top: 26px;">
              <button type="button" class="btn btn-gold open-quote-modal" style="flex: 1;">Request Residential Catalog →</button>
            </div>
          </div>
        </div>
      </div>

      <!-- ==============================================================
           PANEL 5: HEALTHCARE
           ============================================================== -->
      <div class="project-detail-panel" id="panel-healthcare">
        <div style="display: grid; grid-template-columns: 1.25fr 1fr; gap: 36px; margin-bottom: 50px;">
          <div>
            <div style="position: relative; overflow: hidden; border-radius: 14px; box-shadow: var(--shadow-sm);">
              <img id="mainImg-healthcare" src="assets/images/developer.jpg" alt="International Hospital Expansion" class="gallery-main-img">
              <span class="project-card-tag" style="top: 18px; left: 18px;">Medical & Cleanroom</span>
            </div>
          </div>
          <div class="detail-meta-card">
            <span class="section-tag">HEALTHCARE EXPANSION</span>
            <h2 style="font-size: 1.8rem; font-weight: 700; color: var(--color-primary); margin: 6px 0 16px;">
              International Hospital Expansion
            </h2>
            <p style="color: #64748b; font-size: 0.92rem; line-height: 1.6; margin-bottom: 24px;">
              Antibacterial medical-grade vinyl sheet flooring, anti-static cleanroom fixtures, and sensored surgical scrub sinks meeting strict international hospital hygiene benchmarks.
            </p>
            <div class="meta-stat-grid">
              <div class="meta-stat-item"><h6>Location</h6><p>Surabaya</p></div>
              <div class="meta-stat-item"><h6>Spec</h6><p>ISO 14644 Cleanroom</p></div>
              <div class="meta-stat-item"><h6>Volume</h6><p>8,500 sqm</p></div>
              <div class="meta-stat-item"><h6>Compliance</h6><p style="color: var(--color-gold);">100% Kemenkes</p></div>
            </div>
            <button type="button" class="btn btn-gold open-quote-modal" style="width: 100%;">Inquire Medical Grade Materials →</button>
          </div>
        </div>
      </div>

      <!-- ==============================================================
           PANEL 6: INFRASTRUCTURE
           ============================================================== -->
      <div class="project-detail-panel" id="panel-infrastructure">
        <div style="display: grid; grid-template-columns: 1.25fr 1fr; gap: 36px; margin-bottom: 50px;">
          <div>
            <div style="position: relative; overflow: hidden; border-radius: 14px; box-shadow: var(--shadow-sm);">
              <img id="mainImg-infrastructure" src="assets/images/logistics.jpg" alt="Logistics Hub" class="gallery-main-img">
              <span class="project-card-tag" style="top: 18px; left: 18px;">Industrial & Logistics</span>
            </div>
          </div>
          <div class="detail-meta-card">
            <span class="section-tag">LOGISTICS HUB</span>
            <h2 style="font-size: 1.8rem; font-weight: 700; color: var(--color-primary); margin: 6px 0 16px;">
              Logistics Center & Warehouse Facility
            </h2>
            <p style="color: #64748b; font-size: 0.92rem; line-height: 1.6; margin-bottom: 24px;">
              Procurement of heavy-duty polyurethane floor coatings, automated dock levelers, and energy-efficient commercial high-bay LED floodlighting in Cikarang industrial corridor.
            </p>
            <div class="meta-stat-grid">
              <div class="meta-stat-item"><h6>Location</h6><p>Cikarang, West Java</p></div>
              <div class="meta-stat-item"><h6>Floor Area</h6><p>42,000 sqm</p></div>
              <div class="meta-stat-item"><h6>Load Rating</h6><p>12 Ton / m²</p></div>
              <div class="meta-stat-item"><h6>Savings</h6><p style="color: var(--color-gold);">30.5% Factory Direct</p></div>
            </div>
            <button type="button" class="btn btn-gold open-quote-modal" style="width: 100%;">Inquire Industrial Sourcing →</button>
          </div>
        </div>
      </div>

      <!-- Quick Back & CTA Bar -->
      <div style="margin-top: 40px; padding: 24px; background: #ffffff; border-radius: 12px; border: 1px solid var(--color-border); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px;">
        <div>
          <a href="projects.html" class="btn btn-outline-gold">← Back to All Projects</a>
        </div>
        <div style="display: flex; gap: 14px; align-items: center;">
          <span style="font-size: 0.88rem; color: #64748b;">Have a similar project?</span>
          <button type="button" class="btn btn-gold open-quote-modal">Get a Custom Sourcing Quote →</button>
        </div>
      </div>

    </div>
  </main>

  <script>
    function switchMainImage(panelKey, src, thumbEl) {{
      const mainImg = document.getElementById('mainImg-' + panelKey);
      if (mainImg) mainImg.src = src;
      const parent = thumbEl.parentElement;
      parent.querySelectorAll('.gallery-thumb-item').forEach(t => t.classList.remove('active'));
      thumbEl.classList.add('active');
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      const urlParams = new URLSearchParams(window.location.search);
      const requestedId = urlParams.get('id') || 'retail';

      const tabBtns = document.querySelectorAll('.detail-tab-btn');
      const panels = document.querySelectorAll('.project-detail-panel');
      const breadcrumb = document.getElementById('breadcrumbCurrent');

      function showProject(id) {{
        tabBtns.forEach(btn => {{
          btn.classList.toggle('active', btn.dataset.target === id);
        }});
        panels.forEach(p => {{
          p.classList.toggle('active', p.id === 'panel-' + id);
        }});

        if (breadcrumb) {{
          const activeBtn = document.querySelector(`.detail-tab-btn[data-target="${{id}}"]`);
          if (activeBtn) breadcrumb.textContent = activeBtn.querySelector('span:first-child').textContent;
        }}
      }}

      tabBtns.forEach(btn => {{
        btn.addEventListener('click', () => {{
          const target = btn.dataset.target;
          showProject(target);
          history.replaceState(null, '', '?id=' + target);
        }});
      }});

      // Initial show from URL param
      showProject(requestedId);
    }});
  </script>
{footer_clean}
"""

with open("/Users/mekari/Documents/Visifokus/project-detail.html", "w") as f:
    f.write(project_detail_html)
print("Created project-detail.html successfully.")

# -------------------------------------------------------------
# 2. PRODUCT DETAIL HTML GENERATOR
# -------------------------------------------------------------
product_header = header_clean.replace('nav-link-item active', 'nav-link-item')
product_header = product_header.replace('mobile-nav-link active', 'mobile-nav-link')
product_header = product_header.replace('href="product-library.html" class="nav-link-item"', 'href="product-library.html" class="nav-link-item active"')

product_detail_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Material Specification & Technical Catalog | Vision Focus</title>
  <meta name="description" content="Detailed engineering specifications, dimensions, finishes, and direct factory procurement terms for porcelain slabs, architectural stainless steel, and commercial fixtures.">
  <link rel="icon" type="image/png" href="assets/images/logo.png">
  <link rel="stylesheet" href="css/main.css">
  <style>
    .material-tabs-bar {{
      display: flex;
      gap: 10px;
      overflow-x: auto;
      padding: 12px 0 24px;
      scrollbar-width: none;
    }}
    .material-tabs-bar::-webkit-scrollbar {{ display: none; }}
    .material-tab-btn {{
      padding: 10px 20px;
      border-radius: 50px;
      border: 1px solid var(--color-border);
      background: #ffffff;
      color: var(--color-primary);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all var(--transition-fast);
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .material-tab-btn:hover,
    .material-tab-btn.active {{
      background: var(--color-primary);
      color: #ffffff;
      border-color: var(--color-primary);
      box-shadow: 0 4px 14px rgba(17, 30, 46, 0.15);
    }}
    .material-tab-btn.active .tab-badge {{
      background: var(--color-gold);
      color: #ffffff;
    }}
    .material-detail-panel {{
      display: none;
    }}
    .material-detail-panel.active {{
      display: block;
      animation: fadeIn 0.4s ease;
    }}
    .spec-table-grid {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 14px;
    }}
    .spec-table-grid td {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--color-border);
      font-size: 0.86rem;
    }}
    .spec-table-grid tr:last-child td {{ border-bottom: none; }}
    .spec-table-grid td:first-child {{
      font-weight: 700;
      color: var(--color-primary);
      width: 38%;
      background: rgba(0, 0, 0, 0.015);
    }}
    .spec-table-grid td:last-child {{
      color: #475569;
    }}
  </style>
</head>
<body>
{product_header}

  <!-- PAGE HERO -->
  <section class="page-hero-section">
    <div class="hero-background-wrapper">
      <img src="assets/images/guangzhou-hero.png" alt="Guangzhou Pearl River Canton Tower Skyline" class="hero-background-img">
    </div>
    <div class="hero-overlay"></div>

    <div class="container" style="position: relative; z-index: 3;">
      <div class="page-hero-content">
        <span class="hero-eyebrow">CURATED MATERIALS</span>
        <h1 class="page-hero-title">Technical Material Library</h1>
        <p class="page-hero-subtitle">
          Direct manufacturer specifications, dimensional data, ASTM/SNI compliance ratings, and physical sample coordination from Foshan.
        </p>

        <div class="page-breadcrumbs">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <a href="product-library.html">Product Library</a>
          <span class="separator">/</span>
          <span id="breadcrumbMaterialCurrent">Porcelain & Granite Slabs</span>
        </div>
      </div>
    </div>
  </section>

  <!-- MAIN DETAIL CONTENT -->
  <main style="padding: 50px 0 90px; background: #fafbfc;">
    <div class="container">

      <!-- Interactive Material Selector Tabs -->
      <div class="material-tabs-bar" role="tablist" aria-label="Select Material Category">
        <button type="button" class="material-tab-btn active" data-target="porcelain">
          <span>Porcelain & Granite Slabs</span>
          <span class="tab-badge">Large Format</span>
        </button>
        <button type="button" class="material-tab-btn" data-target="stainless">
          <span>Architectural Stainless Steel</span>
          <span class="tab-badge">PVD Titanium</span>
        </button>
        <button type="button" class="material-tab-btn" data-target="sanitary">
          <span>Commercial Sanitaryware</span>
          <span class="tab-badge">WaterMark / SNI</span>
        </button>
        <button type="button" class="material-tab-btn" data-target="racking">
          <span>Modular Display Racking</span>
          <span class="tab-badge">Retail Systems</span>
        </button>
      </div>

      <!-- ==============================================================
           PANEL 1: PORCELAIN & GRANITE SLABS
           ============================================================== -->
      <div class="material-detail-panel active" id="mat-panel-porcelain">
        <div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 36px; margin-bottom: 50px;">
          <!-- Left: Images -->
          <div>
            <div style="position: relative; overflow: hidden; border-radius: 14px; box-shadow: var(--shadow-sm);">
              <img id="matImg-porcelain" src="assets/images/prod-granite.jpg" alt="Porcelain & Granite Slabs" class="gallery-main-img">
              <span class="project-card-tag" style="top: 18px; left: 18px;">Direct Foshan Sintered Stone</span>
            </div>
            <div class="gallery-thumbs">
              <div class="gallery-thumb-item active" onclick="switchMatImage('porcelain', 'assets/images/prod-granite.jpg', this)">
                <img src="assets/images/prod-granite.jpg" alt="Calacatta Porcelain Slab">
              </div>
              <div class="gallery-thumb-item" onclick="switchMatImage('porcelain', 'assets/images/project-residential.jpg', this)">
                <img src="assets/images/project-residential.jpg" alt="Installed Villa Living Room">
              </div>
              <div class="gallery-thumb-item" onclick="switchMatImage('porcelain', 'assets/images/project-hospitality.jpg', this)">
                <img src="assets/images/project-hospitality.jpg" alt="Honed Bathroom Application">
              </div>
            </div>
          </div>

          <!-- Right: Overview & CTA -->
          <div class="detail-meta-card">
            <span class="section-tag">PORCELAIN & SINTERED STONE</span>
            <h2 style="font-size: 1.8rem; font-weight: 700; color: var(--color-primary); margin: 6px 0 16px;">
              Large Format Porcelain & Granite Slabs
            </h2>
            <p style="color: #64748b; font-size: 0.92rem; line-height: 1.6; margin-bottom: 24px;">
              Engineered with advanced 36,000-ton Italian SACMI press technology and high-definition digital inkjet printing. Completely non-porous, UV-stable, and resistant to stains, extreme heat, and scratching.
            </p>

            <div class="meta-stat-grid">
              <div class="meta-stat-item">
                <h6>Absorption</h6>
                <p>&lt; 0.05% (Impervious)</p>
              </div>
              <div class="meta-stat-item">
                <h6>Hardness</h6>
                <p>Mohs 7 (Scratch Proof)</p>
              </div>
              <div class="meta-stat-item">
                <h6>Slip Rating</h6>
                <p>R10 - R11 Honed</p>
              </div>
              <div class="meta-stat-item">
                <h6>MOQ</h6>
                <p style="color: var(--color-gold);">1 x 20ft Container (~680m²)</p>
              </div>
            </div>

            <h4 style="font-size: 1.05rem; font-weight: 700; color: var(--color-primary); margin-bottom: 8px;">Standard Dimensions & Thickness</h4>
            <table class="spec-table-grid">
              <tbody>
                <tr><td>Available Sizes</td><td>750x1500mm, 800x2600mm, 1200x2700mm bookmatched</td></tr>
                <tr><td>Thickness Options</td><td>6mm (Wall Cladding), 9mm (Floor), 12mm (Countertops)</td></tr>
                <tr><td>Surface Finishes</td><td>Mirror Polished, Soft-Matte Honed, Leathered, Micro-Carved</td></tr>
                <tr><td>Packaging</td><td>Fumigated steel A-frames + reinforced wooden crating</td></tr>
                <tr><td>Certifications</td><td>CE, ISO 9001, SNI ISO 13006:2018</td></tr>
              </tbody>
            </table>

            <div style="display: flex; gap: 14px; margin-top: 26px;">
              <button type="button" class="btn btn-gold open-quote-modal" style="flex: 1;">Request Sample Box →</button>
              <a href="https://wa.me/6281234567890?text=Halo%20Vision%20Focus%2C%20saya%20ingin%20sample%20box%20Porcelain%20Slabs" target="_blank" rel="noopener noreferrer" class="btn-wa-solutions" style="padding: 12px 18px;">
                Chat WhatsApp
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==============================================================
           PANEL 2: ARCHITECTURAL STAINLESS STEEL
           ============================================================== -->
      <div class="material-detail-panel" id="mat-panel-stainless">
        <div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 36px; margin-bottom: 50px;">
          <div>
            <div style="position: relative; overflow: hidden; border-radius: 14px; box-shadow: var(--shadow-sm);">
              <img id="matImg-stainless" src="assets/images/prod-stainless.jpg" alt="Architectural Stainless Steel" class="gallery-main-img">
              <span class="project-card-tag" style="top: 18px; left: 18px;">PVD Titanium Vacuum Coating</span>
            </div>
          </div>

          <div class="detail-meta-card">
            <span class="section-tag">DECORATIVE METALS</span>
            <h2 style="font-size: 1.8rem; font-weight: 700; color: var(--color-primary); margin: 6px 0 16px;">
              Architectural Stainless Steel Panels
            </h2>
            <p style="color: #64748b; font-size: 0.92rem; line-height: 1.6; margin-bottom: 24px;">
              Specialized water ripple, mirror finish, hairline brushed, and custom embossed textures for luxury ceiling installations, column claddings, and elevator entrances.
            </p>

            <div class="meta-stat-grid">
              <div class="meta-stat-item"><h6>Grade</h6><p>AISI 304 & 316 Marine</p></div>
              <div class="meta-stat-item"><h6>Thickness</h6><p>0.8mm – 3.0mm</p></div>
              <div class="meta-stat-item"><h6>Coating</h6><p>PVD Titanium Vacuum</p></div>
              <div class="meta-stat-item"><h6>Protection</h6><p style="color: var(--color-gold);">Nano Anti-Fingerprint</p></div>
            </div>

            <table class="spec-table-grid">
              <tbody>
                <tr><td>Standard Sheet Sizes</td><td>1219x2438mm (4x8ft), 1219x3048mm (4x10ft), Custom CNC</td></tr>
                <tr><td>Popular Textures</td><td>Small/Medium Water Ripple, Mirror 8K, Hairline, Cross-stamped</td></tr>
                <tr><td>Available Colors</td><td>Champagne Gold, Rose Gold, Titanium Black, Bronze, Emerald</td></tr>
                <tr><td>Fabrication Support</td><td>Grooving, bending, laser cutting, welding studs pre-applied</td></tr>
              </tbody>
            </table>

            <div style="display: flex; gap: 14px; margin-top: 26px;">
              <button type="button" class="btn btn-gold open-quote-modal" style="flex: 1;">Request Stainless Swatches →</button>
            </div>
          </div>
        </div>
      </div>

      <!-- ==============================================================
           PANEL 3: COMMERCIAL SANITARYWARE
           ============================================================== -->
      <div class="material-detail-panel" id="mat-panel-sanitary">
        <div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 36px; margin-bottom: 50px;">
          <div>
            <div style="position: relative; overflow: hidden; border-radius: 14px; box-shadow: var(--shadow-sm);">
              <img id="matImg-sanitary" src="assets/images/prod-sanitary.jpg" alt="Commercial Sanitaryware" class="gallery-main-img">
              <span class="project-card-tag" style="top: 18px; left: 18px;">Commercial Grade</span>
            </div>
          </div>
          <div class="detail-meta-card">
            <span class="section-tag">SANITARY & HARDWARE</span>
            <h2 style="font-size: 1.8rem; font-weight: 700; color: var(--color-primary); margin: 6px 0 16px;">
              Commercial Sanitaryware & Fixtures
            </h2>
            <p style="color: #64748b; font-size: 0.92rem; line-height: 1.6; margin-bottom: 24px;">
              Engineered for malls, hotels, and airports. Water-saving rimless ceramic WCs, automatic infra-red sensor mixers, and vandal-resistant concealed flush mechanisms.
            </p>
            <div class="meta-stat-grid">
              <div class="meta-stat-item"><h6>Glaze</h6><p>Self-Cleaning Nano Glaze</p></div>
              <div class="meta-stat-item"><h6>Flush System</h6><p>Tornado Dual Flush 3/4.5L</p></div>
              <div class="meta-stat-item"><h6>Cartridge</h6><p>Sedal Ceramic (500k cycles)</p></div>
              <div class="meta-stat-item"><h6>Certification</h6><p style="color: var(--color-gold);">SNI & WaterMark</p></div>
            </div>
            <button type="button" class="btn btn-gold open-quote-modal" style="width: 100%;">Inquire Sanitary Catalog →</button>
          </div>
        </div>
      </div>

      <!-- ==============================================================
           PANEL 4: MODULAR RACKING
           ============================================================== -->
      <div class="material-detail-panel" id="mat-panel-racking">
        <div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 36px; margin-bottom: 50px;">
          <div>
            <div style="position: relative; overflow: hidden; border-radius: 14px; box-shadow: var(--shadow-sm);">
              <img id="matImg-racking" src="assets/images/supermarket.jpg" alt="Modular Racking" class="gallery-main-img">
              <span class="project-card-tag" style="top: 18px; left: 18px;">Commercial Retail Systems</span>
            </div>
          </div>
          <div class="detail-meta-card">
            <span class="section-tag">RETAIL FIXTURES</span>
            <h2 style="font-size: 1.8rem; font-weight: 700; color: var(--color-primary); margin: 6px 0 16px;">
              Modular Commercial Display Racking
            </h2>
            <p style="color: #64748b; font-size: 0.92rem; line-height: 1.6; margin-bottom: 24px;">
              Standardized modular shelving units for supermarkets, department stores, and boutique specialty retailers with quick boltless tool-free assembly.
            </p>
            <div class="meta-stat-grid">
              <div class="meta-stat-item"><h6>Material</h6><p>SPCC Cold-Rolled Steel</p></div>
              <div class="meta-stat-item"><h6>Capacity</h6><p>80kg - 150kg per shelf</p></div>
              <div class="meta-stat-item"><h6>Finish</h6><p>AkzoNobel Powder Coat</p></div>
              <div class="meta-stat-item"><h6>MOQ</h6><p style="color: var(--color-gold);">50 Sets / Modular Run</p></div>
            </div>
            <button type="button" class="btn btn-gold open-quote-modal" style="width: 100%;">Request Retail Rack Quote →</button>
          </div>
        </div>
      </div>

      <!-- Quick Back & CTA Bar -->
      <div style="margin-top: 40px; padding: 24px; background: #ffffff; border-radius: 12px; border: 1px solid var(--color-border); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px;">
        <div>
          <a href="product-library.html" class="btn btn-outline-gold">← Back to Full Product Library</a>
        </div>
        <div style="display: flex; gap: 14px; align-items: center;">
          <span style="font-size: 0.88rem; color: #64748b;">Need physical material samples?</span>
          <button type="button" class="btn btn-gold open-quote-modal">Request Sample Box →</button>
        </div>
      </div>

    </div>
  </main>

  <script>
    function switchMatImage(panelKey, src, thumbEl) {{
      const mainImg = document.getElementById('matImg-' + panelKey);
      if (mainImg) mainImg.src = src;
      const parent = thumbEl.parentElement;
      parent.querySelectorAll('.gallery-thumb-item').forEach(t => t.classList.remove('active'));
      thumbEl.classList.add('active');
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      const urlParams = new URLSearchParams(window.location.search);
      const requestedId = urlParams.get('id') || 'porcelain';

      const tabBtns = document.querySelectorAll('.material-tab-btn');
      const panels = document.querySelectorAll('.material-detail-panel');
      const breadcrumb = document.getElementById('breadcrumbMaterialCurrent');

      function showMaterial(id) {{
        tabBtns.forEach(btn => {{
          btn.classList.toggle('active', btn.dataset.target === id);
        }});
        panels.forEach(p => {{
          p.classList.toggle('active', p.id === 'mat-panel-' + id);
        }});

        if (breadcrumb) {{
          const activeBtn = document.querySelector(`.material-tab-btn[data-target="${{id}}"]`);
          if (activeBtn) breadcrumb.textContent = activeBtn.querySelector('span:first-child').textContent;
        }}
      }}

      tabBtns.forEach(btn => {{
        btn.addEventListener('click', () => {{
          const target = btn.dataset.target;
          showMaterial(target);
          history.replaceState(null, '', '?id=' + target);
        }});
      }});

      // Initial show from URL param
      showMaterial(requestedId);
    }});
  </script>
{footer_clean}
"""

with open("/Users/mekari/Documents/Visifokus/product-detail.html", "w") as f:
    f.write(product_detail_html)
print("Created product-detail.html successfully.")

# -------------------------------------------------------------
# 3. EVENT DETAIL HTML GENERATOR (ARTICLE PAGE LAYOUT)
# -------------------------------------------------------------
event_header = header_clean.replace('nav-link-item active', 'nav-link-item')
event_header = event_header.replace('mobile-nav-link active', 'mobile-nav-link')
event_header = event_header.replace('href="about.html" class="nav-link-item"', 'href="about.html" class="nav-link-item active"')
event_header = event_header.replace('href="about.html" class="mobile-nav-link mobile-accordion-trigger"', 'href="about.html" class="mobile-nav-link mobile-accordion-trigger active"')
event_header = event_header.replace('href="events.html" class="dropdown-item"', 'href="events.html" class="dropdown-item active"')
event_header = event_header.replace('href="events.html">Event</a>', 'href="events.html" class="active">Event</a>')

event_detail_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Event & Exhibition Article Details | Vision Focus</title>
  <meta name="description" content="In-depth event coverage, exhibition highlights, architectural material showcases, and buyer delegation reports from IndoBuildTech, Guangzhou Design Week, and Canton Fair.">
  <link rel="icon" type="image/png" href="assets/images/logo.png">
  <link rel="stylesheet" href="css/main.css">
  <style>
    .event-tabs-bar {{
      display: flex;
      gap: 10px;
      overflow-x: auto;
      padding: 12px 0 24px;
      scrollbar-width: none;
    }}
    .event-tabs-bar::-webkit-scrollbar {{ display: none; }}
    .event-tab-btn {{
      padding: 10px 20px;
      border-radius: 50px;
      border: 1px solid var(--color-border);
      background: #ffffff;
      color: var(--color-primary);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all var(--transition-fast);
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .event-tab-btn:hover,
    .event-tab-btn.active {{
      background: var(--color-primary);
      color: #ffffff;
      border-color: var(--color-primary);
      box-shadow: 0 4px 14px rgba(17, 30, 46, 0.15);
    }}
    .event-tab-btn.active .tab-badge {{
      background: var(--color-gold);
      color: #ffffff;
    }}
    .event-article-panel {{
      display: none;
    }}
    .event-article-panel.active {{
      display: block;
      animation: fadeIn 0.4s ease;
    }}
    .article-layout {{
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 40px;
      align-items: start;
    }}
    .article-content-card {{
      background: #ffffff;
      border-radius: 14px;
      border: 1px solid var(--color-border);
      padding: 40px;
      box-shadow: var(--shadow-sm);
    }}
    .article-lead {{
      font-size: 1.15rem;
      line-height: 1.75;
      color: #334155;
      font-weight: 500;
      margin-bottom: 28px;
      padding-bottom: 24px;
      border-bottom: 1px solid var(--color-border);
    }}
    .article-body-text h2,
    .article-body-text h3 {{
      font-family: var(--font-serif);
      color: var(--color-primary);
      margin: 32px 0 14px;
    }}
    .article-body-text h2 {{ font-size: 1.6rem; }}
    .article-body-text h3 {{ font-size: 1.3rem; }}
    .article-body-text p {{
      color: #475569;
      font-size: 0.96rem;
      line-height: 1.75;
      margin-bottom: 20px;
    }}
    .article-body-text ul {{
      margin: 16px 0 24px 20px;
      color: #475569;
      font-size: 0.95rem;
      line-height: 1.7;
    }}
    .article-body-text li {{ margin-bottom: 8px; }}
    .pull-quote-box {{
      border-left: 4px solid var(--color-gold);
      background: var(--color-surface-soft);
      border-radius: 0 10px 10px 0;
      padding: 22px 26px;
      margin: 30px 0;
      font-family: var(--font-serif);
      font-size: 1.15rem;
      font-style: italic;
      color: var(--color-primary);
      line-height: 1.65;
    }}
    .highlights-callout-card {{
      background: rgba(200, 155, 83, 0.08);
      border: 1px solid rgba(200, 155, 83, 0.35);
      border-radius: 12px;
      padding: 24px 28px;
      margin: 28px 0;
    }}
    .highlights-callout-card h4 {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--color-primary);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .highlights-checklist {{
      list-style: none;
      padding: 0;
      margin: 0;
    }}
    .highlights-checklist li {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.9rem;
      color: #334155;
      margin-bottom: 10px;
      line-height: 1.5;
    }}
    .highlights-checklist li svg {{
      color: var(--color-gold);
      flex-shrink: 0;
      margin-top: 3px;
    }}
    .article-sidebar-sticky {{
      position: sticky;
      top: calc(var(--header-height) + 20px);
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    .sidebar-widget {{
      background: #ffffff;
      border-radius: 14px;
      border: 1px solid var(--color-border);
      padding: 24px;
      box-shadow: var(--shadow-sm);
    }}
    .sidebar-widget-title {{
      font-size: 1rem;
      font-weight: 700;
      color: var(--color-primary);
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--color-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .event-meta-list {{
      display: flex;
      flex-direction: column;
      gap: 14px;
      font-size: 0.88rem;
    }}
    .event-meta-item strong {{
      display: block;
      color: #94a3b8;
      font-size: 0.74rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 2px;
    }}
    .event-meta-item span {{
      color: var(--color-primary);
      font-weight: 600;
    }}
    .article-author-card {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 20px;
      border-radius: 10px;
      background: var(--color-surface-soft);
      border: 1px solid var(--color-border);
      margin-top: 36px;
    }}
    .article-author-avatar {{
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: var(--color-primary);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 1.2rem;
      flex-shrink: 0;
    }}
    @media (max-width: 992px) {{
      .article-layout {{ grid-template-columns: 1fr; }}
      .article-content-card {{ padding: 26px 20px; }}
    }}
  </style>
</head>
<body>
{event_header}

  <!-- PAGE HERO -->
  <section class="page-hero-section">
    <div class="hero-background-wrapper">
      <img src="assets/images/guangzhou-hero.png" alt="Guangzhou Pearl River Skyline" class="hero-background-img">
    </div>
    <div class="hero-overlay"></div>

    <div class="container" style="position: relative; z-index: 3;">
      <div class="page-hero-content">
        <span class="hero-eyebrow">INDUSTRY EXHIBITIONS & EDITORIAL</span>
        <h1 class="page-hero-title">Event & Exhibition Coverage</h1>
        <p class="page-hero-subtitle">
          Full event articles, exclusive sourcing insights, VIP delegation programs, and architectural material showcases from major global trade fairs.
        </p>

        <div class="page-breadcrumbs">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <a href="events.html">Events</a>
          <span class="separator">/</span>
          <span id="breadcrumbEventCurrent">IndoBuildTech Expo 2025</span>
        </div>
      </div>
    </div>
  </section>

  <!-- MAIN ARTICLE CONTENT -->
  <main style="padding: 50px 0 90px; background: #fafbfc;">
    <div class="container">

      <!-- Interactive Event Selector Tabs -->
      <div class="event-tabs-bar" role="tablist" aria-label="Select Event Article">
        <button type="button" class="event-tab-btn active" data-target="ibt2025">
          <span>IndoBuildTech 2025</span>
          <span class="tab-badge">Upcoming</span>
        </button>
        <button type="button" class="event-tab-btn" data-target="gzdw">
          <span>Guangzhou Design Week</span>
          <span class="tab-badge">VIP Delegation</span>
        </button>
        <button type="button" class="event-tab-btn" data-target="ibt2024">
          <span>IndoBuildTech 2024</span>
          <span class="tab-badge">Past Showcase</span>
        </button>
        <button type="button" class="event-tab-btn" data-target="canton">
          <span>137th Canton Fair</span>
          <span class="tab-badge">Foshan Summit</span>
        </button>
        <button type="button" class="event-tab-btn" data-target="homelife">
          <span>HomeLife Indonesia</span>
          <span class="tab-badge">B2B Trade</span>
        </button>
      </div>

      <!-- ==============================================================
           ARTICLE 1: INDOBUILDTECH 2025
           ============================================================== -->
      <div class="event-article-panel active" id="article-ibt2025">
        <div class="article-layout">
          <!-- Main Article Body -->
          <article class="article-content-card">
            <!-- Article Header Info -->
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; flex-wrap: wrap;">
              <span class="section-tag" style="margin: 0;">UPCOMING FLAGSHIP EXPO</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">June 18–22, 2025</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">5 min read</span>
            </div>

            <h1 style="font-family: var(--font-serif); font-size: 2.2rem; font-weight: 700; color: var(--color-primary); line-height: 1.3; margin-bottom: 20px;">
              IndoBuildTech Expo 2025: Next-Generation Building Surfaces & Direct Factory Sourcing
            </h1>

            <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 28px;">
              <img src="assets/images/step-needs.jpg" alt="IndoBuildTech Exhibition Booth" style="width: 100%; height: 400px; object-fit: cover;">
              <div style="position: absolute; bottom: 0; left: 0; right: 0; background: rgba(10, 18, 28, 0.7); backdrop-filter: blur(8px); padding: 10px 16px; color: #e2e8f0; font-size: 0.8rem;">
                Vision Focus Exhibition Pavilion at ICE BSD City Hall 3 (Booth 3-A12).
              </div>
            </div>

            <p class="article-lead">
              At Indonesia's largest architecture, interior, and building technology fair, Vision Focus Trade Line will present our comprehensive 2025/2026 material showcase—bridging certified Foshan manufacturing with prominent Indonesian developers, contractors, and design consultancies.
            </p>

            <div class="highlights-callout-card">
              <h4>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
                Key Exhibition Highlights at Booth 3-A12:
              </h4>
              <ul class="highlights-checklist">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>1200x2700mm Continuous-Vein Sintered Slabs:</strong> Live demonstration of scratch resistance (Mohs 7) and zero water absorption.</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>Titanium PVD Water Ripple Stainless Steel:</strong> Mirrored ceiling claddings and custom gold, rose gold, and deep bronze panels.</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>Antibacterial Medical & Commercial Finishes:</strong> Seamless vinyl flooring and sensored touchless sanitary suites for healthcare and high-traffic projects.</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>Direct Factory Cost Calculator:</strong> Instant procurement cost comparison vs local middleman pricing for ongoing project BOQs.</span>
                </li>
              </ul>
            </div>

            <div class="article-body-text">
              <h2>Direct Sourcing: Eliminating the 30% Specifier Markup</h2>
              <p>
                Historically, Indonesian project developers have faced steep premiums when procuring imported architectural materials through multi-tiered broker networks. At IndoBuildTech 2025, our bilingual technical team will demonstrate our direct sourcing model—connecting developers straight to Guangdong automated manufacturing facilities with full quality control, sea freight logistics, and Indonesian customs clearance included.
              </p>

              <div class="pull-quote-box">
                "Our mission at IndoBuildTech is to show Indonesian architects that they can specify international tier-1 luxury materials without having to compromise budget or deal with uncertain shipping lead times."
              </div>

              <h2>Exclusive VIP Architect & Developer Consultation Lounge</h2>
              <p>
                In addition to the public exhibition floor, Vision Focus is hosting a private 2nd-floor VIP lounge at Booth 3-A12 for prescheduled business discussions. Architects can bring their ongoing project blueprints, CAD drawings, and material schedules to consult directly with our procurement engineers.
              </p>
              <p>
                Complimentary curated material sample boxes containing custom stone cuttings, titanium stainless swatches, and certified test reports will be dispatched directly to attending registered architectural practices.
              </p>

              <h2>How to Register for VIP Access</h2>
              <p>
                VIP access grants expedited badge collection at ICE BSD City, reserved seating during technical material seminars, and one-on-one procurement consulting sessions. Registration is complimentary for certified developers, contractors, and IAI / HDII design members.
              </p>
            </div>

            <!-- Author Bio Card -->
            <div class="article-author-card">
              <div class="article-author-avatar">VF</div>
              <div>
                <strong style="display: block; color: var(--color-primary); font-size: 1rem;">Vision Focus Trade Delegation Team</strong>
                <p style="font-size: 0.82rem; color: #64748b; margin-top: 4px; line-height: 1.5;">
                  Specialized in direct China-Indonesia supply chains, quality compliance, and commercial project procurement since 2016. Offices in Surabaya, Jakarta, and Foshan.
                </p>
              </div>
            </div>

            <!-- Share & Back Row -->
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 36px; padding-top: 24px; border-top: 1px solid var(--color-border); flex-wrap: wrap; gap: 14px;">
              <a href="events.html" class="btn btn-outline-gold">← Back to All Events</a>
              <div style="display: flex; gap: 10px;">
                <button type="button" class="btn btn-gold open-quote-modal">Register for VIP Pass →</button>
              </div>
            </div>
          </article>

          <!-- Sidebar Sticky Widget -->
          <aside class="article-sidebar-sticky">
            <div class="sidebar-widget">
              <h3 class="sidebar-widget-title">
                <span>Event Fast Facts</span>
                <span style="font-size: 0.72rem; color: var(--color-gold); font-weight: 700;">LIVE</span>
              </h3>
              <div class="event-meta-list">
                <div class="event-meta-item">
                  <strong>Date & Schedule</strong>
                  <span>June 18 – 22, 2025</span>
                </div>
                <div class="event-meta-item">
                  <strong>Venue</strong>
                  <span>ICE BSD City, Tangerang</span>
                </div>
                <div class="event-meta-item">
                  <strong>Vision Focus Location</strong>
                  <span>Hall 3 &bull; Booth 3-A12</span>
                </div>
                <div class="event-meta-item">
                  <strong>Target Audience</strong>
                  <span>Architects, Developers, Contractors</span>
                </div>
                <div class="event-meta-item">
                  <strong>VIP Concierge</strong>
                  <span>Fast-track entry + Sample box</span>
                </div>
              </div>

              <div style="margin-top: 22px;">
                <button type="button" class="btn btn-gold open-quote-modal" style="width: 100%; margin-bottom: 10px;">
                  Register VIP Pass →
                </button>
                <a href="https://wa.me/6281234567890?text=Halo%20Vision%20Focus%2C%20saya%20ingin%20registrasi%20VIP%20Pass%20IndoBuildTech%202025" target="_blank" rel="noopener noreferrer" class="btn-wa-solutions" style="width: 100%; justify-content: center;">
                  WhatsApp Concierge
                </a>
              </div>
            </div>

            <div class="sidebar-widget" style="background: var(--color-surface-soft);">
              <h3 class="sidebar-widget-title">Related Delegations</h3>
              <div style="display: flex; flex-direction: column; gap: 12px;">
                <a href="event-detail.html?id=gzdw" style="text-decoration: none; display: block; padding: 12px; background: #ffffff; border-radius: 8px; border: 1px solid var(--color-border);">
                  <span style="font-size: 0.7rem; color: var(--color-gold); font-weight: 700; text-transform: uppercase;">CHINA TOUR</span>
                  <strong style="display: block; font-size: 0.88rem; color: var(--color-primary); margin: 4px 0;">Guangzhou Design Week 2025</strong>
                  <span style="font-size: 0.76rem; color: #64748b;">5-Day VIP Architect Sourcing Tour →</span>
                </a>
                <a href="event-detail.html?id=canton" style="text-decoration: none; display: block; padding: 12px; background: #ffffff; border-radius: 8px; border: 1px solid var(--color-border);">
                  <span style="font-size: 0.7rem; color: var(--color-gold); font-weight: 700; text-transform: uppercase;">TRADE SUMMIT</span>
                  <strong style="display: block; font-size: 0.88rem; color: var(--color-primary); margin: 4px 0;">137th Canton Fair & Summit</strong>
                  <span style="font-size: 0.76rem; color: #64748b;">Direct B2B Pricing Channels →</span>
                </a>
              </div>
            </div>
          </aside>
        </div>
      </div>

      <!-- ==============================================================
           ARTICLE 2: GUANGZHOU DESIGN WEEK (GZDW)
           ============================================================== -->
      <div class="event-article-panel" id="article-gzdw">
        <div class="article-layout">
          <article class="article-content-card">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; flex-wrap: wrap;">
              <span class="section-tag" style="margin: 0;">ANNUAL CHINA DELEGATION</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">December 5–9, 2025</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">6 min read</span>
            </div>

            <h1 style="font-family: var(--font-serif); font-size: 2.2rem; font-weight: 700; color: var(--color-primary); line-height: 1.3; margin-bottom: 20px;">
              Guangzhou Design Week & The Foshan Sourcing Delegation: An Insider's Look
            </h1>

            <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 28px;">
              <img src="assets/images/guangzhou-hero.png" alt="Guangzhou Pearl River Canton Tower" style="width: 100%; height: 400px; object-fit: cover;">
              <div style="position: absolute; bottom: 0; left: 0; right: 0; background: rgba(10, 18, 28, 0.7); backdrop-filter: blur(8px); padding: 10px 16px; color: #e2e8f0; font-size: 0.8rem;">
                Guangzhou Poly World Trade Center & Foshan Ceramic Industrial Cluster.
              </div>
            </div>

            <p class="article-lead">
              Every winter, Vision Focus hosts a strictly curated, 5-day VIP tour for prominent Indonesian architects, interior designers, and real estate developers—combining Asia's most progressive design festival with backstage access to China's foremost industrial factories.
            </p>

            <div class="article-body-text">
              <h2>Beyond the Fairgrounds: Direct Plant Walkthroughs</h2>
              <p>
                While public exhibition visitors only see finished trade displays, Vision Focus delegates travel by private executive coach directly into Foshan and Zhongshan manufacturing plants. Delegates inspect 500-meter-long ceramic kilns, observe robotic automated sorting lines, and collaborate with factory color technicians to formulate bespoke glaze finishes.
              </p>

              <div class="highlights-callout-card">
                <h4>
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
                  Curated 5-Day VIP Delegation Itinerary:
                </h4>
                <ul class="highlights-checklist">
                  <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Day 1:</strong> Arrival in Guangzhou &bull; Welcome Dinner with Vision Focus China Team.</span></li>
                  <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Day 2:</strong> Guangzhou Design Week VIP Access & Guided Pavilion Tour at Poly World Trade Center.</span></li>
                  <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Day 3:</strong> Foshan Sintered Stone & Porcelain Megaplant Inspection & Laboratory Scratch Tests.</span></li>
                  <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Day 4:</strong> Decorative Stainless Steel & Commercial Lighting Custom Fabrication Workshops.</span></li>
                  <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Day 5:</strong> Private Roundtable with Factory CEOs to lock in direct project price covenants.</span></li>
                </ul>
              </div>

              <h2>Locking in Direct Contract Pricing</h2>
              <p>
                Participating firms frequently finalize material covenants for major multi-villa developments, corporate towers, and boutique hotel projects during the delegation, cutting delivery turnaround times by up to 45 days.
              </p>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 36px; padding-top: 24px; border-top: 1px solid var(--color-border); flex-wrap: wrap; gap: 14px;">
              <a href="events.html" class="btn btn-outline-gold">← Back to All Events</a>
              <button type="button" class="btn btn-gold open-quote-modal">Inquire for December 2025 Tour →</button>
            </div>
          </article>

          <!-- Sidebar -->
          <aside class="article-sidebar-sticky">
            <div class="sidebar-widget">
              <h3 class="sidebar-widget-title">Delegation Info</h3>
              <div class="event-meta-list">
                <div class="event-meta-item"><strong>Date</strong><span>December 5–9, 2025</span></div>
                <div class="event-meta-item"><strong>Location</strong><span>Guangzhou & Foshan, China</span></div>
                <div class="event-meta-item"><strong>Group Size</strong><span>Limited to 18 Delegates</span></div>
                <div class="event-meta-item"><strong>Language</strong><span>Bilingual (Indonesian / Mandarin)</span></div>
                <div class="event-meta-item"><strong>Includes</strong><span>Hotels, Transfers, Factory Access</span></div>
              </div>
              <button type="button" class="btn btn-gold open-quote-modal" style="width: 100%; margin-top: 20px;">Request Delegation Dossier →</button>
            </div>
          </aside>
        </div>
      </div>

      <!-- ==============================================================
           ARTICLE 3: INDOBUILDTECH 2024 RETROSPECTIVE
           ============================================================== -->
      <div class="event-article-panel" id="article-ibt2024">
        <div class="article-layout">
          <article class="article-content-card">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
              <span class="section-tag" style="margin: 0;">PAST EVENT SHOWCASE</span>
              <span style="font-size: 0.82rem; color: #64748b;">July 12–16, 2024 &bull; 4 min read</span>
            </div>
            <h1 style="font-family: var(--font-serif); font-size: 2.2rem; font-weight: 700; color: var(--color-primary); line-height: 1.3; margin-bottom: 20px;">
              IndoBuildTech 2024 Highlights: Connecting 5,000+ Designers with Direct Tier-1 Metals & Stones
            </h1>
            <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 28px;">
              <img src="assets/images/step-source.jpg" alt="IndoBuildTech 2024 Booth" style="width: 100%; height: 380px; object-fit: cover;">
            </div>
            <p class="article-lead">
              Our 2024 presence at ICE BSD City showcased the full breadth of Vision Focus direct sourcing capabilities—generating over Rp 18 Billion in verified project specifications across hospitality, commercial, and residential sectors.
            </p>
            <div class="article-body-text">
              <h2>Key Takeaways from the 2024 Exhibition Floor</h2>
              <p>
                Architectural demand heavily coalesced around tactile, organic surfaces and reflective titanium metals. Our water ripple stainless steel panels and bookmatched terrazzo displays drew continuous crowds from design firms across Jakarta, Surabaya, Bali, and Bandung.
              </p>
            </div>
            <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid var(--color-border);">
              <a href="product-library.html" class="btn btn-gold">Explore Showcased Materials →</a>
            </div>
          </article>
        </div>
      </div>

      <!-- ==============================================================
           ARTICLE 4: CANTON FAIR
           ============================================================== -->
      <div class="event-article-panel" id="article-canton">
        <div class="article-layout">
          <article class="article-content-card">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
              <span class="section-tag" style="margin: 0;">GLOBAL TRADE SUMMIT</span>
              <span style="font-size: 0.82rem; color: #64748b;">April 15–19, 2025 &bull; 5 min read</span>
            </div>
            <h1 style="font-family: var(--font-serif); font-size: 2.2rem; font-weight: 700; color: var(--color-primary); line-height: 1.3; margin-bottom: 20px;">
              137th Canton Fair & The Foshan Global Sourcing Summit
            </h1>
            <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 28px;">
              <img src="assets/images/developer.jpg" alt="Canton Fair Sourcing" style="width: 100%; height: 380px; object-fit: cover;">
            </div>
            <p class="article-lead">
              Navigating the world's premier export gathering. Direct insights into container freight economics, Guangdong industrial pricing trends, and factory direct contract negotiations.
            </p>
            <div class="article-body-text">
              <h2>Navigating the World's Largest Trade Fair</h2>
              <p>
                The Canton Fair spans over 1.5 million square meters of exhibition space. Vision Focus procurement officers coordinate curated walk routes for Indonesian purchasing managers, focusing specifically on verified Tier-1 building material manufacturers with established SNI and international quality credentials.
              </p>
            </div>
            <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid var(--color-border);">
              <button type="button" class="btn btn-gold open-quote-modal">Consult Canton Fair Team →</button>
            </div>
          </article>
        </div>
      </div>

      <!-- ==============================================================
           ARTICLE 5: HOMELIFE
           ============================================================== -->
      <div class="event-article-panel" id="article-homelife">
        <div class="article-layout">
          <article class="article-content-card">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
              <span class="section-tag" style="margin: 0;">B2B TRADE EXPO</span>
              <span style="font-size: 0.82rem; color: #64748b;">November 27–29, 2024 &bull; 4 min read</span>
            </div>
            <h1 style="font-family: var(--font-serif); font-size: 2.2rem; font-weight: 700; color: var(--color-primary); line-height: 1.3; margin-bottom: 20px;">
              HomeLife Indonesia B2B Expo: Connecting Guangdong Industrial Power with Indonesian Trade
            </h1>
            <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 28px;">
              <img src="assets/images/logistics.jpg" alt="HomeLife Expo" style="width: 100%; height: 380px; object-fit: cover;">
            </div>
            <p class="article-lead">
              At JIExpo Kemayoran, Vision Focus facilitated direct B2B matchmaking between verified Foshan hardware manufacturers and regional Indonesian distribution networks.
            </p>
            <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid var(--color-border);">
              <button type="button" class="btn btn-gold open-quote-modal">Schedule Business Meeting →</button>
            </div>
          </article>
        </div>
      </div>

    </div>
  </main>

  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const urlParams = new URLSearchParams(window.location.search);
      const requestedId = urlParams.get('id') || 'ibt2025';

      const tabBtns = document.querySelectorAll('.event-tab-btn');
      const panels = document.querySelectorAll('.event-article-panel');
      const breadcrumb = document.getElementById('breadcrumbEventCurrent');

      function showEvent(id) {{
        tabBtns.forEach(btn => {{
          btn.classList.toggle('active', btn.dataset.target === id);
        }});
        panels.forEach(p => {{
          p.classList.toggle('active', p.id === 'article-' + id);
        }});

        if (breadcrumb) {{
          const activeBtn = document.querySelector(`.event-tab-btn[data-target="${{id}}"]`);
          if (activeBtn) breadcrumb.textContent = activeBtn.querySelector('span:first-child').textContent;
        }}
      }}

      tabBtns.forEach(btn => {{
        btn.addEventListener('click', () => {{
          const target = btn.dataset.target;
          showEvent(target);
          history.replaceState(null, '', '?id=' + target);
        }});
      }});

      // Initial show from URL param
      showEvent(requestedId);
    }});
  </script>
{footer_clean}
"""

with open("/Users/mekari/Documents/Visifokus/event-detail.html", "w") as f:
    f.write(event_detail_html)
print("Created event-detail.html successfully.")

# -------------------------------------------------------------
# 4. INSIGHT DETAIL HTML GENERATOR (BLOG MODEL ARTICLE PAGE)
# -------------------------------------------------------------
insight_header = header_clean.replace('nav-link-item active', 'nav-link-item')
insight_header = insight_header.replace('mobile-nav-link active', 'mobile-nav-link')
insight_header = insight_header.replace('href="insights.html" class="nav-link-item"', 'href="insights.html" class="nav-link-item active"')
insight_header = insight_header.replace('href="insights.html" class="mobile-nav-link"', 'href="insights.html" class="mobile-nav-link active"')

insight_detail_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sourcing Insights & Strategic Guides | Vision Focus</title>
  <meta name="description" content="In-depth analysis, expert guides, and market intelligence on China factory sourcing, landed costs, SNI compliance, and cross-border logistics.">
  <link rel="icon" type="image/png" href="assets/images/logo.png">
  <link rel="stylesheet" href="css/main.css">
  <style>
    .insight-tabs-bar {{
      display: flex;
      gap: 10px;
      overflow-x: auto;
      padding: 12px 0 24px;
      scrollbar-width: none;
    }}
    .insight-tabs-bar::-webkit-scrollbar {{ display: none; }}
    .insight-tab-btn {{
      padding: 10px 20px;
      border-radius: 50px;
      border: 1px solid var(--color-border);
      background: #ffffff;
      color: var(--color-primary);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all var(--transition-fast);
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .insight-tab-btn:hover,
    .insight-tab-btn.active {{
      background: var(--color-primary);
      color: #ffffff;
      border-color: var(--color-primary);
      box-shadow: 0 4px 14px rgba(17, 30, 46, 0.15);
    }}
    .insight-tab-btn .tab-badge {{
      font-size: 0.7rem;
      padding: 2px 8px;
      border-radius: 12px;
      background: var(--color-surface-soft);
      color: var(--color-gold);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .insight-tab-btn.active .tab-badge {{
      background: var(--color-gold);
      color: #ffffff;
    }}
    .insight-article-panel {{
      display: none;
    }}
    .insight-article-panel.active {{
      display: block;
      animation: fadeIn 0.4s ease;
    }}
    .article-layout {{
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 40px;
      align-items: start;
    }}
    .article-content-card {{
      background: #ffffff;
      border-radius: 14px;
      border: 1px solid var(--color-border);
      padding: 40px;
      box-shadow: var(--shadow-sm);
    }}
    .article-lead {{
      font-size: 1.15rem;
      line-height: 1.75;
      color: #334155;
      font-weight: 500;
      margin-bottom: 28px;
      padding-bottom: 24px;
      border-bottom: 1px solid var(--color-border);
    }}
    .article-body-text h2,
    .article-body-text h3 {{
      font-family: var(--font-serif);
      color: var(--color-primary);
      margin: 32px 0 14px;
    }}
    .article-body-text h2 {{ font-size: 1.6rem; }}
    .article-body-text h3 {{ font-size: 1.3rem; }}
    .article-body-text p {{
      color: #475569;
      font-size: 0.96rem;
      line-height: 1.75;
      margin-bottom: 20px;
    }}
    .article-body-text ul,
    .article-body-text ol {{
      margin: 16px 0 24px 20px;
      color: #475569;
      font-size: 0.95rem;
      line-height: 1.7;
    }}
    .article-body-text li {{ margin-bottom: 8px; }}
    .pull-quote-box {{
      border-left: 4px solid var(--color-gold);
      background: var(--color-surface-soft);
      border-radius: 0 10px 10px 0;
      padding: 22px 26px;
      margin: 30px 0;
      font-family: var(--font-serif);
      font-size: 1.15rem;
      font-style: italic;
      color: var(--color-primary);
      line-height: 1.65;
    }}
    .highlights-callout-card {{
      background: rgba(200, 155, 83, 0.08);
      border: 1px solid rgba(200, 155, 83, 0.35);
      border-radius: 12px;
      padding: 24px 28px;
      margin: 28px 0;
    }}
    .highlights-callout-card h4 {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--color-primary);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .highlights-checklist {{
      list-style: none;
      padding: 0;
      margin: 0;
    }}
    .highlights-checklist li {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.9rem;
      color: #334155;
      margin-bottom: 10px;
      line-height: 1.5;
    }}
    .highlights-checklist li svg {{
      color: var(--color-gold);
      flex-shrink: 0;
      margin-top: 3px;
    }}
    .data-table-wrap {{
      overflow-x: auto;
      margin: 24px 0;
      border: 1px solid var(--color-border);
      border-radius: 10px;
    }}
    .article-data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      text-align: left;
    }}
    .article-data-table th {{
      background: var(--color-surface-soft);
      padding: 12px 16px;
      color: var(--color-primary);
      font-weight: 700;
      border-bottom: 1px solid var(--color-border);
    }}
    .article-data-table td {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--color-border);
      color: #475569;
    }}
    .article-data-table tr:last-child td {{ border-bottom: none; }}
    .article-sidebar-sticky {{
      position: sticky;
      top: calc(var(--header-height) + 20px);
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    .sidebar-widget {{
      background: #ffffff;
      border-radius: 14px;
      border: 1px solid var(--color-border);
      padding: 24px;
      box-shadow: var(--shadow-sm);
    }}
    .sidebar-widget-title {{
      font-size: 1rem;
      font-weight: 700;
      color: var(--color-primary);
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--color-border);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .toc-list li a {{
      font-size: 0.85rem;
      color: #64748b;
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: color var(--transition-fast);
      padding: 4px 0;
    }}
    .toc-list li a:hover {{
      color: var(--color-gold);
    }}
    .article-author-card {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 20px;
      border-radius: 10px;
      background: var(--color-surface-soft);
      border: 1px solid var(--color-border);
      margin-top: 36px;
    }}
    .article-author-avatar {{
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: var(--color-primary);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 1.2rem;
      flex-shrink: 0;
    }}
    .article-share-cta-bar {{
      margin-top: 36px;
      padding-top: 24px;
      border-top: 1px solid var(--color-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
    }}
    @media (max-width: 992px) {{
      .article-layout {{ grid-template-columns: 1fr; }}
      .article-content-card {{ padding: 26px 20px; }}
    }}
  </style>
</head>
<body>
{insight_header}

  <!-- PAGE HERO -->
  <section class="page-hero-section">
    <div class="hero-background-wrapper">
      <img src="assets/images/guangzhou-hero.png" alt="Guangzhou Pearl River Skyline" class="hero-background-img">
    </div>
    <div class="hero-overlay"></div>

    <div class="container" style="position: relative; z-index: 3;">
      <div class="page-hero-content">
        <span class="hero-eyebrow">KNOWLEDGE HUB & INDUSTRY INSIGHTS</span>
        <h1 class="page-hero-title">Sourcing Insights & Strategic Guides</h1>
        <p class="page-hero-subtitle">
          Authoritative intelligence on China factory pricing, supply chain shifts, SNI customs compliance, and landed cost optimization for Indonesian business leaders.
        </p>

        <div class="page-breadcrumbs">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <a href="insights.html">Insights</a>
          <span class="separator">/</span>
          <span id="breadcrumbInsightCurrent">China Supply Chain Update 2026</span>
        </div>
      </div>
    </div>
  </section>

  <!-- MAIN ARTICLE CONTENT -->
  <main style="padding: 50px 0 90px; background: #fafbfc;">
    <div class="container">

      <!-- Interactive Blog Topic Selector Tabs -->
      <div class="insight-tabs-bar" role="tablist" aria-label="Select Article Topic">
        <button type="button" class="insight-tab-btn active" data-target="china-supply">
          <span>Supply Chain 2026</span>
          <span class="tab-badge">Market Analysis</span>
        </button>
        <button type="button" class="insight-tab-btn" data-target="how-to-source">
          <span>Direct Sourcing Guide</span>
          <span class="tab-badge">Playbook</span>
        </button>
        <button type="button" class="insight-tab-btn" data-target="customs">
          <span>Customs & SNI</span>
          <span class="tab-badge">Regulations</span>
        </button>
        <button type="button" class="insight-tab-btn" data-target="landed-cost">
          <span>Landed Cost Formula</span>
          <span class="tab-badge">Financial</span>
        </button>
        <button type="button" class="insight-tab-btn" data-target="retail-playbook">
          <span>Retail Fitout Playbook</span>
          <span class="tab-badge">Retail Sourcing</span>
        </button>
      </div>

      <!-- ==============================================================
           ARTICLE 1: CHINA SUPPLY CHAIN UPDATE 2026
           ============================================================== -->
      <div class="insight-article-panel active" id="article-china-supply">
        <div class="article-layout">
          <!-- Main Blog Content -->
          <article class="article-content-card">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; flex-wrap: wrap;">
              <span class="section-tag" style="margin: 0;">MARKET ANALYSIS</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">October 15, 2026</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">6 min read</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: var(--color-gold); font-weight: 600;">By Jason Shi</span>
            </div>

            <h1 style="font-family: var(--font-serif); font-size: 2.2rem; font-weight: 700; color: var(--color-primary); line-height: 1.3; margin-bottom: 20px;">
              China Supply Chain Update 2026: Factory Automation, Green Building Mandates & Lead Times in Guangdong
            </h1>

            <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 28px;">
              <img src="assets/images/insights-featured.jpg" alt="Guangdong Industrial Supply Chain" style="width: 100%; height: 420px; object-fit: cover;">
              <div style="position: absolute; bottom: 0; left: 0; right: 0; background: rgba(10, 18, 28, 0.7); backdrop-filter: blur(8px); padding: 10px 16px; color: #e2e8f0; font-size: 0.8rem;">
                Automated continuous roller kilns inside a Tier-1 sintered stone facility in Nanhai District, Foshan.
              </div>
            </div>

            <p class="article-lead">
              As Guangdong province enforces stricter dual-carbon energy quotas and environmental monitoring across the Pearl River Delta, manufacturing economics for ceramic slabs, stainless steel facades, and commercial fixtures are transforming rapidly. Here is our field analysis on pricing trends, lead times, and risk mitigation strategies for Indonesian developers and procurement directors.
            </p>

            <div class="highlights-callout-card">
              <h4>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
                Key Market Intelligence for Q3/Q4 2026:
              </h4>
              <ul class="highlights-checklist">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>Automated Kilns Reduce Waste by 18%:</strong> Italian Sacmi Continua+ lines in Foshan now produce zero-tension sintered slabs with ±0.3mm planar accuracy.</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>Tier-1 Manufacturer Consolidation:</strong> Smaller polluting workshops have closed; certified mega-plants now guarantee steady capacity and reliable ISO/SNI compliance.</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>Nansha / Chiwan Port Transit Times:</strong> Direct ocean vessels to Tanjung Priok (Jakarta) and Tanjung Perak (Surabaya) maintain consistent 8 to 11 days sailing times.</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>Quarterly FOB Pricing Stability:</strong> Locking raw material contracts 60–90 days ahead hedges against natural gas fluctuations during northern winter months.</span>
                </li>
              </ul>
            </div>

            <div class="article-body-text">
              <h2>1. The Industrial Shift in Foshan's Ceramic & Metal Hubs</h2>
              <p>
                Over the past 24 months, Guangdong's provincial administration has accelerated the transition toward green manufacturing. For Indonesian buyers, this has eliminated many unreliable fly-by-night subcontractors who previously competed solely on price while compromising thickness tolerances and glaze durability.
              </p>
              <p>
                Today, surviving Tier-1 factories operate robotic glaze printing, computerized color spectrophotometers, and zero-discharge closed-loop water filtration. The result is superior batch-to-batch color consistency that Indonesian architects require for luxury hotels, commercial podiums, and expansive retail malls.
              </p>

              <div class="pull-quote-box">
                "Direct factory relationships in China are no longer just about shaving 30% off local distributor markups—they are about engineering control, certified testing standards, and guaranteed shipping schedules."
              </div>

              <h2>2. Ocean Logistics & Lead Time Planning Matrix</h2>
              <p>
                To avoid construction delays, project procurement managers must account for production cycling, holiday shutdowns (most notably Chinese New Year and Golden Week), and container consolidation windows:
              </p>

              <div class="data-table-wrap">
                <table class="article-data-table">
                  <thead>
                    <tr>
                      <th>Material Category</th>
                      <th>Production Lead Time</th>
                      <th>QC & Packing</th>
                      <th>Transit to Indo Ports</th>
                      <th>Total Safe Buffer</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Large Porcelain Slabs</strong></td>
                      <td>20 - 25 Days</td>
                      <td>4 - 6 Days</td>
                      <td>9 - 12 Days</td>
                      <td><strong>45 - 50 Days</strong></td>
                    </tr>
                    <tr>
                      <td><strong>PVD Stainless Steel Panels</strong></td>
                      <td>18 - 22 Days</td>
                      <td>3 - 5 Days</td>
                      <td>9 - 12 Days</td>
                      <td><strong>40 - 45 Days</strong></td>
                    </tr>
                    <tr>
                      <td><strong>Supermarket Racking Fixtures</strong></td>
                      <td>15 - 20 Days</td>
                      <td>3 - 4 Days</td>
                      <td>8 - 11 Days</td>
                      <td><strong>35 - 40 Days</strong></td>
                    </tr>
                    <tr>
                      <td><strong>Commercial Sanitaryware</strong></td>
                      <td>25 - 30 Days</td>
                      <td>5 - 7 Days</td>
                      <td>9 - 12 Days</td>
                      <td><strong>50 - 55 Days</strong></td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <h2>3. How Vision Focus Protects Indonesian Clients</h2>
              <p>
                Because our headquarters maintains full-time engineering and inspection teams permanently stationed in Foshan, Vision Focus conducts on-site raw material inspections before production, dry-fit mockups before crating, and direct supervised container stuffing. Clients receive detailed high-resolution inspection reports and timestamped video documentation prior to authorising final balance payments.
              </p>
            </div>

            <!-- Author Bio Card -->
            <div class="article-author-card">
              <div class="article-author-avatar">JS</div>
              <div>
                <strong style="color: var(--color-primary); font-size: 1.05rem;">Jason Shi</strong>
                <p style="font-size: 0.8rem; color: var(--color-gold); font-weight: 600; margin: 2px 0 6px;">Founder & Managing Director, Vision Focus Trade Line</p>
                <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5; margin: 0;">
                  With over a decade of cross-border manufacturing leadership in Foshan and Indonesia, Jason has structured direct sourcing operations for more than 40 premier hotel, commercial, and retail developments across Southeast Asia.
                </p>
              </div>
            </div>

            <!-- Share / Consultation CTA -->
            <div class="article-share-cta-bar">
              <div>
                <span style="font-size: 0.82rem; color: #64748b; font-weight: 600;">Need a supply chain review for your project?</span>
              </div>
              <div style="display: flex; gap: 10px;">
                <button type="button" class="btn btn-gold open-quote-modal">Request Project Review →</button>
                <a href="https://wa.me/6281234567890?text=Halo%20Vision%20Focus%2C%20saya%20ingin%20konsultasi%20analisis%20Supply%20Chain%202026" target="_blank" rel="noopener noreferrer" class="btn-wa-solutions">
                  WhatsApp Sourcing Desk
                </a>
              </div>
            </div>
          </article>

          <!-- Sticky Sidebar -->
          <aside class="article-sidebar-sticky">
            <div class="sidebar-widget">
              <h4 class="sidebar-widget-title">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>
                Article Sections
              </h4>
              <ul class="toc-list">
                <li><a href="#article-china-supply">1. Industrial Shift in Foshan</a></li>
                <li><a href="#article-china-supply">2. Direct Contracts vs Middlemen</a></li>
                <li><a href="#article-china-supply">3. Lead Time Planning Matrix</a></li>
                <li><a href="#article-china-supply">4. Quality Protection in Foshan</a></li>
              </ul>
            </div>

            <div class="sidebar-widget" style="background: linear-gradient(135deg, #111e2e 0%, #1e334c 100%); color: #ffffff;">
              <span style="color: var(--color-gold); font-size: 0.72rem; font-weight: 700; text-transform: uppercase;">FREE WHITEPAPER</span>
              <h4 style="color: #ffffff; font-size: 1.1rem; margin: 8px 0 10px;">Ceramics & Stone Price Index 2026</h4>
              <p style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5; margin-bottom: 18px;">
                Download our 18-page quarterly whitepaper with factory pricing benchmarks and ocean freight forecasts.
              </p>
              <button type="button" class="btn btn-gold open-quote-modal" style="width: 100%; text-align: center;">Download PDF (Free) →</button>
            </div>

            <div class="sidebar-widget">
              <h4 class="sidebar-widget-title">Trending Insights</h4>
              <div style="display: flex; flex-direction: column; gap: 14px;">
                <a href="insight-detail.html?id=how-to-source" style="text-decoration: none; display: block;">
                  <span style="font-size: 0.7rem; color: var(--color-gold); font-weight: 700;">SOURCING PLAYBOOK</span>
                  <h6 style="color: var(--color-primary); font-size: 0.88rem; margin: 2px 0;">Direct Factory Sourcing in Foshan: Step-by-Step</h6>
                </a>
                <a href="insight-detail.html?id=customs" style="text-decoration: none; display: block;">
                  <span style="font-size: 0.7rem; color: var(--color-gold); font-weight: 700;">TRADE REGULATIONS</span>
                  <h6 style="color: var(--color-primary); font-size: 0.88rem; margin: 2px 0;">Navigating Indonesian Customs & SNI Standards</h6>
                </a>
                <a href="insight-detail.html?id=landed-cost" style="text-decoration: none; display: block;">
                  <span style="font-size: 0.7rem; color: var(--color-gold); font-weight: 700;">COST TRANSPARENCY</span>
                  <h6 style="color: var(--color-primary); font-size: 0.88rem; margin: 2px 0;">The Complete Landed Cost Formula Explained</h6>
                </a>
              </div>
            </div>
          </aside>
        </div>
      </div>

      <!-- ==============================================================
           ARTICLE 2: HOW TO DIRECT SOURCE FROM FOSHAN
           ============================================================== -->
      <div class="insight-article-panel" id="article-how-to-source">
        <div class="article-layout">
          <article class="article-content-card">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; flex-wrap: wrap;">
              <span class="section-tag" style="margin: 0;">SOURCING PLAYBOOK</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">October 10, 2026</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">8 min read</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: var(--color-gold); font-weight: 600;">By Vision Focus Procurement Team</span>
            </div>

            <h1 style="font-family: var(--font-serif); font-size: 2.2rem; font-weight: 700; color: var(--color-primary); line-height: 1.3; margin-bottom: 20px;">
              Direct Factory Sourcing in Foshan: The Practical Step-by-Step Guide for Indonesian Businesses
            </h1>

            <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 28px;">
              <img src="assets/images/step-shipping.jpg" alt="Direct Sourcing in China" style="width: 100%; height: 420px; object-fit: cover;">
              <div style="position: absolute; bottom: 0; left: 0; right: 0; background: rgba(10, 18, 28, 0.7); backdrop-filter: blur(8px); padding: 10px 16px; color: #e2e8f0; font-size: 0.8rem;">
                On-site dimensional and flatness verification before packing at a Guangdong manufacturer.
              </div>
            </div>

            <p class="article-lead">
              Sourcing directly from Chinese manufacturers provides Indonesian developers, contractors, and retail chains with access to superior pricing and bespoke customization. However, without established protocols, companies face counterfeit materials, broken tiles, and contract ambiguities. This playbook outlines the exact 4-phase framework we use to secure flawless procurement.
            </p>

            <div class="highlights-callout-card">
              <h4>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
                Core Pillars of Safe Direct Sourcing:
              </h4>
              <ul class="highlights-checklist">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>Manufacturer Verification:</strong> Confirming genuine factory ownership vs trading brokers via on-site kiln audits and business registry checks.</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>Bilingual Legal Contracts:</strong> Enforceable agreements specifying exact tolerances (ASTM/EN/SNI) and penalty clauses in both English and Mandarin.</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>Golden Sample Archival:</strong> Retaining dual signed physical reference samples in Foshan and Surabaya to benchmark production batches.</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>30/70 Escrow Milestone:</strong> Never releasing final balance until independent pre-shipment quality inspection is certified 100% passed.</span>
                </li>
              </ul>
            </div>

            <div class="article-body-text">
              <h2>Phase 1: Due Diligence & Factory Qualification</h2>
              <p>
                In Foshan alone, there are tens of thousands of trading firms posing as manufacturers in showrooms and online portals. Working with an intermediary adds an unnecessary 15% to 35% margin markup and distorts communication between your structural engineers and factory machine operators.
              </p>
              <p>
                Vision Focus conducts on-site factory verification checks: reviewing the manufacturer's export license, verifying environmental permits, inspecting continuous kiln production lines, and reviewing past supply records for major international hotel chains.
              </p>

              <h2>Phase 2: Specification Locking & Counter-Sampling</h2>
              <p>
                Never initiate mass production based solely on a digital catalog or PDF render. In our procurement lifecycle:
              </p>
              <ol>
                <li>We request physical sample swatches under controlled D65 daylight lamps.</li>
                <li>The factory produces two identical "Golden Samples"—one remains sealed at our Foshan QA laboratory, while the other is couriered to the client's architect in Indonesia.</li>
                <li>Both parties sign physical stickers on the reverse of the sample, documenting acceptable tolerances for gloss level, vein variation, and surface texture.</li>
              </ol>

              <div class="pull-quote-box">
                "The golden sample is the supreme court of cross-border procurement. When physical standards are sealed in advance, dispute risks during container unloading are practically zero."
              </div>

              <h2>Phase 3: Milestone-Based Payment Structuring</h2>
              <p>
                Traditional wire transfers offer zero leverage if quality fails upon container arrival in Jakarta. We structure production contracts around strict milestone gates:
              </p>
              <ul>
                <li><strong>30% Deposit:</strong> To purchase raw materials and initiate production tooling.</li>
                <li><strong>In-Line Inspection Gate:</strong> Photographic and video validation during slab pressing and kiln firing.</li>
                <li><strong>Pre-Shipment Inspection (PSI):</strong> Full testing of dimensions, scratch hardness, packaging crate moisture, and fumigation stamps.</li>
                <li><strong>70% Balance Release:</strong> Only after the client approves the final comprehensive QA inspection report and bill of lading draft.</li>
              </ul>
            </div>

            <div class="article-author-card">
              <div class="article-author-avatar">VF</div>
              <div>
                <strong style="color: var(--color-primary); font-size: 1.05rem;">Vision Focus Sourcing Advisory Desk</strong>
                <p style="font-size: 0.8rem; color: var(--color-gold); font-weight: 600; margin: 2px 0 6px;">Bilingual Procurement & Quality Engineers</p>
                <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5; margin: 0;">
                  Operating directly from Foshan and Surabaya, our engineers manage factory audits, supplier contracts, and pre-shipment quality protocols for leading Indonesian projects.
                </p>
              </div>
            </div>

            <div class="article-share-cta-bar">
              <div>
                <span style="font-size: 0.82rem; color: #64748b; font-weight: 600;">Have a vendor in China you need verified?</span>
              </div>
              <div style="display: flex; gap: 10px;">
                <button type="button" class="btn btn-gold open-quote-modal">Request Factory Audit →</button>
                <a href="https://wa.me/6281234567890?text=Halo%20Vision%20Focus%2C%20saya%20butuh%20bantuan%20audit%20pabrik%20di%20China" target="_blank" rel="noopener noreferrer" class="btn-wa-solutions">
                  Audit Consultation
                </a>
              </div>
            </div>
          </article>

          <!-- Sidebar -->
          <aside class="article-sidebar-sticky">
            <div class="sidebar-widget">
              <h4 class="sidebar-widget-title">Table of Contents</h4>
              <ul class="toc-list">
                <li><a href="#article-how-to-source">Phase 1: Due Diligence</a></li>
                <li><a href="#article-how-to-source">Phase 2: Golden Samples</a></li>
                <li><a href="#article-how-to-source">Phase 3: Milestone Payments</a></li>
                <li><a href="#article-how-to-source">Phase 4: Pre-Shipment QC</a></li>
              </ul>
            </div>

            <div class="sidebar-widget">
              <span class="section-tag" style="margin-bottom: 8px;">SOURCING PLAYBOOK</span>
              <h5 style="color: var(--color-primary); font-size: 1rem; margin-bottom: 8px;">Direct Factory BOQ Review</h5>
              <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5; margin-bottom: 16px;">
                Send us your bill of quantities or architectural drawings. We provide an itemized factory price comparison within 48 hours.
              </p>
              <button type="button" class="btn btn-gold open-quote-modal" style="width: 100%;">Submit BOQ for Review →</button>
            </div>
          </aside>
        </div>
      </div>

      <!-- ==============================================================
           ARTICLE 3: CUSTOMS & SNI REGULATIONS
           ============================================================== -->
      <div class="insight-article-panel" id="article-customs">
        <div class="article-layout">
          <article class="article-content-card">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; flex-wrap: wrap;">
              <span class="section-tag" style="margin: 0;">TRADE REGULATIONS</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">October 5, 2026</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">7 min read</span>
            </div>

            <h1 style="font-family: var(--font-serif); font-size: 2.2rem; font-weight: 700; color: var(--color-primary); line-height: 1.3; margin-bottom: 20px;">
              Navigating Indonesian Customs, SNI Certifications & Port Clearance Procedures
            </h1>

            <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 28px;">
              <img src="assets/images/logistics.jpg" alt="Port Clearance and Customs" style="width: 100%; height: 420px; object-fit: cover;">
              <div style="position: absolute; bottom: 0; left: 0; right: 0; background: rgba(10, 18, 28, 0.7); backdrop-filter: blur(8px); padding: 10px 16px; color: #e2e8f0; font-size: 0.8rem;">
                Container vessel discharging cargo at Tanjung Priok Port, Jakarta.
              </div>
            </div>

            <p class="article-lead">
              Importing building materials into Indonesia without exact regulatory compliance can lead to costly red-line customs physical inspections, container demurrage penalties, or cargo rejection. Here is how Vision Focus ensures 100% legal, zero-demurrage clearance through SNI compliance and ACFTA Form E tariff optimization.
            </p>

            <div class="highlights-callout-card">
              <h4>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
                Key Regulatory Checkpoints for Importers:
              </h4>
              <ul class="highlights-checklist">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>Mandatory SNI Testing:</strong> Required for ceramic tiles (SNI ISO 13006), sanitary ceramics (SNI 03-0797), and architectural structural steel.</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>Form E Tariff Elimination:</strong> Utilizing ASEAN-China Free Trade Agreement (ACFTA) certificates to reduce import tariffs from 5–15% down to 0%.</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>Pre-Arrival Electronic Manifest:</strong> Submitting BC 1.1 documentation prior to vessel berthing to secure immediate green-line customs release.</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                  <span><strong>ISPM 15 Wood Fumigation:</strong> Mandatory IPPC heat treatment stamp on all wooden packing crates to prevent quarantine holds.</span>
                </li>
              </ul>
            </div>

            <div class="article-body-text">
              <h2>1. Understanding Mandatory SNI Requirements</h2>
              <p>
                The Indonesian Ministry of Industry enforces mandatory SNI (Standar Nasional Indonesia) on specific building material categories to protect public safety and domestic standards. Importing uncertified materials exposes buyers to confiscation and hefty administrative fines.
              </p>
              <p>
                Vision Focus only partners with Chinese factories that already possess valid SPPT-SNI certificates or facilitates comprehensive factory audit testing with accredited certification bodies (LSPro) prior to commercial shipment.
              </p>

              <h2>2. Slashing Import Duties with ACFTA Form E</h2>
              <p>
                Under the ASEAN-China Free Trade Agreement, qualifying building materials manufactured in China can enter Indonesia at <strong>0% preferential import duty</strong>, provided a valid Form E Certificate of Origin is issued by China Customs (GACC):
              </p>

              <div class="data-table-wrap">
                <table class="article-data-table">
                  <thead>
                    <tr>
                      <th>Material Item</th>
                      <th>Standard MFN Duty</th>
                      <th>With Form E (ACFTA)</th>
                      <th>Duty Savings</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Porcelain & Ceramic Slabs</td>
                      <td>10% - 15%</td>
                      <td><strong>0%</strong></td>
                      <td>Save 10% - 15%</td>
                    </tr>
                    <tr>
                      <td>PVD Stainless Steel Sheets</td>
                      <td>5% - 7.5%</td>
                      <td><strong>0%</strong></td>
                      <td>Save 5% - 7.5%</td>
                    </tr>
                    <tr>
                      <td>Commercial Sanitaryware</td>
                      <td>10%</td>
                      <td><strong>0%</strong></td>
                      <td>Save 10%</td>
                    </tr>
                    <tr>
                      <td>Display Shelving & Fixtures</td>
                      <td>10%</td>
                      <td><strong>0%</strong></td>
                      <td>Save 10%</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <h2>3. Port Handling & Avoiding Demurrage Fees</h2>
              <p>
                At container terminals such as Tanjung Priok (Jakarta) or Tanjung Perak (Surabaya), shipping lines permit 5 to 7 days of free container storage. Any paperwork discrepancies or delayed import duty payments trigger demurrage charges ranging from $80 to $180 per container per day.
              </p>
              <p>
                By pre-clearing drafts of commercial invoices, packing lists, bills of lading, and Form E before the vessel departs China, our customs brokerage team ensures goods are released within 24 to 48 hours of berthing.
              </p>
            </div>

            <div class="article-share-cta-bar">
              <div>
                <span style="font-size: 0.82rem; color: #64748b; font-weight: 600;">Need assistance with SNI verification or customs documentation?</span>
              </div>
              <div style="display: flex; gap: 10px;">
                <button type="button" class="btn btn-gold open-quote-modal">Consult Customs Desk →</button>
                <a href="https://wa.me/6281234567890?text=Halo%20Vision%20Focus%2C%20saya%20butuh%20info%20SNI%20dan%20Customs%20Clearance" target="_blank" rel="noopener noreferrer" class="btn-wa-solutions">
                  WhatsApp Support
                </a>
              </div>
            </div>
          </article>

          <aside class="article-sidebar-sticky">
            <div class="sidebar-widget">
              <h4 class="sidebar-widget-title">Customs Checklist</h4>
              <ul class="toc-list">
                <li><a href="#article-customs">1. Mandatory SNI Products</a></li>
                <li><a href="#article-customs">2. ACFTA Form E Benefits</a></li>
                <li><a href="#article-customs">3. Port Demurrage Prevention</a></li>
                <li><a href="#article-customs">4. Green Line Clearance</a></li>
              </ul>
            </div>

            <div class="sidebar-widget" style="background: var(--color-surface-soft);">
              <span style="color: var(--color-gold); font-size: 0.72rem; font-weight: 700;">REGULATORY GUIDE</span>
              <h5 style="color: var(--color-primary); font-size: 1rem; margin: 6px 0 10px;">The Indonesia SNI Handbook</h5>
              <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5; margin-bottom: 16px;">
                Download our 24-page guide detailing HS codes, mandatory test standards, and customs clearance procedures.
              </p>
              <button type="button" class="btn btn-outline-gold open-quote-modal" style="width: 100%;">Download Handbook →</button>
            </div>
          </aside>
        </div>
      </div>

      <!-- ==============================================================
           ARTICLE 4: LANDED COST FORMULA
           ============================================================== -->
      <div class="insight-article-panel" id="article-landed-cost">
        <div class="article-layout">
          <article class="article-content-card">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; flex-wrap: wrap;">
              <span class="section-tag" style="margin: 0;">FINANCIAL STRATEGY</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">September 28, 2026</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">5 min read</span>
            </div>

            <h1 style="font-family: var(--font-serif); font-size: 2.2rem; font-weight: 700; color: var(--color-primary); line-height: 1.3; margin-bottom: 20px;">
              The Complete Landed Cost Formula: How to Calculate Ex-Factory to Job Site Costs Without Surprises
            </h1>

            <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 28px;">
              <img src="assets/images/step-quote.jpg" alt="Cost Transparency and Sourcing" style="width: 100%; height: 420px; object-fit: cover;">
            </div>

            <p class="article-lead">
              A common trap for new importers is comparing Chinese factory quotes (FOB) directly against local Indonesian distributor prices without calculating the true landed cost. Understanding the 6 cost layers ensures complete financial transparency and predictable project ROI.
            </p>

            <div class="article-body-text">
              <h2>The 6 Pillars of Cross-Border Landed Cost</h2>
              <p>
                Landed cost is the total net expense of moving goods from factory floor in Guangdong to your construction job site in Indonesia:
              </p>
              <div class="pull-quote-box">
                Landed Cost = Ex-Factory FOB + Sea Freight + Marine Cargo Insurance + Port Clearance & Terminal Fees + Import Duties & PPh/PPN + Inland Flatbed Trucking
              </div>

              <h2>Real Project Case Study: 180-Key Luxury Resort in Bali</h2>
              <p>
                In a recent hospitality development in Nusa Dua, Bali, the developer required 28,000 sqm of large format porcelain slabs and 360 sets of custom PVD champagne sanitary suites:
              </p>
              <ul>
                <li><strong>Local Indonesian Middleman Quote:</strong> Rp 14.8 Billion (with a 90-day lead time and limited finish selections).</li>
                <li><strong>Vision Focus Direct Landed Cost:</strong> Rp 9.4 Billion (including all ocean freight, Form E zero duty, customs brokerage, and site trucking).</li>
                <li><strong>Net Developer Savings:</strong> <strong>Rp 5.4 Billion (36.5% Net Reduction)</strong> alongside fully customized bookmatched slab veining.</li>
              </ul>
            </div>

            <div class="article-share-cta-bar">
              <div>
                <span style="font-size: 0.82rem; color: #64748b; font-weight: 600;">Want an itemized landed cost calculation for your BOQ?</span>
              </div>
              <div style="display: flex; gap: 10px;">
                <button type="button" class="btn btn-gold open-quote-modal">Request Landed Cost Sheet →</button>
                <a href="https://wa.me/6281234567890?text=Halo%20Vision%20Focus%2C%20saya%20ingin%20hitung%20Landed%20Cost%20proyek" target="_blank" rel="noopener noreferrer" class="btn-wa-solutions">
                  WhatsApp Calculator
                </a>
              </div>
            </div>
          </article>

          <aside class="article-sidebar-sticky">
            <div class="sidebar-widget">
              <h4 class="sidebar-widget-title">Cost Elements</h4>
              <ul class="toc-list">
                <li><a href="#article-landed-cost">1. The 6 Cost Pillars</a></li>
                <li><a href="#article-landed-cost">2. Bali Luxury Resort Case</a></li>
                <li><a href="#article-landed-cost">3. Eliminating Middleman Fees</a></li>
              </ul>
            </div>

            <div class="sidebar-widget">
              <span class="section-tag">CALCULATOR</span>
              <h5 style="color: var(--color-primary); font-size: 1rem; margin: 8px 0 10px;">Landed Cost Breakdown</h5>
              <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5; margin-bottom: 16px;">
                Get a transparent breakdown with zero hidden fees before committing to procurement.
              </p>
              <button type="button" class="btn btn-gold open-quote-modal" style="width: 100%;">Get Landed Cost Quote →</button>
            </div>
          </aside>
        </div>
      </div>

      <!-- ==============================================================
           ARTICLE 5: RETAIL PLAYBOOK
           ============================================================== -->
      <div class="insight-article-panel" id="article-retail-playbook">
        <div class="article-layout">
          <article class="article-content-card">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; flex-wrap: wrap;">
              <span class="section-tag" style="margin: 0;">RETAIL SOURCING</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">September 20, 2026</span>
              <span style="font-size: 0.82rem; color: #94a3b8;">&bull;</span>
              <span style="font-size: 0.82rem; color: #64748b;">6 min read</span>
            </div>

            <h1 style="font-family: var(--font-serif); font-size: 2.2rem; font-weight: 700; color: var(--color-primary); line-height: 1.3; margin-bottom: 20px;">
              Retail Chain Sourcing Playbook: Standardizing Store Fixtures & Display Racking from China
            </h1>

            <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 28px;">
              <img src="assets/images/step-needs.jpg" alt="Retail Chain Sourcing" style="width: 100%; height: 420px; object-fit: cover;">
            </div>

            <p class="article-lead">
              For rapid supermarket, minimarket, and lifestyle retail chain rollouts across Indonesia, securing uniform visual identity, modular flexibility, and predictable fixture costs is critical. Here is how our centralized China sourcing program accelerates store opening schedules.
            </p>

            <div class="article-body-text">
              <h2>1. Modular Shelving Standardization</h2>
              <p>
                By engineering standardized powder-coated steel gondolas and uprights produced by specialized robotic stamping facilities in Guangdong, retail chains achieve 100% component interchangeability across flagship hypermarkets and suburban convenience branches.
              </p>

              <h2>2. Foshan Warehouse Multi-Vendor Consolidation</h2>
              <p>
                Rather than coordinating separate shipments from display shelving factories, lighting makers, and refrigeration suppliers, Vision Focus consolidates all items at our dedicated Foshan logistics hub. Containers are stuffed according to each new store opening sequence—allowing immediate store fitout upon container arrival.
              </p>
            </div>

            <div class="article-share-cta-bar">
              <div>
                <span style="font-size: 0.82rem; color: #64748b; font-weight: 600;">Planning a multi-store nationwide expansion?</span>
              </div>
              <div style="display: flex; gap: 10px;">
                <button type="button" class="btn btn-gold open-quote-modal">Consult Retail Sourcing →</button>
                <a href="https://wa.me/6281234567890?text=Halo%20Vision%20Focus%2C%20saya%20ingin%20tanya%20Retail%20Fixtures%20Sourcing" target="_blank" rel="noopener noreferrer" class="btn-wa-solutions">
                  WhatsApp Retail Desk
                </a>
              </div>
            </div>
          </article>

          <aside class="article-sidebar-sticky">
            <div class="sidebar-widget">
              <h4 class="sidebar-widget-title">Retail Playbook</h4>
              <ul class="toc-list">
                <li><a href="#article-retail-playbook">1. Modular Gondola Shelving</a></li>
                <li><a href="#article-retail-playbook">2. Hub Consolidation</a></li>
                <li><a href="#article-retail-playbook">3. Nationwide Rollout Buffer</a></li>
              </ul>
            </div>

            <div class="sidebar-widget" style="background: var(--color-surface-soft);">
              <span style="color: var(--color-gold); font-size: 0.72rem; font-weight: 700;">PLAYBOOK PDF</span>
              <h5 style="color: var(--color-primary); font-size: 1rem; margin: 6px 0 10px;">Retail Fitout Playbook</h5>
              <p style="font-size: 0.82rem; color: #64748b; line-height: 1.5; margin-bottom: 16px;">
                Download specifications, load testing ratings, and store opening schedule templates.
              </p>
              <button type="button" class="btn btn-outline-gold open-quote-modal" style="width: 100%;">Download Playbook →</button>
            </div>
          </aside>
        </div>
      </div>

    </div>
  </main>

  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const urlParams = new URLSearchParams(window.location.search);
      const requestedId = urlParams.get('id') || 'china-supply';

      const tabBtns = document.querySelectorAll('.insight-tab-btn');
      const panels = document.querySelectorAll('.insight-article-panel');
      const breadcrumb = document.getElementById('breadcrumbInsightCurrent');

      function showArticle(id) {{
        tabBtns.forEach(btn => {{
          btn.classList.toggle('active', btn.dataset.target === id);
        }});
        panels.forEach(p => {{
          p.classList.toggle('active', p.id === 'article-' + id);
        }});

        if (breadcrumb) {{
          const activeBtn = document.querySelector(`.insight-tab-btn[data-target="${{id}}"]`);
          if (activeBtn) breadcrumb.textContent = activeBtn.querySelector('span:first-child').textContent;
        }}
      }}

      tabBtns.forEach(btn => {{
        btn.addEventListener('click', () => {{
          const target = btn.dataset.target;
          showArticle(target);
          history.replaceState(null, '', '?id=' + target);
        }});
      }});

      // Initial show from URL param
      showArticle(requestedId);
    }});
  </script>
{footer_clean}
"""

with open("/Users/mekari/Documents/Visifokus/insight-detail.html", "w") as f:
    f.write(insight_detail_html)
print("Created insight-detail.html successfully.")

