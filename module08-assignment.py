# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# ─────────────────────────────────────────────────────────────
# TODO 1: Create a dictionary of service categories and hourly rates
# ─────────────────────────────────────────────────────────────
services = {
    "Web Development":      150,
    "Data Analysis":        175,
    "Cloud Infrastructure": 200,
    "Cybersecurity":        225,
    "IT Consulting":         95,
    "Mobile Development":   160,
    "Database Management":  140,
}

# ─────────────────────────────────────────────────────────────
# TODO 2: Create customer dictionaries
# ─────────────────────────────────────────────────────────────
customer1 = {
    "company_name":    "Yahoo Industries",
    "contact_person":  "Lisa Johnson",
    "email":           "sjohnson@yahooindustries.com",
    "phone":           "555-101-2020",
}
customer2 = {
    "company_name":    "Bright Horizons LLC",
    "contact_person":  "Marcus Lee",
    "email":           "mlee@brighthorizons.com",
    "phone":           "555-202-3030",
}
customer3 = {
    "company_name":    "Coastal Dynamics",
    "contact_person":  "Nina Patel",
    "email":           "npatel@coastaldynamics.com",
    "phone":           "555-303-4040",
}
customer4 = {
    "company_name":    "Delta Systems Corp",
    "contact_person":  "Tom Rivera",
    "email":           "trivera@deltasystems.com",
    "phone":           "555-404-5050",
}
customer5 = {
    "company_name":    "Evergreen Tech",
    "contact_person":  "Aisha Brown",
    "email":           "abrown@evergreentech.com",
    "phone":           "555-505-6060",
}

# ─────────────────────────────────────────────────────────────
# TODO 3: Create a master customers dictionary (customer ID → customer dict)
# ─────────────────────────────────────────────────────────────
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4,
    "C005": customer5,
}

# ─────────────────────────────────────────────────────────────
# TODO 4: Display all customers
# ─────────────────────────────────────────────────────────────
print("\nAll Customers:")
print("-" * 60)
for cid, info in customers.items():
    print(f"  Customer ID : {cid}")
    print(f"  Company     : {info['company_name']}")
    print(f"  Contact     : {info['contact_person']}")
    print(f"  Email       : {info['email']}")
    print(f"  Phone       : {info['phone']}")
    print()

# ─────────────────────────────────────────────────────────────
# TODO 5: Look up specific customers
# ─────────────────────────────────────────────────────────────
print("\nCustomer Lookups:")
print("-" * 60)

# Full record for C002
c002_info = customers["C002"]
print("C002 Information:")
for key, val in c002_info.items():
    print(f"  {key}: {val}")

# Contact person for C003
c003_contact = customers["C003"]["contact_person"]
print(f"\nC003 Contact Person: {c003_contact}")

# Safe lookup for a non-existent customer
c999_info = customers.get("C999", "Customer not found")
print(f"\nC999 Lookup Result: {c999_info}")

# ─────────────────────────────────────────────────────────────
# TODO 6: Update the customer information
# ─────────────────────────────────────────────────────────────
print("\n\nUpdating Customer Information:")
print("-" * 60)

# Update C001's phone number
customers["C001"]["phone"] = "555-111-9999"
print(f"C001 phone updated to: {customers['C001']['phone']}")

# Add 'industry' field to C002
customers["C002"]["industry"] = "Financial Services"
print(f"C002 industry added: {customers['C002']['industry']}")

# Confirm the changes
print("\nUpdated C001 Record:")
for key, val in customers["C001"].items():
    print(f"  {key}: {val}")

print("\nUpdated C002 Record:")
for key, val in customers["C002"].items():
    print(f"  {key}: {val}")

# ─────────────────────────────────────────────────────────────
# TODO 7: Project data structure
# ─────────────────────────────────────────────────────────────
projects = {
    "C001": [
        {"name": "Yahoo Web Redesign",        "service": "Web Development",      "hours": 80,  "budget": 12000, "status": "completed"},
        {"name": "Yahoo Data Pipeline",       "service": "Data Analysis",        "hours": 50,  "budget":  8750, "status": "active"},
    ],
    "C002": [
        {"name": "BH Cloud Migration",       "service": "Cloud Infrastructure", "hours": 120, "budget": 24000, "status": "active"},
        {"name": "BH Security Audit",        "service": "Cybersecurity",        "hours": 40,  "budget":  9000, "status": "pending"},
    ],
    "C003": [
        {"name": "Coastal IT Strategy",      "service": "IT Consulting",        "hours": 30,  "budget":  2850, "status": "completed"},
        {"name": "Coastal Mobile App",       "service": "Mobile Development",   "hours": 100, "budget": 16000, "status": "active"},
        {"name": "Coastal DB Optimisation",  "service": "Database Management",  "hours": 60,  "budget":  8400, "status": "pending"},
    ],
    "C004": [
        {"name": "Delta Cybersecurity Plan", "service": "Cybersecurity",        "hours": 90,  "budget": 20250, "status": "active"},
        {"name": "Delta Cloud Setup",        "service": "Cloud Infrastructure", "hours": 75,  "budget": 15000, "status": "pending"},
    ],
    "C005": [
        {"name": "Evergreen Web Platform",   "service": "Web Development",      "hours": 110, "budget": 16500, "status": "active"},
    ],
}

