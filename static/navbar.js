/**
 * Responsive Navbar JavaScript
 * Enhances the Bootstrap navbar with additional functionality
 */

document.addEventListener('DOMContentLoaded', function() {
  // Initialize navbar components
  initNavbar();
  
  // Update active state when URL changes without page reload
  window.addEventListener('popstate', function() {
    setActiveNavItem();
  });
  
  // Listen for custom navigation events that might be triggered by client-side routing
  document.addEventListener('navigation:complete', function() {
    setActiveNavItem();
  });
  
  // Monitor for potential client-side navigation
  const originalPushState = history.pushState;
  if (originalPushState) {
    history.pushState = function() {
      originalPushState.apply(this, arguments);
      setActiveNavItem(); // Update active state when pushState is called
    };
  }
});

/**
 * Initialize navbar functionality
 */
function initNavbar() {
  // Handle dropdown behavior on mobile devices
  initMobileDropdowns();
  
  // Initialize search toggle functionality
  initSearchToggle();
  
  // Set active navigation item based on current URL
  setActiveNavItem();
  
  // Add accessibility enhancements
  enhanceAccessibility();
  
  // Enhance keyboard navigation
  enhanceKeyboardNavigation();
  
  // Initialize ARIA live regions
  initAriaLiveRegions();
  
  // Handle responsive behavior
  handleResponsiveBehavior();
  
  // Initialize scroll effect
  initScrollEffect();
}

/**
 * Handle dropdown behavior for both mobile and desktop devices
 * Enhanced as part of task 7.1: Add dropdown behavior enhancements
 */
function initMobileDropdowns() {
  // Check if we're on a touch device
  const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
  
  // Get all dropdown toggle elements
  const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
  
  // For each dropdown toggle
  dropdownToggles.forEach(toggle => {
    // Handle click events for all devices
    toggle.addEventListener('click', function(e) {
      // Only prevent default on mobile or for touch devices on desktop
      if (window.innerWidth < 768 || (isTouchDevice && window.innerWidth >= 768)) {
        e.preventDefault();
        e.stopPropagation();
        
        // Toggle the dropdown menu
        const dropdownMenu = this.nextElementSibling;
        if (dropdownMenu.classList.contains('show')) {
          dropdownMenu.classList.remove('show');
          this.setAttribute('aria-expanded', 'false');
        } else {
          // Close any other open dropdowns at the same level
          const parentUl = this.closest('ul');
          if (parentUl) {
            parentUl.querySelectorAll('.dropdown-menu.show').forEach(menu => {
              if (menu !== dropdownMenu && menu.parentElement.parentElement === parentUl) {
                menu.classList.remove('show');
                const otherToggle = menu.previousElementSibling;
                if (otherToggle) {
                  otherToggle.setAttribute('aria-expanded', 'false');
                }
              }
            });
          }
          
          dropdownMenu.classList.add('show');
          this.setAttribute('aria-expanded', 'true');
          
          // Focus first item in dropdown for accessibility
          setTimeout(() => {
            const firstItem = dropdownMenu.querySelector('a');
            if (firstItem) {
              firstItem.focus();
            }
          }, 100);
        }
      }
    });
    
    // Add hover behavior for desktop non-touch devices
    if (!isTouchDevice) {
      const dropdownParent = toggle.closest('.dropdown');
      
      if (dropdownParent && window.innerWidth >= 768) {
        let leaveTimeout;
        // Add hover event listeners for desktop
        dropdownParent.addEventListener('mouseenter', function() {
          if (window.innerWidth >= 768) {
            const dropdownMenu = this.querySelector('.dropdown-menu');
            if (dropdownMenu) {
              clearTimeout(leaveTimeout);
              dropdownMenu.classList.add('show');
              toggle.setAttribute('aria-expanded', 'true');
            }
          }
        });
        
        dropdownParent.addEventListener('mouseleave', function() {
          if (window.innerWidth >= 768) {
            const dropdownMenu = this.querySelector('.dropdown-menu');
            if (dropdownMenu) {
              leaveTimeout = setTimeout(() => {
                dropdownMenu.classList.remove('show');
                toggle.setAttribute('aria-expanded', 'false');
              }, 300);
            }
          }
        });
      }
    }
  });
  
  // Handle nested dropdown toggles
  const submenuToggles = document.querySelectorAll('.dropdown-submenu > .dropdown-item.dropdown-toggle');
  submenuToggles.forEach(toggle => {
    // Handle click events for all devices
    toggle.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      
      const submenu = this.nextElementSibling;
      
      // Toggle submenu visibility
      if (submenu.classList.contains('show')) {
        submenu.classList.remove('show');
        this.setAttribute('aria-expanded', 'false');
      } else {
        // Close other submenus at the same level
        const parentMenu = this.closest('.dropdown-menu');
        if (parentMenu) {
          parentMenu.querySelectorAll('.dropdown-submenu-menu.show').forEach(menu => {
            if (menu !== submenu) {
              menu.classList.remove('show');
              const otherToggle = menu.previousElementSibling;
              if (otherToggle) {
                otherToggle.setAttribute('aria-expanded', 'false');
              }
            }
          });
        }
        
        submenu.classList.add('show');
        this.setAttribute('aria-expanded', 'true');
        
        // Focus first item in submenu for accessibility
        setTimeout(() => {
          const firstItem = submenu.querySelector('a');
          if (firstItem) {
            firstItem.focus();
          }
        }, 100);
      }
    });
    
    // Add hover behavior for desktop non-touch devices
    if (!isTouchDevice) {
      const submenuParent = toggle.closest('.dropdown-submenu');
      
      if (submenuParent) {
        let leaveTimeout;
        // Add hover event listeners for desktop
        submenuParent.addEventListener('mouseenter', function() {
          if (window.innerWidth >= 768) {
            const submenu = this.querySelector('.dropdown-submenu-menu');
            if (submenu) {
              clearTimeout(leaveTimeout);
              submenu.classList.add('show');
              toggle.setAttribute('aria-expanded', 'true');
            }
          }
        });
        
        submenuParent.addEventListener('mouseleave', function() {
          if (window.innerWidth >= 768) {
            const submenu = this.querySelector('.dropdown-submenu-menu');
            if (submenu) {
              leaveTimeout = setTimeout(() => {
                submenu.classList.remove('show');
                toggle.setAttribute('aria-expanded', 'false');
              }, 300);
            }
          }
        });
      }
    }
  });
  
  // Close dropdowns when clicking outside
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.dropdown')) {
      document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
        menu.classList.remove('show');
        const toggle = menu.previousElementSibling;
        if (toggle) {
          toggle.setAttribute('aria-expanded', 'false');
        }
      });
    }
  });
  
  // Enhanced touch behavior for touch devices on desktop
  if (isTouchDevice) {
    // Add touch-specific behavior for desktop view
    const dropdowns = document.querySelectorAll('.navbar .dropdown, .navbar .dropdown-submenu');
    
    dropdowns.forEach(dropdown => {
      // Store touch count as a property on the element
      dropdown.touchCount = 0;
      
      dropdown.addEventListener('touchstart', function(e) {
        if (window.innerWidth >= 768) {
          const toggle = dropdown.querySelector('.dropdown-toggle') || 
                         dropdown.querySelector('.dropdown-item.dropdown-toggle');
          const menu = dropdown.querySelector('.dropdown-menu') || 
                       dropdown.querySelector('.dropdown-submenu-menu');
          
          if (toggle && menu && (e.target === toggle || toggle.contains(e.target))) {
            // Increment touch count
            this.touchCount = (this.touchCount || 0) + 1;
            
            // First touch opens dropdown, second touch follows link
            if (this.touchCount === 1) {
              e.preventDefault();
              e.stopPropagation();
              
              // Close any other open dropdowns
              dropdowns.forEach(d => {
                if (d !== dropdown) {
                  const dMenu = d.querySelector('.dropdown-menu') || 
                               d.querySelector('.dropdown-submenu-menu');
                  const dToggle = d.querySelector('.dropdown-toggle') || 
                                 d.querySelector('.dropdown-item.dropdown-toggle');
                  
                  if (dMenu && dMenu.classList.contains('show')) {
                    dMenu.classList.remove('show');
                    if (dToggle) {
                      dToggle.setAttribute('aria-expanded', 'false');
                    }
                  }
                  
                  // Reset touch count for other dropdowns
                  d.touchCount = 0;
                }
              });
              
              // Show this dropdown
              menu.classList.add('show');
              toggle.setAttribute('aria-expanded', 'true');
              
              // Add visual feedback for touch
              toggle.classList.add('touch-active');
              setTimeout(() => {
                toggle.classList.remove('touch-active');
              }, 300);
            } else {
              // Second touch - follow the link if it's not just a toggle
              this.touchCount = 0;
              
              if (toggle.getAttribute('href') && toggle.getAttribute('href') !== '#') {
                window.location.href = toggle.getAttribute('href');
              }
            }
          } else if (!e.target.closest('.dropdown-menu') && !e.target.closest('.dropdown-submenu-menu')) {
            // If touching outside dropdown menus, reset all touch counts
            dropdowns.forEach(d => {
              d.touchCount = 0;
            });
          }
        }
      });
    });
    
    // Reset touch counts when touching elsewhere on the document
    document.addEventListener('touchstart', function(e) {
      if (!e.target.closest('.dropdown') && !e.target.closest('.dropdown-submenu')) {
        const dropdowns = document.querySelectorAll('.navbar .dropdown, .navbar .dropdown-submenu');
        dropdowns.forEach(d => {
          d.touchCount = 0;
        });
      }
    });
  }
  
  // Handle window resize to reset dropdown states
  window.addEventListener('resize', debounce(function() {
    // Reset all dropdowns when window size changes between mobile and desktop breakpoints
    const wasMobile = window.innerWidth < 768;
    const isMobile = window.innerWidth < 768;
    
    if (wasMobile !== isMobile) {
      document.querySelectorAll('.dropdown-menu.show, .dropdown-submenu-menu.show').forEach(menu => {
        menu.classList.remove('show');
        const toggle = menu.previousElementSibling;
        if (toggle) {
          toggle.setAttribute('aria-expanded', 'false');
        }
      });
      
      // Reset touch counts
      document.querySelectorAll('.navbar .dropdown, .navbar .dropdown-submenu').forEach(d => {
        d.touchCount = 0;
      });
    }
  }, 250));
}

/**
 * Initialize search toggle functionality for mobile view
 * Enhanced as part of task 7.2: Implement search toggle functionality
 */
