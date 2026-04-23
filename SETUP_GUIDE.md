# SETUP GUIDE FOR FIDELITY PORTFOLIO ANALYZER

## Overview
The Fidelity Portfolio Analyzer is a powerful tool designed to help users analyze and optimize their investment portfolios. This guide provides comprehensive documentation on features, installation, usage, daily import workflow, API endpoints, troubleshooting, and best practices.

## Features
- Portfolio performance tracking
- Asset allocation analysis
- Risk assessmen
- Customizable reporting options

## Installation Steps
1. **Clone the Repository**  
   Run the following command to clone the repository:
   ```bash
   git clone https://github.com/phemonoe-stack/quantfolio-v3.git
   cd quantfolio-v3
   ```

2. **Install Dependencies**  
   Install required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**  
   Create a `.env` file in the root directory and add necessary configurations:
   ```dotenv
   API_KEY=your_api_key
   DATABASE_URL=your_database_url
   ```

4. **Run Initial Migration**  
   If using a database, run the migration command to set up the database schema:
   ```bash
   python manage.py migrate
   ```

5. **Start the Application**  
   Launch the application with:
   ```bash
   python manage.py runserver
   ```

## Usage Guide
### Accessing the Application
After starting the application, access it at `http://localhost:8000`. 

### Daily Import Workflow
1. **Collect Data**: Gather your transaction data and save it in CSV format.
2. **Import Data**: Use the import functionality in the app to upload your files.
3. **Review and Analyze**: Check the imported data for accuracy and start analyzing your portfolio.

## UTF-8-BOM Encoding Support
Ensure your CSV files are saved with UTF-8-BOM encoding to avoid character issues during import. Most spreadsheet applications have an option to save with this encoding.

## API Endpoints
- `GET /api/portfolio`: Retrieve portfolio information.
- `POST /api/import`: Import transaction data.
- `GET /api/reports`: Generate performance reports.

## Troubleshooting
- **Issue**: Application does not start
  **Solution**: Ensure all dependencies are installed and environment variables are correctly set.
- **Issue**: Data import fails
  **Solution**: Check CSV formatting and ensure it is saved in UTF-8-BOM format.

## Best Practices
- Regularly update your dependencies to the latest versions.
- Back up your data before performing major changes or updates.  
- Document any changes made to the application for future reference.

## Conclusion
This setup guide should help you get started with the Fidelity Portfolio Analyzer. For further assistance, consult the documentation or reach out to the community.