print("\n\nProject Information:")
print("-" * 60)
for cid, proj_list in projects.items():
    company = customers[cid]["company_name"]
    print(f"\n  {cid} – {company}:")
    for proj in proj_list:
        print(f"    • {proj['name']}  |  Service: {proj['service']}  |  Hours: {proj['hours']}  |  Budget: ${proj['budget']:,.2f}  |  Status: {proj['status']}")

# ─────────────────────────────────────────────────────────────
# TODO 8: Calculate the project costs  (the rate × hours)
# ─────────────────────────────────────────────────────────────
print("\n\nProject Cost Calculations:")
print("-" * 60)
for cid, proj_list in projects.items():
    company = customers[cid]["company_name"]
    print(f"\n  {cid} – {company}:")
    for proj in proj_list:
        rate = services[proj["service"]]
        cost = rate * proj["hours"]
        print(f"    {proj['name']}")
        print(f"      Service: {proj['service']}  |  Rate: ${rate}/hr  |  Hours: {proj['hours']}  |  Calculated Cost: ${cost:,.2f}")

# ─────────────────────────────────────────────────────────────
# TODO 9: Customer statistics using dictionary methods
# ─────────────────────────────────────────────────────────────
print("\n\nCustomer Statistics:")
print("-" * 60)

# All customer IDs
all_ids = list(customers.keys())
print(f"Customer IDs   : {all_ids}")

# All company names (extracted from values)
all_companies = [info["company_name"] for info in customers.values()]
print(f"Company Names  : {all_companies}")

# Total count
total_customers = len(customers)
print(f"Total Customers: {total_customers}")

# ─────────────────────────────────────────────────────────────
# TODO 10: Service usage analysis
# ─────────────────────────────────────────────────────────────
print("\n\nService Usage Analysis:")
print("-" * 60)

service_counts = {}
for proj_list in projects.values():
    for proj in proj_list:
        svc = proj["service"]
        service_counts[svc] = service_counts.get(svc, 0) + 1

for svc, count in service_counts.items():
    print(f"  {svc:<25}: {count} project(s)")

# ─────────────────────────────────────────────────────────────
# TODO 11: Financial aggregations
# ─────────────────────────────────────────────────────────────
print("\n\nFinancial Summary:")
print("-" * 60)

all_projects_flat = [proj for proj_list in projects.values() for proj in proj_list]

total_hours  = sum(proj["hours"]  for proj in all_projects_flat)
total_budget = sum(proj["budget"] for proj in all_projects_flat)
avg_budget   = total_budget / len(all_projects_flat)
max_budget   = max(proj["budget"] for proj in all_projects_flat)
min_budget   = min(proj["budget"] for proj in all_projects_flat)

# Identify the projects that hit max/min
max_project  = max(all_projects_flat, key=lambda p: p["budget"])
min_project  = min(all_projects_flat, key=lambda p: p["budget"])

print(f"  Total Hours          : {total_hours}")
print(f"  Total Budget         : ${total_budget:,.2f}")
print(f"  Average Project Budget: ${avg_budget:,.2f}")
print(f"  Most Expensive Project: {max_project['name']} – ${max_budget:,.2f}")
print(f"  Least Expensive Project: {min_project['name']} – ${min_budget:,.2f}")

# ─────────────────────────────────────────────────────────────
# TODO 12: Customer summary report
# ─────────────────────────────────────────────────────────────
print("\n\nCustomer Summary Report:")
print("-" * 60)
for cid, proj_list in projects.items():
    info         = customers[cid]
    num_projects = len(proj_list)
    cust_hours   = sum(p["hours"]  for p in proj_list)
    cust_budget  = sum(p["budget"] for p in proj_list)

    print(f"\n  {cid} | {info['company_name']}")
    print(f"    Contact        : {info['contact_person']}")
    print(f"    Email          : {info['email']}")
    print(f"    Phone          : {info['phone']}")
    print(f"    # of Projects  : {num_projects}")
    print(f"    Total Hours    : {cust_hours}")
    print(f"    Total Budget   : ${cust_budget:,.2f}")

# ─────────────────────────────────────────────────────────────
# TODO 13: Create rate adjustments using dictionary comprehension (10 % increase)
# ─────────────────────────────────────────────────────────────
print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)

adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

for svc, rate in adjusted_rates.items():
    print(f"  {svc:<25}: ${rate:,.2f}/hr")

# ─────────────────────────────────────────────────────────────
# TODO 14: Filter active customers using dictionary comprehension
# ─────────────────────────────────────────────────────────────
print("\n\nActive Customers (with projects):")
print("-" * 60)