function initSearchToggle() {
  const searchToggle = document.querySelector('.search-toggle');
  if (searchToggle) {
    // Set initial aria-expanded state
    searchToggle.setAttribute('aria-expanded', 'false');
    
    // Add ARIA label for better accessibility
    if (!searchToggle.getAttribute('aria-label')) {
      searchToggle.setAttribute('aria-label', 'Toggle search form');
    }
    
    searchToggle.addEventListener('click', function(e) {
      e.preventDefault();
      
      const searchCollapse = document.querySelector('.search-collapse');
      if (searchCollapse) {
        // Toggle the search collapse with enhanced animation
        if (searchCollapse.classList.contains('show')) {
          // Add closing animation class
          searchCollapse.classList.add('closing');
          
          // Wait for animation to complete before hiding
          setTimeout(() => {
            searchCollapse.classList.remove('show');
            searchCollapse.classList.remove('closing');
            searchToggle.setAttribute('aria-expanded', 'false');
            searchToggle.setAttribute('aria-label', 'Open search form');
            
            // Update toggle button text
            const toggleText = searchToggle.querySelector('span');
            if (toggleText) {
              toggleText.textContent = 'Search';
            }
            
            // Announce to screen readers that search is closed
            announceToScreenReader('Search form closed');
          }, 300);
          
          // Animate the icon
          const searchIcon = searchToggle.querySelector('i');
          if (searchIcon) {
            // Change icon back to search with animation
            searchIcon.classList.add('fa-flip');
            
            setTimeout(() => {
              searchIcon.classList.remove('fa-times');
              searchIcon.classList.add('fa-search');
              searchIcon.classList.remove('fa-flip');
            }, 150);
          }
        } else {
          // Show the search collapse with enhanced animation
          searchCollapse.classList.add('show');
          searchToggle.setAttribute('aria-expanded', 'true');
          searchToggle.setAttribute('aria-label', 'Close search form');
          
          // Update toggle button text
          const toggleText = searchToggle.querySelector('span');
          if (toggleText) {
            toggleText.textContent = 'Close';
          }
          
          // Focus the search input when expanded
          const searchInput = searchCollapse.querySelector('input[type="search"]');
          if (searchInput) {
            setTimeout(() => {
              searchInput.focus();
            }, 300);
          }
          
          // Add animation class to the icon
          const searchIcon = searchToggle.querySelector('i');
          if (searchIcon) {
            // Change icon to times/close with animation
            searchIcon.classList.add('fa-flip');
            
            setTimeout(() => {
              searchIcon.classList.remove('fa-search');
              searchIcon.classList.add('fa-times');
              searchIcon.classList.remove('fa-flip');
            }, 150);
          }
          
          // Announce to screen readers that search is open
          announceToScreenReader('Search form opened');
        }
      }
    });
    
    // Close search on escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        const searchCollapse = document.querySelector('.search-collapse.show');
        if (searchCollapse) {
          // Add closing animation class
          searchCollapse.classList.add('closing');
          
          // Wait for animation to complete before hiding
          setTimeout(() => {
            searchCollapse.classList.remove('show');
            searchCollapse.classList.remove('closing');
            searchToggle.setAttribute('aria-expanded', 'false');
            searchToggle.setAttribute('aria-label', 'Open search form');
            
            // Reset icon and text
            const searchIcon = searchToggle.querySelector('i');
            if (searchIcon) {
              searchIcon.classList.remove('fa-times');
              searchIcon.classList.add('fa-search');
            }
            
            const toggleText = searchToggle.querySelector('span');
            if (toggleText) {
              toggleText.textContent = 'Search';
            }
            
            // Announce to screen readers that search is closed
            announceToScreenReader('Search form closed with escape key');
          }, 300);
          
          // Animate the icon
          const searchIcon = searchToggle.querySelector('i');
          if (searchIcon) {
            searchIcon.classList.add('fa-flip');
            setTimeout(() => {
              searchIcon.classList.remove('fa-flip');
            }, 300);
          }
          
          // Return focus to the toggle button for better accessibility
          setTimeout(() => {
            searchToggle.focus();
          }, 350);
        }
      }
    });
    
    // Close search when clicking outside
    document.addEventListener('click', function(e) {
      if (!e.target.closest('.search-collapse') && !e.target.closest('.search-toggle')) {
        const searchCollapse = document.querySelector('.search-collapse.show');
        if (searchCollapse) {
          // Add closing animation class
          searchCollapse.classList.add('closing');
          
          // Wait for animation to complete before hiding
          setTimeout(() => {
            searchCollapse.classList.remove('show');
            searchCollapse.classList.remove('closing');
            searchToggle.setAttribute('aria-expanded', 'false');
            searchToggle.setAttribute('aria-label', 'Open search form');
            
            // Reset icon and text
            const searchIcon = searchToggle.querySelector('i');
            if (searchIcon) {
              searchIcon.classList.remove('fa-times');
              searchIcon.classList.add('fa-search');
            }
            
            const toggleText = searchToggle.querySelector('span');
            if (toggleText) {
              toggleText.textContent = 'Search';
            }
          }, 300);
          
          // Animate the icon
          const searchIcon = searchToggle.querySelector('i');
          if (searchIcon) {
            searchIcon.classList.add('fa-flip');
            setTimeout(() => {
              searchIcon.classList.remove('fa-flip');
            }, 300);
          }
        }
      }
    });
    
    // Handle window resize to properly manage search state
    window.addEventListener('resize', debounce(function() {
      const searchCollapse = document.querySelector('.search-collapse');
      
      // If transitioning from mobile to desktop view, reset search state
      if (window.innerWidth >= 768 && searchCollapse && searchCollapse.classList.contains('show')) {
        searchCollapse.classList.remove('show');
        searchCollapse.classList.remove('closing');
        searchToggle.setAttribute('aria-expanded', 'false');
        searchToggle.setAttribute('aria-label', 'Open search form');
        
        // Reset icon and text
        const searchIcon = searchToggle.querySelector('i');
        if (searchIcon) {
          searchIcon.classList.remove('fa-times');
          searchIcon.classList.add('fa-search');
        }
        
        const toggleText = searchToggle.querySelector('span');
        if (toggleText) {
          toggleText.textContent = 'Search';
        }
      }
    }, 250));
    
    // Add touch ripple effect for mobile devices
    if ('ontouchstart' in window || navigator.maxTouchPoints > 0) {
      searchToggle.addEventListener('touchstart', function(e) {
        // Create ripple effect
        const ripple = document.createElement('span');
        ripple.classList.add('search-toggle-ripple');
        this.appendChild(ripple);
        
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        
        ripple.style.width = ripple.style.height = `${size}px`;
        ripple.style.left = `${e.touches[0].clientX - rect.left - size/2}px`;
        ripple.style.top = `${e.touches[0].clientY - rect.top - size/2}px`;
        
        // Remove ripple after animation completes
        setTimeout(() => {
          ripple.remove();
        }, 600);
      });
    }
  }
  
  // Initialize desktop search enhancements
  initDesktopSearch();
  
  // Initialize search form validation
  initSearchFormValidation();
}

/**
 * Initialize desktop search enhancements
 * Enhanced as part of task 7.2: Implement search toggle functionality
 */
function initDesktopSearch() {
  const desktopSearchContainer = document.querySelector('.d-none.d-md-block .search-form');
  
  if (desktopSearchContainer) {
    const searchInput = desktopSearchContainer.querySelector('input[type="search"]');
    const searchButton = desktopSearchContainer.querySelector('button[type="submit"]');
    
    if (searchInput) {
      // Add focus/blur animations for desktop search
      searchInput.addEventListener('focus', function() {
        desktopSearchContainer.classList.add('search-focused');
        
        // Animate the search icon when input is focused
        if (searchButton) {
          const searchIcon = searchButton.querySelector('i');
          if (searchIcon) {
            searchIcon.classList.add('fa-beat');
            setTimeout(() => {
              searchIcon.classList.remove('fa-beat');
            }, 500);
          }
        }
      });
      
      searchInput.addEventListener('blur', function() {
        if (!this.value) {
          desktopSearchContainer.classList.remove('search-focused');
        }
      });
      
      // Add hover effect for search button
      if (searchButton) {
        searchButton.addEventListener('mouseenter', function() {
          const searchIcon = this.querySelector('i');
          if (searchIcon) {
            searchIcon.classList.add('fa-flip');
            setTimeout(() => {
              searchIcon.classList.remove('fa-flip');
            }, 500);
          }
        });
        
        // Add click animation
        searchButton.addEventListener('click', function() {
          this.classList.add('search-button-clicked');
          setTimeout(() => {
            this.classList.remove('search-button-clicked');
          }, 300);
        });
      }
      
      // Add input animation
      searchInput.addEventListener('input', function() {
        if (this.value) {
          this.classList.add('has-content');
        } else {
          this.classList.remove('has-content');
        }
      });
    }
  }
}

/**
 * Initialize search form validation
 * Added as part of task 7.2: Implement search toggle functionality
 */
function initSearchFormValidation() {
  const searchForms = document.querySelectorAll('.search-form');
  
  searchForms.forEach(form => {
    form.addEventListener('submit', function(e) {
      const searchInput = this.querySelector('input[type="search"]');
      
      if (searchInput && !searchInput.value.trim()) {
        e.preventDefault();
        
        // Add validation error class
        searchInput.classList.add('empty');
        searchInput.setAttribute('aria-invalid', 'true');
        
        // Shake animation for empty search
        searchInput.classList.add('search-shake');
        
        // Remove shake class after animation completes
        setTimeout(() => {
          searchInput.classList.remove('search-shake');
        }, 600);
        
        // Focus the input
        searchInput.focus();
        
        // Announce error to screen readers
        announceToScreenReader('Please enter a search term');
        
        // Remove error class after a delay
        setTimeout(() => {
          searchInput.classList.remove('empty');
          searchInput.removeAttribute('aria-invalid');
        }, 3000);
      }
    });
  });
}

/**
 * Initialize ARIA live regions for better screen reader support
 * Enhanced for accessibility improvements
 */
function initAriaLiveRegions() {
  // Create navigation status announcer
  let navAnnouncer = document.getElementById('nav-announcer');
  if (!navAnnouncer) {
    navAnnouncer = document.createElement('div');
    navAnnouncer.id = 'nav-announcer';
    navAnnouncer.setAttribute('aria-live', 'polite');
    navAnnouncer.setAttribute('aria-atomic', 'true');
    navAnnouncer.className = 'sr-only';
    document.body.appendChild(navAnnouncer);
  }
  
  // Announce navigation changes
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
  navLinks.forEach(link => {
    link.addEventListener('click', function() {
      const linkText = this.textContent.trim();
      setTimeout(() => {
        announceToScreenReader(`Navigating to ${linkText}`);
      }, 100);
    });
  });
  
  // Announce dropdown state changes
  const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
  dropdownToggles.forEach(toggle => {
    toggle.addEventListener('click', function() {
      const isExpanded = this.getAttribute('aria-expanded') === 'true';
      const toggleText = this.textContent.trim();
      setTimeout(() => {
        announceToScreenReader(`${toggleText} menu ${isExpanded ? 'closed' : 'opened'}`);
      }, 100);
    });
  });
}

/**
 * Enhanced accessibility features for navbar
 * Implements comprehensive accessibility improvements
 */
function enhanceAccessibility() {
  // Add proper ARIA labels to navigation elements
  const navbar = document.querySelector('.navbar');
  if (navbar && !navbar.getAttribute('aria-label')) {
    navbar.setAttribute('aria-label', 'Main navigation');
  }
  
  // Enhance dropdown menus with proper ARIA attributes
  const dropdowns = document.querySelectorAll('.dropdown');
  dropdowns.forEach(dropdown => {
    const toggle = dropdown.querySelector('.dropdown-toggle');
    const menu = dropdown.querySelector('.dropdown-menu');
    
    if (toggle && menu) {
      // Ensure proper ARIA relationship
      if (!toggle.getAttribute('aria-haspopup')) {
        toggle.setAttribute('aria-haspopup', 'true');
      }
      
      if (!toggle.getAttribute('aria-expanded')) {
        toggle.setAttribute('aria-expanded', 'false');
      }
      
      // Add role to dropdown menu
      if (!menu.getAttribute('role')) {
        menu.setAttribute('role', 'menu');
      }
      
      // Add role to dropdown items
      const items = menu.querySelectorAll('.dropdown-item');
      items.forEach(item => {
        if (!item.getAttribute('role')) {
          item.setAttribute('role', 'menuitem');
        }
      });
    }
  });
  
  // Enhance navbar toggler accessibility
  const toggler = document.querySelector('.navbar-toggler');
  if (toggler) {
    if (!toggler.getAttribute('aria-label')) {
      toggler.setAttribute('aria-label', 'Toggle navigation menu');
    }
    
    // Update aria-label based on state
    toggler.addEventListener('click', function() {
      const isExpanded = this.getAttribute('aria-expanded') === 'true';
      this.setAttribute('aria-label', isExpanded ? 'Close navigation menu' : 'Open navigation menu');
    });
  }
  
  // Add landmarks to navigation sections
  const mainNav = document.querySelector('.navbar-nav');
  if (mainNav && !mainNav.getAttribute('role')) {
    mainNav.setAttribute('role', 'menubar');
  }
  
  const userNav = document.querySelector('.user-account-section');
  if (userNav && !userNav.getAttribute('aria-label')) {
    userNav.setAttribute('aria-label', 'User account menu');
  }
  
  // Enhance search form accessibility
  const searchForm = document.querySelector('.search-form');
  if (searchForm) {
    const searchInput = searchForm.querySelector('input[type="search"]');
    const searchButton = searchForm.querySelector('button[type="submit"]');
    
    if (searchInput && !searchInput.getAttribute('aria-label')) {
      searchInput.setAttribute('aria-label', 'Search');
    }
    
    if (searchButton && !searchButton.getAttribute('aria-label')) {
      searchButton.setAttribute('aria-label', 'Submit search');
    }
  }
}

