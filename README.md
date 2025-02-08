# One of the trial projects I was assigned to when I joined my previous company.
## Objective
The purpose of this trial task is to evaluate the skills in Python for web scraping, MySQL for database management, and HTML/CSS/JavaScript for building a simple front-end interface. The task involves scraping data from specified websites, storing it in a MySQL database, and creating a front-end page to display and filter the data.

---
 
## Task Description
### **1. Web Scraping**
Scrape the following data from the `/services` pages of the provided websites:
- **Service ID**
- **Service Name**
- **Rate per Thousand**
- **Minimum Quantity**
- **Maximum Quantity**
- **Average Time**
- **Category of the Service**
- **Details/Description** (if available)

### **Websites to Scrape**
1. [smmbind.com](https://smmbind.com)
2. [likesoutlet.com](https://likesoutlet.com)
3. [godofpanel.com](https://godofpanel.com)
4. [postlikes.com](https://postlikes.com)
5. [bulkfollows.com](https://bulkfollows.com)
6. [followiz.com](https://followiz.com)

### **2. Database Setup**
- Use **MySQL** to store the scraped data.
- The database should have a table with columns for:
  - `provider`
  - `service_id`
  - `service_name`
  - `min_quantity`
  - `max_quantity`
  - `rate_per_thousand`
  - `average_time`
  - `details/description` (if possible)
  - `category`
  

### **3. Front-End Display**
- Build a simple **HTML/CSS/JavaScript** front-end to:
  - Display the scraped data in a table format.
  - Include a filter feature to:
    - Search by **service name**.
    - Filter by a range of **rates per thousand**.

### **4. Performance Optimization**
- Ensure the front-end loads and filters data efficiently, even for a large dataset.
- Optimize MySQL queries for fast retrieval of data.

---

## Requirements
1. Use **Python** for web scraping (e.g., BeautifulSoup, Selenium, Scrapy, or another tool of your choice).
2. Use **PHP** for the back-end.
3. Use **MySQL** for the database.
4. Use **HTML/CSS/JavaScript** for the front-end.
5. Include a `requirements.txt` file for Python dependencies.
6. Provide detailed comments in your code for clarity.
7. Submit the task by pushing your code to the repository on GitHub.

---

## Deliverables
1. **Python Script** for scraping the required data.
2. **MySQL Database Dump** containing the scraped data.
3. **Front-End Files** (HTML/CSS/JavaScript).
4. **Back-End Files** (PHP).
5. A brief `README.md` explaining:
   - How to run the scraper.
   - How to set up the database.
   - How to launch the front-end and test the filtering functionality.

---

## Deadline
Complete the task within **5 days** from the start date.

---

## Evaluation Criteria
- **Code Quality:** Clean, well-documented, and follows best practices.
- **Functionality:** Completeness and accuracy of scraping, database setup, and front-end filtering.
- **Efficiency:** Optimized database queries and fast front-end performance.
- **Creativity:** Innovative or user-friendly design and implementation.
