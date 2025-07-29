# ZPlantilla Blueprint - Standardized Template

## Overview

The `zplantilla` blueprint serves as a standardized template and component demonstration for developing new Flask blueprints in this application. It showcases best practices, UI components, and design patterns that should be followed when creating new features.

## Purpose

This blueprint is designed to:

1. **Demonstrate UI Components**: Show all available UI components from `templates/components/ui_components.html`
2. **Provide Templates**: Serve as copy-paste templates for common functionality
3. **Establish Standards**: Define consistent patterns for new blueprint development
4. **Test Components**: Validate that all UI components work correctly

## Template Files

### 1. `contact_form.html`
**Purpose**: Standard form template with validation

**Features**:
- Complete form validation (client-side and server-side)
- Bootstrap 4 form styling with Font Awesome icons
- Loading states and user feedback
- Responsive design
- Accessibility compliance

**Use Case**: Copy this template when creating forms in new blueprints

### 2. `pruebas.html`
**Purpose**: Component demonstration and testing

**Features**:
- Showcases all available UI components
- Interactive JavaScript examples
- Mermaid diagram integration
- Bootstrap grid layout examples
- Various component states and variations

**Use Case**: Reference for understanding available components and their usage

### 3. `route1.html`
**Purpose**: Standard blueprint template

**Features**:
- Hero section with feature introduction
- Configuration panel with form controls
- Dashboard with statistics and progress indicators
- Data table with CRUD operations
- Comprehensive JavaScript functionality
- Complete responsive design

**Use Case**: Starting template for new blueprint development

## How to Use This Template

### For New Blueprint Development

1. **Copy the Blueprint Structure**:
   ```bash
   cp -r blueprints/zplantilla blueprints/your_new_blueprint
   ```

2. **Rename Files**:
   - Rename `pruebas.py` to `your_blueprint.py`
   - Update blueprint name in the Python file
   - Update route imports

3. **Customize Templates**:
   - Modify `route1.html` as your main template
   - Adapt `contact_form.html` for your forms
   - Remove `pruebas.html` if not needed

4. **Update Routes**:
   - Modify route functions in the `routes/` directory
   - Update URL patterns and function names
   - Implement your specific business logic

### Component Usage Reference

All templates in this blueprint demonstrate proper usage of:

- **Cards**: `card()` and `icon_card()` macros
- **Buttons**: `button()`, `icon_button()`, `loading_button()` macros
- **Forms**: `input_group()`, `textarea_group()`, `select_group()` macros
- **Tables**: `table()` macro with responsive design
- **Alerts**: `alert()` macro for user feedback
- **Progress**: `progress_bar()` macro for status indicators

## Best Practices Demonstrated

### 1. Responsive Design
- Mobile-first approach
- Bootstrap 4 grid system usage
- Proper breakpoint handling

### 2. Accessibility
- ARIA labels and roles
- Semantic HTML structure
- Keyboard navigation support
- Screen reader compatibility

### 3. User Experience
- Loading states for async operations
- Form validation feedback
- Consistent iconography
- Intuitive navigation

### 4. Code Organization
- Modular template structure
- Reusable component macros
- Separation of concerns
- Clear documentation

## Styling Guidelines

### Colors (Cerulean Theme)
- Primary: `#2FA4E7` (Bootstrap primary)
- Success: `#73A839` (Bootstrap success)
- Info: `#033C73` (Bootstrap info)
- Warning: `#DD5600` (Bootstrap warning)
- Danger: `#C71C22` (Bootstrap danger)

### Icons (Font Awesome)
- Navigation: Use consistent icons across similar functions
- Actions: Standard icons for CRUD operations
- Status: Visual indicators for different states

### Layout Patterns
- Use Bootstrap 4 grid system
- Consistent spacing with utility classes
- Card-based content organization
- Responsive navigation patterns

## JavaScript Patterns

### Form Validation
```javascript
// Client-side validation example
function validateForm(formData) {
    let isValid = true;
    // Validation logic
    return isValid;
}
```

### Loading States
```javascript
// Button loading state example
function showLoadingState(button) {
    button.disabled = true;
    // Show spinner, update text
}
```

### Dynamic Content
```javascript
// Dynamic alert example
function showDynamicAlert(type, message) {
    // Create and display alert
}
```

## Integration with Main Application

This blueprint is registered in the main Flask application and accessible at:
- `/pruebas` - Component demonstration
- `/route1` - Standard template example
- `/contact` - Form example

## Development Workflow

1. **Start with zplantilla**: Use as reference for component usage
2. **Copy templates**: Use as starting point for new features
3. **Customize**: Adapt to specific requirements
4. **Test**: Ensure responsive design and accessibility
5. **Document**: Update comments and documentation

## Maintenance

This blueprint should be updated when:
- New UI components are added to `ui_components.html`
- Design patterns change
- Bootstrap or Font Awesome versions are updated
- New best practices are established

## Support

For questions about using this template or implementing new blueprints, refer to:
- Component documentation in `templates/components/ui_components.html`
- Design guidelines in `docs/style-guide.md`
- Responsive patterns in `docs/responsive-design-patterns.md`