/**
 * Enhanced keyboard navigation for navbar
 * Implements comprehensive keyboard support
 */
function enhanceKeyboardNavigation() {
  // Handle Enter and Space key activation for dropdown toggles
  const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
  dropdownToggles.forEach(toggle => {
    toggle.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.click();
      } else if (e.key === 'ArrowDown') {
        e.preventDefault();
        const menu = this.nextElementSibling;
        if (menu && menu.classList.contains('dropdown-menu')) {
          menu.classList.add('show');
          this.setAttribute('aria-expanded', 'true');
          const firstItem = menu.querySelector('.dropdown-item');
          if (firstItem) {
            firstItem.focus();
          }
        }
      }
    });
  });
  
  // Handle arrow key navigation in dropdown menus
  const dropdownMenus = document.querySelectorAll('.dropdown-menu');
  dropdownMenus.forEach(menu => {
    const items = menu.querySelectorAll('.dropdown-item');
    
    items.forEach((item, index) => {
      item.addEventListener('keydown', function(e) {
        let nextIndex;
        
        switch (e.key) {
          case 'ArrowDown':
            e.preventDefault();
            nextIndex = (index + 1) % items.length;
            items[nextIndex].focus();
            break;
            
          case 'ArrowUp':
            e.preventDefault();
            nextIndex = index > 0 ? index - 1 : items.length - 1;
            items[nextIndex].focus();
            break;
            
          case 'Home':
            e.preventDefault();
            items[0].focus();
            break;
            
          case 'End':
            e.preventDefault();
            items[items.length - 1].focus();
            break;
            
          case 'Escape':
            e.preventDefault();
            menu.classList.remove('show');
            const toggle = menu.previousElementSibling;
            if (toggle) {
              toggle.setAttribute('aria-expanded', 'false');
              toggle.focus();
            }
            break;
            
          case 'Tab':
            // Allow normal tab behavior but close dropdown
            menu.classList.remove('show');
            const toggleTab = menu.previousElementSibling;
            if (toggleTab) {
              toggleTab.setAttribute('aria-expanded', 'false');
            }
            break;
        }
      });
    });
  });
  
  // Handle navbar toggler keyboard activation
  const toggler = document.querySelector('.navbar-toggler');
  if (toggler) {
    toggler.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.click();
      }
    });
  }
  
  // Focus management for mobile menu
  const navbarCollapse = document.querySelector('.navbar-collapse');
  if (navbarCollapse) {
    // Focus first item when menu opens
    navbarCollapse.addEventListener('shown.bs.collapse', function() {
      const firstLink = this.querySelector('.nav-link');
      if (firstLink) {
        firstLink.focus();
      }
    });
    
    // Return focus to toggler when menu closes
    navbarCollapse.addEventListener('hidden.bs.collapse', function() {
      if (toggler) {
        toggler.focus();
      }
    });
  }
  
  // Trap focus in mobile menu when open
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Tab' && navbarCollapse && navbarCollapse.classList.contains('show')) {
      const focusableElements = navbarCollapse.querySelectorAll(
        'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
      );
      
      const firstElement = focusableElements[0];
      const lastElement = focusableElements[focusableElements.length - 1];
      
      if (e.shiftKey) {
        if (document.activeElement === firstElement) {
          e.preventDefault();
          lastElement.focus();
        }
      } else {
        if (document.activeElement === lastElement) {
          e.preventDefault();
          firstElement.focus();
        }
      }
    }
  });
}

/**
 * Utility function to announce messages to screen readers
 * Enhanced for better accessibility support
 */
function announceToScreenReader(message) {
  // Check if we already have an announcement element
  let announcer = document.getElementById('sr-announcer');
  
  if (!announcer) {
    // Create a visually hidden element for screen reader announcements
    announcer = document.createElement('div');
    announcer.id = 'sr-announcer';
    announcer.setAttribute('aria-live', 'polite');
    announcer.setAttribute('aria-atomic', 'true');
    announcer.className = 'sr-only';
    document.body.appendChild(announcer);
  }
  
  // Clear previous message
  announcer.textContent = '';
  
  // Set the message after a brief delay to ensure it's announced
  setTimeout(() => {
    announcer.textContent = message;
  }, 100);
  
  // Clear the announcer after a delay
  setTimeout(() => {
    announcer.textContent = '';
  }, 3000);
}

/**
 * Initialize desktop search enhancements
 * Added as part of task 7.2: Implement search toggle functionality
 */
function initDesktopSearch() {
  const desktopSearchContainer = document.querySelector('.d-none.d-md-block .search-form');
  
  if (desktopSearchContainer) {
    const searchInput = desktopSearchContainer.querySelector('input[type="search"]');
    const searchButton = desktopSearchContainer.querySelector('button[type="submit"]');
    
    if (searchInput) {
      // Add focus/blur animations for desktop search
      searchInput.addEventListener('focus', function() {
        desktopSearchContainer.classList.add('search-focused');
      });
      
      searchInput.addEventListener('blur', function() {
        if (!this.value) {
          desktopSearchContainer.classList.remove('search-focused');
        }
      });
      
      // Add hover effect for search button
      if (searchButton) {
        searchButton.addEventListener('mouseenter', function() {
          const searchIcon = this.querySelector('i');
          if (searchIcon) {
            searchIcon.classList.add('fa-flip');
            setTimeout(() => {
              searchIcon.classList.remove('fa-flip');
            }, 500);
          }
        });
      }
    }
  }
}

/**
 * Set the active navigation item based on the current URL
 */
function setActiveNavItem() {
  // Get current path
  const currentPath = window.location.pathname;
  
  // Reset all active states first
  document.querySelectorAll('.navbar-nav .active, .navbar-nav .active-parent, .dropdown-item.active').forEach(el => {
    el.classList.remove('active', 'active-parent');
  });
  
  // First check dropdown items (including nested ones)
  let activeItemFound = false;
  const dropdownItems = document.querySelectorAll('.dropdown-item:not(.dropdown-toggle)');
  
  dropdownItems.forEach(item => {
    const href = item.getAttribute('href');
    
    // Skip items without href
    if (!href) {
      return;
    }
    
    // Check if the href matches the current path
    if (href === currentPath || 
        (href !== '/' && currentPath.startsWith(href)) ||
        (href === '/' && currentPath === '/')) {
      
      // Set this item as active
      item.classList.add('active');
      activeItemFound = true;
      
      // If this is in a submenu, set the parent dropdown-toggle as active
      const parentSubmenu = item.closest('.dropdown-submenu');
      if (parentSubmenu) {
        const parentToggle = parentSubmenu.querySelector('.dropdown-item.dropdown-toggle');
        if (parentToggle) {
          parentToggle.classList.add('active');
          parentSubmenu.classList.add('active');
        }
      }
      
      // Set all parent dropdowns as active-parent
      let parentDropdown = item.closest('.dropdown');
      while (parentDropdown) {
        parentDropdown.classList.add('active-parent');
        
        // If this is a top-level dropdown, set its nav-link as active
        const navLink = parentDropdown.querySelector('.nav-link');
        if (navLink) {
          navLink.setAttribute('aria-current', 'page');
        }
        
        // Move up to the next parent dropdown if any
        parentDropdown = parentDropdown.parentElement.closest('.dropdown');
      }
    }
  });
  
  // If no dropdown item was active, check top-level nav links
  if (!activeItemFound) {
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link:not(.dropdown-toggle)');
    
    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      
      // Skip links without href
      if (!href) {
        return;
      }
      
      // Check if the href matches the current path
      if (href === currentPath || 
          (href !== '/' && currentPath.startsWith(href)) ||
          (href === '/' && currentPath === '/')) {
        
        // Set this link's parent as active
        const navItem = link.closest('.nav-item');
        if (navItem) {
          navItem.classList.add('active');
          link.setAttribute('aria-current', 'page');
        }
      }
    });
  }
  
  // Check dropdown toggles if they match the current path exactly
  const dropdownToggles = document.querySelectorAll('.nav-link.dropdown-toggle');
  
  dropdownToggles.forEach(toggle => {
    const href = toggle.getAttribute('href');
    
    // Skip toggles with # or without href
    if (!href || href === '#') {
      return;
    }
    
    // Check if the href matches the current path exactly
    if (href === currentPath) {
      // Set this toggle's parent as active
      const navItem = toggle.closest('.nav-item');
      if (navItem) {
        navItem.classList.add('active');
        toggle.setAttribute('aria-current', 'page');
      }
    }
  });
}

/**
 * Handle responsive behavior for different viewport sizes
 * Enhanced as part of task 7.1 & 7.4: Improve responsive navigation
 */
function handleResponsiveBehavior() {
  // Initial check on page load
  adjustForViewport();
  
  // Listen for window resize events with enhanced debouncing
  window.addEventListener('resize', debounce(function() {
    adjustForViewport();
    handleBreakpointChanges();
  }, 250));
  
  // Enhanced navbar toggler behavior - Task 7.2
  const navbarToggler = document.querySelector('.navbar-toggler');
  const navbarCollapse = document.querySelector('.navbar-collapse');
  
  if (navbarToggler && navbarCollapse) {
    navbarToggler.addEventListener('click', function() {
      // Add pulse animation
      this.classList.add('toggler-active');
      setTimeout(() => {
        this.classList.remove('toggler-active');
      }, 600);
      
      // Enhanced collapse animation
      if (navbarCollapse.classList.contains('show')) {
        // Closing animation
        navbarCollapse.classList.add('closing');
        setTimeout(() => {
          navbarCollapse.classList.remove('closing');
        }, 350);
      }
    });
    
    // Listen for Bootstrap collapse events
    navbarCollapse.addEventListener('show.bs.collapse', function() {
      this.style.willChange = 'height, opacity, transform';
    });
    
    navbarCollapse.addEventListener('shown.bs.collapse', function() {
      this.style.willChange = 'auto';
    });
    
    navbarCollapse.addEventListener('hide.bs.collapse', function() {
      this.style.willChange = 'height, opacity, transform';
      this.classList.add('closing');
    });
    
    navbarCollapse.addEventListener('hidden.bs.collapse', function() {
      this.style.willChange = 'auto';
      this.classList.remove('closing');
    });
  }
}

/**
 * Adjust layout and behavior based on current viewport size
 * Enhanced as part of task 7.4: Test and refine breakpoint behavior
 */
function adjustForViewport() {
  const viewportWidth = window.innerWidth;
  const body = document.body;
  
  // Remove existing viewport classes
  body.classList.remove('viewport-xs', 'viewport-sm', 'viewport-md', 'viewport-lg', 'viewport-xl');
  
  // Add appropriate viewport class for CSS targeting
  if (viewportWidth < 576) {
    body.classList.add('viewport-xs');
    optimizeForMobile();
  } else if (viewportWidth < 768) {
    body.classList.add('viewport-sm');
    optimizeForSmallTablet();
  } else if (viewportWidth < 992) {
    body.classList.add('viewport-md');
    optimizeForTablet();
  } else if (viewportWidth < 1200) {
    body.classList.add('viewport-lg');
    optimizeForDesktop();
  } else {
    body.classList.add('viewport-xl');
    optimizeForLargeDesktop();
  }
}

