app_name = "test_deploy"
app_title = "Test Deploy"
app_publisher = "Mike"
app_description = "Frappe Cloud deployment test app"
app_email = "mike@casualty.co.nz"
app_license = "mit"

# Required apps for cloud deployment
required_apps = ["frappe", "erpnext", "hrms"]

# Build Configuration
# -------------------
# Skip asset building - no frontend assets
skip_assets_build = True

# Installation
# ------------
after_install = "test_deploy.install.after_install"

