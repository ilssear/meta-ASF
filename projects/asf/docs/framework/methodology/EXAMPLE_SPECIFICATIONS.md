# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Project Specifications - AI_Test_WebApp: AI Testing Web Application

This document describes the requirements for a web-based AI testing application that allows users to test OpenAI models and neural network capabilities through a browser interface.

## Project Overview

Create a local web application that provides an interface for testing AI capabilities. Users should be able to run the application locally and access it through their web browser to perform different types of AI tests without needing command-line interaction.

The application serves as a demonstration platform for AI capabilities, making complex AI testing accessible through a simple web interface.

## Getting Started

### What You Need
- A computer with a web browser
- Basic understanding of how to use a web browser
- No coding experience required!

### How It Works
1. You'll run a simple command to start the application
2. Open your web browser and go to a local address (like `http://localhost:5000`)
3. Use the web interface to test AI models and neural networks
4. No need to use the command line or write any code!

## Core Requirements

### 1. Web Application Infrastructure

**Purpose**: Provide a local web server with browser-based interface

**Requirements**:
- Run locally on your computer
- Accessible through your web browser (localhost)
- Responsive interface that works on desktop browsers
- Clean, intuitive user interface
- Real-time feedback for long-running operations
- Error handling with user-friendly messages

**Expected Behavior**:
- Application starts with a simple command
- You can navigate to localhost URL to access interface
- All functionality accessible through web browser
- No command-line interaction required for testing
- Graceful handling of server errors and API failures

### 2. OpenAI Model Testing

**Purpose**: Allow users to test different OpenAI models with custom queries

**Requirements**:
- Model selection interface with at least 2 options (GPT-4o and GPT-o3)
- Text input area for user queries
- Submit functionality to send queries to selected model
- Display response from OpenAI API
- Show model used and response metadata (tokens, timing, etc.)
- Handle API errors gracefully

**User Workflow**:
1. Select desired OpenAI model from dropdown/radio buttons
2. Enter query text in input field
3. Click submit to send query
4. Application displays loading indicator while processing
5. Application shows response, model used, and metadata
6. You can submit additional queries or change models

**Expected Information Display**:
- Selected model name
- Your query (echoed back)
- AI response text
- Response time
- Token usage (if available)
- Error messages if API call fails

### 3. Neural Network Architecture Testing

**Purpose**: Generate and test a basic neural network on the server

**Requirements**:
- Generate a 4-layer deep neural network architecture
- Create and initialize the network on the server
- Test that the server can successfully run the model
- Display network architecture information
- Show test results (success/failure of model execution)
- Demonstrate basic forward pass functionality

**Architecture Specifications**:
- 4-layer deep network structure
- Appropriate for demonstration purposes
- Should work on both CPU and GPU (if available)
- Include basic activation functions
- Generate synthetic test data for validation

**Expected Behavior**:
- Click button to generate network
- Application creates 4-layer network architecture
- Application displays network specifications (layer sizes, activations, parameters)
- Application tests forward pass with sample data
- Application reports success/failure and basic performance metrics
- Show whether GPU or CPU was used for computation

## User Experience Requirements

### Interface Layout
- Single page application with distinct sections for each test
- Each section should have its own action/run button
- Clean, minimal design focused on functionality
- Both tests should be equally prominent on the page

### Results Display
- Results display inline below the test controls or to the right of the setup area
- No history functionality required - focus on current test results
- Results should be clearly formatted and easy to read
- No modal popups or separate pages needed

### User Interaction Flow
- Tests can be run independently of each other
- Each test has its own run button for immediate execution
- You can run tests multiple times without page refresh
- No queuing or batch execution needed

## Technical Requirements

### OpenAI Integration
- Input custom prompts through a text area
- Display basic response metadata (model used, response time, token usage if available)
- No API cost tracking or rate limiting display required
- No caching or storage of responses needed

### Neural Network Specifications
- Fixed CNN architecture with fully connected layers
- Use basic Inception-based architecture (4 layers total)
- Success criteria: CUDA compatibility check, model fits in memory, successful forward pass
- Generate synthetic test data for demonstration
- Display architecture details and memory usage (percentage and GB)
- Show device used (CPU/GPU) and basic performance metrics

### Configuration Management
- API keys stored in config directory in project root
- You manually copy API key to config file
- Auto-detect available compute resources (GPU/CPU)
- Basic logging to console for debugging
- Include .gitignore to prevent API key upload to repository

## Performance Criteria