/**
 * Handle breakpoint changes and reset states
 * Added as part of task 7.4: Test and refine breakpoint behavior
 */
function handleBreakpointChanges() {
  const currentViewport = getCurrentViewport();
  const previousViewport = document.body.getAttribute('data-previous-viewport');
  
  if (currentViewport !== previousViewport) {
    // Reset navigation states when crossing major breakpoints
    if ((previousViewport === 'mobile' && currentViewport === 'desktop') ||
        (previousViewport === 'desktop' && currentViewport === 'mobile')) {
      resetNavigationStates();
    }
    
    // Update previous viewport
    document.body.setAttribute('data-previous-viewport', currentViewport);
    
    // Trigger custom event for other components
    document.dispatchEvent(new CustomEvent('viewport:changed', {
      detail: { 
        current: currentViewport, 
        previous: previousViewport,
        width: window.innerWidth 
      }
    }));
  }
}

/**
 * Get current viewport category
 */
function getCurrentViewport() {
  const width = window.innerWidth;
  if (width < 768) return 'mobile';
  if (width < 992) return 'tablet';
  return 'desktop';
}

/**
 * Reset navigation states when switching between major breakpoints
 */
function resetNavigationStates() {
  // Close all dropdowns
  document.querySelectorAll('.dropdown-menu.show, .dropdown-submenu-menu.show').forEach(menu => {
    menu.classList.remove('show');
    const toggle = menu.previousElementSibling;
    if (toggle) {
      toggle.setAttribute('aria-expanded', 'false');
    }
  });
  
  // Reset search collapse
  const searchCollapse = document.querySelector('.search-collapse.show');
  if (searchCollapse) {
    searchCollapse.classList.remove('show', 'closing');
    const searchToggle = document.querySelector('.search-toggle');
    if (searchToggle) {
      searchToggle.setAttribute('aria-expanded', 'false');
    }
  }
  
  // Reset navbar collapse
  const navbarCollapse = document.querySelector('.navbar-collapse.show');
  if (navbarCollapse && window.innerWidth >= 768) {
    navbarCollapse.classList.remove('show', 'closing');
    const navbarToggler = document.querySelector('.navbar-toggler');
    if (navbarToggler) {
      navbarToggler.setAttribute('aria-expanded', 'false');
    }
  }
}

/**
 * Optimize interface for mobile devices (< 576px)
 */
function optimizeForMobile() {
  // Ensure touch-friendly spacing
  const buttons = document.querySelectorAll('.btn');
  buttons.forEach(btn => {
    if (!btn.classList.contains('btn-sm') && !btn.classList.contains('btn-lg')) {
      btn.style.minHeight = '3rem';
    }
  });
  
  // Optimize form controls
  const formControls = document.querySelectorAll('.form-control');
  formControls.forEach(control => {
    control.style.minHeight = '3rem';
  });
}

/**
 * Optimize interface for small tablets (576px - 768px)
 */
function optimizeForSmallTablet() {
  // Moderate touch targets
  const buttons = document.querySelectorAll('.btn');
  buttons.forEach(btn => {
    if (!btn.classList.contains('btn-sm') && !btn.classList.contains('btn-lg')) {
      btn.style.minHeight = '2.75rem';
    }
  });
}

/**
 * Optimize interface for tablets (768px - 992px)
 */
function optimizeForTablet() {
  // Reset mobile-specific styles
  const buttons = document.querySelectorAll('.btn');
  buttons.forEach(btn => {
    btn.style.minHeight = '';
  });
  
  const formControls = document.querySelectorAll('.form-control');
  formControls.forEach(control => {
    control.style.minHeight = '';
  });
}

/**
 * Optimize interface for desktop (992px - 1200px)
 */
function optimizeForDesktop() {
  // Enable hover effects and desktop-specific features
  document.body.classList.add('desktop-mode');
}

/**
 * Optimize interface for large desktop (> 1200px)
 */
function optimizeForLargeDesktop() {
  // Enable all desktop features
  document.body.classList.add('desktop-mode', 'large-desktop');
}

/**
 * Enhanced debounce function for better performance
 */
function debounce(func, wait, immediate) {
  let timeout;
  return function executedFunction() {
    const context = this;
    const args = arguments;
    const later = function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    const callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
}unce(function() {
    adjustForViewport();
    handleBreakpointTransitions();
  }, 250));
  
  // Initialize enhanced mobile navigation
  initEnhancedMobileNavigation();
  
  // Initialize responsive form optimizations
  initResponsiveFormOptimizations();
}

/**
 * Initialize enhanced mobile navigation behavior
 * Added as part of task 7.1 & 7.2: Enhance mobile navigation
 */
function initEnhancedMobileNavigation() {
  const navbarToggler = document.querySelector('.navbar-toggler');
  const navbarCollapse = document.querySelector('.navbar-collapse');
  
  if (navbarToggler && navbarCollapse) {
    // Enhanced toggler click behavior
    navbarToggler.addEventListener('click', function(e) {
      e.preventDefault();
      
      const isExpanded = this.getAttribute('aria-expanded') === 'true';
      
      if (isExpanded) {
        // Closing animation
        navbarCollapse.style.height = navbarCollapse.scrollHeight + 'px';
        navbarCollapse.classList.add('collapsing');
        navbarCollapse.classList.remove('show');
        
        // Force reflow
        navbarCollapse.offsetHeight;
        
        navbarCollapse.style.height = '0px';
        
        setTimeout(() => {
          navbarCollapse.classList.remove('collapsing');
          navbarCollapse.style.height = '';
          this.setAttribute('aria-expanded', 'false');
          
          // Announce to screen readers
          announceToScreenReader('Navigation menu closed');
        }, 350);
        
      } else {
        // Opening animation
        navbarCollapse.classList.add('collapsing');
        navbarCollapse.style.height = '0px';
        
        // Force reflow
        navbarCollapse.offsetHeight;
        
        navbarCollapse.style.height = navbarCollapse.scrollHeight + 'px';
        
        setTimeout(() => {
          navbarCollapse.classList.remove('collapsing');
          navbarCollapse.classList.add('show');
          navbarCollapse.style.height = '';
          this.setAttribute('aria-expanded', 'true');
          
          // Focus first navigation item for accessibility
          const firstNavLink = navbarCollapse.querySelector('.nav-link');
          if (firstNavLink) {
            firstNavLink.focus();
          }
          
          // Announce to screen readers
          announceToScreenReader('Navigation menu opened');
        }, 350);
      }
    });
    
    // Close navigation when clicking nav links on mobile
    const navLinks = navbarCollapse.querySelectorAll('.nav-link:not(.dropdown-toggle)');
    navLinks.forEach(link => {
      link.addEventListener('click', function() {
        if (window.innerWidth < 768 && navbarCollapse.classList.contains('show')) {
          // Trigger close animation
          navbarToggler.click();
        }
      });
    });
    
    // Enhanced swipe gesture support for mobile
    if ('ontouchstart' in window) {
      let startY = 0;
      let startX = 0;
      let isScrolling = false;
      
      navbarCollapse.addEventListener('touchstart', function(e) {
        startY = e.touches[0].clientY;
        startX = e.touches[0].clientX;
        isScrolling = false;
      }, { passive: true });
      
      navbarCollapse.addEventListener('touchmove', function(e) {
        if (!startY || !startX) return;
        
        const currentY = e.touches[0].clientY;
        const currentX = e.touches[0].clientX;
        const diffY = startY - currentY;
        const diffX = startX - currentX;
        
        // Determine if user is scrolling vertically or horizontally
        if (Math.abs(diffY) > Math.abs(diffX)) {
          isScrolling = true;
        }
        
        // If swiping up significantly and not scrolling, close menu
        if (!isScrolling && diffY > 50 && Math.abs(diffX) < 100) {
          if (navbarCollapse.classList.contains('show')) {
            navbarToggler.click();
          }
        }
      }, { passive: true });
      
      navbarCollapse.addEventListener('touchend', function() {
        startY = 0;
        startX = 0;
        isScrolling = false;
      }, { passive: true });
    }
  }
}

/**
 * Initialize responsive form optimizations
 * Added as part of task 7.3: Optimize form layouts for mobile
 */
function initResponsiveFormOptimizations() {
  // Enhance form inputs for mobile devices
  const formInputs = document.querySelectorAll('input, select, textarea');
  
  formInputs.forEach(input => {
    // Add mobile-specific input enhancements
    if (window.innerWidth <= 575) {
      // Prevent zoom on iOS when focusing inputs
      if (/iPad|iPhone|iPod/.test(navigator.userAgent)) {
        if (input.type === 'email' || input.type === 'tel' || input.type === 'url') {
          input.addEventListener('focus', function() {
            this.style.fontSize = '16px';
          });
          
          input.addEventListener('blur', function() {
            this.style.fontSize = '';
          });
        }
      }
      
      // Enhanced touch feedback for form controls
      input.addEventListener('touchstart', function() {
        this.classList.add('touch-active');
      }, { passive: true });
      
      input.addEventListener('touchend', function() {
        setTimeout(() => {
          this.classList.remove('touch-active');
        }, 150);
      }, { passive: true });
    }
  });
  
  // Optimize button touch targets
  const buttons = document.querySelectorAll('.btn');
  buttons.forEach(button => {
    if (window.innerWidth <= 575) {
      // Ensure minimum touch target size
      const rect = button.getBoundingClientRect();
      if (rect.height < 44) {
        button.style.minHeight = '44px';
        button.style.display = 'flex';
        button.style.alignItems = 'center';
        button.style.justifyContent = 'center';
      }
    }
  });
}

/**
 * Handle breakpoint transitions
 * Added as part of task 7.4: Test and refine breakpoint behavior
 */
function handleBreakpointTransitions() {
  const currentWidth = window.innerWidth;
  
  // Store previous breakpoint
  if (!window.previousBreakpoint) {
    window.previousBreakpoint = getBreakpoint(currentWidth);
  }
  
  const currentBreakpoint = getBreakpoint(currentWidth);
  
  // If breakpoint changed, trigger responsive adjustments
  if (window.previousBreakpoint !== currentBreakpoint) {
    // Reset navigation state when transitioning between mobile and desktop
    if ((window.previousBreakpoint === 'xs' || window.previousBreakpoint === 'sm') && 
        (currentBreakpoint === 'md' || currentBreakpoint === 'lg' || currentBreakpoint === 'xl')) {
      // Transitioning from mobile to desktop
      resetMobileNavigationState();
    } else if ((window.previousBreakpoint === 'md' || window.previousBreakpoint === 'lg' || window.previousBreakpoint === 'xl') && 
               (currentBreakpoint === 'xs' || currentBreakpoint === 'sm')) {
      // Transitioning from desktop to mobile
      resetDesktopNavigationState();
    }
    
    // Update form optimizations based on new breakpoint
    updateFormOptimizations(currentBreakpoint);
    
    // Update component layouts
    updateComponentLayouts(currentBreakpoint);
    
    // Announce breakpoint change to screen readers for debugging (remove in production)
    if (window.location.search.includes('debug=true')) {
      announceToScreenReader(`Breakpoint changed to ${currentBreakpoint}`);
    }
    
    window.previousBreakpoint = currentBreakpoint;
  }
}

/**
 * Get current breakpoint based on window width
 * Added as part of task 7.4: Test and refine breakpoint behavior
 */
