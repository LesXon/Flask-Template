/**
 * UI Components JavaScript
 * Handles interactive functionality for the reusable UI components
 * Enhanced with accessibility features
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize accessibility features
    initAccessibilityFeatures();
    
    // Loading Button Functionality
    function initLoadingButtons() {
        const loadingButtons = document.querySelectorAll('button[data-loading-text]');
        
        loadingButtons.forEach(button => {
            button.addEventListener('click', function() {
                if (this.type === 'submit') {
                    showLoadingState(this);
                }
            });
            
            // Handle form submission
            const form = button.closest('form');
            if (form) {
                form.addEventListener('submit', function() {
                    showLoadingState(button);
                });
            }
        });
    }
    
    function showLoadingState(button) {
        const originalText = button.querySelector('.button-text').textContent;
        const loadingText = button.getAttribute('data-loading-text');
        const spinner = button.querySelector('.spinner-border');
        
        button.disabled = true;
        button.classList.add('loading');
        button.querySelector('.button-text').textContent = loadingText;
        
        if (spinner) {
            spinner.classList.remove('d-none');
        }
        
        // Store original text for potential reset
        button.setAttribute('data-original-text', originalText);
    }
    
    function hideLoadingState(button) {
        const originalText = button.getAttribute('data-original-text');
        const spinner = button.querySelector('.spinner-border');
        
        button.disabled = false;
        button.classList.remove('loading');
        
        if (originalText) {
            button.querySelector('.button-text').textContent = originalText;
        }
        
        if (spinner) {
            spinner.classList.add('d-none');
        }
    }
    
    // Auto-dismiss alerts after 5 seconds
    function initAutoDismissAlerts() {
        const dismissibleAlerts = document.querySelectorAll('.alert-dismissible');
        
        dismissibleAlerts.forEach(alert => {
            // Auto-dismiss after 5 seconds unless it's an error alert
            if (!alert.classList.contains('alert-danger')) {
                setTimeout(() => {
                    const closeButton = alert.querySelector('.close');
                    if (closeButton && alert.parentNode) {
                        closeButton.click();
                    }
                }, 5000);
            }
        });
    }
    
    // Form validation enhancement
    function initFormValidation() {
        const forms = document.querySelectorAll('form');
        
        forms.forEach(form => {
            const inputs = form.querySelectorAll('.form-control');
            
            inputs.forEach(input => {
                // Real-time validation feedback
                input.addEventListener('blur', function() {
                    validateInput(this);
                });
                
                input.addEventListener('input', function() {
                    // Clear invalid state when user starts typing
                    if (this.classList.contains('is-invalid')) {
                        this.classList.remove('is-invalid');
                        const feedback = this.parentNode.querySelector('.invalid-feedback');
                        if (feedback) {
                            feedback.style.display = 'none';
                        }
                    }
                });
            });
        });
    }
    
    function validateInput(input) {
        const value = input.value.trim();
        const isRequired = input.hasAttribute('required');
        const type = input.getAttribute('type');
        
        let isValid = true;
        let errorMessage = '';
        
        // Required field validation
        if (isRequired && !value) {
            isValid = false;
            errorMessage = 'This field is required.';
        }
        
        // Email validation
        if (type === 'email' && value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                isValid = false;
                errorMessage = 'Please enter a valid email address.';
            }
        }
        
        // Password validation (minimum 6 characters)
        if (type === 'password' && value && value.length < 6) {
            isValid = false;
            errorMessage = 'Password must be at least 6 characters long.';
        }
        
        // Update UI based on validation
        if (!isValid) {
            input.classList.add('is-invalid');
            showValidationError(input, errorMessage);
        } else {
            input.classList.remove('is-invalid');
            hideValidationError(input);
        }
        
        return isValid;
    }
    
    function showValidationError(input, message) {
        let feedback = input.parentNode.querySelector('.invalid-feedback');
        
        if (!feedback) {
            feedback = document.createElement('div');
            feedback.className = 'invalid-feedback';
            input.parentNode.appendChild(feedback);
        }
        
        feedback.textContent = message;
        feedback.style.display = 'block';
    }
    
    function hideValidationError(input) {
        const feedback = input.parentNode.querySelector('.invalid-feedback');
        if (feedback) {
            feedback.style.display = 'none';
        }
    }
    
    // Modal enhancement
    function initModalEnhancements() {
        const modals = document.querySelectorAll('.modal');
        
        modals.forEach(modal => {
            // Focus management
            modal.addEventListener('shown.bs.modal', function() {
                const firstInput = this.querySelector('input, textarea, select, button');
                if (firstInput) {
                    firstInput.focus();
                }
            });
            
            // Reset forms when modal is closed
            modal.addEventListener('hidden.bs.modal', function() {
                const form = this.querySelector('form');
                if (form) {
                    form.reset();
                    // Clear validation states
                    const invalidInputs = form.querySelectorAll('.is-invalid');
                    invalidInputs.forEach(input => {
                        input.classList.remove('is-invalid');
                    });
                    const feedbacks = form.querySelectorAll('.invalid-feedback');
                    feedbacks.forEach(feedback => {
                        feedback.style.display = 'none';
                    });
                }
            });
        });
    }
    
    // Tooltip initialization for icon buttons
    function initTooltips() {
        const tooltipElements = document.querySelectorAll('[title]');
        
        tooltipElements.forEach(element => {
            // Only initialize tooltips for buttons with icons
            if (element.tagName === 'BUTTON' && element.querySelector('i')) {
                element.setAttribute('data-toggle', 'tooltip');
                element.setAttribute('data-placement', 'top');
            }
        });
        
        // Initialize Bootstrap tooltips if available
        if (typeof $ !== 'undefined' && $.fn.tooltip) {
            $('[data-toggle="tooltip"]').tooltip();
        }
    }
    
    // Progress bar animation
    function animateProgressBars() {
        const progressBars = document.querySelectorAll('.progress-bar');
        
        progressBars.forEach(bar => {
            const width = bar.style.width;
            bar.style.width = '0%';
            
            setTimeout(() => {
                bar.style.width = width;
            }, 100);
        });
    }
    
    // Initialize all components
    initLoadingButtons();
    initAutoDismissAlerts();
    initFormValidation();
    initModalEnhancements();
    initTooltips();
    animateProgressBars();
    initKeyboardNavigation();
    initScreenReaderSupport();
    
    // Initialize accessibility features
    function initAccessibilityFeatures() {
        // Detect keyboard navigation
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Tab') {
                document.body.classList.add('keyboard-navigation');
            }
        });
        
        // Remove keyboard navigation class on mouse use
        document.addEventListener('mousedown', function() {
            document.body.classList.remove('keyboard-navigation');
        });
        
        // Announce dynamic content changes to screen readers
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                    mutation.addedNodes.forEach(function(node) {
                        if (node.nodeType === Node.ELEMENT_NODE) {
                            // Check if it's an alert or important message
                            if (node.classList && (node.classList.contains('alert') || node.getAttribute('role') === 'alert')) {
                                announceToScreenReader(node.textContent.trim());
                            }
                        }
                    });
                }
            });
        });
        
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    }
    
    // Enhanced keyboard navigation support
    function initKeyboardNavigation() {
        // Handle escape key for modals and dropdowns
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                // Close modals
                const openModal = document.querySelector('.modal.show');
                if (openModal) {
                    const closeButton = openModal.querySelector('[data-dismiss="modal"]');
                    if (closeButton) {
                        closeButton.click();
                    }
                }
                
                // Close dropdowns
                const openDropdowns = document.querySelectorAll('.dropdown-menu.show');
                openDropdowns.forEach(dropdown => {
                    dropdown.classList.remove('show');
                    const toggle = dropdown.previousElementSibling;
                    if (toggle) {
                        toggle.setAttribute('aria-expanded', 'false');
                        toggle.focus();
                    }
                });
                
                // Close alerts that are focusable
                const focusedAlert = document.activeElement;
                if (focusedAlert && focusedAlert.classList.contains('alert')) {
                    const closeButton = focusedAlert.querySelector('[data-dismiss="alert"]');
                    if (closeButton) {
                        closeButton.click();
                    }
                }
            }
        });
        
        // Enhanced focus management for form elements
        const formElements = document.querySelectorAll('input, textarea, select, button');
        formElements.forEach(element => {
            element.addEventListener('focus', function() {
                // Scroll element into view if needed
                this.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            });
        });
        
        // Arrow key navigation for dropdown menus
        document.addEventListener('keydown', function(e) {
            const activeElement = document.activeElement;
            
            if (activeElement && activeElement.classList.contains('dropdown-toggle')) {
                if (e.key === 'ArrowDown' || e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    const dropdown = activeElement.nextElementSibling;
                    if (dropdown && dropdown.classList.contains('dropdown-menu')) {
                        dropdown.classList.add('show');
                        activeElement.setAttribute('aria-expanded', 'true');
                        const firstItem = dropdown.querySelector('a, button');
                        if (firstItem) {
                            firstItem.focus();
                        }
                    }
                }
            }
            
            if (activeElement && activeElement.closest('.dropdown-menu')) {
                const dropdownMenu = activeElement.closest('.dropdown-menu');
                const items = Array.from(dropdownMenu.querySelectorAll('a, button'));
                const currentIndex = items.indexOf(activeElement);
                
                if (e.key === 'ArrowDown') {
                    e.preventDefault();
                    const nextIndex = (currentIndex + 1) % items.length;
                    items[nextIndex].focus();
                } else if (e.key === 'ArrowUp') {
                    e.preventDefault();
                    const prevIndex = currentIndex > 0 ? currentIndex - 1 : items.length - 1;
                    items[prevIndex].focus();
                }
            }
        });
    }
    
    // Screen reader support enhancements
    function initScreenReaderSupport() {
        // Create or get the screen reader announcements region
        let announcer = document.getElementById('sr-announcements');
        if (!announcer) {
            announcer = document.createElement('div');
            announcer.id = 'sr-announcements';
            announcer.setAttribute('aria-live', 'polite');
            announcer.setAttribute('aria-atomic', 'true');
            announcer.className = 'sr-only';
            document.body.appendChild(announcer);
        }
        
        // Announce form validation errors
        document.addEventListener('invalid', function(e) {
            const field = e.target;
            const label = document.querySelector(`label[for="${field.id}"]`);
            const fieldName = label ? label.textContent.trim() : field.name;
            
            setTimeout(() => {
                announceToScreenReader(`Validation error in ${fieldName}: ${field.validationMessage}`);
            }, 100);
        }, true);
        
        // Announce successful form submissions
        document.addEventListener('submit', function(e) {
            const form = e.target;
            if (form.checkValidity()) {
                announceToScreenReader('Form submitted successfully');
            }
        });
        
        // Announce loading states
        const loadingButtons = document.querySelectorAll('[data-loading-text]');
        loadingButtons.forEach(button => {
            button.addEventListener('click', function() {
                if (this.type === 'submit') {
                    setTimeout(() => {
                        announceToScreenReader(this.getAttribute('data-loading-text'));
                    }, 100);
                }
            });
        });
    }
    
    // Utility function to announce messages to screen readers
    function announceToScreenReader(message) {
        const announcer = document.getElementById('sr-announcements');
        if (announcer && message) {
            // Clear previous message
            announcer.textContent = '';
            
            // Set new message after a brief delay to ensure it's announced
            setTimeout(() => {
                announcer.textContent = message.trim();
            }, 100);
            
            // Clear the message after it's been announced
            setTimeout(() => {
                announcer.textContent = '';
            }, 3000);
        }
    }
    
    // Global utility functions
    window.UIComponents = {
        showLoadingState: showLoadingState,
        hideLoadingState: hideLoadingState,
        validateInput: validateInput,
        showValidationError: showValidationError,
        hideValidationError: hideValidationError,
        announceToScreenReader: announceToScreenReader
    };
});

// Utility function to create dynamic alerts
function showAlert(message, type = 'info', dismissible = true, container = 'body') {
    const alertHtml = `
        <div class="alert alert-${type} ${dismissible ? 'alert-dismissible' : ''} fade show" role="alert">
            ${message}
            ${dismissible ? '<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>' : ''}
        </div>
    `;
    
    const containerElement = document.querySelector(container);
    if (containerElement) {
        containerElement.insertAdjacentHTML('afterbegin', alertHtml);
        
        // Auto-dismiss after 5 seconds if not an error
        if (dismissible && type !== 'danger') {
            setTimeout(() => {
                const alert = containerElement.querySelector('.alert');
                if (alert) {
                    const closeButton = alert.querySelector('.close');
                    if (closeButton) {
                        closeButton.click();
                    }
                }
            }, 5000);
        }
    }
}

// Make showAlert globally available
window.showAlert = showAlert;