active_customers = {cid: info for cid, info in customers.items() if cid in projects}

for cid, info in active_customers.items():
    print(f"  {cid}: {info['company_name']}")

# ─────────────────────────────────────────────────────────────
# TODO 15: Create project summaries using dictionary comprehension
# ─────────────────────────────────────────────────────────────
print("\n\nCustomer Budget Totals:")
print("-" * 60)

customer_budgets = {cid: sum(p["budget"] for p in proj_list)
                    for cid, proj_list in projects.items()}

for cid, total in customer_budgets.items():
    print(f"  {cid} – {customers[cid]['company_name']:<25}: ${total:,.2f}")

# ─────────────────────────────────────────────────────────────
# TODO 16: Service pricing tiers using dictionary comprehension
# ─────────────────────────────────────────────────────────────
print("\n\nService Pricing Tiers:")
print("-" * 60)

service_tiers = {
    svc: ("Premium"  if rate >= 200 else
          "Standard" if rate >= 100 else
          "Basic")
    for svc, rate in services.items()
}

for svc, tier in service_tiers.items():
    print(f"  {svc:<25}: {tier} (${services[svc]}/hr)")

# ─────────────────────────────────────────────────────────────
# TODO 17: Customer validation function
# ─────────────────────────────────────────────────────────────
print("\n\nCustomer Validation:")
print("-" * 60)

def validate_customer(customer_dict):

    required_fields = ["company_name", "contact_person", "email", "phone"]
    for field in required_fields:
        if field not in customer_dict or not customer_dict[field]:
            return False
    return True

for cid, info in customers.items():
    valid = validate_customer(info)
    status_label = "VALID" if valid else "INVALID"
    print(f"  {cid} – {info['company_name']:<25}: {status_label}")

# ─────────────────────────────────────────────────────────────
# TODO 18: Project status tracking with loops and conditionals
# ─────────────────────────────────────────────────────────────
print("\n\nProject Status Summary:")
print("-" * 60)

status_counts = {}
for proj_list in projects.values():
    for proj in proj_list:
        s = proj["status"]
        status_counts[s] = status_counts.get(s, 0) + 1

for status, count in status_counts.items():
    print(f"  {status.capitalize():<12}: {count} project(s)")

# ─────────────────────────────────────────────────────────────
# TODO 19: Budget analysis function
# ─────────────────────────────────────────────────────────────
print("\n\nDetailed Budget Analysis:")
print("-" * 60)

def analyze_customer_budgets(projects_dict):

    analysis = {}
    for cid, proj_list in projects_dict.items():
        budgets = [p["budget"] for p in proj_list]
        total   = sum(budgets)
        count   = len(budgets)
        average = total / count if count > 0 else 0
        analysis[cid] = {
            "total":   total,
            "average": average,
            "count":   count,
        }
    return analysis

budget_analysis = analyze_customer_budgets(projects)
for cid, stats in budget_analysis.items():
    print(f"  {cid} – {customers[cid]['company_name']}")
    print(f"    Projects : {stats['count']}")
    print(f"    Total    : ${stats['total']:,.2f}")
    print(f"    Average  : ${stats['average']:,.2f}")

# ─────────────────────────────────────────────────────────────
# TODO 20: Service recommendation system
# ─────────────────────────────────────────────────────────────
print("\n\nService Recommendations:")
print("-" * 60)

def recommend_services(customer_id, customers_dict, projects_dict, services_dict):
    """
    This analyses a customer's past projects then identifies the services they have NOT
    used as yet, and returns those services filtered to the  ones within ±50 % of
    the customer's average project budget.
    """
    # Determine which services the customer already uses
    used_services = set()
    customer_projects = projects_dict.get(customer_id, [])

    for proj in customer_projects:
        used_services.add(proj["service"])

    # Calculate the customer's average project budget for an affordability check
    if customer_projects:
        avg_cust_budget = sum(p["budget"] for p in customer_projects) / len(customer_projects)
    else:
        avg_cust_budget = 0

    # Recommend unused services whose estimated cost (rate × 40 hr baseline)
    # is within a reasonable range of the customer's average budget
    recommendations = []
    for svc, rate in services_dict.items():
        if svc not in used_services:
            estimated_cost = rate * 40          # 40-hr baseline estimate
            if avg_cust_budget == 0 or estimated_cost <= avg_cust_budget * 1.5:
                recommendations.append(svc)

    return recommendations

for cid in customers:
    recs = recommend_services(cid, customers, projects, services)
    company = customers[cid]["company_name"]
    if recs:
        print(f"\n  {cid} – {company}:")
        for svc in recs:
            print(f"    → {svc} (${services[svc]}/hr)")
    else:
        print(f"\n  {cid} – {company}: No new recommendations at this time.")

print("\n" + "=" * 60)
print("END OF REPORT")
print("=" * 60)