function getBreakpoint(width) {
  if (width < 576) return 'xs';
  if (width < 768) return 'sm';
  if (width < 992) return 'md';
  if (width < 1200) return 'lg';
  return 'xl';
}

/**
 * Reset mobile navigation state
 * Added as part of task 7.4: Test and refine breakpoint behavior
 */
function resetMobileNavigationState() {
  const navbarCollapse = document.querySelector('.navbar-collapse');
  const navbarToggler = document.querySelector('.navbar-toggler');
  
  if (navbarCollapse && navbarToggler) {
    navbarCollapse.classList.remove('show', 'collapsing');
    navbarCollapse.style.height = '';
    navbarToggler.setAttribute('aria-expanded', 'false');
  }
  
  // Reset all dropdown states
  document.querySelectorAll('.dropdown-menu.show, .dropdown-submenu-menu.show').forEach(menu => {
    menu.classList.remove('show');
    const toggle = menu.previousElementSibling;
    if (toggle) {
      toggle.setAttribute('aria-expanded', 'false');
    }
  });
}

/**
 * Reset desktop navigation state
 * Added as part of task 7.4: Test and refine breakpoint behavior
 */
function resetDesktopNavigationState() {
  // Reset any desktop-specific states that shouldn't persist on mobile
  document.querySelectorAll('.dropdown').forEach(dropdown => {
    dropdown.touchCount = 0;
  });
}

/**
 * Update form optimizations based on breakpoint
 * Added as part of task 7.4: Test and refine breakpoint behavior
 */
function updateFormOptimizations(breakpoint) {
  const forms = document.querySelectorAll('form');
  
  forms.forEach(form => {
    if (breakpoint === 'xs' || breakpoint === 'sm') {
      // Mobile optimizations
      form.classList.add('form-mobile-optimized');
      
      // Stack form elements vertically
      const formRows = form.querySelectorAll('.form-row, .row');
      formRows.forEach(row => {
        row.classList.add('flex-mobile-column');
      });
      
    } else {
      // Desktop optimizations
      form.classList.remove('form-mobile-optimized');
      
      // Restore horizontal layout
      const formRows = form.querySelectorAll('.form-row, .row');
      formRows.forEach(row => {
        row.classList.remove('flex-mobile-column');
      });
    }
  });
}

/**
 * Update component layouts based on breakpoint
 * Added as part of task 7.4: Test and refine breakpoint behavior
 */
function updateComponentLayouts(breakpoint) {
  // Update card layouts
  const cardDecks = document.querySelectorAll('.card-deck');
  cardDecks.forEach(deck => {
    if (breakpoint === 'xs' || breakpoint === 'sm') {
      deck.classList.add('flex-mobile-column');
    } else {
      deck.classList.remove('flex-mobile-column');
    }
  });
  
  // Update table responsiveness
  const tables = document.querySelectorAll('.table');
  tables.forEach(table => {
    const wrapper = table.closest('.table-responsive');
    if (wrapper) {
      if (breakpoint === 'xs') {
        table.classList.add('table-stack');
      } else {
        table.classList.remove('table-stack');
      }
    }
  });
  
  // Update button groups
  const buttonGroups = document.querySelectorAll('.btn-group');
  buttonGroups.forEach(group => {
    if (breakpoint === 'xs') {
      group.classList.add('btn-group-vertical');
      group.classList.remove('btn-group');
    } else {
      group.classList.add('btn-group');
      group.classList.remove('btn-group-vertical');
    }
  });
}

/**
 * Adjust navbar elements based on viewport size
 * Enhanced as part of task 7.1 & 7.4: Improve responsive behavior
 */
function adjustForViewport() {
  const currentBreakpoint = getBreakpoint(window.innerWidth);
  
  // Adjust search form visibility and behavior
  const searchContainer = document.querySelector('.search-container');
  if (searchContainer) {
    if (currentBreakpoint === 'xs' || currentBreakpoint === 'sm') {
      // Mobile: Show search toggle, hide inline search
      const searchToggle = searchContainer.querySelector('.search-toggle');
      const searchForm = searchContainer.querySelector('.search-form');
      
      if (searchToggle) searchToggle.style.display = 'block';
      if (searchForm) searchForm.style.display = 'none';
    } else {
      // Desktop: Show inline search, hide search toggle
      const searchToggle = searchContainer.querySelector('.search-toggle');
      const searchForm = searchContainer.querySelector('.search-form');
      
      if (searchToggle) searchToggle.style.display = 'none';
      if (searchForm) searchForm.style.display = 'flex';
    }
  }
  
  // Adjust navigation item spacing
  const navItems = document.querySelectorAll('.navbar-nav .nav-item');
  navItems.forEach(item => {
    if (currentBreakpoint === 'md') {
      // Reduce spacing on medium screens
      item.style.marginLeft = '0.25rem';
      item.style.marginRight = '0.25rem';
    } else {
      // Reset to default spacing
      item.style.marginLeft = '';
      item.style.marginRight = '';
    }
  });
  
  // Adjust dropdown menu positioning
  const dropdownMenus = document.querySelectorAll('.dropdown-menu');
  dropdownMenus.forEach(menu => {
    if (currentBreakpoint === 'xs' || currentBreakpoint === 'sm') {
      // Mobile: Full width dropdowns
      menu.style.width = '100%';
      menu.style.left = '0';
      menu.style.right = '0';
    } else {
      // Desktop: Auto width dropdowns
      menu.style.width = '';
      menu.style.left = '';
      menu.style.right = '';
    }
  });
} on current viewport size
 */
function adjustForViewport() {
  const isMobile = window.innerWidth < 768;
  const navbar = document.querySelector('.navbar');
  
  if (navbar) {
    // Apply specific classes based on viewport
    if (isMobile) {
      navbar.classList.add('navbar-mobile');
      navbar.classList.remove('navbar-desktop');
    } else {
      navbar.classList.add('navbar-desktop');
      navbar.classList.remove('navbar-mobile');
      
      // Reset any mobile-specific states
      document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
        if (!menu.closest('.dropdown').matches(':hover')) {
          menu.classList.remove('show');
        }
      });
      
      // Reset mobile search if it exists
      const searchCollapse = document.querySelector('.search-collapse');
      if (searchCollapse) {
        searchCollapse.classList.remove('show');
      }
    }
  }
}

/**
 * Enhance accessibility for the navbar
 */
function enhanceAccessibility() {
  // Add appropriate ARIA attributes to main dropdowns
  const dropdowns = document.querySelectorAll('.dropdown');
  
  dropdowns.forEach((dropdown, index) => {
    const toggle = dropdown.querySelector('.dropdown-toggle');
    const menu = dropdown.querySelector('.dropdown-menu');
    
    if (toggle && menu) {
      // Generate unique IDs if not already present
      const toggleId = toggle.id || `navbar-dropdown-toggle-${index}`;
      const menuId = menu.id || `navbar-dropdown-menu-${index}`;
      
      // Set IDs if not already present
      if (!toggle.id) toggle.id = toggleId;
      if (!menu.id) menu.id = menuId;
      
      // Set ARIA attributes
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-haspopup', 'true');
      toggle.setAttribute('aria-controls', menuId);
      
      menu.setAttribute('aria-labelledby', toggleId);
      
      // Update ARIA attributes on toggle
      toggle.addEventListener('click', function() {
        const expanded = menu.classList.contains('show');
        toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
      });
    }
  });
  
  // Add appropriate ARIA attributes to submenu dropdowns
  const submenuDropdowns = document.querySelectorAll('.dropdown-submenu');
  
  submenuDropdowns.forEach((submenu, index) => {
    const toggle = submenu.querySelector('.dropdown-item.dropdown-toggle');
    const menu = submenu.querySelector('.dropdown-submenu-menu');
    
    if (toggle && menu) {
      // Generate unique IDs if not already present
      const toggleId = toggle.id || `navbar-submenu-toggle-${index}`;
      const menuId = menu.id || `navbar-submenu-menu-${index}`;
      
      // Set IDs if not already present
      if (!toggle.id) toggle.id = toggleId;
      if (!menu.id) menu.id = menuId;
      
      // Set ARIA attributes
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-haspopup', 'true');
      toggle.setAttribute('aria-controls', menuId);
      
      menu.setAttribute('aria-labelledby', toggleId);
      
      // Update ARIA attributes on toggle
      toggle.addEventListener('click', function() {
        const expanded = menu.classList.contains('show');
        toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
      });
    }
  });
  
  // Ensure all interactive elements are keyboard accessible
  const interactiveElements = document.querySelectorAll('.navbar button, .navbar a');
  interactiveElements.forEach(el => {
    if (!el.getAttribute('tabindex')) {
      el.setAttribute('tabindex', '0');
    }
  });
  
  // Add keyboard navigation for dropdowns
  enhanceKeyboardNavigation();
}

/**
 * Enhance keyboard navigation for the navbar
 */
