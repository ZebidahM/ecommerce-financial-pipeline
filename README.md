# ecommerce-financial-pipeline📊
**Project Overview**

Developed a scalable data pipeline to transform raw, messy e-commerce data into actionable insights. This project simulates a real-world scenario where data is cleaned locally, hosted in a cloud environment, and visualized for stakeholders to monitor global revenue and customer retention.

**Technical Architecture**

1. Data Cleaning (Python): Processed a 1M row dataset to handle missing values, correct data types (DateTime locale issues), and engineer new features like TotalRevenue and IsChurned.

2. Cloud Infrastructure (Azure): Deployed an Azure Data Lake Storage Gen2 environment. Organized data within Resource Groups and secure Containers for optimized cloud storage.

3. BI Integration (Power BI): Established a live connection between Azure Blob Storage and Power BI Desktop using Access Keys and Power Query.

**Business Insights Delivered**

1.  KPIs: Real-time tracking of Total Gross Revenue and Distinct Active Customer counts.

2. Geographic Expansion: A Top-10 Stacked Bar Chart identifying high-value markets (UK, Netherlands, Germany, etc.), filtered for executive clarity.

3. Customer Churn Analysis: Identified "At-Risk" revenue by segmenting customers based on a 90-day inactivity threshold.

4. Revenue Projections: Implemented time-series forecasting to project sales trends into the upcoming fiscal year.
   <img width="1052" height="593" alt="ecommercedashboard" src="https://github.com/user-attachments/assets/15c0c9cc-d28b-4b36-8352-e2080e90980b" />