### Response Times
- OpenAI API calls should complete within 60 seconds or timeout gracefully
- Neural network generation should complete within 30 seconds
- Web interface should be responsive (page loads < 3 seconds)
- Real-time feedback for operations taking longer than 5 seconds

### Resource Usage
- Application should run on typical development machines
- Minimal memory footprint when idle
- Efficient handling of concurrent requests (if multiple users)
- Graceful degradation when GPU unavailable

## Security Requirements

### API Key Management
- Secure handling of OpenAI API keys
- No exposure of credentials in client-side code
- Clear instructions for secure configuration
- Validation of API keys before use

### Web Security
- Basic protection against common web vulnerabilities
- Input validation for all user inputs
- Safe handling of API responses
- No exposure of server internals in error messages

## Installation and Setup Requirements

### Environment Setup
- Simple installation process (single command preferred)
- Clear documentation for dependencies
- Cross-platform compatibility (Windows, macOS, Linux)
- Virtual environment or containerization support

### Configuration
- Easy configuration process for API credentials
- Sensible defaults for all settings
- Validation of configuration before starting server
- Clear error messages for misconfiguration

### Startup Process
- Single command to start the web server
- Clear indication when server is ready
- Automatic browser opening (optional)
- Graceful shutdown capability

## Development Framework Requirements

### Web Framework
- Use Flask for maximum simplicity and minimal overhead
- Single Python file application preferred for initial implementation
- Static file serving for CSS/JS (if needed)
- No database requirements
- No containerization needed

### Project Structure
```
AI_Test_WebApp/
├── app.py                    # Main Flask application
├── config/
│   ├── config.json.template  # API key template
│   └── config.json          # User's API key (gitignored)
├── static/                  # CSS/JS files (if needed)
├── templates/
│   └── index.html           # Main page template
├── requirements.txt         # Python dependencies
├── .gitignore              # Exclude config.json and other sensitive files
└── README.md               # Setup and usage instructions
```

### Dependencies
- Flask (web framework)
- OpenAI Python client
- PyTorch with CUDA support (for neural network testing)
- Basic HTML/CSS for frontend (no complex JavaScript frameworks)

### CUDA and GPU Requirements
- **CUDA Detection**: Application must properly detect and utilize available CUDA GPUs
- **PyTorch CUDA**: Install PyTorch with CUDA support matching system CUDA version
- **Multiple Installation Methods**: Support both pip and conda/mamba installation paths
- **Build Verification**: Check PyTorch build strings to ensure CUDA-enabled installation
- **Conda/Mamba Considerations**: Handle conda CPU vs CUDA build conflicts
- **Fallback Behavior**: Graceful fallback to CPU if CUDA unavailable or misconfigured
- **Verification Steps**: Include comprehensive CUDA verification in setup documentation
- **Environment Debugging**: Provide commands to debug PyTorch CUDA installation issues

## Implementation Priorities

### Phase 1: Basic Setup
1. Flask application structure
2. Configuration management
3. Basic HTML interface
4. API key validation

### Phase 2: OpenAI Integration
1. Model selection interface
2. Query submission and processing
3. Response display with metadata
4. Error handling for API failures

### Phase 3: Neural Network Testing
1. Inception-based CNN architecture implementation
2. CUDA detection and memory checking
3. Forward pass execution
4. Results display with architecture and memory info

## Example Workflows

### 1. Initial Project Setup Example
```markdown
# Example: Setting Up AI Testing Web App
Trigger: User starts new project
Steps:
1. AI Assistant prompts for project overview
   User: "I want to create a web app for testing AI capabilities"
   AI: "Let's define the key aspects of your project:
        - Purpose: Local web interface for AI testing
        - Target Users: Developers, AI researchers
        - Key Features: Model testing, architecture testing
        - Success Criteria: Easy setup, comprehensive testing"

2. AI Assistant creates initial specifications.txt
   - Basic requirements documented
   - Technical constraints identified
   - Stakeholders defined
   - Initial assumptions listed

3. AI Assistant guides refinement to SPECIFICATIONS.md
   - Technical requirements detailed
   - User workflows defined
   - Security measures specified
   - Implementation priorities set

4. AI Assistant generates project structure
   - Flask application setup
   - Documentation hierarchy
   - Test framework
   - Configuration templates
```