function enhanceKeyboardNavigation() {
  // Handle keyboard navigation for main dropdown menus
  const dropdownToggles = document.querySelectorAll('.navbar-nav > .nav-item > .dropdown-toggle');
  
  dropdownToggles.forEach(toggle => {
    toggle.addEventListener('keydown', function(e) {
      // Open dropdown on Enter or Space
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        
        const dropdownMenu = this.nextElementSibling;
        if (dropdownMenu) {
          const isExpanded = dropdownMenu.classList.contains('show');
          
          if (!isExpanded) {
            // Close other dropdowns
            document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
              menu.classList.remove('show');
              const otherToggle = menu.previousElementSibling;
              if (otherToggle) {
                otherToggle.setAttribute('aria-expanded', 'false');
              }
            });
            
            // Open this dropdown
            dropdownMenu.classList.add('show');
            this.setAttribute('aria-expanded', 'true');
            
            // Focus first item in dropdown
            const firstItem = dropdownMenu.querySelector('a');
            if (firstItem) {
              setTimeout(() => {
                firstItem.focus();
              }, 100);
            }
          } else {
            // Close this dropdown
            dropdownMenu.classList.remove('show');
            this.setAttribute('aria-expanded', 'false');
          }
        }
      }
      
      // Arrow down to navigate into dropdown
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        
        const dropdownMenu = this.nextElementSibling;
        if (dropdownMenu) {
          dropdownMenu.classList.add('show');
          this.setAttribute('aria-expanded', 'true');
          
          const firstItem = dropdownMenu.querySelector('a');
          if (firstItem) {
            firstItem.focus();
          }
        }
      }
    });
  });
  
  // Handle keyboard navigation for submenu toggles
  const submenuToggles = document.querySelectorAll('.dropdown-submenu > .dropdown-item.dropdown-toggle');
  
  submenuToggles.forEach(toggle => {
    toggle.addEventListener('keydown', function(e) {
      // Open submenu on Enter, Space, or Right Arrow
      if (e.key === 'Enter' || e.key === ' ' || e.key === 'ArrowRight') {
        e.preventDefault();
        
        const submenu = this.nextElementSibling;
        if (submenu) {
          const isExpanded = submenu.classList.contains('show');
          
          if (!isExpanded) {
            // Close other submenus at the same level
            const parentMenu = this.closest('.dropdown-menu');
            if (parentMenu) {
              parentMenu.querySelectorAll('.dropdown-submenu-menu.show').forEach(menu => {
                if (menu !== submenu) {
                  menu.classList.remove('show');
                  const otherToggle = menu.previousElementSibling;
                  if (otherToggle) {
                    otherToggle.setAttribute('aria-expanded', 'false');
                  }
                }
              });
            }
            
            // Open this submenu
            submenu.classList.add('show');
            this.setAttribute('aria-expanded', 'true');
            
            // Focus first item in submenu
            const firstItem = submenu.querySelector('a');
            if (firstItem) {
              setTimeout(() => {
                firstItem.focus();
              }, 100);
            }
          } else if (e.key === 'ArrowRight') {
            // If already expanded and right arrow pressed, focus first item
            const firstItem = submenu.querySelector('a');
            if (firstItem) {
              firstItem.focus();
            }
          } else {
            // Close this submenu on Enter or Space if already open
            submenu.classList.remove('show');
            this.setAttribute('aria-expanded', 'false');
          }
        }
      }
      
      // Left arrow to close submenu and return focus to parent
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        
        const submenu = this.nextElementSibling;
        if (submenu && submenu.classList.contains('show')) {
          submenu.classList.remove('show');
          this.setAttribute('aria-expanded', 'false');
        }
        
        // Focus on parent menu item if available
        const parentMenu = this.closest('.dropdown-menu');
        if (parentMenu) {
          const parentItem = parentMenu.previousElementSibling;
          if (parentItem) {
            parentItem.focus();
          }
        }
      }
    });
  });
  
  // Handle keyboard navigation within all dropdown menus (main and submenu)
  const dropdownItems = document.querySelectorAll('.dropdown-menu a');
  
  dropdownItems.forEach(item => {
    item.addEventListener('keydown', function(e) {
      const parentMenu = this.closest('.dropdown-menu');
      const isSubmenuItem = this.closest('.dropdown-submenu-menu') !== null;
      
      // Arrow down to next item
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        
        const nextItem = this.parentNode.nextElementSibling;
        if (nextItem) {
          const link = nextItem.querySelector('a');
          if (link) {
            link.focus();
          }
        }
      }
      
      // Arrow up to previous item
      if (e.key === 'ArrowUp') {
        e.preventDefault();
        
        const prevItem = this.parentNode.previousElementSibling;
        if (prevItem) {
          const link = prevItem.querySelector('a');
          if (link) {
            link.focus();
          }
        } else {
          // If no previous item, go back to toggle
          const toggle = parentMenu.previousElementSibling;
          if (toggle) {
            toggle.focus();
          }
        }
      }
      
      // Right arrow to open submenu if this is a submenu toggle
      if (e.key === 'ArrowRight') {
        if (this.classList.contains('dropdown-toggle')) {
          e.preventDefault();
          
          const submenu = this.nextElementSibling;
          if (submenu) {
            submenu.classList.add('show');
            this.setAttribute('aria-expanded', 'true');
            
            const firstItem = submenu.querySelector('a');
            if (firstItem) {
              firstItem.focus();
            }
          }
        }
      }
      
      // Left arrow to close submenu and return to parent menu
      if (e.key === 'ArrowLeft' && isSubmenuItem) {
        e.preventDefault();
        
        const submenu = this.closest('.dropdown-submenu-menu');
        if (submenu) {
          submenu.classList.remove('show');
          
          const toggle = submenu.previousElementSibling;
          if (toggle) {
            toggle.setAttribute('aria-expanded', 'false');
            toggle.focus();
          }
        }
      }
      
      // Escape to close dropdown
      if (e.key === 'Escape') {
        e.preventDefault();
        
        if (isSubmenuItem) {
          // If in submenu, close just the submenu
          const submenu = this.closest('.dropdown-submenu-menu');
          if (submenu) {
            submenu.classList.remove('show');
            
            const toggle = submenu.previousElementSibling;
            if (toggle) {
              toggle.setAttribute('aria-expanded', 'false');
              toggle.focus();
            }
          }
        } else {
          // If in main dropdown, close the whole dropdown
          parentMenu.classList.remove('show');
          
          const toggle = parentMenu.previousElementSibling;
          if (toggle) {
            toggle.setAttribute('aria-expanded', 'false');
            toggle.focus();
          }
        }
      }
    });
  });
}

/**
 * Initialize scroll effect for the navbar
 */
function initScrollEffect() {
  const navbar = document.querySelector('.navbar-custom');
  if (navbar) {
    // Initial check on page load
    checkScrollPosition();
    
    // Listen for scroll events
    window.addEventListener('scroll', debounce(function() {
      checkScrollPosition();
    }, 100));
    
    // Function to check scroll position and apply/remove class
    function checkScrollPosition() {
      if (window.scrollY > 50) {
        navbar.classList.add('navbar-scrolled');
      } else {
        navbar.classList.remove('navbar-scrolled');
      }
    }
  }
}

/**
 * Debounce function to limit how often a function can be called
 */
function debounce(func, wait) {
  let timeout;
  return function() {
    const context = this;
    const args = arguments;
    clearTimeout(timeout);
    timeout = setTimeout(function() {
      func.apply(context, args);
    }, wait);
  };
}/**
 
* Handle search form submission
 * Added as part of task 6.2: Add search form submission handling
 */
document.addEventListener('DOMContentLoaded', function() {
  // Initialize search form submission handling
  initSearchFormSubmission();
});

/**
 * Initialize search form submission handling
 */
function initSearchFormSubmission() {
  const searchForms = document.querySelectorAll('.search-form');
  
  searchForms.forEach(form => {
    form.addEventListener('submit', function(e) {
      const searchInput = form.querySelector('input[type="search"]');
      
      // Only submit if search input has value
      if (!searchInput || !searchInput.value.trim()) {
        e.preventDefault();
        
        // Add shake animation to indicate empty search
        searchInput.classList.add('shake-animation');
        setTimeout(() => {
          searchInput.classList.remove('shake-animation');
        }, 500);
        
        // Focus the input
        searchInput.focus();
      } else {
        // Track search analytics if needed
        if (typeof gtag === 'function') {
          gtag('event', 'search', {
            search_term: searchInput.value.trim()
          });
        }
        
        // If search results page doesn't exist yet, prevent default and show message
        if (!window.searchResultsPageExists) {
          // This can be removed once search results page is implemented
          // Uncomment the line below when search functionality is ready
          // e.preventDefault();
          // console.log('Search functionality will be implemented soon');
        }
      }
    });
  });
  
  // Add conditional rendering for search component based on URL
  const currentPath = window.location.pathname;
  const searchContainer = document.querySelector('.search-container');
  const mobileSearchToggle = document.querySelector('.d-md-none .search-toggle');
  
  // Hide search on specific pages if needed
  // Example: Hide search on login/register pages
  if (currentPath === '/login' || currentPath === '/register') {
    if (searchContainer) {
      searchContainer.style.display = 'none';
    }
    if (mobileSearchToggle) {
      mobileSearchToggle.style.display = 'none';
    }
  }
}

// Add CSS for shake animation
document.addEventListener('DOMContentLoaded', function() {
  const style = document.createElement('style');
  style.textContent = `
    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
      20%, 40%, 60%, 80% { transform: translateX(5px); }
    }
    .shake-animation {
      animation: shake 0.5s cubic-bezier(.36,.07,.19,.97) both;
    }
  `;
  document.head.appendChild(style);
});/**
 *
 Enhance keyboard navigation for better accessibility
 * Added as part of task 8.2: Test and fix accessibility issues
 */
function enhanceKeyboardNavigation() {
  // Add keyboard navigation for dropdown menus
  const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
  
  dropdownToggles.forEach(toggle => {
    // Handle arrow key navigation
    toggle.addEventListener('keydown', function(e) {
      const dropdownMenu = this.nextElementSibling;
      
      // Open dropdown and focus first item on arrow down
      if (e.key === 'ArrowDown' || e.key === 'Down') {
        e.preventDefault();
        
        if (!dropdownMenu.classList.contains('show')) {
          dropdownMenu.classList.add('show');
          this.setAttribute('aria-expanded', 'true');
        }
        
        // Focus first item in dropdown
        const firstItem = dropdownMenu.querySelector('a');
        if (firstItem) {
          firstItem.focus();
        }
      }
      
      // Close dropdown on escape
      if (e.key === 'Escape') {
        if (dropdownMenu.classList.contains('show')) {
          dropdownMenu.classList.remove('show');
          this.setAttribute('aria-expanded', 'false');
          this.focus(); // Return focus to toggle
        }
      }
      
      // Handle space or enter to toggle dropdown
      if (e.key === ' ' || e.key === 'Enter') {
        e.preventDefault();
        
        if (dropdownMenu.classList.contains('show')) {
          dropdownMenu.classList.remove('show');
          this.setAttribute('aria-expanded', 'false');
        } else {
          dropdownMenu.classList.add('show');
          this.setAttribute('aria-expanded', 'true');
          
          // Focus first item in dropdown
          setTimeout(() => {
            const firstItem = dropdownMenu.querySelector('a');
            if (firstItem) {
              firstItem.focus();
            }
          }, 100);
        }
      }
    });
  });
  
  // Add keyboard navigation within dropdown menus
  const dropdownMenus = document.querySelectorAll('.dropdown-menu');
  
  dropdownMenus.forEach(menu => {
    const menuItems = menu.querySelectorAll('a.dropdown-item');
    
    menuItems.forEach((item, index) => {
      item.addEventListener('keydown', function(e) {
        // Navigate to next item on arrow down
        if (e.key === 'ArrowDown' || e.key === 'Down') {
          e.preventDefault();
          
          if (index < menuItems.length - 1) {
            menuItems[index + 1].focus();
          } else {
            // Wrap to first item
            menuItems[0].focus();
          }
        }
        
        // Navigate to previous item on arrow up
        if (e.key === 'ArrowUp' || e.key === 'Up') {
          e.preventDefault();
          
          if (index > 0) {
            menuItems[index - 1].focus();
          } else {
            // Wrap to last item
            menuItems[menuItems.length - 1].focus();
          }
        }
        
        // Close dropdown and return focus to toggle on escape
        if (e.key === 'Escape') {
          e.preventDefault();
          
          const dropdown = item.closest('.dropdown');
          if (dropdown) {
            const toggle = dropdown.querySelector('.dropdown-toggle');
            const dropdownMenu = dropdown.querySelector('.dropdown-menu');
            
            if (toggle && dropdownMenu) {
              dropdownMenu.classList.remove('show');
              toggle.setAttribute('aria-expanded', 'false');
              toggle.focus();
            }
          }
        }
        
        // Handle submenu navigation
        if ((e.key === 'ArrowRight' || e.key === 'Right') && item.classList.contains('dropdown-toggle')) {
          e.preventDefault();
          
          const submenu = item.nextElementSibling;
          if (submenu && submenu.classList.contains('dropdown-submenu-menu')) {
            submenu.classList.add('show');
            item.setAttribute('aria-expanded', 'true');
            
            // Focus first item in submenu
            const firstSubmenuItem = submenu.querySelector('a');
            if (firstSubmenuItem) {
              firstSubmenuItem.focus();
            }
          }
        }
        
        // Handle navigation back to parent menu
        if (e.key === 'ArrowLeft' || e.key === 'Left') {
          e.preventDefault();
          
          const submenu = item.closest('.dropdown-submenu-menu');
          if (submenu) {
            const parentToggle = submenu.previousElementSibling;
            if (parentToggle) {
              submenu.classList.remove('show');
              parentToggle.setAttribute('aria-expanded', 'false');
              parentToggle.focus();
            }
          }
        }
        
        // Close current dropdown level on Tab if it's the last item
        if (e.key === 'Tab' && !e.shiftKey && index === menuItems.length - 1) {
          const dropdown = item.closest('.dropdown');
          if (dropdown) {
            setTimeout(() => {
              const dropdownMenu = dropdown.querySelector('.dropdown-menu');
              const toggle = dropdown.querySelector('.dropdown-toggle');
              
              // Check if focus has moved outside the dropdown
              if (dropdownMenu && !dropdownMenu.contains(document.activeElement) && document.activeElement !== toggle) {
                dropdownMenu.classList.remove('show');
                if (toggle) {
                  toggle.setAttribute('aria-expanded', 'false');
                }
              }
            }, 10);
          }
        }
        
        // Close current dropdown level on Shift+Tab if it's the first item
        if (e.key === 'Tab' && e.shiftKey && index === 0) {
          const dropdown = item.closest('.dropdown');
          if (dropdown) {
            setTimeout(() => {
              const dropdownMenu = dropdown.querySelector('.dropdown-menu');
              const toggle = dropdown.querySelector('.dropdown-toggle');
              
              // Check if focus has moved outside the dropdown
              if (dropdownMenu && !dropdownMenu.contains(document.activeElement) && document.activeElement !== toggle) {
                dropdownMenu.classList.remove('show');
                if (toggle) {
                  toggle.setAttribute('aria-expanded', 'false');
                }
              }
            }, 10);
          }
        }
      });
    });
  });
  
  // Enhance search toggle keyboard accessibility
  const searchToggle = document.querySelector('.search-toggle');
  if (searchToggle) {
    searchToggle.addEventListener('keydown', function(e) {
      // Toggle search on Enter or Space
      if (e.key === ' ' || e.key === 'Enter') {
        e.preventDefault();
        this.click(); // Trigger the click event
      }
    });
  }
  
  // Add focus trap for mobile search
  const mobileSearchCollapse = document.querySelector('.search-collapse');
  if (mobileSearchCollapse) {
    const searchInput = mobileSearchCollapse.querySelector('input[type="search"]');
    const searchButton = mobileSearchCollapse.querySelector('button[type="submit"]');
    
    if (searchInput && searchButton) {
      // Trap focus within search form when open
      searchInput.addEventListener('keydown', function(e) {
        if (e.key === 'Tab' && e.shiftKey) {
          e.preventDefault();
          searchButton.focus();
        }
      });
      
      searchButton.addEventListener('keydown', function(e) {
        if (e.key === 'Tab' && !e.shiftKey) {
          e.preventDefault();
          searchInput.focus();
        }
      });
    }
  }
  
  // Add skip link for keyboard users to bypass navigation
  addSkipToContentLink();
}

