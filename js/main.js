/**
 * VISION FOCUS TRADE LINE
 * Main Javascript Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. STICKY / SCROLLED HEADER
  const siteHeader = document.querySelector('.site-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      siteHeader?.classList.add('scrolled');
    } else {
      siteHeader?.classList.remove('scrolled');
    }
  });

  // 2. MEGA MENU CONTROLLER
  const megaOverlay = document.getElementById('megaMenuOverlay');
  const megaItems = document.querySelectorAll('.has-mega-menu');
  const allNavLinks = document.querySelectorAll('.desktop-nav .nav-link-item');
  const simpleDropdowns = document.querySelectorAll('.has-dropdown');
  const siteHeaderEl = document.querySelector('.site-header');

  function closeAllMegaMenus() {
    megaItems.forEach(item => {
      item.classList.remove('menu-open');
    });
    simpleDropdowns.forEach(item => {
      item.classList.remove('menu-open');
    });
    megaOverlay?.classList.remove('active');
  }

  // On clicking any nav link, navigate directly to page and close mega menus
  allNavLinks.forEach(link => {
    link.addEventListener('click', () => {
      closeAllMegaMenus();
      // Allow default link navigation to link.href
    });
  });

  // Simple Dropdown (About Us, Service, Event) hover & click handling
  simpleDropdowns.forEach(dropdown => {
    const trigger = dropdown.querySelector('.nav-link-item');
    dropdown.addEventListener('mouseenter', () => {
      simpleDropdowns.forEach(d => { if (d !== dropdown) d.classList.remove('menu-open'); });
      dropdown.classList.add('menu-open');
    });

    dropdown.addEventListener('mouseleave', () => {
      dropdown.classList.remove('menu-open');
    });

    trigger?.addEventListener('click', (e) => {
      if (window.innerWidth <= 1024) {
        e.preventDefault();
        dropdown.classList.toggle('menu-open');
      }
    });
  });

  // Hover handling with smooth timeout for fluid cursor movement
  let megaHoverTimeout = null;

  megaItems.forEach(item => {
    item.addEventListener('mouseenter', () => {
      if (megaHoverTimeout) clearTimeout(megaHoverTimeout);
      
      // Close simple dropdowns immediately
      simpleDropdowns.forEach(d => d.classList.remove('menu-open'));

      // Close other mega menus immediately
      megaItems.forEach(other => {
        if (other !== item) other.classList.remove('menu-open');
      });
      
      item.classList.add('menu-open');
      megaOverlay?.classList.add('active');
    });

    item.addEventListener('mouseleave', () => {
      if (megaHoverTimeout) clearTimeout(megaHoverTimeout);
      megaHoverTimeout = setTimeout(() => {
        item.classList.remove('menu-open');
        const anyStillOpen = Array.from(megaItems).some(i => i.classList.contains('menu-open'));
        if (!anyStillOpen) {
          megaOverlay?.classList.remove('active');
        }
      }, 150);
    });
  });

  // Clicking outside header closes all menus
  document.addEventListener('click', (e) => {
    if (!siteHeaderEl?.contains(e.target)) {
      closeAllMegaMenus();
    }
  });

  // Close mega menu on overlay click
  megaOverlay?.addEventListener('click', closeAllMegaMenus);

  // 3. MOBILE DRAWER NAVIGATION
  const mobileToggle = document.getElementById('mobileMenuToggle');
  const mobileDrawer = document.getElementById('mobileNavDrawer');
  const mobileClose = document.getElementById('mobileCloseBtn');

  mobileToggle?.addEventListener('click', () => {
    mobileDrawer?.classList.add('open');
    document.body.style.overflow = 'hidden';
  });

  mobileClose?.addEventListener('click', () => {
    mobileDrawer?.classList.remove('open');
    document.body.style.overflow = '';
  });

  // Mobile Accordion Items
  const accordionTriggers = document.querySelectorAll('.mobile-accordion-trigger');
  accordionTriggers.forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      const content = trigger.nextElementSibling;
      const isOpen = content?.classList.contains('open');
      
      // Close other accordions
      document.querySelectorAll('.mobile-accordion-content').forEach(c => c.classList.remove('open'));
      document.querySelectorAll('.mobile-accordion-trigger').forEach(t => t.classList.remove('active'));

      if (!isOpen && content) {
        content.classList.add('open');
        trigger.classList.add('active');
      }
    });
  });

  // 4. FLOATING WHATSAPP POPUP
  const waTrigger = document.getElementById('waTriggerBtn');
  const waCard = document.getElementById('waPopupCard');
  const waClose = document.getElementById('waCloseBtn');

  waTrigger?.addEventListener('click', (e) => {
    e.stopPropagation();
    waCard?.classList.toggle('open');
  });

  waClose?.addEventListener('click', (e) => {
    e.stopPropagation();
    waCard?.classList.remove('open');
  });

  document.addEventListener('click', (e) => {
    if (!waCard?.contains(e.target) && !waTrigger?.contains(e.target)) {
      waCard?.classList.remove('open');
    }
  });

  // Department Choice direct WhatsApp redirect
  const waChoices = document.querySelectorAll('.wa-choice-btn');
  waChoices.forEach(btn => {
    btn.addEventListener('click', () => {
      const dept = btn.getAttribute('data-dept') || 'General';
      const text = encodeURIComponent(`Halo Vision Focus, saya tertarik berkonsultasi mengenai kebutuhan: ${dept}. Mohon informasi lebih lanjut.`);
      const phone = '628113188878'; // official WhatsApp
      window.open(`https://wa.me/${phone}?text=${text}`, '_blank');
    });
  });

  // 5. GET A QUOTE MODAL
  const quoteModal = document.getElementById('quoteModal');
  const openQuoteBtns = document.querySelectorAll('.open-quote-modal');
  const closeQuoteBtn = document.getElementById('closeQuoteBtn');

  openQuoteBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      quoteModal?.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  });

  closeQuoteBtn?.addEventListener('click', () => {
    quoteModal?.classList.remove('open');
    document.body.style.overflow = '';
  });

  quoteModal?.addEventListener('click', (e) => {
    if (e.target === quoteModal) {
      quoteModal.classList.remove('open');
      document.body.style.overflow = '';
    }
  });

  const quoteForm = document.getElementById('quoteForm');
  quoteForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('quoteName')?.value || 'Client';
    const email = document.getElementById('quoteEmail')?.value;
    const project = document.getElementById('quoteType')?.value;
    
    alert(`Thank you ${name}! Your quotation inquiry for ${project} has been submitted. Our procurement team will contact you within 24 business hours.`);
    quoteModal?.classList.remove('open');
    document.body.style.overflow = '';
    quoteForm.reset();
  });

  // 6. QUICK SEARCH MODAL
  const searchModal = document.getElementById('searchModal');
  const openSearchBtn = document.getElementById('openSearchBtn');
  const closeSearchBtn = document.getElementById('closeSearchBtn');
  const searchInput = document.getElementById('globalSearchInput');
  const searchResultsContainer = document.getElementById('searchResultsContainer');

  openSearchBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    searchModal?.classList.add('open');
    searchInput?.focus();
    document.body.style.overflow = 'hidden';
  });

  closeSearchBtn?.addEventListener('click', () => {
    searchModal?.classList.remove('open');
    document.body.style.overflow = '';
  });

  searchModal?.addEventListener('click', (e) => {
    if (e.target === searchModal) {
      searchModal.classList.remove('open');
      document.body.style.overflow = '';
    }
  });

  // Search items index
  const searchableItems = [
    { title: 'Supermarket & Retail Chains Sourcing', category: 'Solutions', link: '#solutions' },
    { title: 'Manufacturing Raw Materials & Machinery', category: 'Solutions', link: '#solutions' },
    { title: 'Developer & Project Procurement', category: 'Solutions', link: '#solutions' },
    { title: 'Architects & Interior Designers Support', category: 'Solutions', link: '#solutions' },
    { title: 'Granite Tiles & Large Slabs', category: 'Product Library', link: '#product-library' },
    { title: 'Architectural Stainless Steel Panels', category: 'Product Library', link: '#product-library' },
    { title: 'Designer Mosaics & Terrazzo', category: 'Product Library', link: '#product-library' },
    { title: 'Commercial Buildings Project Reference', category: 'Projects', link: '#projects' },
    { title: 'Hospitality & Luxury Hotel Sourcing', category: 'Projects', link: '#projects' },
    { title: 'China Supply Chain Update 2026', category: 'Insights', link: '#insights' },
    { title: 'How to Source from China Direct Guide', category: 'Insights', link: '#insights' },
    { title: 'Founder & CEO Mr. Jason Shi Story', category: 'About Us', link: '#about' },
    { title: 'Surabaya, Jakarta & Foshan Offices', category: 'Contact', link: '#contact' },
  ];

  searchInput?.addEventListener('input', (e) => {
    const val = e.target.value.toLowerCase().trim();
    if (!val) {
      searchResultsContainer.innerHTML = '<p class="search-empty-text">Type keywords to search solutions, products, projects, or insights...</p>';
      return;
    }
    const filtered = searchableItems.filter(item => 
      item.title.toLowerCase().includes(val) || item.category.toLowerCase().includes(val)
    );

    if (filtered.length === 0) {
      searchResultsContainer.innerHTML = `<p class="search-empty-text">No results found for "${val}". Please try another keyword.</p>`;
      return;
    }

    searchResultsContainer.innerHTML = filtered.map(item => `
      <a href="${item.link}" class="search-result-row" onclick="document.getElementById('searchModal').classList.remove('open'); document.body.style.overflow='';">
        <div>
          <span class="search-res-title">${item.title}</span>
          <span class="search-res-cat">${item.category}</span>
        </div>
        <span class="search-res-arrow">→</span>
      </a>
    `).join('');
  });

  // 7. OFFICE TABS SWITCHER
  const officeTabs = document.querySelectorAll('.office-tab-btn');
  const officePanes = document.querySelectorAll('.office-pane-content');

  officeTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.getAttribute('data-target');
      officeTabs.forEach(t => t.classList.remove('active'));
      officePanes.forEach(p => p.classList.remove('active'));

      tab.classList.add('active');
      const pane = document.getElementById(target);
      if (pane) pane.classList.add('active');
    });
  });

  // 8. CATEGORY & PROJECT FILTER TABS
  const filterBars = document.querySelectorAll('.filter-pill-bar, .projects-filter-bar');
  if (filterBars.length > 0) {
    filterBars.forEach(bar => {
      const parentSection = bar.closest('section') || bar.closest('main') || document;
      const cards = parentSection.querySelectorAll('.project-item-card, .insight-item-card, .service-clean-card[data-category]');
      const btns = bar.querySelectorAll('.filter-pill-btn');

      btns.forEach(btn => {
        btn.addEventListener('click', () => {
          btns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');

          const filter = btn.getAttribute('data-filter');
          cards.forEach(card => {
            if (filter === 'all' || card.getAttribute('data-category') === filter) {
              card.style.display = 'flex';
            } else {
              card.style.display = 'none';
            }
          });
        });
      });
    });
  } else {
    const filterBtns = document.querySelectorAll('.filter-pill-btn');
    const projectCards = document.querySelectorAll('.project-item-card, .insight-item-card, .service-clean-card[data-category]');
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filter = btn.getAttribute('data-filter');
        projectCards.forEach(card => {
          if (filter === 'all' || card.getAttribute('data-category') === filter) {
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // 9. GOOGLE TRANSLATE WEBSITE INTEGRATION (SINGLE WIDGET SYNC)
  document.addEventListener('change', function(e) {
    if (e.target && e.target.classList.contains('goog-te-combo')) {
      const selected = e.target.value || 'en';
      const host = window.location.hostname;
      const cookieVal = (selected === 'en') ? '/en/en' : ('/en/' + selected);
      document.cookie = 'googtrans=' + cookieVal + '; path=/;';
      if (host) {
        document.cookie = 'googtrans=' + cookieVal + '; path=/; domain=' + host + ';';
        document.cookie = 'googtrans=' + cookieVal + '; path=/; domain=.' + host + ';';
      }
    }
  });

  // 10. HERO CAROUSEL CONTROLLER (HOMEPAGE 3 SLIDES)
  const heroSlides = document.querySelectorAll('.hero-slide');
  const heroDots = document.querySelectorAll('.hero-dot');
  const prevBtn = document.querySelector('.hero-prev-btn');
  const nextBtn = document.querySelector('.hero-next-btn');

  if (heroSlides.length > 1) {
    let currentSlide = 0;
    let slideTimer = null;

    function activateSlide(index) {
      heroSlides.forEach((slide, i) => {
        slide.classList.toggle('active', i === index);
      });
      heroDots.forEach((dot, i) => {
        dot.classList.toggle('active', i === index);
      });
      currentSlide = index;
    }

    function advanceSlide() {
      const nextIndex = (currentSlide + 1) % heroSlides.length;
      activateSlide(nextIndex);
    }

    function retreatSlide() {
      const prevIndex = (currentSlide - 1 + heroSlides.length) % heroSlides.length;
      activateSlide(prevIndex);
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        advanceSlide();
        restartSlideTimer();
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        retreatSlide();
        restartSlideTimer();
      });
    }

    heroDots.forEach((dot, i) => {
      dot.addEventListener('click', () => {
        activateSlide(i);
        restartSlideTimer();
      });
    });

    function restartSlideTimer() {
      if (slideTimer) clearInterval(slideTimer);
      slideTimer = setInterval(advanceSlide, 6500);
    }

    restartSlideTimer();
  }

  // 11. ACTIVE NAVIGATION LINK INDICATOR CONTROLLER
  // 9. LIGHTBOX MODAL CONTROLLER
  const lightboxModal = document.getElementById('imageLightboxModal');
  const lightboxImg = document.getElementById('lightboxActiveImg');
  const lightboxCaption = document.getElementById('lightboxCaptionText');
  const lightboxCloseBtn = document.getElementById('lightboxCloseBtn');

  function openLightbox(src, caption) {
    if (!lightboxModal || !lightboxImg) return;
    lightboxImg.src = src;
    if (lightboxCaption) {
      lightboxCaption.textContent = caption || '';
      lightboxCaption.style.display = caption ? 'block' : 'none';
    }
    lightboxModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    if (!lightboxModal) return;
    lightboxModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('.event-photo-tile, .photo-item').forEach(item => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      const caption = item.querySelector('.event-photo-caption, .photo-caption')?.innerText.trim() || img?.getAttribute('alt') || '';
      if (img?.src) {
        openLightbox(img.src, caption);
      }
    });
  });

  lightboxCloseBtn?.addEventListener('click', closeLightbox);
  lightboxModal?.addEventListener('click', (e) => {
    if (e.target === lightboxModal) closeLightbox();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightboxModal?.classList.contains('active')) {
      closeLightbox();
    }
  });

  // 10. MULTI-LANGUAGE TRANSLATOR (Default: English, also supports Indonesian & Chinese)
  // 10. MULTI-LANGUAGE TRANSLATOR (Full Sitewide Support: EN, ID, ZH)
  const translations = {
    en: {
      nav_home: 'HOME',
      nav_about: 'ABOUT US',
      nav_service: 'SERVICE',
      nav_projects: 'PROJECT REFERENCE',
      nav_events: 'EVENT',
      nav_insights: 'INSIGHTS',
      nav_contact: 'CONTACT',
      hero_eyebrow: 'YOUR GLOBAL TRADE PARTNER',
      hero_title_1: 'Connecting Businesses.',
      hero_title_2: 'Delivering Solutions.',
      hero_desc: 'Direct sourcing and trade solutions connecting China with global markets.',
      hero_btn_learn: 'LEARN MORE',
      about_title: 'ABOUT US',
      about_headline: 'A Trusted Bridge Between Two Nations',
      about_desc: 'Founded in 2016 with offices in Surabaya, Jakarta, and Foshan, connecting developers and architects directly with verified factories.',
      why_title: 'WHY CHOOSE US',
      brands_title: 'BRAND COLLABORATIONS',
      service_title: 'OUR SERVICES',
      service_sub: 'Direct Bridge Between Indonesia & China',
      service_indo_title: 'THE GATE TO INDONESIA',
      service_indo_target: 'FOR CHINA SUPPLIERS',
      service_indo_desc: 'Market entry, licensing, and direct access to Indonesian projects.',
      service_china_title: 'THE GATE TO CHINA',
      service_china_target: 'FOR INDONESIAN CLIENTS',
      service_china_desc: 'Direct factory sourcing, QC audits, and consolidated logistics from Foshan.',
      gzdw_title: 'STRATEGIC PARTNER OF GUANGZHOU DESIGN WEEK IN INDONESIA',
      gzdw_desc: 'Official registered partner of Guangzhou Design Week, bridging China and Indonesia across exhibitions and architectural innovations.',
      gzdw_about_title: 'ABOUT GUANGZHOU DESIGN WEEK (GZDW)',
      gzdw_about_desc: 'Asia\'s premier architectural and design event, linking international designers with tier-1 manufacturers.',
      offer_title: 'WHAT WE OFFER',
      offer_c1_title: 'REPRESENTATIVE OFFICE',
      offer_c2_title: 'IMPORT & SERVICE',
      offer_c3_title: 'SUPPORTING ORDER',
      events_title: 'EVENTS & COLLABORATIONS',
      events_sub: 'IndoBuildTech 2025 & Strategic Partnership with Guangzhou Design Week',
      footer_company: 'PT VISI FOKUS SINDOTAMA PERKASA',
      footer_china: 'China Partner',
      footer_surabaya: 'Surabaya Office',
      footer_jakarta: 'Jakarta Office'
    },
    id: {
      nav_home: 'BERANDA',
      nav_about: 'TENTANG KAMI',
      nav_service: 'LAYANAN',
      nav_projects: 'REFERENSI PROYEK',
      nav_events: 'KEGIATAN',
      nav_insights: 'WAWASAN',
      nav_contact: 'KONTAK',
      hero_eyebrow: 'MITRA PERDAGANGAN GLOBAL ANDA',
      hero_title_1: 'Menghubungkan Bisnis.',
      hero_title_2: 'Menghadirkan Solusi.',
      hero_desc: 'Solusi pengadaan langsung dan perdagangan dari China ke pasar global.',
      hero_btn_learn: 'PELAJARI LEBIH LANJUT',
      about_title: 'TENTANG KAMI',
      about_headline: 'Jembatan Terpercaya Antara Dua Negara',
      about_desc: 'Didirikan tahun 2016 dengan basis di Surabaya, Jakarta, dan Foshan, menghubungkan arsitek dan pengembang langsung ke pabrik terverifikasi.',
      why_title: 'MENGAPA MEMILIH KAMI',
      brands_title: 'KOLABORASI MEREK',
      service_title: 'LAYANAN KAMI',
      service_sub: 'Jembatan Langsung Antara Indonesia & China',
      service_indo_title: 'GERBANG MENUJU INDONESIA',
      service_indo_target: 'UNTUK PEMASOK CHINA',
      service_indo_desc: 'Masuk pasar, perizinan, dan akses langsung ke proyek Indonesia.',
      service_china_title: 'GERBANG MENUJU CHINA',
      service_china_target: 'UNTUK KLIEN INDONESIA',
      service_china_desc: 'Pengadaan langsung pabrik, inspeksi QC, dan logistik dari Foshan.',
      gzdw_title: 'MITRA STRATEGIS GUANGZHOU DESIGN WEEK DI INDONESIA',
      gzdw_desc: 'Mitra resmi Guangzhou Design Week di Indonesia, menghubungkan produsen China langsung dengan kebutuhan proyek Indonesia.',
      gzdw_about_title: 'TENTANG GUANGZHOU DESIGN WEEK (GZDW)',
      gzdw_about_desc: 'Pameran arsitektur dan desain terkemuka di Asia, menghubungkan desainer global dengan pabrik manufaktur tier-1.',
      offer_title: 'LAYANAN UTAMA KAMI',
      offer_c1_title: 'KANTOR PERWAKILAN',
      offer_c2_title: 'IMPOR & LAYANAN',
      offer_c3_title: 'DUKUNGAN PROYEK',
      events_title: 'KEGIATAN & KOLABORASI',
      events_sub: 'IndoBuildTech 2025 & Kemitraan Strategis Guangzhou Design Week',
      footer_company: 'PT VISI FOKUS SINDOTAMA PERKASA',
      footer_china: 'Mitra China',
      footer_surabaya: 'Kantor Surabaya',
      footer_jakarta: 'Kantor Jakarta'
    },
    zh: {
      nav_home: '首页',
      nav_about: '关于我们',
      nav_service: '业务服务',
      nav_projects: '项目案例',
      nav_events: '展会活动',
      nav_insights: '行业洞察',
      nav_contact: '联系我们',
      hero_eyebrow: '您值得信赖的全球贸易伙伴',
      hero_title_1: '直连源头商业，',
      hero_title_2: '交付全流程解决方案。',
      hero_desc: '链接中国实力制造与全球市场的源头直采与贸易方案。',
      hero_btn_learn: '探索更多',
      about_title: '关于我们',
      about_headline: '两国之间值得信赖的商贸桥梁',
      about_desc: '创立于2016年，在泗水、雅加达与佛山设立办事处，直连印尼工程与源头实力工厂。',
      why_title: '为什么选择我们',
      brands_title: '战略合作品牌',
      service_title: '核心业务',
      service_sub: '印尼与中国之间的双向直采桥梁',
      service_indo_title: '通往印尼的大门',
      service_indo_target: '专为中国供应商打造',
      service_indo_desc: '开拓印尼市场、合规资质及对接本地大型工程项目。',
      service_china_title: '通往中国的大门',
      service_china_target: '专为印尼客户提供',
      service_china_desc: '佛山源头实力工厂直采、全流程质检与集运物流服务。',
      gzdw_title: '广州设计周（GZDW）印尼官方战略合作伙伴',
      gzdw_desc: '作为广州设计周在印尼的官方授权战略合作伙伴，建立中印尼设计展会与建筑创新交流桥梁。',
      gzdw_about_title: '关于广州设计周 (GZDW)',
      gzdw_about_desc: '深耕18年的亚洲知名设计盛会，联动全球设计师与高端制造品牌。',
      offer_title: '核心服务板块',
      offer_c1_title: '印尼代表处服务',
      offer_c2_title: '进出口清关服务',
      offer_c3_title: '大型工程订单配套',
      events_title: '展会活动与实况',
      events_sub: '2025 IndoBuildTech 展位及广州设计周战略合作',
      footer_company: 'PT VISI FOKUS SINDOTAMA PERKASA',
      footer_china: '中国常驻办事处',
      footer_surabaya: '泗水办事处（总部）',
      footer_jakarta: '雅加达代表处'
    }
  };

  // Comprehensive phrase dictionary for sitewide subpages content translation
  const phraseDictionary = {
    // Nav items & dropdowns
    'Home': { id: 'Beranda', zh: '首页' },
    'HOME': { id: 'BERANDA', zh: '首页' },
    'About Us': { id: 'Tentang Kami', zh: '关于我们' },
    'ABOUT US': { id: 'TENTANG KAMI', zh: '关于我们' },
    'About Vision Focus': { id: 'Tentang Vision Focus', zh: '关于 Vision Focus' },
    'Why Choose Us': { id: 'Mengapa Memilih Kami', zh: '为什么选择我们' },
    'Why Vision Focus': { id: 'Mengapa Vision Focus', zh: '为什么选择 Vision Focus' },
    'How We Work': { id: 'Cara Kerja Kami', zh: '合作流程' },
    'Service': { id: 'Layanan', zh: '业务服务' },
    'SERVICE': { id: 'LAYANAN', zh: '业务服务' },
    'The Gate to China': { id: 'Gerbang Menuju China', zh: '通往中国的大门' },
    'THE GATE TO CHINA': { id: 'GERBANG MENUJU CHINA', zh: '通往中国的大门' },
    'The Gate to Indonesia': { id: 'Gerbang Menuju Indonesia', zh: '通往印尼的大门' },
    'THE GATE TO INDONESIA': { id: 'GERBANG MENUJU INDONESIA', zh: '通往印尼的大门' },
    'All Supply Chain Services': { id: 'Semua Layanan Rantai Pasok', zh: '全流程供应链服务' },
    'Our Services & Solutions': { id: 'Layanan & Solusi Kami', zh: '核心业务与全流程解决方案' },
    'Project Reference': { id: 'Referensi Proyek', zh: '项目案例参考' },
    'PROJECT REFERENCE': { id: 'REFERENSI PROYEK', zh: '项目案例参考' },
    'Selected Project Details': { id: 'Detail Proyek Terpilih', zh: '精选工程项目详情' },
    'Event': { id: 'Kegiatan', zh: '展会活动' },
    'EVENT': { id: 'KEGIATAN', zh: '展会活动' },
    'Events': { id: 'Kegiatan', zh: '展会活动' },
    'Events & Exhibitions': { id: 'Kegiatan & Pameran', zh: '展会与交流活动' },
    'All Events & Exhibitions': { id: 'Semua Kegiatan & Pameran', zh: '全部展会与交流活动' },
    'Exhibitions': { id: 'Pameran', zh: '专业展会' },
    'VIP Delegations': { id: 'Delegasi VIP', zh: 'VIP 考察团' },
    'Trade Summits': { id: 'KTT Perdagangan', zh: '商贸峰会' },
    'Event & Exhibition Coverage': { id: 'Liputan Pameran & Kegiatan', zh: '展会实况与现场回顾' },
    'IndoBuildTech 2025': { id: 'IndoBuildTech 2025', zh: 'IndoBuildTech 2025 展会' },
    'Guangzhou Design Week (GZDW 2024)': { id: 'Guangzhou Design Week (GZDW 2024)', zh: '广州设计周 (GZDW 2024)' },
    'Guangzhou Design Week 2024': { id: 'Guangzhou Design Week 2024', zh: '2024 广州设计周' },
    '137th Canton Fair & Summit': { id: '137th Canton Fair & KTT', zh: '第137届广交会与商贸峰会' },
    'All Exhibitions': { id: 'Semua Pameran', zh: '全部展会' },
    'All Exhibitions & GZDW': { id: 'Semua Pameran & GZDW', zh: '全部展会与广州设计周' },
    'EVENT RECAP': { id: 'KILAS BALIK ACARA', zh: '展会活动回顾' },
    'Contact': { id: 'Kontak', zh: '联系我们' },
    'CONTACT': { id: 'KONTAK', zh: '联系我们' },
    'Contact Us': { id: 'Hubungi Kami', zh: '联系我们' },
    'Showroom': { id: 'Showroom', zh: '展厅中心' },
    'Showrooms': { id: 'Showroom', zh: '展厅中心' },
    'Showroom & Material Hubs': { id: 'Showroom & Pusat Material', zh: '展厅与材料选品中心' },
    'Insights': { id: 'Wawasan', zh: '行业洞察' },
    'INSIGHTS': { id: 'WAWASAN', zh: '行业洞察' },
    'Insights & Guides': { id: 'Wawasan & Panduan', zh: '采购洞察与战略指南' },
    'Sourcing Insights & Strategic Guides': { id: 'Wawasan & Panduan Pengadaan Strategis', zh: '源头直采洞察与战略指南' },
    'Technical Material Library': { id: 'Pustaka Material Teknis', zh: '工程材料技术选品库' },

    // Page Hero Eyebrows
    'PROCESS': { id: 'METODOLOGI', zh: '合作流程' },
    'ADVANTAGES': { id: 'KEUNGGULAN', zh: '核心优势' },
    'SERVICES': { id: 'LAYANAN', zh: '业务服务' },
    'PORTFOLIO': { id: 'PORTOFOLIO', zh: '项目案例' },
    'EXHIBITION': { id: 'PAMERAN', zh: '现场展会' },
    'GLOBAL INDUSTRY PRESENCE': { id: 'KEHADIRAN INDUSTRI GLOBAL', zh: '全球展会与行业盛会' },
    'GALLERY': { id: 'GALERI', zh: '展厅中心' },
    'GUIDE': { id: 'PANDUAN', zh: '实战指南' },
    'MATERIALS': { id: 'MATERIAL', zh: '材料中心' },
    'CASE STUDY': { id: 'STUDI KASUS', zh: '案例分析' },

    // Common Buttons & Actions
    'LEARN MORE': { id: 'PELAJARI LEBIH LANJUT', zh: '了解更多' },
    'EXPLORE ALL SERVICES': { id: 'JELAJAHI SEMUA LAYANAN', zh: '查看全部服务' },
    'EXPLORE ALL PROJECTS': { id: 'LIHAT SEMUA PROYEK', zh: '查看全部案例' },
    'REGISTER FOR NEXT EXPO VIP PASS': { id: 'DAFTAR TIKET VIP EXPO BERIKUTNYA', zh: '注册下届展会 VIP 通行证' },
    'INQUIRE GZDW DELEGATION SCHEDULE': { id: 'INFO JADWAL DELEGASI GZDW', zh: '咨询广州设计周考察团行程' },
    'CHAT DIRECTLY ON WHATSAPP (+62 811-3188-878)': { id: 'HUBUNGI LANGSUNG VIA WHATSAPP (+62 811-3188-878)', zh: '直接通过 WhatsApp 沟通 (+62 811-3188-878)' },
    'Chat on WhatsApp': { id: 'Chat di WhatsApp', zh: '通过 WhatsApp 咨询' },
    'CHAT ON WHATSAPP': { id: 'CHAT DI WHATSAPP', zh: 'WHATSAPP 在线沟通' },
    'SEND INQUIRY VIA WHATSAPP': { id: 'KIRIM PERTANYAAN VIA WHATSAPP', zh: '通过 WhatsApp 提交需求' },
    'REQUEST SOURCING CONSULTATION': { id: 'MINTA KONSULTASI PENGADAAN', zh: '预约源头直采咨询' },
    'GET A QUOTE': { id: 'MINTA PENAWARAN', zh: '获取方案报价' },
    'SUBMIT INQUIRY': { id: 'KIRIM PERMINTAAN', zh: '立即提交咨询' },
    'BOOK PRIVATE VISIT': { id: 'JADWALKAN KUNJUNGAN PRIBADI', zh: '预约专属展厅品鉴' },
    'INQUIRE RETAIL SYSTEMS': { id: 'KONSULTASI SISTEM RITEL', zh: '商超系统采购咨询' },
    'INQUIRE HOSPITALITY SOURCING': { id: 'KONSULTASI PENGADAAN HOTEL', zh: '酒店工程选品咨询' },
    'INQUIRE COMMERCIAL SOURCING': { id: 'KONSULTASI PENGADAAN KOMERSIAL', zh: '商业地产直采咨询' },
    'INQUIRE RESIDENTIAL SOURCING': { id: 'KONSULTASI PENGADAAN RESIDENSIAL', zh: '高端豪宅直采咨询' },

    // Section Eyebrows & Titles
    '01 / ABOUT US': { id: '01 / TENTANG KAMI', zh: '01 / 关于我们' },
    '01 / OUR FOUNDATION': { id: '01 / PONDASI KAMI', zh: '01 / 发展基石' },
    '01 / THE VISION FOCUS ADVANTAGE': { id: '01 / KEUNGGULAN VISION FOCUS', zh: '01 / 我们的核心优势' },
    '01 / PROCUREMENT METHODOLOGY': { id: '01 / METODOLOGI PENGADAAN', zh: '01 / 采购执行方法论' },
    '01 / FLAGSHIP EXHIBITION RECAP': { id: '01 / REKAP PAMERAN UTAMA', zh: '01 / 旗舰展会现场实况' },
    '01 / SELECTED PORTFOLIO': { id: '01 / PORTOFOLIO TERPILIH', zh: '01 / 精选工程项目案例' },
    '01 / PHYSICAL PRESENCE': { id: '01 / KEHADIRAN FISIK', zh: '01 / 实体办公地点' },
    '01 / PHYSICAL LOCATIONS': { id: '01 / LOKASI FISIK', zh: '01 / 实体展厅分布' },

    '02 / WHY CHOOSE US': { id: '02 / MENGAPA MEMILIH KAMI', zh: '02 / 为什么选择我们' },
    '02 / THE VISION FOCUS ADVANTAGE': { id: '02 / KEUNGGULAN VISION FOCUS', zh: '02 / 核心优势' },
    '02 / FULL PHOTO MOSAIC': { id: '02 / MOSAIK FOTO LENGKAP', zh: '02 / 现场全景精彩图集' },
    '02 / SEND US AN INQUIRY': { id: '02 / KIRIM PERTANYAAN KEPADA KAMI', zh: '02 / 在线提交采购需求' },
    '02 / QUICK TOPIC INQUIRY': { id: '02 / PILIHAN TOPIK CEPAT', zh: '02 / 快捷咨询类别' },

    '03 / OUR SERVICES': { id: '03 / LAYANAN KAMI', zh: '03 / 核心业务' },
    '03 / PHYSICAL NETWORK': { id: '03 / JARINGAN FISIK', zh: '03 / 实体常驻网络' },
    '03 / ANNUAL CHINA TOUR': { id: '03 / TUR TAHUNAN CHINA', zh: '03 / 年度中国商务考察' },
    '04 / PROJECT REFERENCE': { id: '04 / REFERENSI PROYEK', zh: '04 / 工程案例参考' },
    '05 / EXHIBITIONS & COLLABORATIONS': { id: '05 / PAMERAN & KOLABORASI', zh: '05 / 展会活动与战略合作' },

    // Page Headlines
    'A Trusted Bridge Between Two Nations': { id: 'Jembatan Terpercaya Antara Dua Negara', zh: '中印尼之间值得信赖的经贸桥梁' },
    'Tri-City Infrastructure': { id: 'Infrastruktur di Tiga Kota', zh: '三城一体常驻实体网络' },
    'Permanent operational presence ensuring accountability at every stage.': { id: 'Kehadiran operasional permanen yang menjamin akuntabilitas di setiap tahapan.', zh: '全资常驻实体，确保采购履约每一步都有迹可循。' },
    'Eliminating Cross-Border Friction': { id: 'Menghilangkan Hambatan Lintas Batas', zh: '杜绝跨境采购痛点与风险' },
    'Traditional sourcing from China often carries risks of inconsistent quality, language barriers, and inflated broker fees. We offer a secure, transparent, and direct bridge.': { id: 'Pengadaan tradisional dari China kerap berisiko kualitas tidak konsisten, hambatan bahasa, dan biaya perantara tinggi. Kami hadirkan jembatan aman, transparan, dan langsung.', zh: '传统跨境采购常面临品质不稳定、语言沟通障碍及高额中间商差价。我们为您构建安全、透明、直连的一站式直采桥梁。' },
    'A Clear Process from Start to Success': { id: 'Proses Jelas dari Awal Hingga Sukses', zh: '从需求沟通到落地交付的标准流程' },
    'Our 5-stage procurement framework guarantees transparency, uncompromised quality, and punctuality at every milestone.': { id: 'Kerangka kerja 5 tahap kami menjamin transparansi, kualitas tanpa kompromi, dan ketepatan waktu di setiap tonggak pencapaian.', zh: '五阶段严谨执行流程，确保全流程透明可溯、品质卓越把控与准时高效交付。' },
    'Verified Procurement Track Record': { id: 'Rekam Jejak Pengadaan Terverifikasi', zh: '真实可查的工程直采落地业绩' },
    'Delivering high-specification building materials, interior finishes, and retail systems for prestigious landmarks nationwide.': { id: 'Memasok material bangunan berspesifikasi tinggi, interior, dan sistem ritel untuk proyek bergengsi di seluruh Indonesia.', zh: '为全印尼众多高端地标项目提供高品质建筑材料、室内精品饰面及商超零售系统。' },
    'IndoBuildTech 2025 Photo Gallery': { id: 'Galeri Foto IndoBuildTech 2025', zh: 'IndoBuildTech 2025 展会精彩图集' },
    'Click on any photo to view in high resolution with client and partner details.': { id: 'Klik pada foto mana saja untuk melihat resolusi tinggi dengan detail klien dan mitra.', zh: '点击任意照片可查看高清大图及客户与合作伙伴详情。' },
    'The Architect\'s Sourcing Delegation to GZDW & Foshan': { id: 'Delegasi Pengadaan Arsitek ke GZDW & Foshan', zh: '印尼建筑师考察团直访广州设计周与佛山工厂' },
    'Our Operational Offices': { id: 'Kantor Operasional Kami', zh: '实体常驻办事处分布' },
    'Our Tri-City Office Network': { id: 'Jaringan Kantor di Tiga Kota', zh: '三城实体办事处网络' },
    'Visit our material galleries or schedule an in-person procurement meeting.': { id: 'Kunjungi galeri material kami atau jadwalkan pertemuan pengadaan langsung.', zh: '欢迎莅临我们的材料选品展厅或预约线下采购洽谈。' },
    'What Can We Help You Source?': { id: 'Apa yang Dapat Kami Bantu Carikan?', zh: '我们需要为您寻找什么源头供应链？' },
    'Select your interest below to connect immediately with our sourcing directors on WhatsApp.': { id: 'Pilih minat Anda di bawah untuk terhubung langsung dengan direktur pengadaan kami via WhatsApp.', zh: '选择您的需求类别，即可在 WhatsApp 上直接与我们的供应链负责人沟通。' },
    'Building & Interior Materials': { id: 'Material Bangunan & Interior', zh: '建筑与室内精品材料' },
    'Retail Supermarket Systems': { id: 'Sistem Supermarket & Ritel', zh: '商超系统与零售货架设备' },
    'Factory Audits & China QC': { id: 'Audit Pabrik & QC di China', zh: '源头验厂核查与驻华品控质检' },
    'GZDW Delegation & Tours': { id: 'Delegasi & Tur GZDW', zh: '广州设计周官方考察团' },
    'Experience Materials in Person': { id: 'Rasakan Material Secara Langsung', zh: '亲临品鉴源头材料实物' },
    'Surabaya Experience Center': { id: 'Pusat Pengalaman Surabaya', zh: '泗水材料品鉴体验中心' },
    'Jakarta Commercial Hub': { id: 'Pusat Komersial Jakarta', zh: '雅加达商务中心' },
    'Foshan Procurement & QC Center': { id: 'Pusat Pengadaan & QC Foshan', zh: '佛山直采与质检中心' },
    'China Partner Office': { id: 'Kantor Mitra China', zh: '中国合作办事处' },
    'Surabaya Headquarters': { id: 'Kantor Pusat Surabaya', zh: '泗水总部' },
    'Jakarta Office': { id: 'Kantor Jakarta', zh: '雅加达办事处' },
    'CHINA PRESENCE': { id: 'KEHADIRAN CHINA', zh: '中国办事处' },
    'INDONESIA HQ': { id: 'KANTOR PUSAT INDONESIA', zh: '印尼总部' },
    'COMMERCIAL OFFICE': { id: 'KANTOR KOMERSIAL', zh: '商务办事处' },
    'Start Your Sourcing Consultation': { id: 'Mulai Konsultasi Pengadaan Anda', zh: '开启您的源头直采咨询' },
    'Why Choose Vision Focus': { id: 'Mengapa Memilih Vision Focus', zh: '为什么选择 Vision Focus' },
    'Eliminating cross-border friction with direct pricing, on-site QC, and secure Indonesian logistics.': { id: 'Menghilangkan hambatan lintas negara dengan harga pabrik langsung, QC di lokasi, dan logistik aman di Indonesia.', zh: '杜绝跨境痛点，源头直采出厂价、驻厂专业质检及印尼全境清关派送。' },

    // How We Work Steps
    'Understand Your Needs': { id: 'Memahami Kebutuhan Anda', zh: '明确设计与工程需求' },
    'Source & Verify Factory Capacity': { id: 'Mencari & Memverifikasi Kapasitas Pabrik', zh: '优选并深度验厂核验产能' },
    'Procurement & Quality Control (QC)': { id: 'Pengadaan & Kontrol Kualitas (QC)', zh: '全流程驻厂采购与质检把关' },
    'Delivery & Port Clearance to Indonesia': { id: 'Pengiriman & Bea Cukai ke Indonesia', zh: '海运运输与印尼正规双清派送' },
    'After-Sales & Continuous Replenishment': { id: 'Layanan Purna Jual & Pasokan Berkelanjutan', zh: '售后质保与长期稳定补货支持' },

    // Core Advantages & Cards
    '100% Direct Factory Pricing': { id: '100% Harga Langsung Pabrik', zh: '100% 实力源头工厂出厂价' },
    'On-Site Foshan Engineering QC': { id: 'QC Engineering Langsung di Foshan', zh: '佛山驻地工程师全流程驻厂质检' },
    'Door-to-Door Indo Delivery': { id: 'Pengiriman Door-to-Door ke Indonesia', zh: '印尼全境双清门到门包办交付' },
    'Door-to-Door Indo Logistics': { id: 'Logistik Door-to-Door Indonesia', zh: '印尼全境双清门到门包办物流' },
    'Physical Sample Express': { id: 'Ekspres Sampel Fisik', zh: '实物样品极速空运试样' },
    'Custom OEM & Specification Sizing': { id: 'Kustom OEM & Ukuran Spesifikasi', zh: '定制 OEM 与工程特殊规格定制' },
    'Comprehensive Local Warranty & Support': { id: 'Garansi Lokal & Dukungan Menyeluruh', zh: '印尼本地质保与技术支持' },
    'Bilingual Professional Teams': { id: 'Tim Profesional Bilingual', zh: '双语专业执行团队' },
    'Tier-1 Direct Manufacturers': { id: 'Pabrik Produsen Tier-1 Langsung', zh: '直连源头一级实力制造商' },
    'End-to-End Reliability': { id: 'Keandalan Dari Awal Hingga Akhir', zh: '全流程无缝交付保障' },

    // Footer & Generic Labels
    'QUICK LINKS': { id: 'TAUTAN CEPAT', zh: '快捷导航' },
    'SOLUTIONS': { id: 'SOLUSI', zh: '业务板块' },
    'GET IN TOUCH': { id: 'HUBUNGI KAMI', zh: '联系方式' },
    'ALL PROJECTS': { id: 'SEMUA PROYEK', zh: '全部项目' },
    'All Projects': { id: 'Semua Proyek', zh: '全部项目' },
    'Commercial': { id: 'Komersial', zh: '商业地产' },
    'Hospitality': { id: 'Perhotelan', zh: '酒店度假' },
    'Residential': { id: 'Residensial', zh: '豪宅住宅' }
  };

  // Helper function to match clean text and handle prefixes/suffixes
  function translatePhrase(text, lang) {
    if (!text || lang === 'en') return text;
    const clean = text.replace(/[\s\u00A0]+/g, ' ').trim();
    if (!clean) return text;

    // 1. Direct match
    if (phraseDictionary[clean] && phraseDictionary[clean][lang]) {
      return phraseDictionary[clean][lang];
    }

    // 1b. Case-insensitive lookup fallback
    const lower = clean.toLowerCase();
    for (const [key, val] of Object.entries(phraseDictionary)) {
      if (key.toLowerCase() === lower && val[lang]) {
        if (clean === clean.toUpperCase() && val[lang].toUpperCase) {
          return val[lang].toUpperCase();
        }
        return val[lang];
      }
    }

    // 2. Handle numeric prefixes like "01 / ABOUT US"
    const prefixMatch = clean.match(/^(\d{2}\s*\/\s*)(.+)$/);
    if (prefixMatch) {
      const pfx = prefixMatch[1];
      const base = prefixMatch[2].trim();
      const translatedBase = translatePhrase(base, lang);
      if (translatedBase && translatedBase !== base) {
        return pfx + translatedBase;
      }
    }

    // 3. Handle trailing arrows like "LEARN MORE ›" or "Chat on WhatsApp ↗"
    const arrowMatch = clean.match(/^(.*?)\s*([›→↗&rsaquo;▾▸]+)$/);
    if (arrowMatch) {
      const base = arrowMatch[1].trim();
      const arrow = arrowMatch[2];
      const translatedBase = translatePhrase(base, lang);
      if (translatedBase && translatedBase !== base) {
        return translatedBase + ' ' + arrow;
      }
    }

    return null;
  }

  function setLanguage(lang) {
    if (!translations[lang]) lang = 'en';
    localStorage.setItem('vf_preferred_lang', lang);

    // Sync HTML lang attribute
    document.documentElement.lang = (lang === 'zh') ? 'zh-CN' : lang;

    // Update active class on all language buttons (desktop and mobile)
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    // 1. Apply translations to explicit [data-i18n] elements
    const dict = translations[lang];
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (dict[key]) {
        if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
          el.placeholder = dict[key];
        } else {
          // Preserve child chevron icon or arrows if present
          const icon = el.querySelector('.chevron-icon, svg, .nav-arrow, span');
          if (icon && (icon.classList.contains('chevron-icon') || icon.tagName === 'svg' || icon.classList.contains('nav-arrow') || (icon.tagName === 'SPAN' && (icon.innerText.includes('▾') || icon.innerText.includes('›'))))) {
            if (!el.dataset.iconHtml) {
              el.dataset.iconHtml = icon.outerHTML;
            }
            el.innerHTML = dict[key] + ' ' + el.dataset.iconHtml;
          } else {
            el.innerHTML = dict[key];
          }
        }
      }
    });

    // 2. Scan and translate general headings, buttons, links, breadcrumbs, eyebrows across subpages
    const textSelectors = [
      'h1', 'h2', 'h3', 'h4', 'h5',
      '.about-eyebrow', '.page-hero-eyebrow', '.page-hero-title',
      '.editorial-section-title', '.editorial-section-sub',
      '.service-card-title', '.service-card-desc',
      '.why-card-heading', '.why-card-text',
      '.service-flag-country', '.editorial-card-link',
      '.btn-clear-wa', '.dropdown-item span',
      '.page-breadcrumbs span', '.page-breadcrumbs a',
      '.step-process-card h3', '.step-process-card p',
      '.tag-badge', '.filter-pill-btn',
      '.footer-col h4', '.nav-link-item', '.mobile-nav-link'
    ];

    document.querySelectorAll(textSelectors.join(', ')).forEach(el => {
      // Don't override if already managed by data-i18n
      if (el.hasAttribute('data-i18n')) return;

      // Preserve child elements if it has complex nested structure
      if (el.children.length > 0 && !el.classList.contains('mobile-nav-link') && !el.classList.contains('dropdown-item')) {
        return;
      }

      // Cache original text on first encounter
      if (!el.dataset.i18nOrig) {
        el.dataset.i18nOrig = el.innerText.trim();
      }

      if (lang === 'en') {
        if (el.dataset.i18nOrig) {
          el.innerText = el.dataset.i18nOrig;
        }
      } else {
        const translated = translatePhrase(el.dataset.i18nOrig, lang);
        if (translated) {
          el.innerText = translated;
        }
      }
    });

    // 3. Sync with Google Translate cookie if present
    const host = window.location.hostname;
    const cookieVal = (lang === 'en') ? '/en/en' : (lang === 'zh' ? '/en/zh-CN' : ('/en/' + lang));
    document.cookie = 'googtrans=' + cookieVal + '; path=/;';
    if (host) {
      document.cookie = 'googtrans=' + cookieVal + '; path=/; domain=' + host + ';';
      document.cookie = 'googtrans=' + cookieVal + '; path=/; domain=.' + host + ';';
    }
  }

  // Bind language buttons (both desktop pill and mobile drawer)
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const lang = btn.getAttribute('data-lang');
      setLanguage(lang);
    });
  });

  // Initialize language: Persist preferred language or default to English
  const savedLang = localStorage.getItem('vf_preferred_lang') || 'en';
  setLanguage(savedLang);

  // 11. ACTIVE NAV INDICATOR
  (function initActiveNavIndicator() {
    const currentPath = window.location.pathname.toLowerCase();
    const currentPage = currentPath.substring(currentPath.lastIndexOf('/') + 1) || 'index.html';

    const desktopNavLinks = document.querySelectorAll('.desktop-nav .nav-link-item');
    const mobileLinks = document.querySelectorAll('.mobile-nav-link');

    desktopNavLinks.forEach(l => l.classList.remove('active'));
    mobileLinks.forEach(m => m.classList.remove('active'));

    function matchLink(selector, hrefKeyword) {
      return document.querySelector(`${selector}[href*="${hrefKeyword}"]`);
    }

    if (currentPage === '' || currentPage === 'index.html') {
      matchLink('.desktop-nav .nav-link-item', 'index.html')?.classList.add('active');
      matchLink('.mobile-nav-link', 'index.html')?.classList.add('active');
    } else if (currentPage.includes('project')) {
      matchLink('.desktop-nav .nav-link-item', 'projects.html')?.classList.add('active');
      matchLink('.mobile-nav-link', 'projects.html')?.classList.add('active');
    } else if (currentPage.includes('solution') || currentPage.includes('service')) {
      matchLink('.desktop-nav .nav-link-item', 'solutions.html')?.classList.add('active');
      matchLink('.mobile-nav-link', 'solutions.html')?.classList.add('active');
    } else if (currentPage.includes('event')) {
      matchLink('.desktop-nav .nav-link-item', 'events.html')?.classList.add('active');
      matchLink('.mobile-nav-link', 'events.html')?.classList.add('active');
    } else if (currentPage.includes('insight')) {
      matchLink('.desktop-nav .nav-link-item', 'insights.html')?.classList.add('active');
      matchLink('.mobile-nav-link', 'insights.html')?.classList.add('active');
    } else if (currentPage.includes('contact')) {
      matchLink('.desktop-nav .nav-link-item', 'contact.html')?.classList.add('active');
      matchLink('.mobile-nav-link', 'contact.html')?.classList.add('active');
    } else if (currentPage.includes('why') || currentPage.includes('how-we-work') || currentPage.includes('about')) {
      matchLink('.desktop-nav .nav-link-item', 'about.html')?.classList.add('active');
      matchLink('.mobile-nav-link', 'about.html')?.classList.add('active');
    }
  })();

  // 12. FULL-SCREEN SECTION SCROLL SPY & SIDE DOT NAVIGATION
  (function initSideSectionNav() {
    const sideLinks = document.querySelectorAll('.side-dot-link');
    if (!sideLinks.length) return;

    const sections = Array.from(sideLinks).map(link => {
      const targetId = link.getAttribute('href');
      return document.querySelector(targetId);
    }).filter(Boolean);

    function updateActiveSection() {
      const scrollPos = window.scrollY + window.innerHeight * 0.35;
      let currentSectionId = '';

      sections.forEach(section => {
        const top = section.offsetTop;
        const height = section.offsetHeight;
        if (scrollPos >= top && scrollPos < top + height) {
          currentSectionId = section.getAttribute('id');
        }
      });

      if (!currentSectionId && window.scrollY < 100) {
        currentSectionId = 'home';
      }

      // If scrolled near page bottom, activate contact/footer dot
      if ((window.innerHeight + window.scrollY) >= (document.documentElement.scrollHeight - 60)) {
        currentSectionId = 'contact';
      }

      sideLinks.forEach(link => {
        const href = link.getAttribute('href').replace('#', '');
        link.classList.toggle('active', href === currentSectionId);
      });
    }

    window.addEventListener('scroll', updateActiveSection, { passive: true });
    updateActiveSection();
  })();

  // 13. PREMIUM SMOOTH SCROLL FOR ANCHOR LINKS
  (function initSmoothScroll() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]:not([href="#"]):not([href="#!"])');
    anchorLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href');
        const targetEl = document.querySelector(targetId);
        if (!targetEl) return;
        e.preventDefault();
        
        const headerOffset = 70;
        const elementPosition = targetEl.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - (targetId === '#home' ? 0 : headerOffset);

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });

        if (history.pushState) {
          history.pushState(null, null, targetId);
        }
      });
    });
  })();

  // 14. LUXURY FADE-IN & FADE-IN-UP INTERSECTION OBSERVER
  (function initScrollAnimations() {
    const animatedElements = document.querySelectorAll('.fade-in-up, .fade-in');
    if (!animatedElements.length) return;

    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px'
      });

      animatedElements.forEach(el => observer.observe(el));
    } else {
      animatedElements.forEach(el => el.classList.add('is-visible'));
    }

    // Immediately trigger any hero animations
    setTimeout(() => {
      document.querySelectorAll('#home .fade-in-up, #home .fade-in').forEach(el => {
        el.classList.add('is-visible');
      });
    }, 150);
  })();
});