### 2. Feature Addition Example
```markdown
# Example: Adding Neural Network Testing
Trigger: User requests new feature
Steps:
1. AI Assistant checks SPECIFICATIONS.md
   User: "I want to add neural network architecture testing"
   AI: "Let's validate this against our specs:
        - Fits core requirements
        - Aligns with user workflows
        - Requires new technical components
        - Impacts security considerations"

2. AI Assistant updates specifications
   - Adds neural network requirements
   - Updates user workflows
   - Documents technical constraints
   - Updates success criteria

3. AI Assistant guides implementation
   - Generates architecture code
   - Creates test cases
   - Updates documentation
   - Validates changes
```

### 3. Bug Fix Example
```markdown
# Example: Fixing API Key Validation
Trigger: User reports security issue
Steps:
1. AI Assistant analyzes bug report
   User: "API key validation is not working properly"
   AI: "Let's check the specifications:
        - Security requirements
        - API key handling
        - Validation procedures
        - Impact assessment"

2. AI Assistant updates documentation
   - Documents the issue
   - Plans the fix
   - Updates test cases
   - Tracks changes

3. AI Assistant guides fix implementation
   - Generates secure validation code
   - Updates security tests
   - Validates against specs
   - Updates documentation
```

### 4. Documentation Update Example
```markdown
# Example: Updating Installation Guide
Trigger: Code changes affect setup
Steps:
1. AI Assistant identifies affected docs
   User: "We've updated the installation process"
   AI: "Let's check all related documentation:
        - Installation guide
        - Configuration docs
        - User setup guide
        - Troubleshooting guide"

2. AI Assistant updates documentation
   - Updates installation steps
   - Revises configuration guide
   - Updates user instructions
   - Maintains consistency

3. AI Assistant validates changes
   - Checks completeness
   - Verifies accuracy
   - Validates cross-references
   - Updates version info
```

### 5. Code Review Example
```markdown
# Example: Reviewing Model Integration
Trigger: New model code submitted
Steps:
1. AI Assistant checks against specs
   User: "Please review the new model integration"
   AI: "Let's validate against specifications:
        - Implementation matches specs
        - Documentation is complete
        - Tests are comprehensive
        - Security is maintained"

2. AI Assistant provides feedback
   - Specification alignment
   - Code quality assessment
   - Documentation review
   - Security compliance

3. AI Assistant guides improvements
   - Suggests optimizations
   - Updates documentation
   - Adds missing tests
   - Fixes security issues
```

### 6. Testing Example
```markdown
# Example: Implementing Model Tests
Trigger: New model feature added
Steps:
1. AI Assistant checks specifications
   User: "We need tests for the new model"
   AI: "Let's define test requirements:
        - Model functionality
        - Input validation
        - Output verification
        - Error handling"

2. AI Assistant generates tests
   - Creates test cases
   - Sets up test environment
   - Writes test code
   - Documents procedures

3. AI Assistant validates tests
   - Runs test suite
   - Checks coverage
   - Verifies results
   - Updates documentation
```

### 7. Security Review Example
```markdown
# Example: Reviewing API Security
Trigger: New API endpoint added
Steps:
1. AI Assistant checks security specs
   User: "Please review the new API endpoint"
   AI: "Let's assess security:
        - Authentication requirements
        - Input validation
        - Rate limiting
        - Error handling"

2. AI Assistant guides security implementation
   - Generates secure code
   - Adds security tests
   - Updates documentation
   - Validates measures

3. AI Assistant validates security
   - Runs security checks
   - Verifies compliance
   - Updates documentation
   - Tracks issues
```

## Workflow Integration Examples

### Specification-Driven Development
```markdown
# Example: Feature Implementation
1. Start with specifications.txt
   - Basic feature requirements
   - Initial constraints
   - User needs

2. Refine to SPECIFICATIONS.md
   - Detailed requirements
   - Technical specifications
   - User workflows
   - Success criteria

3. Implement based on specs
   - Generate code
   - Create tests
   - Update documentation
   - Validate changes
```

### Documentation Maintenance
```markdown
# Example: Keeping Docs in Sync
1. Code changes trigger updates
   - Feature implementation
   - Bug fixes
   - Security updates

2. Documentation updates
   - Technical docs
   - User guides
   - API documentation
   - Security guides

3. Validation and review
   - Check completeness
   - Verify accuracy
   - Update cross-references
   - Maintain consistency
```

### Security Implementation
```markdown
# Example: Secure Feature Development
1. Start with security specs
   - Authentication requirements
   - Authorization rules
   - Data protection
   - API security

2. Implement security measures
   - Secure code generation
   - Security testing
   - Documentation
   - Validation

3. Regular security reviews
   - Code review
   - Security testing
   - Documentation updates
   - Issue tracking
```

This specification is now complete and ready for implementation. 