/**
 * Add a skip to content link for keyboard users
 * Added as part of task 8.2: Test and fix accessibility issues
 */
function addSkipToContentLink() {
  // Check if skip link already exists
  if (document.getElementById('skip-to-content')) {
    return;
  }
  
  // Create skip link
  const skipLink = document.createElement('a');
  skipLink.id = 'skip-to-content';
  skipLink.href = '#main-content';
  skipLink.textContent = 'Skip to main content';
  skipLink.className = 'skip-link';
  
  // Add styles for skip link
  const style = document.createElement('style');
  style.textContent = `
    .skip-link {
      position: absolute;
      top: -40px;
      left: 0;
      background: #2FA4E7;
      color: white;
      padding: 8px;
      z-index: 100;
      transition: top 0.3s ease;
    }
    
    .skip-link:focus {
      top: 0;
      outline: 2px solid white;
    }
  `;
  
  // Add skip link and styles to document
  document.head.appendChild(style);
  document.body.insertBefore(skipLink, document.body.firstChild);
  
  // Add id to main content if it doesn't exist
  const mainContent = document.querySelector('main');
  if (mainContent && !mainContent.id) {
    mainContent.id = 'main-content';
    mainContent.setAttribute('tabindex', '-1');
  }
}

/**
 * Add accessibility enhancements to the navbar
 */
function enhanceAccessibility() {
  // Set appropriate ARIA attributes for active items
  document.querySelectorAll('.navbar-nav .active').forEach(item => {
    const link = item.querySelector('.nav-link');
    if (link) {
      link.setAttribute('aria-current', 'page');
    }
  });
  
  // Ensure all interactive elements are keyboard accessible
  document.querySelectorAll('.navbar a, .navbar button').forEach(element => {
    if (!element.getAttribute('tabindex') && !element.hasAttribute('disabled')) {
      element.setAttribute('tabindex', '0');
    }
  });
  
  // Add appropriate roles to dropdown menus if not already set
  document.querySelectorAll('.dropdown-menu').forEach(menu => {
    if (!menu.getAttribute('role')) {
      menu.setAttribute('role', 'menu');
    }
    
    // Ensure dropdown items have appropriate roles
    menu.querySelectorAll('.dropdown-item').forEach(item => {
      if (!item.getAttribute('role')) {
        item.setAttribute('role', 'menuitem');
      }
    });
  });
  
  // Add appropriate ARIA attributes to dropdown toggles
  document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
    if (!toggle.getAttribute('aria-haspopup')) {
      toggle.setAttribute('aria-haspopup', 'true');
    }
    
    if (!toggle.getAttribute('aria-expanded')) {
      toggle.setAttribute('aria-expanded', 'false');
    }
  });
  
  // Add focus management for dropdowns
  document.querySelectorAll('.dropdown').forEach(dropdown => {
    const toggle = dropdown.querySelector('.dropdown-toggle');
    const menu = dropdown.querySelector('.dropdown-menu');
    
    if (toggle && menu) {
      // Close dropdown when focus leaves
      document.addEventListener('focusin', function(e) {
        // If dropdown is open and focus moves outside dropdown
        if (menu.classList.contains('show') && !dropdown.contains(e.target)) {
          menu.classList.remove('show');
          toggle.setAttribute('aria-expanded', 'false');
        }
      });
    }
  });
  
  // Add ARIA live region for dynamic content
  const liveRegion = document.createElement('div');
  liveRegion.id = 'navbar-live-region';
  liveRegion.className = 'sr-only';
  liveRegion.setAttribute('aria-live', 'polite');
  liveRegion.setAttribute('aria-atomic', 'true');
  document.body.appendChild(liveRegion);
  
  // Ensure proper focus indication
  const focusStyle = document.createElement('style');
  focusStyle.textContent = `
    .navbar a:focus, .navbar button:focus {
      outline: 2px solid rgba(255, 255, 255, 0.5);
      outline-offset: 2px;
    }
    
    .dropdown-menu a:focus {
      outline: 2px solid rgba(47, 164, 231, 0.5);
      outline-offset: -2px;
    }
    
    @media (forced-colors: active) {
      .navbar a:focus, .navbar button:focus, .dropdown-menu a:focus {
        outline: 2px solid CanvasText;
      }
    }
  `;
  document.head.appendChild(focusStyle);
}

/**
 * Utility function to debounce function calls
 */
function debounce(func, wait) {
  let timeout;
  return function() {
    const context = this;
    const args = arguments;
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(context, args), wait);
  };
}/*
*
 * Detect keyboard navigation to enhance focus styles
 * Added as part of task 8.2: Test and fix accessibility issues
 */
document.addEventListener('DOMContentLoaded', function() {
  // Add class to body when using keyboard navigation
  let usingKeyboard = false;
  
  // Add keyboard class on Tab key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Tab') {
      usingKeyboard = true;
      document.body.classList.add('keyboard-nav');
    }
  });
  
  // Remove keyboard class on mouse use
  document.addEventListener('mousedown', function() {
    usingKeyboard = false;
    document.body.classList.remove('keyboard-nav');
  });
  
  // Add keyboard trap for modal dialogs
  const trapFocusInModal = function(modal) {
    if (!modal) return;
    
    const focusableElements = modal.querySelectorAll(
      'a[href], button, textarea, input[type="text"], input[type="search"], input[type="radio"], input[type="checkbox"], select'
    );
    
    if (focusableElements.length === 0) return;
    
    const firstElement = focusableElements[0];
    const lastElement = focusableElements[focusableElements.length - 1];
    
    // Trap focus in modal
    modal.addEventListener('keydown', function(e) {
      if (e.key === 'Tab') {
        // Shift + Tab on first element should focus last element
        if (e.shiftKey && document.activeElement === firstElement) {
          e.preventDefault();
          lastElement.focus();
        }
        // Tab on last element should focus first element
        else if (!e.shiftKey && document.activeElement === lastElement) {
          e.preventDefault();
          firstElement.focus();
        }
      }
      
      // Close modal on Escape
      if (e.key === 'Escape') {
        // Find close button and click it
        const closeButton = modal.querySelector('[data-dismiss="modal"]');
        if (closeButton) {
          closeButton.click();
        }
      }
    });
  };
  
  // Apply focus trap to any modals
  document.querySelectorAll('.modal').forEach(trapFocusInModal);
  
  // Announce page changes for screen readers
  const announcePageChange = function() {
    const pageTitle = document.title;
    const liveRegion = document.getElementById('navbar-live-region');
    
    if (liveRegion) {
      liveRegion.textContent = 'Navigated to ' + pageTitle;
      
      // Clear announcement after screen readers have time to read it
      setTimeout(function() {
        liveRegion.textContent = '';
      }, 3000);
    }
  };
  
  // Listen for navigation events
  window.addEventListener('popstate', announcePageChange);
  document.addEventListener('navigation:complete', announcePageChange);
  
  // Add focus management for modals
  document.addEventListener('shown.bs.modal', function(e) {
    // Focus first focusable element in modal
    const modal = e.target;
    const focusableElement = modal.querySelector(
      'a[href], button:not([disabled]), textarea, input[type="text"], input[type="search"], input[type="radio"], input[type="checkbox"], select'
    );
    
    if (focusableElement) {
      focusableElement.focus();
    }
    
    // Apply focus trap
    trapFocusInModal(modal);
  });
  
  // Return focus after modal is closed
  document.addEventListener('hidden.bs.modal', function(e) {
    // Find the element that triggered the modal
    const trigger = document.querySelector('[data-target="#' + e.target.id + '"]') || 
                    document.querySelector('[href="#' + e.target.id + '"]');
    
    if (trigger) {
      trigger.focus();
    }
  });
  
  // Add ARIA attributes to any dynamically loaded content
  const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
      if (mutation.type === 'childList') {
        mutation.addedNodes.forEach(function(node) {
          if (node.nodeType === 1) { // Element node
            // Check for dropdown menus
            const dropdownMenus = node.querySelectorAll ? node.querySelectorAll('.dropdown-menu') : [];
            dropdownMenus.forEach(function(menu) {
              if (!menu.getAttribute('role')) {
                menu.setAttribute('role', 'menu');
              }
              
              // Set role for dropdown items
              menu.querySelectorAll('.dropdown-item').forEach(function(item) {
                if (!item.getAttribute('role')) {
                  item.setAttribute('role', 'menuitem');
                }
              });
            });
            
            // Check for dropdown toggles
            const dropdownToggles = node.querySelectorAll ? node.querySelectorAll('.dropdown-toggle') : [];
            dropdownToggles.forEach(function(toggle) {
              if (!toggle.getAttribute('aria-haspopup')) {
                toggle.setAttribute('aria-haspopup', 'true');
              }
              
              if (!toggle.getAttribute('aria-expanded')) {
                toggle.setAttribute('aria-expanded', 'false');
              }
            });
          }
        });
      }
    });
  });
  
  // Observe the document body for changes
  observer.observe(document.body, { childList: true, subtree: true });
});
/**

 * Initialize scroll effect for navbar
 * Enhanced as part of task 7.1: Improve navigation experience
 */
function initScrollEffect() {
  const navbar = document.querySelector('.navbar-custom');
  if (!navbar) return;
  
  let lastScrollTop = 0;
  let scrollTimeout;
  
  window.addEventListener('scroll', function() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    // Clear existing timeout
    clearTimeout(scrollTimeout);
    
    // Add scrolled class when scrolling down
    if (scrollTop > 50) {
      navbar.classList.add('navbar-scrolled');
    } else {
      navbar.classList.remove('navbar-scrolled');
    }
    
    // Hide/show navbar on scroll (mobile only)
    if (window.innerWidth <= 767) {
      if (scrollTop > lastScrollTop && scrollTop > 100) {
        // Scrolling down - hide navbar
        navbar.style.transform = 'translateY(-100%)';
      } else {
        // Scrolling up - show navbar
        navbar.style.transform = 'translateY(0)';
      }
    } else {
      // Always show navbar on desktop
      navbar.style.transform = 'translateY(0)';
    }
    
    lastScrollTop = scrollTop;
    
    // Reset navbar position after scroll stops
    scrollTimeout = setTimeout(() => {
      if (window.innerWidth <= 767) {
        navbar.style.transform = 'translateY(0)';
      }
    }, 1000);
  }, { passive: true });
}

/**
 * Enhance accessibility features
 * Enhanced as part of task 7.1: Improve navigation accessibility
 */
function enhanceAccessibility() {
  // Add skip navigation link
  const skipLink = document.createElement('a');
  skipLink.href = '#main-content';
  skipLink.textContent = 'Skip to main content';
  skipLink.className = 'sr-only sr-only-focusable';
  skipLink.style.cssText = `
    position: absolute;
    top: -40px;
    left: 6px;
    width: 1px;
    height: 1px;
    padding: 8px 16px;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    border: 0;
    z-index: 9999;
    background: #2FA4E7;
    color: white;
    text-decoration: none;
    border-radius: 4px;
  `;
  
  skipLink.addEventListener('focus', function() {
    this.style.cssText += `
      position: absolute;
      top: 6px;
      left: 6px;
      width: auto;
      height: auto;
      clip: auto;
      overflow: visible;
    `;
  });
  
  skipLink.addEventListener('blur', function() {
    this.style.cssText = `
      position: absolute;
      top: -40px;
      left: 6px;
      width: 1px;
      height: 1px;
      padding: 8px 16px;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      border: 0;
      z-index: 9999;
      background: #2FA4E7;
      color: white;
      text-decoration: none;
      border-radius: 4px;
    `;
  });
  
  document.body.insertBefore(skipLink, document.body.firstChild);
  
  // Enhance dropdown accessibility
  const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
  dropdownToggles.forEach(toggle => {
    // Ensure proper ARIA attributes
    if (!toggle.getAttribute('aria-haspopup')) {
      toggle.setAttribute('aria-haspopup', 'true');
    }
    if (!toggle.getAttribute('aria-expanded')) {
      toggle.setAttribute('aria-expanded', 'false');
    }
    
    // Add keyboard support
    toggle.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.click();
      }
    });
  });
  
  // Enhance form accessibility
  const formControls = document.querySelectorAll('.form-control');
  formControls.forEach(control => {
    // Associate labels with form controls
    const label = document.querySelector(`label[for="${control.id}"]`);
    if (!label && control.id) {
      const parentLabel = control.closest('label');
      if (parentLabel) {
        parentLabel.setAttribute('for', control.id);
      }
    }
    
    // Add required field indicators
    if (control.hasAttribute('required')) {
      const label = document.querySelector(`label[for="${control.id}"]`);
      if (label && !label.querySelector('.text-danger')) {
        const required = document.createElement('span');
        required.className = 'text-danger';
        required.textContent = ' *';
        required.setAttribute('aria-label', 'required');
        label.appendChild(required);
      }
    }
  });
}

/**
 * Enhance keyboard navigation
 * Enhanced as part of task 7.1: Improve navigation accessibility
 */
function enhanceKeyboardNavigation() {
  // Trap focus within mobile navigation when open
  const navbarCollapse = document.querySelector('.navbar-collapse');
  const navbarToggler = document.querySelector('.navbar-toggler');
  
  if (navbarCollapse && navbarToggler) {
    document.addEventListener('keydown', function(e) {
      // Only trap focus on mobile when navigation is open
      if (window.innerWidth < 768 && navbarCollapse.classList.contains('show')) {
        const focusableElements = navbarCollapse.querySelectorAll(
          'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
        );
        
        const firstElement = focusableElements[0];
        const lastElement = focusableElements[focusableElements.length - 1];
        
        if (e.key === 'Tab') {
          if (e.shiftKey) {
            // Shift + Tab
            if (document.activeElement === firstElement) {
              e.preventDefault();
              lastElement.focus();
            }
          } else {
            // Tab
            if (document.activeElement === lastElement) {
              e.preventDefault();
              firstElement.focus();
            }
          }
        }
        
        // Close navigation with Escape
        if (e.key === 'Escape') {
          navbarToggler.click();
          navbarToggler.focus();
        }
      }
    });
  }
  
  // Add arrow key navigation for dropdown menus
  const dropdownMenus = document.querySelectorAll('.dropdown-menu');
  dropdownMenus.forEach(menu => {
    const menuItems = menu.querySelectorAll('.dropdown-item:not(.disabled)');
    
    menuItems.forEach((item, index) => {
      item.addEventListener('keydown', function(e) {
        let nextIndex;
        
        switch (e.key) {
          case 'ArrowDown':
            e.preventDefault();
            nextIndex = (index + 1) % menuItems.length;
            menuItems[nextIndex].focus();
            break;
            
          case 'ArrowUp':
            e.preventDefault();
            nextIndex = (index - 1 + menuItems.length) % menuItems.length;
            menuItems[nextIndex].focus();
            break;
            
          case 'Home':
            e.preventDefault();
            menuItems[0].focus();
            break;
            
          case 'End':
            e.preventDefault();
            menuItems[menuItems.length - 1].focus();
            break;
            
          case 'Escape':
            e.preventDefault();
            const toggle = menu.previousElementSibling;
            if (toggle) {
              menu.classList.remove('show');
              toggle.setAttribute('aria-expanded', 'false');
              toggle.focus();
            }
            break;
        }
      });
    });
  });
}

/**
 * Debounce function to limit the rate of function execution
 * Enhanced as part of task 7.4: Optimize performance
 */
function debounce(func, wait, immediate) {
  let timeout;
  return function executedFunction() {
    const context = this;
    const args = arguments;
    
    const later = function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    
    const callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    
    if (callNow) func.apply(context, args);
  };
}

/**
 * Initialize enhanced touch support for better mobile experience
 * Added as part of task 7.1: Improve mobile navigation experience
 */
function initEnhancedTouchSupport() {
  // Add touch feedback to all interactive elements
  const interactiveElements = document.querySelectorAll('a, button, .btn, .nav-link, .dropdown-item');
  
  interactiveElements.forEach(element => {
    // Add touch start feedback
    element.addEventListener('touchstart', function() {
      this.classList.add('touch-feedback');
    }, { passive: true });
    
    // Remove touch feedback
    element.addEventListener('touchend', function() {
      setTimeout(() => {
        this.classList.remove('touch-feedback');
      }, 150);
    }, { passive: true });
    
    element.addEventListener('touchcancel', function() {
      this.classList.remove('touch-feedback');
    }, { passive: true });
  });
  
  // Prevent double-tap zoom on buttons
  const buttons = document.querySelectorAll('button, .btn');
  buttons.forEach(button => {
    button.addEventListener('touchend', function(e) {
      e.preventDefault();
      this.click();
    });
  });
}

// Initialize enhanced touch support if touch is available
if ('ontouchstart' in window || navigator.maxTouchPoints > 0) {
  document.addEventListener('DOMContentLoaded', initEnhancedTouchSupport);
}
/
**
 * Initialize scroll effect for navbar
 * Added as part of task 7.1: Improve mobile navigation experience
 */
function initScrollEffect() {
  const navbar = document.querySelector('.navbar-custom');
  if (!navbar) return;
  
  let lastScrollTop = 0;
  let scrollTimeout;
  
  window.addEventListener('scroll', function() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    // Clear existing timeout
    clearTimeout(scrollTimeout);
    
    // Add scrolled class when scrolling down
    if (scrollTop > 50) {
      navbar.classList.add('navbar-scrolled');
    } else {
      navbar.classList.remove('navbar-scrolled');
    }
    
    // Hide/show navbar on mobile when scrolling
    if (window.innerWidth < 768) {
      if (scrollTop > lastScrollTop && scrollTop > 100) {
        // Scrolling down - hide navbar
        navbar.style.transform = 'translateY(-100%)';
      } else {
        // Scrolling up - show navbar
        navbar.style.transform = 'translateY(0)';
      }
    } else {
      // Reset transform on desktop
      navbar.style.transform = '';
    }
    
    lastScrollTop = scrollTop;
    
    // Reset scroll state after scrolling stops
    scrollTimeout = setTimeout(() => {
      if (window.innerWidth < 768) {
        navbar.style.transform = 'translateY(0)';
      }
    }, 150);
  });
}

/**
 * Enhance accessibility features
 * Enhanced as part of task 7.1: Improve mobile navigation experience
 */
function enhanceAccessibility() {
  // Add skip links if not present
  if (!document.querySelector('.skip-link')) {
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.className = 'skip-link sr-only sr-only-focusable';
    skipLink.textContent = 'Skip to main content';
    document.body.insertBefore(skipLink, document.body.firstChild);
  }
  
  // Enhance dropdown accessibility
  const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
  dropdownToggles.forEach(toggle => {
    // Ensure proper ARIA attributes
    if (!toggle.getAttribute('aria-haspopup')) {
      toggle.setAttribute('aria-haspopup', 'true');
    }
    if (!toggle.getAttribute('aria-expanded')) {
      toggle.setAttribute('aria-expanded', 'false');
    }
    
    // Add keyboard support
    toggle.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.click();
      }
    });
  });
  
  // Enhance form accessibility
  const formControls = document.querySelectorAll('.form-control');
  formControls.forEach(control => {
    const label = document.querySelector(`label[for="${control.id}"]`);
    if (!label && control.getAttribute('placeholder')) {
      // Add aria-label if no label exists
      control.setAttribute('aria-label', control.getAttribute('placeholder'));
    }
  });
}

/**
 * Enhance keyboard navigation
 * Added as part of task 7.1: Improve mobile navigation experience
 */
function enhanceKeyboardNavigation() {
  // Trap focus in mobile menu when open
  const navbarCollapse = document.querySelector('.navbar-collapse');
  const navbarToggler = document.querySelector('.navbar-toggler');
  
  if (navbarCollapse && navbarToggler) {
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && navbarCollapse.classList.contains('show')) {
        // Close mobile menu on escape
        navbarToggler.click();
        navbarToggler.focus();
      }
      
      // Trap focus in mobile menu
      if (navbarCollapse.classList.contains('show') && window.innerWidth < 768) {
        const focusableElements = navbarCollapse.querySelectorAll(
          'a, button, input, textarea, select, [tabindex]:not([tabindex="-1"])'
        );
        
        if (focusableElements.length > 0) {
          const firstElement = focusableElements[0];
          const lastElement = focusableElements[focusableElements.length - 1];
          
          if (e.key === 'Tab') {
            if (e.shiftKey) {
              // Shift + Tab
              if (document.activeElement === firstElement) {
                e.preventDefault();
                lastElement.focus();
              }
            } else {
              // Tab
              if (document.activeElement === lastElement) {
                e.preventDefault();
                firstElement.focus();
              }
            }
          }
        }
      }
    });
  }
  
  // Add arrow key navigation for dropdowns
  const dropdownMenus = document.querySelectorAll('.dropdown-menu');
  dropdownMenus.forEach(menu => {
    const items = menu.querySelectorAll('.dropdown-item');
    
    items.forEach((item, index) => {
      item.addEventListener('keydown', function(e) {
        let nextIndex;
        
        switch (e.key) {
          case 'ArrowDown':
            e.preventDefault();
            nextIndex = (index + 1) % items.length;
            items[nextIndex].focus();
            break;
          case 'ArrowUp':
            e.preventDefault();
            nextIndex = (index - 1 + items.length) % items.length;
            items[nextIndex].focus();
            break;
          case 'Home':
            e.preventDefault();
            items[0].focus();
            break;
          case 'End':
            e.preventDefault();
            items[items.length - 1].focus();
            break;
        }
      });
    });
  });
}

// Initialize everything when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  initNavbar();
});